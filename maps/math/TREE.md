# TREE.md — Math skill tree (v5, 2026-11-07)

Versions: v4 2026-10-24 rebuilt on learning trajectories; v5 2026-11-07 column „Erklärung (DE)“ added (plain-language meaning with example, for parents); no node changes.

Shared by all kids. Changes rarely. Kid progress lives in `log/<kid>.md` and `status/<kid>.md`, never here.

## How to read this file

- **One table row = one skill node.** IDs are stable and never reused. v3 IDs were kept; v4 rebuilt the tree without Maths — No Problem!.
- **Order of skills** follows the Clements & Sarama learning trajectories (learningtrajectories.org); the strand header names the trajectory. Grade-1 checks lean on Fuchs (Number Rockets) and Krajewski ("Mengen, zählen, Zahlen").
- **Age** = age in years at which most children show the skill. A planning guide, not a deadline.
- **Track**
  - `core` — part of the mastery path. Gates its descendants.
  - `stretch` — beyond the grade-1 goal, or contested for grade 1. Tracked and gates its own descendants, but never counts as a gap.
  - `shadow` — only in the Portuguese curriculum. Tracked for the Schule report; never gates, never unlocks, never a gap.
  - `obs` — observation only. Logged, never gates.
- **Requires** = prerequisites. A node is *unlocked* when every prerequisite is Developing or better (see RULES.md).
- **Exercises** = Requires, unless stated. When a node is Mastered, every node it exercises becomes Mastered (inferred), recursively.
- **Rule** = check rule code, defined in RULES.md (SEQ, SEQx2, SEQ+match, P5, P3, E3, FL, ST, G2, NL, OBS).
- **Check (DE)** = what the parent says. Items in `…` come from the pool, fresh each time.
- **📷** = needs a photo of paper work.
- **PT** = Portuguese 1.º ano objective(s) this node serves (table at the end). `–` = none.
- **Erklärung (DE)** = what the skill means in plain German, with an example. For reading, never for scoring.

---

## CNT — Verbal counting · trajectory: Counting

| ID | Skill | Age | Track | Requires | Rule | Check (DE) | Pool / correct looks like | PT | Erklärung (DE) |
|---|---|---|---|---|---|---|---|---|---|
| CNT-01 | Rote count to 5 | 3 | core | – | SEQ | „Zähl mal bis fünf.“ | 1–5 in order | – | Sagt die Zahlwörter eins bis fünf der Reihe nach auf, wie ein Lied. Noch ohne Gegenstände. |
| CNT-02 | Rote count to 10 | 4 | core | CNT-01 | SEQ | „Zähl bis zehn.“ | 1–10 | – | Sagt eins bis zehn der Reihe nach auf, ohne Auslassen oder Vertauschen. |
| CNT-03 | Count to 10 on fingers, one word per finger | 4 | core | CNT-02 | SEQ+match | „Zähl mit den Fingern bis zehn.“ | one word per raised finger | – | Zählt bis zehn und klappt dabei pro Zahlwort genau einen Finger aus. Erstes Verbinden von Wort und Menge. |
| CNT-04 | Rote count to 20 | 5 | core | CNT-02 | SEQ | „Zähl bis zwanzig.“ | watch elf, zwölf, dreizehn–neunzehn | PT-N02 | Zählt bis zwanzig. Schwer sind elf, zwölf und die Dreizehn-bis-Neunzehn-Wörter. |
| CNT-05 | Number after, within 10, without starting at 1 | 5 | core | CNT-02 | P5 | „Welche Zahl kommt nach …?“ | 1–9; restarting from 1 = wrong | – | Weiß, welche Zahl nach einer anderen kommt (nach 6 kommt 7), ohne wieder bei eins anzufangen. |
| CNT-07 | Number before, within 10 | 5 | core | CNT-05 | P5 | „Welche Zahl kommt vor …?“ | 2–10 | – | Weiß, welche Zahl vor einer anderen kommt (vor 8 kommt 7). Schwerer als „danach“. |
| CNT-06 | Count back from 10 to 0 | 5 | core | CNT-02 | SEQ | „Zähl rückwärts von zehn bis null.“ | 10…0 | PT-N02 | Zählt von zehn rückwärts bis null, wie beim Raketenstart. |
| CNT-14 | Count on from any number within 20 | 5 | core | CNT-04, CNT-05 | SEQx2 | „Zähl weiter ab …“ (stop after 6 numbers) | starts 4–14 | PT-N02 | Kann mitten in der Reihe einsteigen: „Zähl weiter ab 14“ → 15, 16, 17 … |
| CNT-11 | Count back from any number within 20 | 6 | core | CNT-06, CNT-04 | SEQx2 | „Zähl rückwärts ab …“ (6 numbers) | starts 9–20; one run crosses 10 | PT-N02 | Zählt von einer beliebigen Zahl unter 20 rückwärts: „ab 16“ → 15, 14, 13 … Wichtig fürs Minusrechnen. |
| CNT-15 | Decade transitions and decade names | 6 | core | CNT-04 | P5 | „Was kommt nach neunundzwanzig?“ | x9 → next decade, 19…89 | – | Weiß, was nach 29, 39, 49 kommt (30, 40, 50) und kennt die Zehnernamen dreißig, vierzig, fünfzig … |
| CNT-08 | Count across decades to 100 | 6 | core | CNT-15 | SEQx2 | „Zähl weiter ab … bis …“ | e.g. 56→72, 87→100 | PT-N02 | Zählt über Zehnergrenzen bis 100 weiter, z. B. ab 56 bis 72, ohne Stocken bei 59 → 60. |
| CNT-13 | Count back across decades within 100 | 6 | core | CNT-08, CNT-11 | SEQx2 | „Zähl rückwärts ab … bis …“ | e.g. 63→48 | PT-N02 | Zählt im Hunderterraum rückwärts über eine Zehnergrenze, z. B. ab 63 bis 48 (62, 61, 60, 59 …). |
| CNT-09 | Count by 10s to 100 | 6 | core | CNT-15 | SEQ | „Zähl in Zehnerschritten bis hundert.“ | 10…100 | PT-N02 | Zählt in Zehnerschritten: 10, 20, 30 … bis 100. |
| CNT-10 | Count by 10s from any number | 6 | core | CNT-09, PV-02 | SEQx2 | „Zähl in Zehnern ab dreiundzwanzig.“ | start off-decade, up to <100 | PT-N02, PT-A09 | Zählt in Zehnern ab einer krummen Zahl: 23, 33, 43, 53 … Zeigt, dass sie den Zehner als Einheit sieht. |
| CNT-16 | Skip count by 2s to 20 | 6 | core | CNT-04 | SEQ | „Zähl in Zweierschritten bis zwanzig.“ | 2…20 | PT-N02 | Zählt in Zweierschritten: 2, 4, 6 … bis 20. |
| CNT-17 | Skip count by 5s to 100 | 6 | core | CNT-09 | SEQ | „Zähl in Fünferschritten bis hundert.“ | 5…100 | PT-N02 | Zählt in Fünferschritten: 5, 10, 15 … bis 100. |
| CNT-18 | Count beyond 100 to 120 | 7 | stretch | CNT-08 | SEQx2 | „Zähl weiter ab siebenundneunzig.“ | starts 95–99, run to ~112 | – | Zählt über 100 hinaus weiter: 98, 99, 100, 101, 102 … bis etwa 120. |

## CRD — Counting objects and cardinality · trajectory: Counting (objects); Krajewski levels 1–2

