from pathlib import Path

import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Sia Roy", page_icon="🤖", layout="wide")

# Streamlit ka default header/footer/padding hatao, taaki app poori screen le
st.markdown(
    """
    <style>
    #MainMenu, header, footer {visibility: hidden;}
    .block-container {padding: 0 !important; max-width: 100% !important;}
    iframe {border: 0; width: 100%;}
    </style>
    """,
    unsafe_allow_html=True,
)

# app.py ke saath wali index.html (kisi bhi folder se run karo, chalega)
html_file = Path(__file__).parent / "index.html"

if html_file.exists():
    components.html(html_file.read_text(encoding="utf-8"), height=900, scrolling=False)
else:
    st.error("index.html nahi mili. Isse app.py ke saath same folder mein rakho.")
