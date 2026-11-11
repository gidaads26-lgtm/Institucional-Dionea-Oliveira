"""Gera o index.html final a partir de fonte/src.html.

As fotos ficam na pasta assets/ (na raiz) e o index.html aponta para elas.
Uso (na raiz do repositório):  python3 fonte/build.py
"""
from pathlib import Path

FONTE = Path(__file__).resolve().parent
RAIZ = FONTE.parent

html = (FONTE / "src.html").read_text(encoding="utf-8")
html = (html.replace("{{HERO}}", "assets/hero.jpg")
            .replace("{{SOBRE}}", "assets/sobre.jpg")
            .replace("{{CONSULTORIO}}", "assets/consultorio.jpg")
            .replace("{{APPLE}}", "/assets/apple-touch-icon.png"))
assert "{{" not in html, "Ficou algum marcador sem substituir no src.html"
for img in ("hero.jpg", "sobre.jpg", "consultorio.jpg", "apple-touch-icon.png"):
    assert (RAIZ / "assets" / img).exists(), f"Falta assets/{img}"
(RAIZ / "index.html").write_text(html, encoding="utf-8")
print(f"index.html gerado ({len(html.encode('utf-8')) // 1024} KB)")
