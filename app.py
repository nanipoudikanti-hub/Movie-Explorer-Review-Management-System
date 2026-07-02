import streamlit as st
import requests
import pandas as pd

API_URL = "http://127.0.0.1:8000"

st.title("Movie Explorer & Review Management System")

menu = st.sidebar.selectbox(
    "Select Operation",
    (
        "Movie ID",
        "Add Movie",
        "View Movies",
        "Update Movie",
        "Delete Movie"
    )
)

# ---------------- Movie By ID ----------------

if menu == "Movie ID":

    st.header("View Movie By ID")

    movie_id = st.number_input("Enter Movie ID", min_value=1, step=1)

    if st.button("Get Movie"):

        response = requests.get(f"{API_URL}/movies/{movie_id}")

        movie = response.json()

        if "message" in movie:
            st.warning(movie["message"])
        else:
            st.table(pd.DataFrame([movie]))


# ---------------- Add Movie ----------------

elif menu == "Add Movie":

    st.header("Add Movie")

    movie_id = st.number_input("Movie ID", min_value=1, step=1)

    name = st.text_input("Movie Name")

    genre = st.selectbox(
        "Genre",
        ["Action", "Comedy", "Drama", "Sci-Fi"]
    )

    language = st.selectbox(
        "Language",
        ["English", "Telugu", "Hindi", "Tamil"]
    )

    rating = st.number_input(
        "Rating",
        min_value=1,
        max_value=10,
        step=1
    )

    if st.button("Add Movie"):

        data = {
            "id": movie_id,
            "name": name,
            "genre": genre,
            "language": language,
            "rating": rating
        }

        response = requests.post(
            f"{API_URL}/movie",
            json=data
        )

        st.success(response.json()["message"])


# ---------------- View Movies ----------------

elif menu == "View Movies":

    st.header("All Movies")

    response = requests.get(f"{API_URL}/movies")

    movies = response.json()

    if len(movies) > 0:

        df = pd.DataFrame(movies)

        st.dataframe(df, use_container_width=True)

    else:
        st.warning("No Movies Found")


# ---------------- Update Movie ----------------

elif menu == "Update Movie":

    st.header("Update Movie")

    movie_id = st.number_input("Movie ID", min_value=1, step=1)

    name = st.text_input("Movie Name")

    genre = st.selectbox(
        "Genre",
        ["Action", "Comedy", "Drama", "Sci-Fi"]
    )

    language = st.selectbox(
        "Language",
        ["English", "Telugu", "Hindi", "Tamil"]
    )

    rating = st.number_input(
        "Rating",
        min_value=1,
        max_value=10,
        step=1
    )

    if st.button("Update Movie"):

        data = {
            "id": movie_id,
            "name": name,
            "genre": genre,
            "language": language,
            "rating": rating
        }

        response = requests.put(
            f"{API_URL}/movies/{movie_id}",
            json=data
        )

        st.success(response.json()["message"])


# ---------------- Delete Movie ----------------

elif menu == "Delete Movie":

    st.header("Delete Movie")

    movie_id = st.number_input("Movie ID", min_value=1, step=1)

    if st.button("Delete Movie"):

        response = requests.delete(f"{API_URL}/movies/{movie_id}")

        st.success(response.json()["message"])