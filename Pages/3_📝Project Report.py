import streamlit as st

st.set_page_config(page_title='About This Project', page_icon=None, layout='wide', initial_sidebar_state='collapsed')

def add_bg_from_url():
    st.markdown(
        f"""
         <style>
         .stApp {{
             background-image: url("https://wallpapercave.com/wp/wp6354033.jpg");
             background-attachment: fixed;
             background-size: 100%
         }}
         </style>
         """,
        unsafe_allow_html=True
    )

hide_st_style = """
            <style>
            #mainmenu {visibility: hidden;}
            header {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)  

add_bg_from_url()

with st.sidebar:
    add_radio = st.radio(
        "Select Theme (Non Functional)",
        ("Light", "Dark")
    )

    add_text = st.write(
        "New to MovieFind? Sign up now and save your recommendation history!"
    )

    add_button = st.button(
       "Sign Up" 
    )

    add_text = st.write(
        "Already a member? Log in"
    )

    add_button = st.button(
       "Login" 
    )