| ID | Skill | Age | Track | Requires | Rule | Check (DE) | Pool / correct looks like | PT | Erklärung (DE) |
|---|---|---|---|---|---|---|---|---|---|
| CRD-01 | Count 1–3 objects, one word per object | 3 | core | CNT-01 | P3 | „Zähl die Bären.“ | touches each once | – | Zählt zwei oder drei Dinge und tippt dabei jedes genau einmal an. Kein Ding doppelt, keins ausgelassen. |
| CRD-02 | Says the last number as "how many" | 3 | obs | CRD-01 | OBS | after counting: „Wie viele sind es?“ | can be a rote reply — never gates | – | Antwortet nach dem Zählen auf „Wie viele?“ mit der zuletzt gesagten Zahl, statt nochmal zu zählen. Nur Beobachtung. |
| CRD-06 | Give-N 1–3 | 3 | core | – | P5 | „Gib mir zwei Bären in die Tasse.“ | N 1–3, mixed order, pile of 10 | – | Gibt auf Bitte genau 1, 2 oder 3 Dinge aus einem Haufen, und hört dann auf. Zeigt: Zahl heißt Menge. |
| CRD-07 | Give-N 1–5 | 4 | core | CRD-06, CRD-01 | P5 | same, N 1–5 | every check includes 4 and 5 | – | Dasselbe mit bis zu fünf: „Gib mir vier Bären“ → zählt vier ab und stoppt. |
| CRD-04 | Count a row of up to 10 | 4 | core | CRD-01, CNT-02 | P3 | „Wie viele Steine liegen hier?“ | rows of 6–10 | – | Zählt eine Reihe von bis zu zehn Dingen richtig durch. |
| CRD-03 | Count a scattered set to 10, keeping track | 5 | core | CRD-04 | P3 | scatter 6–10: „Wie viele?“ | marks or moves counted ones | – | Zählt bis zu zehn durcheinanderliegende Dinge und behält den Überblick, z. B. indem sie Gezähltes beiseite schiebt. |
| CRD-08 | Give-N 5–8 (cardinality gate) | 4 | core | CRD-07, CRD-04 | P5 | „Gib mir sieben Bären.“ (pile of 15) | N 5–8; counts out and stops | – | Gibt auf Bitte 5 bis 8 Dinge aus einem großen Haufen. Der wichtigste Test dafür, dass Zahlen Mengen bedeuten. |
| CRD-05 | Conservation: same number after spreading | 5 | core | CRD-03 | P3 | count 7, spread them out: „Wie viele jetzt?“ | answers without recounting | – | Weiß, dass es gleich viele bleiben, wenn man die Dinge auseinanderschiebt. Sagt „immer noch sieben“ ohne nachzuzählen. |
| CRD-12 | Order irrelevance | 5 | core | CRD-03 | E3 | „Wenn du hier anfängst — wie viele sind es dann?“ | same total, says why | – | Versteht, dass es egal ist, bei welchem Ding man zu zählen anfängt – es kommt dieselbe Zahl raus. |
| CRD-10 | Count a set to 20 | 5 | core | CRD-03, CNT-04 | P3 | scatter 12–20: „Wie viele?“ | keeps track | PT-N02 | Zählt 12 bis 20 durcheinanderliegende Dinge richtig. |
| CRD-09 | Count out N up to 20 from a larger pile | 5 | core | CRD-08, CNT-04 | P3 | „Leg mir fünfzehn Steine hin.“ | N 11–20 | – | Legt auf Bitte eine genaue Anzahl bis 20 hin: „Leg mir fünfzehn Steine hin.“ |
| CRD-11 | Count up to 50 objects by grouping in tens | 6 | core | CRD-10, CNT-09 | P3 | „Wie viele? Ordne sie so, dass du gut zählen kannst.“ | makes 10-groups, counts tens then ones | PT-N07 | Zählt 30 bis 50 Dinge, indem sie Zehnergruppen bildet und dann 10, 20, 30 … zählt, statt eins nach dem anderen. |

## SUB — Subitizing · trajectory: Subitizing

Flash cards are shown for about 2 seconds.

| ID | Skill | Age | Track | Requires | Rule | Check (DE) | Pool / correct looks like | PT | Erklärung (DE) |
|---|---|---|---|---|---|---|---|---|---|
| SUB-01 | Perceptual subitize 1–3 | 3 | core | – | P5 | flash card: „Wie viele?“ | 1–3, varied layouts | – | Sieht auf einen Blick, ob es 1, 2 oder 3 Punkte sind, ohne zu zählen. |
| SUB-02 | Perceptual subitize to 5 | 4 | core | SUB-01 | FL | flash dot card | 1–5; dice and random layouts | PT-N02 | Erkennt bis zu fünf Punkte auf einen Blick, auch in ungewohnter Anordnung, nicht nur das Würfelbild. |
| SUB-04 | Five-frame 0–5 at a glance | 4 | core | SUB-02 | FL | flash Fünferfeld | 0–5 | PT-N02 | Erkennt im Fünferfeld (eine Reihe mit fünf Kästchen) auf einen Blick, wie viele gefüllt sind. |
| SUB-03 | Finger patterns to 10 at a glance | 5 | core | CNT-03, SUB-02 | FL | „Zeig mir sieben Finger — schnell!“ / parent shows fingers: „Wie viele?“ | no one-by-one counting | – | Zeigt sieben Finger in einem Rutsch (5 und 2), statt einzeln hochzuzählen; erkennt gezeigte Fingerzahlen sofort. |
| SUB-06 | Conceptual subitize to 10 | 5 | core | SUB-02, PW-02 | E3 | flash two dice: „Wie viele? Wie hast du's gesehen?“ | names the parts („4 und 3“) | – | Sieht zwei Würfel (4 und 3) und sagt „sieben – vier und drei“. Erkennt Mengen als Teile. Grundlage fürs Kopfrechnen. |
| SUB-05 | Ten-frame 6–10 as five and some | 5 | core | SUB-04, PW-03 | FL | flash Zehnerfeld | 6–10 | PT-N02, PT-N12 | Sieht im Zehnerfeld 8 als „fünf und drei“ auf einen Blick. |
| SUB-07 | Twenty-frame / 20-bead string in 5s and 10s | 6 | core | SUB-05, PW-07 | FL | show Rechenkette or Zwanzigerfeld: „Wie viele?“ | 11–20 | PT-N02 | Liest an der Rechenkette oder im Zwanzigerfeld Zahlen wie 13 als „zehn und drei“ ab, ohne einzeln zu zählen. |

## CMP — Comparing, ordering, estimating · trajectory: Comparing, Ordering, Estimating

| ID | Skill | Age | Track | Requires | Rule | Check (DE) | Pool / correct looks like | PT | Erklärung (DE) |
|---|---|---|---|---|---|---|---|---|---|
| CMP-01 | More, by looking (very different sets) | 3 | core | – | G2 | „Wo sind mehr?“ | ratio at least 1:2 | – | Sieht bei deutlich verschiedenen Haufen (3 gegen 9) sofort, wo mehr ist. |
| CMP-02 | Compare two sets to 10 by matching or counting | 5 | core | CRD-03 | G2 | „Wo sind mehr — oder gleich viele?“ | close pairs, some equal; bigger objects in the smaller set | – | Vergleicht ähnliche Mengen (6 gegen 7), indem sie zählt oder paarweise zuordnet. Erkennt auch „gleich viele“. |
| CMP-03 | Compare two numbers to 10 (no objects) | 5 | core | NUM-02, CNT-05 | G2 | „Was ist mehr, sieben oder vier?“ | balanced | PT-N04 | Weiß ohne Gegenstände, dass 7 mehr ist als 4. |
| CMP-04 | One more / one less within 10 | 5 | core | CNT-05, CNT-07 | P5 | „Was ist eins mehr als sechs?“ | mix more and less | PT-N12 | Sagt, was eins mehr oder eins weniger als eine Zahl bis 10 ist. |
| CMP-07 | Place numbers on a 0–10 line | 5 | core | NUM-02, CMP-03 | NL | printed 0–10 line, mark 5 numbers 📷 | | PT-N03 | Trägt Zahlen auf einem leeren Zahlenstrahl von 0 bis 10 ungefähr an der richtigen Stelle ein (5 in der Mitte). |
| CMP-11 | Compare numbers to 20 | 5 | core | CMP-03, NUM-04 | G2 | „Was ist mehr, vierzehn oder siebzehn?“ | include teen vs one-digit | PT-N04 | Vergleicht Zahlen bis 20: 14 oder 17, 9 oder 12. |
| CMP-05 | One more / one less within 20 | 5 | core | CMP-04, CNT-14 | P5 | „Eins weniger als vierzehn?“ | include 10, 11, 19, 20 | PT-N10 | Eins mehr oder weniger bis 20, auch über die 10 hinweg (eins weniger als 11 ist 10). |
| CMP-09 | Order 4 numbers to 20 | 6 | core | CMP-11 | P5 | cards: „Leg sie der Größe nach — dann rückwärts.“ | 5 sets | PT-N04 | Legt vier Zahlenkarten bis 20 der Größe nach, vorwärts und rückwärts. |
| CMP-13 | Use <, >, = | 6 | core | CMP-11 | G2 | „Welches Zeichen passt?“ | balanced | PT-N04 | Setzt die Zeichen <, > und = richtig zwischen zwei Zahlen. |
| CMP-14 | Estimate a set to 20, then check | 6 | core | CRD-10, CMP-11 | P3 | show set 2 s: „Ungefähr wie viele?“ then count | within ±25% | PT-N07 | Schätzt eine Menge bis 20 nach kurzem Hinsehen („ungefähr 15“) und prüft dann durch Zählen. |
| CMP-06 | Compare 2-digit numbers | 6 | core | PV-02 | G2 | „Was ist mehr, 34 oder 43?“ | include reversed pairs | PT-N04, PT-N08 | Vergleicht zweistellige Zahlen, auch mit vertauschten Ziffern: 34 oder 43? |
| CMP-10 | Order numbers to 100 | 6 | core | CMP-06, CMP-09 | P5 | cards, 4 numbers per item | | PT-N04 | Ordnet vier Zahlen bis 100 der Größe nach. |
| CMP-12 | 10 more / 10 less within 100 | 6 | core | CNT-10, PV-02 | P5 | „Zehn mehr als siebenundvierzig?“ | | PT-A09 | Sagt, was zehn mehr oder zehn weniger ist: 47 → 57 / 37. |
| CMP-08 | Place numbers on a 0–100 line | 6 | core | CMP-06, CNT-08 | NL | printed 0–100 line, mark 5 numbers 📷 | | PT-N03 | Trägt Zahlen auf einem Zahlenstrahl von 0 bis 100 ungefähr richtig ein (50 in der Mitte, 90 fast am Ende). |

