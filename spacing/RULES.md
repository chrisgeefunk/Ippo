# spacing/RULES.md — when a mastered skill is re-checked (v3, 2026-11-10)

Versions: v1 2026-11-06; v2 2026-11-09 scripted pass on the node itself counts as retrieval; interval expands only after ≥ half the interval has elapsed (MIN_GAP 0.5); v3 2026-11-10 nodes flagged `exempt` are not tracked.

DESCRIBE. The spacing service answers one question: **which mastered skills are due for a retrieval check, and how urgent is each.** It plans no session, picks no order within a day and knows no cap; that is the orchestrator's job (INDEX.md, "Tagesplan"). It changes no map file.

Research basis: spacing effect; retrieval practice; expanding intervals adjusted to performance (Leitner / SM-2 family); Cepeda et al. 2008 (for retention over a year, the best gap is roughly 10–20 % of the retention interval); Rawson & Dunlosky (successive relearning). Nearly all of it is on facts and older learners, so every number below is a design default *(dd)* to calibrate on this child's own re-check results.

## 1. Files
| Path | Type | Job |
|---|---|---|
| `spacing/RULES.md` | DESCRIBE | this file |
| `spacing/compute.py` | DESCRIBE | the calculator; `python3 spacing/compute.py <kid>` rebuilds that kid's state from the map logs |
| `spacing/state/<kid>.md` | VIEW | one row per mastered skill across all maps: interval, next due, urgency; never edited by hand |

Inputs: `maps/<map>/log/<kid>.md`, `maps/<map>/status/<kid>.md`, `maps/<map>/TREE.md`. Output: only `spacing/state/<kid>.md`. Re-check results are logged in the map (Kind R) like any other check; the service reads them on its next run. Nothing flows from spacing into a map.

## 2. What is tracked
Every node whose status is **Mastered** or **Mastered (placed)** in any map. Nodes carrying the flag `exempt` (CONTRACT §7) are **not tracked**: the parent has declared them permanently acquired. *(v3)* Nodes that are **Mastered (inferred)** are not tracked: they are covered by the mastered node above them. Growth tracks are not here (fixed 14-day takt, in the map's RULES).

## 3. The interval
For each tracked node, `interval` is the number of days until the next retrieval check, counted from its last *retrieval event*.

| Event (from the map log) | Effect |
|---|---|
| Becomes Mastered / Mastered (placed) | interval = **14 d** *(dd)*; last retrieval = that date |
| Re-check (Kind R) PASS | interval × **2.5** *(dd)*, capped at **180 d** *(dd)* |
| Re-check DEV | interval unchanged; last retrieval = that date |
| Re-check FAIL | interval = **7 d** *(dd)*; the map sets Needs refresh. When the map returns it to Mastered, continue from 7 d × 2.5 |
| **Incidental retrieval**: a scripted PASS (Kind S, P or R, never an attestation or parent-statement row, never O/X/U) dated on or after mastery, on a node that *exercises* this node (Requires, recursively) | counts as a PASS re-check of this node |
| Second FAIL on re-checks within 90 d | **leech**: removed from the rotation and flagged in state; it goes back to the map's Next 3 as a teaching item. Spacing never repairs missing understanding |

A scripted PASS (Kind S or P) on the node itself, on or after its mastery date, is a retrieval event like a re-check. *(v2)*

A PASS expands the interval only if at least **half the current interval** *(dd, MIN_GAP 0.5)* has passed since the last retrieval; an earlier PASS moves the last-retrieval date but leaves the interval. Several passes within days are one retrieval's worth of evidence. *(v2)*

Attested nodes (flag `attested` in the map status, parent override without a scripted check) start at **7 d** *(dd)* instead of 14, so the first scripted confirmation comes soon.

Sequence from 14 d: 14 → 35 → 88 → 180 → 180 … That matches a 10–20 % gap for retention over a school year.

## 4. Due and urgency
`due = last retrieval + interval`. Urgency, recomputed every run from today:
| Urgency | Rule |
|---|---|
| `overdue` | today > due + 14 d |
| `due` | due ≤ today ≤ due + 14 d |
| `soon` | due within the next 7 days |
| `ok` | later |

`Covered by` lists the tracked higher skills whose check would retrieve this one; the orchestrator checks the **roots** (nothing covers them) and lets the rest be retrieved incidentally. Within one urgency, roots come first, then the state file sorts by **shorter interval first** (least stable first), then by days overdue. That is the only ordering spacing gives; the orchestrator applies the daily cap and the "never two from one lane" rule.

## 5. Breaks
If no check of any kind was logged for a kid for more than **14 d** *(dd)*, every node mastered in the **6 weeks** before the break becomes `due` on the first day after it, whatever its interval said.

## 6. Calibration
Once a quarter, or when the parent asks: if more than 90 % of re-checks were PASS, intervals are too short → raise the factor (e.g. 2.5 → 3). If fewer than 70 % were PASS, lower the start interval (14 → 10) or the factor. Change the number here, bump the version line, add a RULES row to each kid's map logs.
