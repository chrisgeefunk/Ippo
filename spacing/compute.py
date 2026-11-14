#!/usr/bin/env python3
# Part of Ippo. Copyright (c) 2026 Christian Greiner. PolyForm Noncommercial License 1.0.0, see LICENSE.md.
"""Spacing service calculator. Reads maps/*/{TREE,status,log}/<kid>; writes spacing/state/<kid>.md.
Usage: python3 spacing/compute.py <kid> [YYYY-MM-DD]   (date defaults to today)"""
import re, sys, os, datetime as dt
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
kid=sys.argv[1]; today=dt.date.fromisoformat(sys.argv[2]) if len(sys.argv)>2 else dt.date.today()
START, START_ATTESTED, FACTOR, CAP, FAIL_INT, OVERDUE, SOON, BREAK, BREAK_WINDOW, MIN_GAP = 14, 7, 2.5, 180, 7, 14, 7, 14, 42, 0.5
def cells(l): return [x.strip() for x in l.strip().strip('|').split('|')]
def d(s):
    m=re.search(r'(\d{4}-\d{2}-\d{2})',s); return dt.date.fromisoformat(m.group(1)) if m else None
rows=[]; all_check_dates=[]
for mp in sorted(os.listdir(f'{ROOT}/maps')):
    base=f'{ROOT}/maps/{mp}'
    if not os.path.isdir(base) or not os.path.exists(f'{base}/log/{kid}.md'): continue
    tree={}; strand=None
    for l in open(f'{base}/TREE.md',encoding='utf-8'):
        m=re.match(r'^## ([A-Z]{2,3}) — (.+?)( ·.*)?$',l)
        if m: strand=m.group(1)
        c=cells(l)
        if re.match(r'^[A-Z]{2,3}-\d\d$',c[0]) and len(c)>=7:
            req=c[4]  # column 4 is Requires in every map
            tree[c[0]]=dict(name=c[1],req=[r.strip() for r in req.split(',') if r.strip() not in('–','')],strand=strand)
    def expand(rs):
        out=[]
        for p in rs:
            mm=re.match(r'^(BL)-(\d\d)\.\.BL-(\d\d)$',p)
            out+= [f'BL-{i:02d}' for i in range(int(mm.group(2)),int(mm.group(3))+1)] if mm else [p]
        return out
    if not os.path.exists(f'{base}/status/{kid}.md'): continue
    status={c[0]:c for c in map(cells,open(f'{base}/status/{kid}.md',encoding='utf-8')) if re.match(r'^[A-Z]{2,3}-\d\d$',c[0])}
    log=[c for c in map(cells,open(f'{base}/log/{kid}.md',encoding='utf-8')) if re.match(r'^L\d{3}$',c[0])]
    for c in log:
        dd=d(c[1])
        if dd and re.match(r'^[A-Z]{2,3}-\d\d$',c[2]) and c[3] in('S','P','R','O'): all_check_dates.append(dd)
    # ancestors map: node -> set of nodes that exercise it (descendants)
    desc={}
    def walk(top,id,seen):
        for r in expand(tree.get(id,{'req':[]})['req']):
            if r in tree and r not in seen: seen.add(r); desc.setdefault(r,set()).add(top); walk(top,r,seen)
    for n in tree: walk(n,n,set())
    for id,s in status.items():
        if s[1] not in('Mastered','Mastered (placed)'): continue
        if 'exempt' in s[4]: continue  # RULES v3: declared permanently acquired
        mastered=d(s[2]) or d(s[3]) or today
        attested='attested' in s[4]
        interval=START_ATTESTED if attested else START; last=mastered; fails=[]; leech=False; hist=[]
        events=[]
        for c in log:
            dd=d(c[1]); 
            if not dd or dd<mastered: continue
            node,kind,outcome=c[2],c[3],c[10].split()[0] if c[10] else ''
            if 'attestation' in c[4] or 'parent statement' in c[4]: continue  # parent claims are never retrieval events
            if node==id and kind in('R','S','P'): events.append((dd,outcome,'R' if kind=='R' else 'self '+kind))
            elif node in desc.get(id,()) and kind in('S','P','R') and outcome=='PASS': events.append((dd,'PASS','incidental '+node))
        for dd,outcome,src in sorted(events):
            hist.append(f'{dd} {outcome}{"" if src=="R" else " ("+src+")"}')
            if outcome=='PASS':
                if (dd-last).days>=interval*MIN_GAP: interval=min(CAP,round(interval*FACTOR))
                last=dd
            elif outcome=='DEV': last=dd
            elif outcome=='FAIL':
                fails.append(dd); interval=FAIL_INT; last=dd
                if len([f for f in fails if (dd-f).days<=90])>=2: leech=True
        due=last+dt.timedelta(days=interval)
        tracked_desc=sorted(x for x in desc.get(id,()) if x in status and status[x][1] in('Mastered','Mastered (placed)'))
        rows.append(dict(covered=tracked_desc,map=mp,id=id,name=tree.get(id,{'name':'?'})['name'],strand=tree.get(id,{'strand':'?'})['strand'],interval=interval,last=last,due=due,leech=leech,attested=attested,hist=hist))
# breaks
if all_check_dates:
    lastcheck=max(all_check_dates); gap=(today-lastcheck).days
    if gap>BREAK:
        for r in rows:
            if (lastcheck-r['last']).days<=BREAK_WINDOW and r['due']>today: r['due']=today; r['break']=True
def urg(r):
    if r['leech']: return 'leech'
    days=(today-r['due']).days
    if days>OVERDUE: return 'overdue'
    if days>=0: return 'due'
    if -days<=SOON: return 'soon'
    return 'ok'
order={'leech':0,'overdue':1,'due':2,'soon':3,'ok':4}
for r in rows: r['urg']=urg(r)
rows.sort(key=lambda r:(order[r['urg']],bool(r['covered']),r['interval'],-(today-r['due']).days,r['id']))
os.makedirs(f'{ROOT}/spacing/state',exist_ok=True)
out=[f'# spacing state — {kid.capitalize()} — computed {today}','',f'VIEW. Rebuilt by `python3 spacing/compute.py {kid}`. Never edited by hand. Rules: spacing/RULES.md v3.','',
     '| Urgency | Map | Node | Skill | Lane | Interval (d) | Last retrieval | Due | Covered by | Flags | Retrieval history |','|---|---|---|---|---|---|---|---|---|---|---|']
for r in rows:
    flags=', '.join(f for f,v in (('attested',r['attested']),('leech',r['leech']),('break',r.get('break'))) if v) or '–'
    out.append(f"| {r['urg']} | {r['map']} | {r['id']} | {r['name']} | {r['strand']} | {r['interval']} | {r['last']} | {r['due']} | {', '.join(r['covered']) or '–'} | {flags} | {'; '.join(r['hist']) or '–'} |")
from collections import Counter; cnt=Counter(r['urg'] for r in rows)
roots=[r for r in rows if not r['covered'] and r['urg'] in('overdue','due','soon','leech')]
out+=['',f"Roots to check (not covered by a higher tracked skill, due or soon): {', '.join(r['id'] for r in roots) or '–'}"]
out+=['',f"Tracked: {len(rows)} · "+' · '.join(f'{k}: {cnt.get(k,0)}' for k in order)]
open(f'{ROOT}/spacing/state/{kid}.md','w',encoding='utf-8').write('\n'.join(out)+'\n')
print(f"{kid}: {len(rows)} tracked; "+' '.join(f'{k}={cnt.get(k,0)}' for k in order))