## NUM — Numerals and number words · trajectory: Counting / Comparing (numerals)

German says ones before tens ("sechsundvierzig" = 46). Every 2-digit pool includes a reversed pair.

| ID | Skill | Age | Track | Requires | Rule | Check (DE) | Pool / correct looks like | PT | Erklärung (DE) |
|---|---|---|---|---|---|---|---|---|---|
| NUM-09 | Point to numerals 0–5 | 3 | core | – | P5 | lay out 3 cards: „Zeig mir die Drei.“ | | – | Zeigt auf die richtige Ziffer, wenn man eine Zahl von 0 bis 5 nennt. |
| NUM-01 | Name numerals 0–5 | 3 | core | NUM-09 | P5 | card: „Welche Zahl ist das?“ | | – | Benennt die Ziffern 0 bis 5, wenn man sie zeigt. |
| NUM-02 | Name numerals 0–10 | 4 | core | NUM-01 | FL | same, cards 0–10 | every numeral across the window; 6/9 and 2/5 in every check | PT-N03 | Benennt alle Ziffern 0 bis 10, auch 6 und 9 sicher auseinander. |
| NUM-03 | Match numeral to quantity | 4 | core | NUM-02, CRD-08 | P5 | numeral card + dot cards: „Welche Punkte passen?“ | | PT-N01 | Ordnet einer Ziffernkarte die passende Punktekarte zu: zur 6 die sechs Punkte. |
| NUM-04 | Name numerals 11–20 | 5 | core | NUM-02, CNT-04 | FL | cards 11–20 | 12 and 17 in every check | PT-N03 | Liest 11 bis 20, besonders 12 und 17. |
| NUM-05 | Write numerals 0–10 | 5 | core | NUM-02 | P5 | „Schreib die Zahl …“ 📷 | mirror-written digit = right before age 7, but flag it | PT-N03 | Schreibt die Ziffern 0 bis 10 nach Ansage. Spiegelverkehrte Ziffern sind mit 6 noch normal. |
| NUM-10 | Write numerals 11–20 | 5 | core | NUM-04, NUM-05 | P5 | „Schreib vierzehn.“ 📷 | 41 for 14 = wrong | PT-N03 | Schreibt 11 bis 20 nach Ansage, ohne die Ziffern zu vertauschen (14, nicht 41). |
| NUM-19 | Ordinals first to tenth | 5 | core | CNT-02 | P5 | line up 10 toys: „Welches ist das vierte?“ | | PT-N01, PT-N05 | Kennt erster, zweiter, dritter … bis zehnter: „Welches Auto ist das vierte?“ |
| NUM-11 | Name decade numerals 10–90 | 6 | core | NUM-04, CNT-15 | FL | cards 10, 20 … 90 | dreißig, siebzig | PT-N03 | Liest die Zehnerzahlen 10, 20, 30 … 90 (dreißig, siebzig). |
| NUM-18 | Odd and even to 20 | 6 | core | CNT-16, CRD-03 | E3 | „Ist sieben gerade oder ungerade? Woran siehst du das?“ | explains by pairs | PT-N06 | Weiß, ob eine Zahl bis 20 gerade oder ungerade ist, und erklärt es über Paare. |
| NUM-21 | Read number words to twenty (German) | 6 | core | NUM-04 | P5 | word card: „Was steht da?“ | | – | Liest Zahlwörter als Wort: „vierzehn“, „neun“. |
| NUM-22 | Write number words to twenty (German) | 6 | stretch | NUM-21 | P5 | „Schreib das Wort für neun.“ 📷 | depends on spelling | – | Schreibt Zahlwörter als Wort. Hängt an der Rechtschreibung, deshalb kein Kernskill. |
| NUM-12 | Name numerals 21–99 | 6 | core | NUM-11, CNT-08 | FL | cards 21–99 | one reversed pair per check (36 / 63) | PT-N03 | Liest alle Zahlen 21 bis 99. Bei deutschen Zahlwörtern wird leicht 36 und 63 vertauscht. |
| NUM-08 | Write numerals to 100 from dictation | 6 | core | NUM-12, NUM-10 | P5 | „Schreib sechsundvierzig.“ 📷 | 64 for 46 = wrong, note "reversal" | PT-N03 | Schreibt zweistellige Zahlen nach Ansage: „sechsundvierzig“ → 46, nicht 64. |
| NUM-20 | Estimate a quantity under 100 | 6 | core | PV-02, CMP-14 | P3 | jar or pile: „Ungefähr wie viele? Warum?“ then count in tens | within ±25%, gives a reason | PT-N07 | Schätzt eine Menge unter 100 (ein Glas Bohnen) mit Begründung und prüft dann in Zehnern. |
| NUM-13 | Name 3-digit numbers, no zeros | 7 | stretch | NUM-12, PV-04 | FL | e.g. 347 | | – | Liest dreistellige Zahlen ohne Null: 347. |
| NUM-14 | 3-digit numbers with an inner zero | 7 | stretch | NUM-13, PV-05 | P5 | e.g. 405 | | – | Liest dreistellige Zahlen mit Null in der Mitte: 405. Die Null wird oft weggelassen. |
| NUM-15 | 3-digit numbers ending in zero | 7 | stretch | NUM-13 | P5 | e.g. 610 | | – | Liest dreistellige Zahlen mit Null am Ende: 610. |
| NUM-16 | Name 1000 | 7 | stretch | NUM-14, NUM-15 | P5 | mixed with 100, 999 | | – | Kennt die Tausend und unterscheidet sie von 100 und 999. |
| NUM-17 | Write numbers to 1000 | 7 | stretch | NUM-14, NUM-08 | P5 | „Schreib vierhundertfünf.“ 📷 | | – | Schreibt Zahlen bis 1000 nach Ansage. |

## PW — Composing and decomposing numbers · trajectory: Composing Number; Krajewski level 3

