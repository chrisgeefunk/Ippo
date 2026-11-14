#!/usr/bin/env python3
"""Rebuild cockpit/<kid>-<map>.html from maps/<map>/{TREE,status,log}, spacing/state and the kid profile. Usage: python3 cockpit/build.py mia math"""
import re,json,sys,os,datetime
kid,mp=sys.argv[1],sys.argv[2]; root=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
base=f'{root}/maps/{mp}'
nodes=[];strand=None
for line in open(f'{base}/TREE.md',encoding='utf-8'):
    m=re.match(r'^## ([A-Z]{2,3}) — (.+?)( ·.*)?$',line)
    if m: strand=(m.group(1),m.group(2).strip())
    c=[x.strip() for x in line.strip().strip('|').split('|')]
    if re.match(r'^[A-Z]{2,3}-\d\d$',c[0]) and len(c)>=9:
        nodes.append(dict(id=c[0],name=c[1],age=c[2],track=c[3],req=[r.strip() for r in c[4].split(',') if r.strip() not in('–','')],rule=c[5],check=c[6],pool=c[7],strand=strand[0],strandName=strand[1],desc=c[9] if len(c)>9 else ''))
status={};logs={}
lines=lambda p: open(p,encoding='utf-8') if os.path.exists(p) else []  # a new kid has no status or log yet: the map is simply empty
for line in lines(f'{base}/status/{kid}.md'):
    c=[x.strip() for x in line.strip().strip('|').split('|')]
    if re.match(r'^[A-Z]{2,3}-\d\d$',c[0]): status[c[0]]=dict(status=c[1],last=c[3],flags=c[4],evidence=c[5])
for line in lines(f'{base}/log/{kid}.md'):
    c=[x.strip() for x in line.strip().strip('|').split('|')]
    if re.match(r'^L\d{3}$',c[0]) and re.match(r'^[A-Z]{2,3}-\d\d$',c[2]):
        logs.setdefault(c[2],[]).append(dict(n=c[0],date=c[1],kind=c[3],items=c[4],score=c[5],help=c[6],outcome=c[10]))
spacing={}
sp=f'{root}/spacing/state/{kid}.md'
if os.path.exists(sp):
    for line in open(sp,encoding='utf-8'):
        c=[x.strip() for x in line.strip().strip('|').split('|')]
        if len(c)>=11 and c[1]==mp and re.match(r'^[A-Z]{2,3}-\d\d$',c[2]): spacing[c[2]]=dict(urg=c[0],interval=c[5],due=c[7],covered=c[8])
# kid profile (name, birth month) and placement mode: the template works out age and "unknown vs gap" from these
kidinfo=dict(name=kid.capitalize(),born='',age='',placementUntil='')
kp=f'{root}/kids/{kid}.md'
if os.path.exists(kp):
    t=open(kp,encoding='utf-8').read()
    MONTHS='january february march april may june july august september october november december'.split()
    m=re.search(r'born (\w+) (\d{4})',t)
    if m and m.group(1).lower() in MONTHS: kidinfo['born']=f'{m.group(2)}-{MONTHS.index(m.group(1).lower())+1:02d}'
    m=re.search(r'^- Age:\s*(\d+)',t,re.M)
    if m: kidinfo['age']=m.group(1)
    m=re.search(r'^- Cockpit colou?r:.*?(#[0-9a-fA-F]{6})',t,re.M)
    if m: kidinfo['color']=m.group(1)
st=f'{base}/settings.md'
if os.path.exists(st):
    m=re.search(rf'^## {re.escape(kid)}\s*$(.*?)(?=^## |\Z)',open(st,encoding='utf-8').read(),re.M|re.S|re.I)
    m=m and re.search(r'^- Mode:\s*placement until (\d{4}-\d\d-\d\d)',m.group(1),re.M)
    if m: kidinfo['placementUntil']=m.group(1)
data=json.dumps(dict(nodes=nodes,status=status,logs=logs,spacing=spacing,kid=kidinfo,built=datetime.date.today().isoformat(),map=mp),ensure_ascii=False).replace('</','<\\/')
tpl=open(f'{root}/cockpit/template.html',encoding='utf-8').read()
out=f'{root}/cockpit/{kid}-{mp}.html'
open(out,'w',encoding='utf-8').write(tpl.replace('__DATA__',data).replace('__KID__',kid.capitalize()))
print(out,len(nodes),'nodes',len(status),'statused')
