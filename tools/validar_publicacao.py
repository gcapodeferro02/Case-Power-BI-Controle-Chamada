from pathlib import Path
import re
import sys


ROOT = Path(__file__).resolve().parents[1]
FORBIDDEN_NAMES = {".pbix", ".pbip", ".abf"}
FORBIDDEN_TERMS = (
    "password",
    "secret",
    "client_secret",
    "dsn=",
    "sharepoint.com" + "/personal",
)


def iter_files():
    for path in ROOT.rglob("*"):
        if path.is_file() and ".git" not in path.parts:
            yield path


def main():
    errors = []
    for path in iter_files():
        if path.suffix.lower() in FORBIDDEN_NAMES:
            errors.append(f"arquivo proibido: {path.relative_to(ROOT)}")
            continue
        if path.suffix.lower() not in {".md", ".mmd", ".py"}:
            continue
        if path.name == "validar_publicacao.py":
            continue
        text = path.read_text(encoding="utf-8")
        lowered = text.lower()
        for term in FORBIDDEN_TERMS:
            if term in lowered:
                errors.append(f"termo sensível '{term}' em {path.relative_to(ROOT)}")
        if re.search(r"[A-Za-z]:\\\\Users\\\\", text):
            errors.append(f"caminho local em {path.relative_to(ROOT)}")

    if errors:
        print("\n".join(errors))
        return 1

    print("validação de publicação: OK")
    return 0


if __name__ == "__main__":
    sys.exit(main())
