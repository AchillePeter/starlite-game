#!/usr/bin/env python3
# Usage: python3 inject_shim.py newgame.html
# Adds <base href="/"> and the landing deep-link script, writes play/index.html.
import sys, re, os
src = sys.argv[1] if len(sys.argv)>1 else "play/index.html"
html = open(src, encoding="utf-8").read()
html = re.sub(r'\s*<base [^>]*>', '', html, count=1)
html = html.replace('<meta charset="utf-8">', '<meta charset="utf-8">\n  <base href="/">', 1)
shim = '''
<script>
(function(){
  function target(){var h=(location.hash||'').replace('#','').toLowerCase();
    if(h==='multiplayer'||h==='online')return 'online';
    if(h==='campaign')return 'campaign';
    if(h==='computer'||h==='vs'||h==='skirmish')return 'computer';return null;}
  function go(){var w=target();if(!w)return;var t=0;var i=setInterval(function(){t++;
    var b=document.querySelector('#starlite-menu [data-category="'+w+'"]');
    if(b){clearInterval(i);b.click();}else if(t>60){clearInterval(i);}},100);}
  if(document.readyState==='complete')go();else window.addEventListener('load',go);
})();
</script>
'''
if 'starlite-menu [data-category' not in html:
    idx = html.rfind('</body>'); html = html[:idx]+shim+html[idx:]
os.makedirs("play", exist_ok=True)
open("play/index.html","w",encoding="utf-8").write(html)
print("OK -> play/index.html (base + deep-link shim added)")