| ID | Skill | Age | Track | Requires | Rule | Check (DE) | Pool / correct looks like | PT | Erklärung (DE) |
|---|---|---|---|---|---|---|---|---|---|
| PW-01 | Parts of 3 and 4 (hiding game) | 4 | core | CRD-07 | P5 | 4 stones, cover some: „Wie viele sind versteckt?“ | wholes 3–4 | – | Versteckspiel mit 3 oder 4 Steinen: sieht 1, weiß, dass 2 versteckt sind. Erste Zerlegung. |
| PW-02 | Parts of 5 | 4 | core | PW-01, CRD-08 | P5 | same with 5 | all splits across the window | PT-N11 | Kennt alle Zerlegungen der 5: 1+4, 2+3, 3+2, 4+1, 5+0. Wenn 2 Steine zu sehen sind, sind 3 versteckt. |
| PW-06 | Doubles to 5+5 | 5 | core | CRD-08 | FL | „Wie viel ist drei und drei?“ | 1+1 … 5+5 | PT-N12 | Verdoppeln bis 5+5: „drei und drei?“ → sechs, ohne Zählen. |
| PW-03 | Five and some (6–10 as 5 + n) | 5 | core | PW-02, SUB-04 | P5 | „Acht ist fünf und …?“ | | PT-N12 | Sieht 6 bis 10 als „fünf und noch etwas“: 8 ist fünf und drei. |
| PW-05 | Missing part within 10 | 5 | core | PW-02 | P5 | „Acht Steine, drei siehst du — wie viele sind versteckt?“ | wholes 6–10 | PT-N09 | Findet den fehlenden Teil bis 10: 8 Steine, 3 sichtbar → 5 versteckt. |
| PW-04 | Bonds to 10 with objects | 5 | core | PW-03 | P5 | Zehnerfeld: „Wie viele fehlen bis zehn?“ | all pairs across the window | PT-N11 | Weiß mit Material, wie viel bis zehn fehlt: 7 Plättchen im Zehnerfeld → 3 fehlen. |
| PW-11 | All splits of a number 6–10, systematically | 5 | core | PW-05 | E3 | „Finde alle Arten, sieben zu zerlegen.“ | all but one at most; explains the order | PT-N09 | Findet alle Zerlegungen einer Zahl von 6 bis 10 und ordnet sie (7 = 0+7, 1+6, 2+5 …). |
| PW-07 | Teens as ten and some | 5 | core | PW-04, NUM-04 | P5 | „Vierzehn ist zehn und …?“ / „Zehn und sechs?“ | | PT-N08, PT-N09 | Sieht 11 bis 19 als „zehn und noch etwas“: 14 ist zehn und vier. |
| PW-08 | Missing addend, symbolic (3 + __ = 8) | 6 | core | PW-05 | P5 | „Drei plus wie viel ist acht?“ | | PT-A07 | Löst Lückenaufgaben: 3 + __ = 8. |
| PW-10 | Bonds to 5 and 10 from memory | 6 | core | PW-04 | FL | „Wie viel fehlt von drei bis zehn?“ | straight away | PT-N11 | Kennt die Fünfer- und Zehnerpartner auswendig: 3 fehlt bis 10 → 7, sofort. |
| PW-12 | Near doubles within 10 (4+5) | 6 | core | PW-06 | ST | „Vier plus fünf? Wie hast du's gerechnet?“ | target: double ± 1 | PT-N13 | Rechnet 4+5 über das Verdoppeln: 4+4 ist 8, also 9. |
| PW-09 | Doubles to 10+10 | 6 | core | PW-06, PW-07 | FL | „Sieben und sieben?“ | 6+6 … 10+10 | PT-N09 | Verdoppeln bis 10+10: „sieben und sieben?“ → vierzehn. |
| PW-13 | Relate numbers to 5, 10, 15, 20 (±1, ±2) | 6 | core | PW-03, PW-07 | P5 | „Zwei mehr als fünfzehn?“ / „Wie weit ist neun von zehn?“ | | PT-N10 | Nutzt 5, 10, 15 und 20 als Anker: zwei mehr als 15, wie weit ist 9 von 10. |
| PW-14 | Decompose numbers to 20 in several ways | 6 | core | PW-07, PW-11 | E3 | „Zeig mir fünfzehn auf drei Arten.“ | e.g. 10+5, 7+7+1, 9+6 | PT-N09 | Zerlegt Zahlen bis 20 auf mehrere Arten: 15 = 10+5 = 7+7+1 = 9+6. |
| PW-15 | Decompose 2-digit numbers (46 = 40+6 = 30+16) | 6 | core | PV-03 | E3 | „Zerleg sechsundvierzig auf zwei Arten.“ | | PT-N09 | Zerlegt zweistellige Zahlen: 46 = 40+6, aber auch 30+16. Vorbereitung auf Minus mit Übertrag. |

## AS — Adding and subtracting · trajectory: Adding and Subtracting (story types from CGI)

Story checks use neutral names, never the kids' own.

