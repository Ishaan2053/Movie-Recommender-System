import streamlit as st

st.set_page_config(layout="wide")

st.title("Welcome to our Movie Recommender System!")
st.image("https://media.giphy.com/media/w1OBpBd7kJqHrJnJ13/giphy.gif",
 width=50)
st.write ("We are excited to bring you a personalized movie recommendation service that helps you discover new and exciting films based on your individual preferences. Our system uses advanced algorithms and data analysis techniques to provide you with a tailored selection of movies that are sure to satisfy your cinematic cravings.")
st.subheader("But how does our system work?")
st.write ("At the heart of our movie recommendation system is a powerful programming language called Python. Python is a widely-used and versatile programming language that is well-suited for tasks such as data analysis, machine learning, and artificial intelligence. In our system, we use Python to process large amounts of data, analyze movie characteristics and ratings, and generate personalized recommendations for each user.")
st.write("To power our system, we use a dataset called the TMDB 5000 Movie Dataset. This dataset contains information on over 5000 movies, including details such as title, genre, budget, revenue, and cast. We use this dataset to build a comprehensive profile of each movie, which allows us to accurately match films to users based on their preferences.")
st.write("One of the key features of our system is its use of content-based filtering. This type of filtering is based on the idea that users are more likely to enjoy movies that are similar to those they have already watched and rated highly. To implement this, we analyze the characteristics of each movie in our dataset and compare them to the preferences of our users. This allows us to provide recommendations that are tailored specifically to each user's tastes.")
st.write("To make our system even more powerful, we have integrated it with Streamlit. Streamlit is an open-source framework that allows us to easily create interactive web applications. With Streamlit, we are able to present our movie recommendations in a visually appealing and user-friendly way, making it easy for users to browse and select movies that interest them.")
st.write("So whether you're a fan of action, romance, comedy, or any other genre, our movie recommendation system has you covered. We hope you enjoy using our service and discovering new and exciting films!")