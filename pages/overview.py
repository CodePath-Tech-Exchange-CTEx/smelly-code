import streamlit as st
from template import initialize_page, footer_expanders


initialize_page(page_title="Overview")

st.markdown("# Overview")

st.write("""Here is a page with a site overview.""")

footer_expanders()

