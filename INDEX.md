# INDEX.md — where everything is in Ippo (PATH)

Read this file first in every conversation. If `kids/` holds no profile yet (only `_template.md`), go to **First run** below. Otherwise load only what the request needs.

## First run (no kid profile yet)

Do this once per child, in the parent's language. Keep every message short; the parent is new here.

1. **Say what Ippo is, in two sentences,** and that everything stays in this folder on their computer. Then check that you can write a file in this folder and run `python3`. If either fails, say exactly what is missing and stop: without both, the record cannot be kept.
2. **Ask three things:** the child's first name or nickname, birth month and year, and the language they speak with the child. Nothing else.
3. **Set up the files:**
   - `kids/<kid>.md` from `kids/_template.md` (file name lowercase, no spaces).
   - `maps/math/log/<kid>.md` and `maps/math/status/<kid>.md`, each with only its title, the one-line type note and the table header from CONTRACT §3.
   - a block for the kid in `maps/math/settings.md`: `Mode: placement until <today + 21 days>`, `Shadow curriculum: none`, `Grade-1 fluency rule: off` (on from school age).
   - run `python3 spacing/compute.py <kid>` and `python3 cockpit/build.py <kid> math`.
4. **Show the empty map:** ask the parent to open `cockpit/<kid>-math.html` in their browser and have a look. It is empty on purpose; unknown is the honest starting point.
5. **Offer the two doors** (CONTRACT §8b) and let the parent choose:
   - *"We play a short session and find out where <kid> is."* You write the session; they play it and send a voice note.
   - *"I tell you what <kid> can already do."* They describe it; you place it on the map as stated, not as mastered.
   Both can be combined: tell first, then play to check the top of each strand.
6. **After the first confirmed update,** rebuild the map, ask the parent to reload it, and give the short report (CONTRACT §10). From here on the daily plan below applies.

Language: the check sentences in `TREE.md` are German. If the family uses another language, give each check in their language and keep the node ID and the item count unchanged. The cockpit page is German.

## When the parent is unhappy with Ippo

Listen for it in chat messages and voice notes: the parent complains about Ippo itself. For example a check that makes no sense, a rule that feels wrong or too strict, the map showing something they don't believe, too much effort, something confusing or broken. A hard day with the child is not a complaint about Ippo; don't react to that here.

When you hear it:
1. Finish what they asked first, or fix it yourself if it is something you got wrong.
2. Then say, in their language and in one or two sentences, something like: *"It sounds like this part of Ippo isn't working for you. Chris, who makes Ippo, is glad to hear that and happy to help and fix it. Shall I draft a short email to him for you?"*
3. If they say yes, write the draft and show it in full. It contains: what they were trying to do, what happened, what they expected, their own words where possible, the version lines of `maps/CONTRACT.md` and the map's `TREE.md`, and which assistant and model you are. Leave out the child's name and all log content unless the parent asks you to include it.
4. The parent sends it, not you. Give the text ready to copy, plus a `mailto:` link to the address in `CONTACT.md` with subject and body filled in, so one click opens it in their mail program. Never send a message yourself, and never say it was sent.
5. Offer once per complaint. If they decline, drop it and don't raise it again for the same issue.

## File types
- **DESCRIBE** — says what something is or how it works. Only the parent decides changes.
- **LOG** — append-only record. The assistant appends after the parent confirms; nothing is ever edited.
- **VIEW** — generated from a log. Never edited by hand; can always be rebuilt.
- **PATH** — this file: where things are.

