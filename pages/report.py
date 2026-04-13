import streamlit as st
from template import initialize_page, footer_expanders


initialize_page(page_title="Report")

st.markdown("# Report")

st.write(
    """
        Here is a page with a report on it.
    """
)

st.bar_chart({"data": [1, 5, 2, 6, 2, 1]})

st.write(
    """
    Look at those numbers. Amazing.
"""
)

footer_expanders()