| ID | Skill | Age | Track | Requires | Rule | Check (DE) | Pool / correct looks like | PT | Erklärung (DE) |
|---|---|---|---|---|---|---|---|---|---|
| AS-01 | Join small sets with objects (total ≤ 5) | 4 | core | CRD-07 | P5 | „Du hast zwei, ich geb dir zwei. Wie viele hast du?“ | | – | Legt Mengen zusammen und zählt das Ergebnis: 2 Bären und 2 Bären sind 4. |
| AS-02 | Take away with objects (≤ 5) | 4 | core | CRD-07 | P5 | „Du hast fünf, ich nehm zwei weg.“ | | – | Nimmt von einer kleinen Menge etwas weg und zählt den Rest. |
| AS-20 | Zero: none left | 5 | core | CNT-06 | P5 | „Drei Bären, alle drei gehen weg — wie viele bleiben?“ | | PT-A10 | Versteht Null: wenn alle drei weggehen, bleibt keiner. |
| AS-03 | Add hidden sets (≤ 5) | 4 | core | AS-01 | P5 | show 2, cover, slide 1 under: „Wie viele sind drunter?“ | | – | Rechnet mit versteckten Mengen: 2 unter dem Tuch, 1 kommt dazu → 3 drunter, ohne nachzusehen. |
| AS-07 | Add within 10 with objects or fingers | 5 | core | AS-01, NUM-02, CRD-08 | P5 | „Vier und drei — wie viele?“ (objects allowed) | counting all is fine | PT-N17 | Addiert bis 10 mit Gegenständen oder Fingern. Alles abzählen ist hier noch in Ordnung. |
| AS-08 | Take away within 10 with objects | 5 | core | AS-02, CRD-08 | P5 | „Du hast neun, vier gehen weg.“ | | PT-N18 | Subtrahiert bis 10 mit Gegenständen: 9 Steine, 4 weg, 5 bleiben. |
| AS-13 | Join and take-away stories within 10 | 5 | core | AS-07, AS-08 | P5 | „Tom hat sechs Äpfel und isst zwei …“ | mix join and take-away | PT-N17, PT-N18 | Löst kleine Rechengeschichten bis 10 (Tom hat 6 Äpfel, isst 2) und erkennt, ob plus oder minus. |
| AS-04 | Count on from the first addend (big first) | 5 | core | AS-07, CNT-14 | ST | „Sieben plus zwei? Wie hast du's gerechnet?“ | items big-first; target: counting on | – | Zählt beim Addieren vom ersten Summanden weiter: 7+2 → „acht, neun“, statt bei eins anzufangen. |
| AS-15 | Commutativity (3+7 = 7+3 without calculating) | 6 | core | AS-07 | E3 | „Drei plus sieben ist zehn. Was ist sieben plus drei? Woher weißt du das?“ | | PT-A10 | Weiß ohne Rechnen: wenn 3+7 = 10, dann auch 7+3 = 10. Tauschaufgabe. |
| AS-16 | Count on from the larger addend | 6 | core | AS-04, AS-15 | ST | „Zwei plus sieben?“ | items small-first; target: starts at the bigger number | – | Beginnt beim größeren Summanden, auch wenn er hinten steht: 2+7 → „acht, neun“. |
| AS-05 | Count on within 20 | 6 | core | AS-16, CNT-14 | ST | „Dreizehn plus vier?“ | target: counting on or better | PT-N13 | Zählt bis 20 weiter: 13+4 → 14, 15, 16, 17. |
| AS-06 | Count back to subtract (small subtrahend) | 6 | core | CNT-11, AS-08 | ST | „Zwölf minus drei?“ | target: counting back or better | – | Zählt rückwärts zum Subtrahieren: 12−3 → 11, 10, 9. |
| AS-17 | Zero in + and − (n+0, n−0, n−n) | 6 | core | AS-07, AS-08 | P5 | „Acht minus acht?“ | | PT-A10 | Kennt die Regeln mit Null: 8+0, 8−0, 8−8. |
| AS-09 | Use known bonds to add and subtract within 10 | 6 | core | PW-05, AS-07 | ST | „Zehn minus vier?“ | target: bond or just knew | PT-N11 | Nutzt bekannte Zerlegungen zum Rechnen bis 10: 10−4 ist 6, weil 6+4 = 10. |
| AS-19 | Subtraction as a missing addend | 6 | core | PW-08, AS-09 | ST | „Neun minus sieben?“ | target: adds up or uses a bond | PT-N19 | Rechnet Minus als Ergänzen: 9−7 → „von 7 bis 9 sind 2“. |
| AS-30 | Fact families within 10 and 20 | 6 | core | AS-19 | P5 | „Drei plus fünf ist acht. Welche Minus-Aufgaben stecken darin?“ | | PT-N11, PT-N19 | Kennt Aufgabenfamilien: aus 3+5 = 8 folgen 5+3, 8−3 und 8−5. |
| AS-10 | Derived facts via doubles and near doubles | 6 | core | PW-12, AS-09 | ST | „Sechs plus sieben?“ | target: double ± 1 | PT-N13 | Leitet aus Verdopplungen ab: 6+7 ist 6+6+1 = 13. |
| AS-12 | Facts within 10, fluent | 6 | core | AS-09, PW-10 | FL | mixed + and − within 10 | | PT-N12 | Plus und Minus bis 10 kommen sofort, ohne Zählen. Das Ziel von Klasse 1. |
| AS-11 | Make ten (8+5 = 8+2+3) | 6 | core | PW-10, PW-07 | ST | „Acht plus fünf?“ | target: make ten | PT-N13 | Rechnet über die 10 mit Zehnerstopp: 8+5 = 8+2+3 = 13. |
| AS-27 | Add ones to a teen number (13+4) | 6 | core | PW-07, AS-12 | ST | „Dreizehn plus vier?“ | target: 3+4, then the ten | PT-N13 | Addiert Einer zu einer Zehnerzahl: 13+4 → 3+4 = 7, also 17. |
| AS-28 | Subtract ones from a teen number (17−4) | 6 | core | PW-07, AS-12 | ST | „Siebzehn minus vier?“ | target: 7−4, then the ten | PT-N13 | Subtrahiert Einer von einer Zehnerzahl: 17−4 → 7−4 = 3, also 13. |
| AS-29 | Subtract across ten (14−6) | 6 | core | AS-11, AS-19 | ST | „Vierzehn minus sechs?“ | target: via ten, or adds up | PT-N13 | Subtrahiert über die 10: 14−6 = 14−4−2 = 8, oder ergänzt von 6 bis 14. |
| AS-18 | Equal sign means "same as" | 6 | core | PW-08, AS-15 | P5 | „Stimmt das: 4+3 = 5+2?“ / „4+3 = __ + 2“ | mix true/false and open; one compensation item | PT-A07 | Versteht das Gleichheitszeichen als „ist gleich viel wie“, nicht als „jetzt kommt das Ergebnis“: 4+3 = 5+2 stimmt. |
| AS-21 | Compare story: how many more (within 10) | 6 | core | AS-13, CMP-02 | P5 | „Ana hat sieben, Ben hat vier. Wie viele mehr hat Ana?“ | | PT-N18 | Löst Vergleichsgeschichten: Ana hat 7, Ben hat 4 – wie viele mehr hat Ana? |
| AS-22 | Part-part-whole story, missing part (≤ 20) | 6 | core | AS-13, PW-05 | P5 | „Zwölf Kinder, fünf sind Jungs. Wie viele Mädchen?“ | | PT-N17, PT-N18 | Teil-Ganzes-Geschichten: 12 Kinder, 5 sind Jungs – wie viele Mädchen? |
| AS-23 | Difference to 20 (how many more / fewer) | 6 | core | AS-21 | P5 | „Wie viele mehr sind 17 als 12?“ | | PT-N18 | Findet den Unterschied zwischen zwei Zahlen bis 20: 17 und 12 → 5. |
| AS-24 | Change-unknown story | 6 | core | AS-22, PW-08 | P5 | „Tom hatte fünf, bekam welche dazu, jetzt hat er neun.“ | | PT-N18 | Geschichten mit unbekannter Veränderung: Tom hatte 5, bekam welche dazu, jetzt hat er 9 – wie viele kamen dazu? |
| AS-33 | Make up a story for a number sentence | 6 | core | AS-13 | E3 | „Erzähl eine Geschichte zu 8 = 6 + 2.“ | story matches the sentence | PT-A08 | Erfindet selbst eine Geschichte zu einer Aufgabe wie 8 = 6+2. Zeigt Verständnis statt Auswendiglernen. |
| AS-14 | Add three numbers within 20 | 6 | core | AS-11 | ST | „Sieben plus vier plus drei?“ | target: make ten first | – | Addiert drei Zahlen und macht dabei zuerst zehn voll: 7+4+3 → 7+3 = 10, +4. |
| AS-36 | Estimate a sum (more or less than 20?) | 6 | core | AS-11, CMP-11 | G2 | „Fünfzehn plus acht — mehr oder weniger als zwanzig?“ | | PT-N16 | Schätzt ein Ergebnis grob ab: 15+8 – mehr oder weniger als 20? |
| AS-25 | Add and subtract tens (30+20, 34+20) | 6 | core | PV-03, CNT-10 | ST | „Vierunddreißig plus zwanzig?“ | target: tens as units | PT-N13 | Rechnet mit ganzen Zehnern: 30+20, 34+20. |
| AS-26 | 2-digit + 1-digit across a ten (38+5) | 6 | core | AS-11, PV-02 | ST | „Achtunddreißig plus fünf?“ | target: to the next ten | PT-N13 | Zweistellig plus einstellig über den Zehner: 38+5 → 38+2+3 = 43. |
| AS-34 | 2-digit ± 2-digit, no crossing (32+24) | 7 | stretch | AS-25 | ST | „Zweiunddreißig plus vierundzwanzig?“ | | PT-N13 | Zweistellig plus zweistellig ohne Übertrag: 32+24. |
| AS-35 | 2-digit ± 2-digit with crossing, by jumps or compensation (54+27) | 7 | stretch | AS-34, AS-26 | ST | „Vierundfünfzig plus siebenundzwanzig?“ | | PT-N13 | Zweistellig plus zweistellig mit Übertrag, im Kopf durch Sprünge oder Ausgleich: 54+27 = 54+30−3. Klasse 2. |
| AS-37 | Show a calculation on an empty number line | 7 | stretch | AS-25, CMP-08 | P3 | „Zeig achtunddreißig plus fünf mit Sprüngen.“ 📷 | | PT-N14 | Zeigt eine Rechnung als Sprünge auf dem leeren Zahlenstrahl. |
| AS-31 | Start-unknown story | 7 | stretch | AS-24 | P5 | „Tom hatte welche, bekam drei, jetzt elf.“ | | PT-N18 | Geschichten mit unbekanntem Anfang: Tom hatte welche, bekam 3, jetzt hat er 11. Die schwerste Geschichtenart. |
| AS-32 | Two-step story within 20 | 7 | stretch | AS-24 | P3 | | | PT-N18 | Geschichten mit zwei Rechenschritten bis 20. |

## PV — Place value · trajectory: Composing Number (multidigit)

| ID | Skill | Age | Track | Requires | Rule | Check (DE) | Pool / correct looks like | PT | Erklärung (DE) |
|---|---|---|---|---|---|---|---|---|---|
| PV-01 | Bundle 10 ones into a ten | 6 | core | PW-07, CRD-10 | E3 | „Bündel die Stäbchen. Wie viele Bündel, wie viele einzeln?“ | | PT-N08 | Bündelt zehn Einzelne zu einem Zehner und sagt, wie viele Bündel und wie viele Einzelne es sind. |
| PV-02 | Tens and ones in 2-digit numbers | 6 | core | PV-01, CNT-09 | P5 | „Sechsundvierzig — wie viele Zehner, wie viele Einer?“ | | PT-N08 | Weiß bei 46: vier Zehner, sechs Einer. |
| PV-07 | Build and read 2-digit numbers with base-10 material | 6 | core | PV-02, NUM-12 | P5 | „Leg dreiundfünfzig.“ / „Welche Zahl liegt hier?“ | | PT-N03, PT-N08 | Legt eine zweistellige Zahl mit Zehnerstangen und Einerwürfeln und liest gelegte Zahlen ab. |
| PV-03 | Value of a digit by position (34 vs 43) | 6 | core | PV-02 | E3 | „Was bedeutet die 3 in 34 — und in 43?“ | | PT-N08 | Versteht, dass die 3 in 34 dreißig bedeutet, in 43 aber drei. |
| PV-04 | Ten tens make one hundred | 6 | core | PV-02, CNT-09 | E3 | „Wie viele Zehner sind hundert?“ | | – | Weiß, dass zehn Zehner hundert sind. |
| PV-06 | Regroup: 1 ten = 10 ones | 7 | stretch | PV-03 | E3 | „Leg zweiunddreißig anders — mit nur zwei Zehnern.“ | | – | Kann einen Zehner in zehn Einer umtauschen: 32 auch als 2 Zehner und 12 Einer legen. Vorbereitung auf Minus mit Übertrag. |
| PV-05 | Hundreds, tens and ones, with zeros | 7 | stretch | PV-04 | P5 | | | – | Hunderter, Zehner, Einer bei dreistelligen Zahlen, auch mit Null. |