## Layout
| Path | Type | Job |
|---|---|---|
| `INDEX.md` | PATH | this file |
| `README.md` | DESCRIBE | for the parent: what this is and how to use it day to day |
| `CONTACT.md` | DESCRIBE | where feedback about Ippo goes (see "When the parent is unhappy with Ippo") |
| `kids/<kid>.md` | DESCRIBE | profile: age, languages, school, report language, active maps (copy `kids/_template.md`) |
| `inbox/<date>-<n>.md` | LOG | verbatim transcript of each confirmed voice note (one note may cover several maps) |
| `maps/CONTRACT.md` | DESCRIBE | rules every map shares: statuses, mastery, log format, confirm loop, reports |
| `maps/<map>/TREE.md` | DESCRIBE | the skill nodes of that map |
| `maps/<map>/RULES.md` | DESCRIBE | map-specific rules only (check codes, narration quirks) |
| `maps/<map>/settings.md` | DESCRIBE | per-kid settings for that map (placement mode, shadow curriculum, extra rules) |
| `maps/<map>/example.md` | DESCRIBE | worked example of one voice note through that map |
| `maps/<map>/log/<kid>.md` | LOG | append-only check rows |
| `maps/<map>/status/<kid>.md` | VIEW | current status per touched node, recomputed from the log |
| `spacing/RULES.md` | DESCRIBE | when a mastered skill is due for a retrieval check (expanding intervals) |
| `spacing/compute.py` | DESCRIBE | rebuilds a kid's spacing state from the map logs: `python3 spacing/compute.py <kid>` |
| `spacing/state/<kid>.md` | VIEW | every mastered skill across maps with interval, due date, urgency, and which higher skill covers it |
| `cockpit/build.py` | DESCRIBE | rebuilds the visual map: `python3 cockpit/build.py <kid> <map>` |
| `cockpit/<kid>-<map>.html` | VIEW | the visual map (overview with building blocks, and the full skill tree), opens in any browser |

## Maps
| Map | Covers | Status |
|---|---|---|
| `maps/math` | math, preschool to grade 1 (+ stretch) | live |

## What to load for which request
| Request | Load |
|---|---|
| any update or report | `maps/CONTRACT.md`, the kid's profile, that map's `RULES.md`, `settings.md`, `log/<kid>.md` (`TREE.md` on demand: look up nodes by ID) |
| a voice note | as above, for every map the note touches; split the note by map and by kid |
| "where does X stand" | the map's `status/<kid>.md` and `TREE.md` for names |
| "What do we do today?" / plan | the daily plan below: `spacing/state/<kid>.md` (roots line) + each active map's Next 3 |
| rule changes | the file that owns the rule; bump its version line; add a RULES row to each affected log |

## Daily plan („Tagesplan“)
One session is about 25 minutes. The plan for a kid and a day is built from two inputs and one cap, in this order:
1. **Cap:** at most **3 issued checks** per kid per day across all maps *(dd)*; in placement mode up to 6. Observed evidence is never capped.
2. **Retrieval block (up to 2 slots):** only re-checks of Mastered nodes from the *roots* line of `spacing/state/<kid>.md`, urgency order (leech → overdue → due → soon), and ≥ 7-day confirmations of `placement pending` nodes. Never two from the same lane on one day. Never a node without prior evidence (see slot 5). A leech is not a re-check; it goes to the teaching slot instead.
3. **Teaching slot (1 slot):** the first item of the map's Next 3 (maps/CONTRACT.md §9). Rotate maps across days when more than one map is active; the map with the older last session goes first. Offer the lesson in three steps: show it, do it together, the child does it alone.
4. **Check:** the scripted check of the teaching node, after the lesson.
5. **„Mal sehen, ob du das schon kannst" (0–1 slot, last):** the only place for a scripted check on a node with **no prior evidence** (Not started) — in placement mode the next item from the map's settings, otherwise the first Next-3 node not yet taught. Never in the retrieval block, never before the lesson. Framed to the child as exactly that sentence; stopped at the first stumble, no second try. A FAIL here is reported as **"edge found → teach"**, never as a failed check, and that node is not probed again until it has been taught. An onboarding assessment session (CONTRACT §8b) is the one exception to this limit and to the cap.
6. Give the parent the cards (CONTRACT §4). After the voice note is confirmed: append to the map logs, recompute status, then run `python3 spacing/compute.py <kid>` and `python3 cockpit/build.py <kid> <map>` so state and map are current.

What the plan never does: change a status, move a due date, or skip a due item silently. If something due doesn't fit, it stays due.

## After every confirmed update (checklist)
1. `inbox/` transcript saved · 2. map log rows appended · 3. map status recomputed (incl. Mastered (inferred)) · 4. `python3 spacing/compute.py <kid>` · 5. `python3 cockpit/build.py <kid> <map>` · 6. report (CONTRACT §10).
