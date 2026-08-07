#!/usr/bin/env python3
# Usage: python3 inject_base.py nouveau_jeu.html
# Place le jeu dans play/index.html avec <base href="/"> réinjecté.
import sys, os
src = sys.argv[1] if len(sys.argv) > 1 else "play/index.html"
html = open(src, encoding="utf-8").read()
# retire une éventuelle base existante puis réinjecte
import re
html = re.sub(r'\s*<base [^>]*>', '', html, count=1)
html = html.replace('<meta charset="utf-8">',
                    '<meta charset="utf-8">\n  <base href="/">', 1)
os.makedirs("play", exist_ok=True)
open("play/index.html","w",encoding="utf-8").write(html)
print("OK → play/index.html (base href=/ injecté)")
