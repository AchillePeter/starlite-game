# StarLite II — English site + game-menu landing (what to upload)

Everything here is in ENGLISH and the homepage now looks like the in-game menu
(Multiplayer / Vs. Computer / Campaign gates) with the content below on scroll.
Clicking a gate deep-links straight into that game mode — no second click.

## What changed vs. what's already live
You must REPLACE these files on GitHub (they changed to English / new design):

  index.html            → new game-menu landing (English)
  guide/index.html      → English
  factions/index.html   → English
  devlog/index.html      → English
  contact.html          → English
  assets/site.css       → updated styles for the menu gates
  robots.txt, sitemap.xml → updated

  privacy.html          → NEW (English). You can DELETE the old confidentialite.html
                          (or keep it, harmless — but nothing links to it anymore).

  play/index.html       → REPLACE. Same game, but with the deep-link script added
                          so the landing gates jump straight into each mode.
                          (This is the big 2.5MB file — upload, don't copy-paste.)

## Fastest safe way to upload (avoids the folder-flatten bug)
Use "Add file → Create new file" and type the full path in the name box for each:
  - index.html            (paste content)
  - guide/index.html      (paste)
  - factions/index.html   (paste)
  - devlog/index.html     (paste)
  - contact.html          (paste)
  - privacy.html          (paste)
  - assets/site.css       (paste)
For the game (play/index.html, too big to paste): "Add file → Upload files",
drag ONLY play/index.html, and make sure the path shows play/index.html before commit.

## Future game updates from your AI dev
When your AI dev sends a new one-file game, run inject_shim.py on it (included):
  python3 inject_shim.py newgame.html
It re-adds <base href="/"> AND the deep-link script, and writes play/index.html.
Then upload just that one file. Your one-file workflow is preserved.

## AdSense reminder
- Ads go ONLY on the content pages (home content area, guide, factions, devlog).
- NEVER put ad code on /play/ (the game screen is a functional screen).
- Keep the GDPR consent message (CMP) active in your AdSense account.
