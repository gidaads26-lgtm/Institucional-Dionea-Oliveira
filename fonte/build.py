"""Monta o index.html final a partir de fonte/src.html, embutindo as fotos.

Uso (na raiz do repositório):  python3 fonte/build.py
"""
import base64
from pathlib import Path

FONTE = Path(__file__).resolve().parent
RAIZ = FONTE.parent
IMG = FONTE / "imagens"


def data_uri(nome, tipo):
    return f"data:{tipo};base64," + base64.b64encode((IMG / nome).read_bytes()).decode()


html = (FONTE / "src.html").read_text(encoding="utf-8")
html = (html.replace("{{HERO}}", data_uri("hero.jpg", "image/jpeg"))
            .replace("{{SOBRE}}", data_uri("sobre.jpg", "image/jpeg"))
            .replace("{{CONSULTORIO}}", data_uri("consultorio.jpg", "image/jpeg"))
            .replace("{{APPLE}}", data_uri("apple-touch-icon.png", "image/png")))
assert "{{" not in html, "Ficou algum marcador sem substituir no src.html"
(RAIZ / "index.html").write_text(html, encoding="utf-8")
print(f"index.html gerado ({len(html) // 1024} KB)")
