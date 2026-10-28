import re
from datetime import datetime
from PIL import Image, ImageOps, ImageEnhance, ImageFilter
import pytesseract
import streamlit as st

st.set_page_config(page_title="Receipt Data Extractor")
st.title("Receipt Data Extractor")
st.caption("OCR local para recibos e notas simples. Revise todos os campos antes de usar.")
uploaded = st.file_uploader("Envie uma imagem", type=["png", "jpg", "jpeg", "webp"])
if uploaded:
    image = Image.open(uploaded).convert("RGB")
    st.image(image, caption="Imagem enviada", use_container_width=True)
    if st.button("Extrair informações"):
        try:
            processed = ImageOps.grayscale(image)
            processed = ImageEnhance.Contrast(processed).enhance(1.8)
            text = pytesseract.image_to_string(processed, lang="por+eng")
        except Exception as exc:
            st.error("Não foi possível executar o OCR. Verifique a instalação do Tesseract e do idioma português.")
            st.code(str(exc))
            st.stop()
        amounts = re.findall(r"(?<!\d)(?:R\$\s*)?\d{1,3}(?:\.\d{3})*,\d{2}|(?<!\d)\d+\.\d{2}", text)
        dates = re.findall(r"\b\d{1,2}[/-]\d{1,2}[/-]\d{2,4}\b", text)
        lines = [line.strip() for line in text.splitlines() if line.strip()]
        st.subheader("Campos sugeridos")
        st.text_input("Data identificada", value=dates[0] if dates else "")
        st.text_input("Valor(es) identificado(s)", value=", ".join(amounts[:10]))
        st.text_area("Possível nome do estabelecimento (revise)", value=lines[0] if lines else "")
        st.subheader("Texto completo extraído")
        st.text_area("OCR", value=text, height=250)
        st.download_button("Baixar texto OCR", data=text, file_name="recibo_extraido.txt", mime="text/plain")
        st.warning("Extração automática pode conter erros. Não use os campos sem conferência.")
