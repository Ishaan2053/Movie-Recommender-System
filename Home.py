import pickle
import streamlit as st
import requests
import streamlit.components.v1 as components
import time
from streamlit_extras.app_logo import add_logo

st.set_page_config(page_title='MovieFind', page_icon='🎬', layout='wide', initial_sidebar_state='collapsed')

hide_st_style = """
            <style>
            #mainmenu {visibility: hidden;}
            header {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)  

add_logo("")

def add_bg_from_url():
    st.markdown(
        f"""
         <style>
         .stApp {{
             background-image: url("https://wallpapercave.com/wp/wp8226566.png");
             background-attachment: fixed;
             background-size: cover 
         }}
         </style>
         """,
        unsafe_allow_html=True
    )

add_bg_from_url()

##Sidebar
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

def fetch_poster(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US".format(
        movie_id)
    data = requests.get(url)
    data = data.json()
    poster_path = data['poster_path']
    full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
    return full_path


def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(
        list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recommended_movie_names = []
    recommended_movie_posters = []
    for i in distances[1:6]:

        movie_id = movies.iloc[i[0]].movie_id
        recommended_movie_posters.append(fetch_poster(movie_id))
        recommended_movie_names.append(movies.iloc[i[0]].title)

    return recommended_movie_names, recommended_movie_posters

st.header('') 
st.header('') 
st.title('MovieFind Movie Recommender System')
st.subheader('The One-Click Solution to finding your next watch!')
movies = pickle.load(open('movie_list.pkl', 'rb'))
similarity = pickle.load(open('similarity.pkl', 'rb'))

movie_list = movies['title'].values
selected_movie = st.selectbox(
    "Type in your movie or select one from the drop down list📃",
    movie_list
)

if st.button('Show Recommendations'):
    recommended_movie_names, recommended_movie_posters = recommend(
        selected_movie)
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(recommended_movie_names[0])
        st.image(recommended_movie_posters[0])
    with col2:
        st.text(recommended_movie_names[1])
        st.image(recommended_movie_posters[1])

    with col3:
        st.text(recommended_movie_names[2])
        st.image(recommended_movie_posters[2])
    with col4:
        st.text(recommended_movie_names[3])
        st.image(recommended_movie_posters[3])
    with col5:
        st.text(recommended_movie_names[4])
        st.image(recommended_movie_posters[4])

## Footer
footer = """<style>
a:link , a:visited{
color: white;
background-color: transparent;
transition: all 0.5s;
}

a:hover,  a:active {
color: aqua;
background-color: transparent;
transition: all 0.5s;
}

.footer {
position: fixed;
left: 0;
bottom: 0;
width: 100%;
background-color: dark gray;
color: white;
text-align: center;
}

</style>
<div class="footer">
  <div class="container-fluid">
<p>Made with 🔥 by <strong>Ishaan</strong> and <strong>Keshav Sharma</strong></p>
<p><a href="https://github.com/Ishaan2053/MovieFind-Movie-Recommender-System" target="_blank">View This Project on GitHub</a></p>
</div></div>
"""
st.markdown(footer,unsafe_allow_html=True)