## MUL — Equal groups, sharing, halving · trajectory: Multiplying and Dividing (contested for grade 1)

| ID | Skill | Age | Track | Requires | Rule | Check (DE) | Pool / correct looks like | PT | Erklärung (DE) |
|---|---|---|---|---|---|---|---|---|---|
| MUL-05 | Halve a set up to 20 | 6 | core | PW-06, CRD-09 | P3 | „Teil die zwölf gerecht in zwei Hälften.“ | even numbers only | – | Halbiert eine gerade Menge bis 20 gerecht. |
| MUL-02 | Share equally among 3–4 | 6 | stretch | CRD-09 | P3 | „Teil die zwölf gerecht auf drei Teller.“ | | – | Verteilt eine Menge gerecht auf 3 oder 4 Teller. |
| MUL-01 | Make and count equal groups | 6 | stretch | CRD-09, CNT-16 | P3 | „Mach drei Gruppen mit je vier.“ | | – | Bildet gleich große Gruppen (drei Gruppen mit je vier) und zählt das Ganze. |
| MUL-03 | Arrays: equal rows | 7 | stretch | MUL-01 | P3 | | | – | Erkennt gleich lange Reihen (3 Reihen mit je 4) als Anordnung. |
| MUL-04 | Group equally (groups of 3 in 12) | 7 | stretch | MUL-01 | P3 | | | – | Teilt eine Menge in gleich große Gruppen auf: wie viele Dreiergruppen in 12? |

## GEO — Shapes · trajectories: Shape; Composing Shapes

| ID | Skill | Age | Track | Requires | Rule | Check (DE) | Pool / correct looks like | PT | Erklärung (DE) |
|---|---|---|---|---|---|---|---|---|---|
| GEO-01 | Match identical shapes | 3 | core | – | P3 | „Such die gleiche Form.“ | | – | Findet zu einer Form die genau gleiche. |
| GEO-02 | Name circle, square, triangle (typical) | 4 | core | GEO-01 | P5 | „Wie heißt die Form?“ | | – | Benennt Kreis, Quadrat und Dreieck in der üblichen Lage. |
| GEO-11 | Fill outline puzzles with shapes | 4 | core | GEO-01 | P3 | pattern-block outline | | PT-G07 | Füllt eine Umrissvorlage mit Formen aus (Legespiel). |
| GEO-03 | Triangles and rectangles in odd orientations vs non-examples | 5 | core | GEO-02 | G2 | „Ist das ein Dreieck?“ | skinny, rotated, open or curved non-examples | – | Erkennt Dreiecke und Rechtecke auch schief, dünn oder gedreht, und lehnt Fast-Dreiecke (offen, rund) ab. |
| GEO-04 | Rectangle; square vs rectangle | 5 | core | GEO-02 | P5 | | | PT-G04 | Kennt das Rechteck und weiß, dass ein Quadrat ein besonderes Rechteck ist. |
| GEO-12 | Combine shapes into a new shape | 5 | core | GEO-11 | P3 | „Mach aus zwei Dreiecken ein Quadrat.“ | | PT-G07 | Setzt aus Formen eine neue zusammen: zwei Dreiecke ergeben ein Quadrat. |
| GEO-08 | Sort shapes by a rule and name the rule | 5 | core | GEO-02, DAT-01 | E3 | | | – | Sortiert Formen nach einer selbst gewählten Regel und benennt die Regel. |
| GEO-09 | Name solids: Würfel, Kugel, Zylinder, Kegel, Quader, Pyramide, Prisma | 5 | core | GEO-02 | P5 | real objects: „Welche Form hat das?“ | everyday objects | PT-G02 | Benennt Körper an Alltagsgegenständen: Würfel, Kugel, Zylinder, Kegel, Quader, Pyramide. |
| GEO-10 | Flat vs curved surfaces; what rolls, what stacks | 6 | core | GEO-09 | E3 | „Rollt das? Warum?“ | | PT-G03 | Unterscheidet flache und runde Flächen und erklärt, was rollt und was stapelbar ist. |
| GEO-05 | Describe shapes by sides and corners | 6 | core | GEO-04, CRD-03 | E3 | „Wie viele Ecken und Seiten?“ | | – | Beschreibt Formen über Ecken und Seiten: „hat vier Ecken und vier Seiten“. |
| GEO-06 | Pentagon and hexagon | 6 | core | GEO-05 | P5 | | | PT-G04 | Kennt Fünfeck und Sechseck. |
| GEO-07 | Polygon or not (classify) | 6 | core | GEO-05 | E3 | „Gehört das zu den Vielecken? Warum?“ | | PT-G04 | Entscheidet, ob eine Figur ein Vieleck ist (gerade Seiten, geschlossen) und begründet. |
| GEO-13 | Congruent figures (by overlay) | 6 | core | GEO-04 | P3 | „Sind die zwei genau gleich?“ | | PT-G05 | Erkennt, ob zwei Figuren deckungsgleich sind, indem sie sie aufeinanderlegt. |
| GEO-15 | Trace faces of solids and name them | 6 | core | GEO-09, GEO-04 | P3 | 📷 | | PT-G04 | Zeichnet die Flächen von Körpern nach (Würfelseite → Quadrat) und benennt sie. |
| GEO-17 | Copy a design on a square grid | 6 | core | GEO-12 | P3 | 📷 | | – | Zeichnet ein Muster auf Karopapier ab. |
| GEO-16 | Find all five tetrominoes | 6 | shadow | GEO-13 | P3 | 📷 | at least 4 distinct, no duplicates | PT-G06 | Findet alle fünf Formen aus vier Quadraten (Tetrominos). Nur im portugiesischen Lehrplan. |
| GEO-14 | Halves and quarters of a shape | 6 | stretch | GEO-12 | P3 | 📷 | | – | Teilt eine Form in Hälften und Viertel. |

## POS — Position and direction · trajectory: Spatial Thinking

| ID | Skill | Age | Track | Requires | Rule | Check (DE) | Pool / correct looks like | PT | Erklärung (DE) |
|---|---|---|---|---|---|---|---|---|---|
| POS-01 | in, auf, unter, neben | 3 | core | – | P5 | „Leg den Bären unter den Becher.“ | | – | Versteht in, auf, unter, neben: „Leg den Bären unter den Becher.“ |
| POS-02 | vor, hinter, zwischen, über | 4 | core | POS-01 | P5 | | | PT-G01 | Versteht vor, hinter, zwischen, über. |
| POS-05 | Follow movement directions | 5 | core | POS-02 | P3 | „Geh drei Schritte vor und dreh dich um.“ | | – | Folgt Bewegungsanweisungen: drei Schritte vor, umdrehen. |
| POS-03 | Left and right on own body | 5 | core | POS-02 | P5 | „Heb die linke Hand.“ | | PT-G01 | Kennt links und rechts am eigenen Körper. |
| POS-04 | Ordinal positions from left or right in a row | 6 | core | POS-03, NUM-19 | P5 | „Welches Auto ist das dritte von links?“ | | PT-G01, PT-N05 | Findet Positionen in einer Reihe: das dritte Auto von links. |
| POS-06 | Quarter, half and full turns | 6 | core | POS-05 | P3 | „Mach eine Vierteldrehung.“ | | – | Macht eine Viertel-, halbe und ganze Drehung. |
| POS-07 | Left and right from another person's view | 7 | stretch | POS-03 | P3 | | | – | Weiß, was links und rechts für ein Gegenüber ist. |

## PAT — Patterns · trajectory: Patterns and Structure

