"""Builds index.html (one self-contained file) from src/deck.template.html.

Run:  python3 build.py
- {{name}}   -> src/images/name.jpg, inlined as a data URI
- {{p:name}} -> brand icon path from src/brands.json (Simple Icons, CC0)
"""
import base64, json, re, pathlib

root = pathlib.Path(__file__).parent
t = (root / "src/deck.template.html").read_text(encoding="utf-8")
brands = json.loads((root / "src/brands.json").read_text(encoding="utf-8"))

t = re.sub(r"\{\{p:(\w+)\}\}", lambda m: brands[m.group(1)], t)

def uri(name):
    data = (root / f"src/images/{name}.jpg").read_bytes()
    return "data:image/jpeg;base64," + base64.b64encode(data).decode()

cache = {n: uri(n) for n in set(re.findall(r"\{\{(\w+)\}\}", t))}
t = re.sub(r"\{\{(\w+)\}\}", lambda m: cache[m.group(1)], t)
(root / "index.html").write_text(t, encoding="utf-8")
print(f"index.html written ({len(t)/1e6:.2f} MB)")
