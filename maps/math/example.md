# Worked example (fictional data — not part of any kid file)

Use this as the model for how a note is processed. Date: 2026-10-25, both kids in placement mode, no open checks.

## Voice note (transcript)
> „Mia, Placement. Zahlenkarten 36, 63, 47, 81, 59 – vier richtig, bei 63 hat sie sechsunddreißig gesagt, am Ende nochmal gefragt, dann richtig. Keine Hilfe, alles sofort. Dann Zehnerschritte bis hundert, ganz durch, alleine. Dann 8+5, 7+6, 9+4, 8+6, 6+7, alles richtig. Bei 8+5 hat sie gesagt erst 8+2 ist 10, dann noch 3. Bei 9+4 genauso. 7+6 hat sie mit den Fingern gezählt, bei den anderen hat sie nichts gesagt. Dann Leo: Gib mir zwei, drei, eins, drei, zwei – alles richtig, bei der zweiten Drei hat sie erst vier gegeben und dann selbst eins zurückgelegt.“

## Assistant: claims to confirm
```
Mia · 2026-10-25 · note 1
1. [P] NUM-12 Name numerals 21–99 · parent-chosen items 36, 47, 59, 63, 81 · 4/5; said 36 (sechsunddreißig) for 63 (dreiundsechzig), re-ask right · no help · sofort 5/5 → PASS · flags: reversal, placement pending
2. [P] CNT-09 Count by 10s to 100 · one run 10…100 · alone → PASS · placement pending
3. [P] AS-11 Make ten · parent-chosen items 8+5, 7+6, 9+4, 8+6, 6+7 · 5/5 · strategies reported 3: make ten (8+5, 9+4), counted on fingers (7+6) · help not said → ⚠ Q1
Leo · 2026-10-25 · note 1
4. [P] CRD-06 Give-N 1–3 · 2, 3, 1, 3, 2 · 5/5 (second 3: self-corrected 4 → 3) · help not said → ⚠ Q2
Questions:
1. Hattest du Mia bei den Plus-Aufgaben geholfen?
2. Und Leo beim Geben — Hilfe oder alleine?
Reply "ok", or correct any line.
```

## Parent: „Beide ohne Hilfe. ok“

## Assistant: what it writes
`inbox/2026-10-25-1.md` gets the transcript. `maps/math/log/mia.md` gets:
```
| L001 | 2026-10-25 | NUM-12 | P | parent-chosen: 36→36, 47→47, 59→59, 63→36 (re-ask 63), 81→81 | 4/5 +reask | none | – | sofort 5/5 | – | PASS | note 2026-10-25-1 |
| L002 | 2026-10-25 | CNT-09 | P | 10…100 | complete | none | – | – | – | PASS | note 2026-10-25-1 |
| L003 | 2026-10-25 | AS-11 | P | parent-chosen: 8+5, 7+6, 9+4, 8+6, 6+7 all right | 5/5 | none | make ten ×2, counted ×1, 2 unknown | – | – | DEV | note 2026-10-25-1 |
```
Why AS-11 is DEV: ST needs at least 3 reported strategies (3 ✓) and the target on at least 4 items with a reported strategy (only 2) → accuracy pass, strategy below target.

Mia's status table:
```
| NUM-12 | Developing | 2026-10-25 | 2026-10-25 | placement pending, reversal | L001 |
| CNT-09 | Developing | 2026-10-25 | 2026-10-25 | placement pending | L002 |
| AS-11 | Developing | – | 2026-10-25 | strategy | L003 |
```
Leo: `L001 CRD-06 P … PASS`, status Developing, placement pending.

## Assistant: report
```
## Mia — 2026-10-25
Changed: NUM-12, CNT-09 → Developing (placement pending; confirm with a fresh check from 2026-11-01) · AS-11 → Developing (strategy)
Placement next: NUM-08 write numerals to 100 (up from NUM-12) · CNT-17 count by 5s (up from CNT-09) · PW-10 bonds to 10 from memory (down from AS-11)
Next 3 to teach: 1) AS-11 make ten — accurate, but only 2 of 5 by making ten; 2) … (more after placement)
Gaps: none found yet; most nodes still unknown (placement)
Schule (PT 1.º ano): 0 of 48 covered, 3 in progress (PT-N02, PT-N03, PT-N13)

## Leo — 2026-10-25
Changed: CRD-06 Give-N 1–3 → Developing (placement pending)
Placement next: CRD-07 Give-N 1–5 · CNT-01 count to 5 · SUB-01 subitize 1–3
```