| ID | Skill | Age | Track | Requires | Rule | Check (DE) | Pool / correct looks like | PT | Erklärung (DE) |
|---|---|---|---|---|---|---|---|---|---|
| PAT-01 | Copy an AB pattern | 3 | core | – | P3 | | | – | Legt ein Muster rot-blau-rot-blau nach. |
| PAT-02 | Extend an AB pattern | 4 | core | PAT-01 | P3 | „Wie geht es weiter?“ | | PT-A02 | Setzt ein rot-blau-Muster richtig fort. |
| PAT-07 | Translate a pattern to another medium | 5 | core | PAT-02 | P3 | „Mach das Muster mit Klatschen und Stampfen.“ | | – | Überträgt ein Muster in etwas anderes: rot-blau wird Klatschen-Stampfen. |
| PAT-03 | Extend ABB, ABC, AABB patterns | 5 | core | PAT-02 | P3 | | | PT-A02 | Setzt schwerere Muster fort: ABB, ABC, AABB. |
| PAT-04 | Find the error or missing element | 5 | core | PAT-02 | P3 | „Was fehlt? / Wo ist der Fehler?“ | | PT-A01, PT-A03 | Findet den Fehler oder das fehlende Teil in einem Muster. |
| PAT-05 | Name the repeating unit | 5 | core | PAT-03 | E3 | „Was wiederholt sich?“ | | PT-A01 | Sagt, was sich im Muster wiederholt: „immer rot-rot-blau“. |
| PAT-08 | Patterns that vary in two attributes | 6 | core | PAT-05 | P3 | | colour and shape | PT-A06 | Erkennt Muster, bei denen sich zwei Dinge gleichzeitig ändern, z. B. Farbe und Form. |
| PAT-09 | Predict the n-th element | 6 | core | PAT-05, NUM-19 | P3 | „Welche Farbe hat das zehnte?“ | | PT-A04 | Sagt voraus, wie das zehnte Teil aussieht, ohne alles zu legen. |
| PAT-06 | Number patterns (+1, +2, +5, +10; missing numbers) | 6 | core | CNT-16, CNT-17 | P5 | „2, 4, 6, __, 10?“ | | PT-A05 | Setzt Zahlenfolgen fort und füllt Lücken: 2, 4, 6, __, 10. |

## MEA — Measurement · trajectories: Length; Capacity, Weight, Area

| ID | Skill | Age | Track | Requires | Rule | Check (DE) | Pool / correct looks like | PT | Erklärung (DE) |
|---|---|---|---|---|---|---|---|---|---|
| MEA-01 | Compare two lengths directly | 3 | core | – | G2 | „Welcher ist länger?“ | lines up the ends | PT-G08 | Vergleicht zwei Längen direkt und legt dafür die Enden bündig. |
| MEA-02 | Order 3+ objects by length | 4 | core | MEA-01 | P3 | | | PT-G08 | Ordnet drei oder mehr Dinge nach Länge. |
| MEA-04 | Measure with non-standard units, no gaps | 5 | core | MEA-02, CRD-10 | P3 | „Wie viele Klötze lang ist das Buch?“ | | PT-G09 | Misst mit Klötzen oder Büroklammern, lückenlos aneinandergelegt: „das Buch ist 6 Klötze lang“. |
| MEA-13 | Measure with body parts | 5 | core | MEA-04 | P3 | Handspannen, Schritte | | PT-G09 | Misst mit dem Körper: Handspannen, Schritte. |
| MEA-03 | Indirect comparison (with a string) | 6 | core | MEA-02 | P3 | „Ist der Tisch breiter als die Tür? Find's mit der Schnur raus.“ | | PT-G08 | Vergleicht zwei Dinge, die nicht nebeneinander passen, mit einer Schnur als Hilfe. |
| MEA-06 | Bigger unit means fewer units | 6 | core | MEA-04 | E3 | „Warum brauchst du mehr Stifte als Schritte?“ | | PT-G09 | Versteht: mit größeren Einheiten braucht man weniger (weniger Schritte als Stifte). |
| MEA-14 | Estimate a length, then measure | 6 | core | MEA-04 | P3 | „Schätz zuerst: wie viele Klötze?“ | within ±30% | PT-G10 | Schätzt eine Länge zuerst in Klötzen und misst dann nach. |
| MEA-05 | Measure with a ruler in cm, from 0 | 7 | stretch | MEA-04, NUM-12 | P3 | 📷 | | – | Misst mit dem Lineal in Zentimetern und beginnt bei 0. |
| MEA-07 | Compare capacity by pouring | 5 | stretch | – | P3 | | | – | Vergleicht, in welches Gefäß mehr passt, durch Umschütten. |
| MEA-10 | Full, half full, empty | 5 | stretch | MEA-07 | P3 | | | – | Kennt voll, halb voll, leer. |
| MEA-11 | Capacity in non-standard units (cups) | 6 | stretch | MEA-07, MEA-04 | P3 | | | – | Misst Fassungsvermögen in Bechern: „in die Kanne passen 4 Becher“. |
| MEA-09 | Compare mass with hands or a balance | 5 | stretch | – | P3 | | | – | Vergleicht Gewicht mit den Händen oder einer Balkenwaage. |
| MEA-12 | Mass in non-standard units | 6 | stretch | MEA-09 | P3 | | | – | Wiegt mit Alltagsgewichten: „so schwer wie 5 Klötze“. |
| MEA-08 | Compare area by overlay | 6 | stretch | MEA-01 | P3 | | | – | Vergleicht Flächen, indem sie eine auf die andere legt. |

## TIM — Time

| ID | Skill | Age | Track | Requires | Rule | Check (DE) | Pool / correct looks like | PT | Erklärung (DE) |
|---|---|---|---|---|---|---|---|---|---|
| TIM-01 | Order daily events | 4 | core | – | P3 | picture cards: „Was kommt zuerst?“ | | PT-G11 | Bringt Bilder vom Tagesablauf in die richtige Reihenfolge. |
| TIM-08 | gestern, heute, morgen | 4 | core | TIM-01 | P3 | | | PT-G11 | Benutzt gestern, heute und morgen richtig. |
| TIM-02 | Days of the week in order | 5 | core | TIM-08 | SEQ | „Sag die Wochentage ab Montag.“ | | PT-G12 | Sagt die Wochentage der Reihe nach ab Montag. |
| TIM-03 | Months in order | 6 | core | TIM-02 | SEQ | | | PT-G12 | Sagt die Monate der Reihe nach. |
| TIM-04 | Read a calendar (+1, −1, +7 days) | 6 | core | TIM-03, NUM-04 | P5 | „Welches Datum ist nächsten Dienstag?“ | | PT-G12, PT-A09 | Liest den Kalender: welches Datum ist morgen, nächsten Dienstag? |
| TIM-05 | Clock to the hour | 6 | stretch | NUM-04 | P5 | | | – | Liest volle Stunden an der Uhr. |
| TIM-06 | Half past | 6 | stretch | TIM-05 | P5 | | German „halb drei“ = 2:30 | – | Liest halbe Stunden. Achtung: „halb drei“ heißt auf Deutsch 2:30. |
| TIM-07 | Time to 5 minutes | 7 | stretch | TIM-06, CNT-17 | P5 | | | – | Liest die Uhr auf 5 Minuten genau. |
| TIM-09 | Estimate durations | 6 | stretch | TIM-01 | G2 | „Dauert Zähneputzen länger als die Nacht?“ | | – | Schätzt, was länger dauert: Zähneputzen oder die Nacht? |
| TIM-10 | Compare durations | 6 | stretch | TIM-09 | G2 | | | – | Vergleicht zwei Dauern. |

## MON — Money (euro) · not found in PT 1.º ano objectives, so stretch

| ID | Skill | Age | Track | Requires | Rule | Check (DE) | Pool / correct looks like | PT | Erklärung (DE) |
|---|---|---|---|---|---|---|---|---|---|
| MON-01 | Recognise euro coins | 5 | stretch | NUM-02 | P5 | | | – | Erkennt die Euro-Münzen. |
| MON-07 | Recognise euro notes 5–50 | 6 | stretch | MON-01 | P5 | | | – | Erkennt die Scheine von 5 bis 50 Euro. |
| MON-02 | Value is not size (10c vs 1c) | 6 | stretch | MON-01 | E3 | | | – | Versteht, dass die größere Münze nicht die wertvollere sein muss (10 Cent kleiner als 1 Cent). |
| MON-03 | Count cents to 20c | 6 | stretch | MON-01, CNT-17 | P5 | | | – | Zählt Cent-Münzen bis 20 Cent zusammen. |
| MON-04 | Count whole euros to 20 € | 6 | stretch | MON-01, CNT-17 | P5 | | | – | Zählt Euro-Münzen bis 20 Euro zusammen. |
| MON-06 | Pay an exact amount up to 10 € | 6 | stretch | MON-04 | P3 | | | – | Bezahlt einen Betrag bis 10 Euro passend. |

## DAT — Data

