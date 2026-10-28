# Receipt Data Extractor

Extrai texto de imagens de recibos usando OCR e tenta identificar campos básicos por padrões. Projeto demonstrativo; os valores extraídos devem ser revisados manualmente.

## Requisitos
O Tesseract OCR precisa estar instalado no sistema e disponível no PATH:
- Windows: instale o Tesseract OCR e, se necessário, configure o caminho no código.
- Debian/Ubuntu: `sudo apt install tesseract-ocr tesseract-ocr-por`
- macOS: `brew install tesseract tesseract-lang`

## Executar
```bash
python -m venv .venv
# Windows: .venv\Scripts\activate
pip install -r requirements.txt
streamlit run app.py
```

O MVP funciona localmente sem API. A extração é heurística e pode falhar em imagens borradas ou recibos com layouts diferentes.
