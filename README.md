# Math map

A map of early maths, ages 3 to 7, kept as plain files that your AI assistant reads and writes. It answers one question: **where is my child right now, and what comes next?**

You teach and play. The assistant keeps the book: it tells you what to check today, turns your voice note into evidence, and redraws your child's map.

## What you need

- An AI assistant that can **read and write a folder on your computer and run Python**, for example the Claude desktop app with this folder connected. A chat window that can only read a link will not work: it has nowhere to keep your child's record.
- Python 3 (already on most Macs and Linux machines).
- About 15 minutes with your child, a few times a week.

## Start

1. Download this folder (green **Code** button → **Download ZIP**) and put it somewhere you keep, for example your Documents.
2. Connect the folder to your assistant.
3. Say: **"Read INDEX.md in the math map folder and follow it."**

The first time, the assistant asks your child's name and birth month, draws an empty map, and offers two ways to fill it: a short play session that finds out where your child is, or you simply tell it what your child can already do. After that it takes over.

## Every day

1. Before: **"What do I check with Mia today?"**
2. After: send a voice note (30–60 seconds). Say per skill what you asked, what your child did, how many were right, and **"no help" or which help you gave**.
3. Check the claims the assistant shows back and answer "ok" or correct them. Only then does it write anything.
4. Open `cockpit/<name>-math.html` in your browser to see the map.

## Good to know

- **Language.** The check sentences in the tree and the map page are in German for now. The assistant gives you each check in your language.
- **Your data stays with you.** Everything is in this folder on your computer. Nothing is sent anywhere, and the `.gitignore` keeps your child's files out of any fork you publish.
- **There is a logbook.** `maps/math/log/<name>.md` records every check and every correction, and nothing in it is ever edited. If you are asked to share it to help improve the map, read it first; it is yours.
- **Back up the folder** now and then.
- Everything on the map is what a parent saw and reported. It is not a test result or a diagnosis.

## Where things are

`INDEX.md` lists every file. Short version: `kids/` = who they are · `maps/math/` = the skill tree, the rules, and each child's log and status · `cockpit/` = the visual map · `inbox/` = your voice notes.
