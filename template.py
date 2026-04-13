import streamlit as st

def login():
    st.session_state.logged_in = True


def logout():
    st.session_state.logged_in = False

def initialize_page(page_title, page_icon= None, show_side_bar_header = True):
    if st.session_state.get("logged_in") == None:
        st.session_state["logged_in"] = False

    st.set_page_config(page_title=page_title, page_icon=page_icon)

    if show_side_bar_header:
        st.sidebar.header(page_title)

    if st.session_state.logged_in:
        st.sidebar.success("Logged in")
        st.sidebar.button("Log out", key="logout", on_click=logout)
    else:
        st.sidebar.warning("Not logged in")
        st.sidebar.button("Log in", key="login", on_click=login)

    st.sidebar.write("This site is copyright Fake Company LLC Inc., 2024")

def footer_expanders(): 
    with st.expander("Company Info"):
        st.write(
            """
            Fake Company LLC Inc. is located at 1600 Amphitheatre Parkway Mountain View, CA 94043
        """
        )

    with st.expander("Links"):
        st.markdown(
            """
            [Google](https://google.com)

            [Gemini](https://gemini.google.com)

            [Streamlit Docs](https://docs.streamlit.io/)
        """
        )
