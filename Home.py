import pickle
import streamlit as st
import requests
import time
import webbrowser
from streamlit_extras.app_logo import add_logo
import base64

st.set_page_config(page_title='MovieFind', page_icon='🎬', layout='wide', initial_sidebar_state='collapsed')

hide_st_style = """
            <style>
            #mainmenu {visibility: hidden;}
            header {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)

def get_base64(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

##Background
def set_background(png_file):
    bin_str = get_base64(png_file)
    page_bg_img = '''
    <style>
    .stApp {
    background-image: url("data:image/png;base64,%s");
    background-size: cover;
    }
    </style>
    ''' % bin_str
    st.markdown(page_bg_img, unsafe_allow_html=True)

set_background('./background.png')

##Sidebar
with st.sidebar:

    add_text = st.write (
        "Want to drop a review or feedback? Spotted a bug? Reach out to us through this survery form!"
    )

    url = 'Pages\Survey_Form.html'

    if st.button('Survey Form'):
     webbrowser.open_new_tab(url)
   
##Poster fetching function
def fetch_poster(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US".format(
        movie_id)
    data = requests.get(url)
    data = data.json()
    poster_path = data['poster_path']
    full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
    return full_path

##Movie recommeding system
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

##Main UI
st.header('') 
st.header('') 
st.title('MovieFind Movie Recommender System')
st.subheader('The One-Click Solution to finding your next watch!')
movies = pickle.load(open('movie_list.pkl', 'rb'))
similarity = pickle.load(open('similarity.pkl', 'rb'))

##Movie dropdown list
movie_list = movies['title'].values

col1, col2 = st.columns(2)

with col1:
 st.selectbox(
    "Type in your movie or select one from the drop down list📃",
    movie_list
)

##Recommendations button
if st.button('Show Recommendations'):
    with st.spinner('Processing Request'):
     time.sleep(5)
     st.success('Done! Here are some recommendations for your next watch')
       
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
text-decoration: none;
}

a:hover,  a:active {
color: #FF4B4B;
background-color: transparent;
transition: all 0.5s;
}

.footer {
position: fixed;
left: 0;
bottom: 0;
width: 100%;
background-color: #161619;
color: white;
text-align: center;
border-top: 2px solid #FF4B4B;
}

#footertext {
    margin: 5px;
    transition: all 0.3s ease-in-out;
}
#footertext:hover {
    color: #FF4B4B;
}

</style>
<div class="footer">
  <div class="container-fluid">
  <p id="footertext"><a href="https://github.com/Ishaan2053/MovieFind-Movie-Recommender-System" target="_blank">View This Project on GitHub</a></p>
<p id="footertext">Made with 🔥 by <strong>Ishaan</strong> and <strong>Keshav Sharma</strong></p>
</div></div>
"""
st.markdown(footer,unsafe_allow_html=True)