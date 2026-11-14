# RULES.md — math map, map-specific rules (v6, 2026-11-06)

DESCRIBE. Read `maps/CONTRACT.md` first; this file only adds what is specific to math. Nothing here overrides the contract.

Versions: v4 2026-10-24 first; v5 2026-10-24 abbreviations spelled out, glossary; v6 2026-11-06 shared rules moved to CONTRACT.md, no rule changes.

## 1. Files
`TREE.md` (nodes + Portuguese 1.º ano shadow layer), `settings.md` (per-kid: placement mode, shadow curriculum, fluency rule), `example.md`, `log/<kid>.md`, `status/<kid>.md`. Look nodes up in `TREE.md` by ID when a note or report needs them.

## 2. Check rule codes

| Code | Rule |
|---|---|
| SEQ | The parent reports the whole sequence said in order, alone, at most 1 self-correction. Shows recitation, not understanding. |
| SEQx2 | Two runs from two issued start numbers; both meet SEQ. |
| SEQ+match | SEQ, plus one word per finger or object. |
| P5 | 5 items. PASS: 5/5, or 4/5 when the missed item was re-asked at the end and answered right. |
| P3 | 3 trials with different objects or sizes. PASS: 3/3, or 2/3 with a right re-ask. |
| E3 | 3 items, each answer plus „Wie hast du das gesehen / gewusst?“. PASS: 3 right and at least 2 explanations that name parts or a reason. |
| FL | P5 plus speed per item: sofort / kurz überlegt / gezählt. If `settings.md` says `Grade-1 fluency rule: on`, PASS needs P5 *and* "sofort, ohne Zählen" on at least 4 of 5; accuracy without speed = `DEV` with flag `fluency`. If off, speed is only a flag. |
| ST | P5 accuracy, plus after each answer „Wie hast du's gerechnet?“. PASS: the target strategy (or a more advanced one) on at least 4 of the items with a reported strategy, and at least 3 reported. "Didn't say" is unknown, never a fail. Accuracy with a lower strategy = `DEV` with flag `strategy`. |
| G2 | Two-option items (more/less, true/false), answers balanced. PASS: at least 9 of 10 across the last two counted checks, so guessing can't pass. A single check alone can at most be `DEV`. |
| NL | Child marks 5 numbers on a printed line; photo. PASS: mean percent absolute error ≤ 15% *(dd; loosened from 10% for grade 1)*. Measure: Siegler & Booth 2004. |
| OBS | Logged, never gates or unlocks. |

**Fresh material** means items the child has not seen in that node's last two checks. Self-made aids (her own 1–100 chart) are not hints unless the parent points to them.

**Math flags:** `fluency` (right, but not fast enough), `strategy` (right, but with a simpler strategy than the target), `reversal` (digit order flipped, 64 for 46, common with German number words).

**Number of the day** is a re-check format, not a skill: each sub-answer (before, after, parts, ten and some more) is credited to its own node.

## 3. Placement order and priorities
Strand order for placement and for "next 3": number strands first (CNT, CRD, SUB, CMP, NUM, PW, AS, PV), then the rest. Growth tracks: none in this map.

## 4. German narration
- Numbers: ones before tens (dreiundsechzig = 63). Watch dreizehn/dreißig, vierzehn/vierzig, fünfzehn/fünfzig, sechzehn/sechzig, siebzehn/siebzig, and „zwo“ = 2. In the claims-to-confirm message write every number 13 and above, and every 2-digit number, as digits *and* the German word the parent used (`63 (dreiundsechzig)`), because transcription confuses them.
- Time: „halb drei“ = 2:30.
- Speed words: „sofort / wie aus der Pistole“ = sofort; „hat kurz überlegt“ = paused; „hat gezählt / mit Fingern“ = counted.
- Help words: „ich hab geholfen / gezeigt / angetippt / einen Tipp gegeben“ = help. „Ohne Hilfe / alleine“ = no help. Silence about help = ask.
- Children's Portuguese answers (e.g. „sessenta e três“) count like German ones.

## 5. Glossary (math-only)
**Rule codes**: SEQ Reihe aufsagen, alleine, max. 1 Selbstkorrektur · SEQx2 zwei Reihen ab zwei Startzahlen · SEQ+match Reihe plus je ein Wort pro Finger/Gegenstand · P5 5 Aufgaben, 5/5 oder 4/5 mit richtiger Nachfrage · P3 3 Versuche, 3/3 oder 2/3 mit Nachfrage · E3 3 Aufgaben mit Begründung · FL 5 Aufgaben plus Tempo · ST 5 Aufgaben plus Rechenweg · G2 Entweder-oder, zwei Checks zusammen · NL Zahlenstrahl (Foto).
**Flags**: fluency = richtig, aber nicht schnell genug · strategy = richtig, aber einfachere Strategie · reversal = Ziffern vertauscht.
**Strands**: CNT Zählen, CRD Gegenstände zählen/Anzahl, SUB Simultanerfassung, CMP Vergleichen, NUM Ziffern und Zahlwörter, PW Zerlegen, AS Plus und Minus, PV Stellenwert, MUL Gruppen/Teilen, GEO Formen, POS Lage, PAT Muster, MEA Messen, TIM Zeit, MON Geld, DAT Daten.