| ID | Skill | Age | Track | Requires | Rule | Check (DE) | Pool / correct looks like | PT | Erklärung (DE) |
|---|---|---|---|---|---|---|---|---|---|
| DAT-01 | Sort by one attribute | 3 | core | – | P3 | „Sortier nach Farbe.“ | | – | Sortiert Dinge nach einem Merkmal, z. B. Farbe. |
| DAT-02 | Sort by own rule and name the rule | 5 | core | DAT-01 | E3 | | | – | Sortiert nach eigener Regel und erklärt die Regel. |
| DAT-03 | Read a pictogram (most, least, how many) | 5 | core | CRD-03, CMP-02 | P5 | | | PT-D07 | Liest ein Bilddiagramm: wovon am meisten, am wenigsten, wie viele. |
| DAT-05 | Tally marks in groups of 5 (Strichliste) | 6 | core | CNT-17, DAT-01 | P3 | 📷 | | PT-D03, PT-D04 | Führt eine Strichliste in Fünferbündeln. |
| DAT-04 | Make a pictogram with a title | 6 | core | DAT-03 | P3 | 📷 | | PT-D05 | Zeichnet ein Bilddiagramm mit Überschrift. |
| DAT-08 | Compare categories in a chart (how many more) | 6 | core | DAT-03, AS-21 | P5 | | | PT-D07 | Vergleicht in einem Diagramm: wie viele mehr sind es hier als dort? |
| DAT-06 | Dot plot (Punktdiagramm) | 6 | shadow | DAT-04 | P3 | 📷 | | PT-D06 | Zeichnet ein Punktdiagramm. Nur im portugiesischen Lehrplan. |
| DAT-07 | Ask a survey question; choose a public or secret method | 6 | shadow | DAT-02 | E3 | | | PT-D01, PT-D02, PT-D08 | Stellt eine Umfragefrage und überlegt, wie man die Antworten sammelt. Nur im portugiesischen Lehrplan. |

---

## Portuguese shadow layer — Aprendizagens Essenciais, Matemática 1.º ano (DGE, 2021)

Source: dge.mec.pt, ae_mat_1.o_ano.pdf. The AE lists topics with no fixed order and teaches them in a spiral. We only use it to report where the child stands against school expectations.

**Covered** = every mapped node Mastered (any kind). **In progress** = at least one mapped node Started or better. Capacidades transversais (problem solving, reasoning, communication) are not tracked as nodes; ST and E3 checks touch them.

| Code | Objective (PT) | English gist | Nodes |
|---|---|---|---|
| PT-N01 | Significados do número (quantidade, medida, ordem, identificação) | what numbers can mean | NUM-03, NUM-19 |
| PT-N02 | Contar de 1 em 1, 2 em 2, 5 em 5, 10 em 10 com modelos estruturados | count in 1s, 2s, 5s, 10s | CNT-04, CNT-06, CNT-08, CNT-09, CNT-10, CNT-11, CNT-13, CNT-14, CNT-16, CNT-17, CRD-10, SUB-02, SUB-04, SUB-05, SUB-07 |
| PT-N03 | Ler e representar números até 100, incl. reta numérica | read and represent numbers to 100 | NUM-02, NUM-04, NUM-05, NUM-08, NUM-10, NUM-11, NUM-12, CMP-07, CMP-08, PV-07 |
| PT-N04 | Comparar e ordenar (crescente/decrescente) | compare and order | CMP-03, CMP-06, CMP-09, CMP-10, CMP-11, CMP-13 |
| PT-N05 | Ordinais até ao 10.º | ordinals to 10th | NUM-19, POS-04 |
| PT-N06 | Números pares e ímpares | odd and even | NUM-18 |
| PT-N07 | Estimar conjuntos até 50 e verificar por contagem organizada | estimate sets to 50, check | CMP-14, NUM-20, CRD-11 |
| PT-N08 | Valor posicional com materiais de base 10 | place value | PV-01, PV-02, PV-03, PV-07, PW-07, CMP-06 |
| PT-N09 | Compor e decompor até 100 de diversas formas | compose and decompose to 100 | PW-05, PW-07, PW-09, PW-11, PW-14, PW-15 |
| PT-N10 | Relacionar com números de referência 5, 10, 15, 20 | relate to 5, 10, 15, 20 | PW-13, CMP-05 |
| PT-N11 | Automatizar pares que formam 5 e 10; relacionar com subtração | bonds of 5 and 10, automatic | PW-02, PW-04, PW-10, AS-09, AS-30 |
| PT-N12 | Outros factos até 10 (±1, ±2 com o 5; dobros até 5+5) | other facts to 10 | PW-03, PW-06, CMP-04, SUB-05, AS-12 |
| PT-N13 | Estratégias de cálculo mental (dobros, quase dobros, compensação, decomposição) | mental strategies | PW-12, AS-05, AS-10, AS-11, AS-25, AS-26, AS-27, AS-28, AS-29, AS-34, AS-35 |
| PT-N14 | Calcular com a reta numérica e a representação horizontal | number line for calculation | AS-37 |
| PT-N16 | Estimar resultados de cálculos | estimate results | AS-36 |
| PT-N17 | Adição: acrescentar e juntar; problemas | meanings of addition | AS-07, AS-13, AS-22 |
| PT-N18 | Subtração: retirar, completar, comparar; problemas | meanings of subtraction | AS-08, AS-13, AS-21, AS-22, AS-23, AS-24, AS-31, AS-32 |
| PT-N19 | Relacionar adição e subtração | link + and − | AS-19, AS-30 |
| PT-A01 | Reconhecer e descrever regularidades em sequências | spot regularity | PAT-04, PAT-05 |
| PT-A02 | Continuar uma sequência | continue a sequence | PAT-02, PAT-03 |
| PT-A03 | Identificar elementos em falta | find missing elements | PAT-04 |
| PT-A04 | Cada elemento corresponde a uma ordem | position in a sequence | PAT-09 |
| PT-A05 | Sequências ligadas a contagens | sequences and counting | PAT-06 |
| PT-A06 | Criar e modificar sequências | create and modify | PAT-08 |
| PT-A07 | Igualdades aritméticas: decidir, completar, compensar | equalities and the equal sign | PW-08, AS-18 |
| PT-A08 | Descrever situações para uma igualdade | a story for an equation | AS-33 |
| PT-A09 | Regularidades numéricas (calendário ±1, ±7; quadro do 100 ±1, ±10) | calendar and hundred chart | CNT-10, CMP-12, TIM-04 |
| PT-A10 | Comutatividade e zero como elemento neutro | commutativity and zero | AS-15, AS-17, AS-20 |
| PT-D01 | Formular questões estatísticas | ask a data question | DAT-07 |
| PT-D02 | Decidir dados e método de recolha | plan data collection | DAT-07 |
| PT-D03 | Recolher e registar em listas | collect and list | DAT-05 |
| PT-D04 | Tabelas de contagem em grupos de 5 | tally tables | DAT-05 |
| PT-D05 | Pictogramas (um para um) com título e legenda | pictograms | DAT-04 |
| PT-D06 | Gráficos de pontos | dot plots | DAT-06 |
| PT-D07 | Ler e interpretar: o que mais e menos se repete | read charts | DAT-03, DAT-08 |
| PT-D08 | Conclusões, novas questões, apresentar | conclude and present | DAT-07 |
| PT-G01 | Descrever posição relativa | describe position | POS-02, POS-03, POS-04 |
| PT-G02 | Reconhecer sólidos em objetos do quotidiano | solids in everyday objects | GEO-09 |
| PT-G03 | Superfícies planas e curvas | flat and curved surfaces | GEO-10 |
| PT-G04 | Triângulos, quadrados, retângulos, pentágonos, hexágonos, círculos | plane figures | GEO-04, GEO-06, GEO-07, GEO-15 |
| PT-G05 | Figuras congruentes | congruent figures | GEO-13 |
| PT-G06 | Construir e comparar figuras compostas (tetraminós) | tetrominoes | GEO-16 |
| PT-G07 | Compor e decompor figuras (tangram, blocos padrão) | compose shapes | GEO-11, GEO-12 |
| PT-G08 | Comprimento: comparar e ordenar | compare lengths | MEA-01, MEA-02, MEA-03 |
| PT-G09 | Medir com unidades não convencionais | non-standard units | MEA-04, MEA-06, MEA-13 |
| PT-G10 | Estimar comprimentos e resolver problemas | estimate length | MEA-14 |
| PT-G11 | Ordenar acontecimentos | order events | TIM-01, TIM-08 |
| PT-G12 | Ler o calendário | read the calendar | TIM-02, TIM-03, TIM-04 |

Not in the 1.º ano objectives: written algorithms (from 3.º ano), fractions (from 2.º ano), clock times, multiplication. Money appears only as a general 1.º ciclo theme, not as a 1.º ano objective.
Preschool: the Portuguese preschool guidelines (OCEPE 2016) are not mapped yet.
