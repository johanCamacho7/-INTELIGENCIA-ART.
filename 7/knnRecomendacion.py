import pandas as pd
from sklearn.neighbors import NearestNeighbors
import numpy as np

# Cargar el archivo CSV con las películas
df = pd.read_csv(r"C:\Users\POLVO\PycharmProjects\pythonProject\16k_Movies.csv")

# Asegurarse de que las columnas necesarias estén presentes
if 'Title' not in df.columns or 'Genres' not in df.columns or 'Rating' not in df.columns:
    print("Faltan las columnas necesarias ('Title', 'Genres', 'Rating')")
    exit()

# Eliminar filas con valores NaN en la columna 'Genres'
df = df.dropna(subset=['Genres'])

# Convertir la columna 'Rating' a valores numéricos
df['Rating'] = pd.to_numeric(df['Rating'], errors='coerce')

# Asegurarse de que no haya valores NaN en 'Rating' después de la conversión
df = df.dropna(subset=['Rating'])


# Función para recomendar películas utilizando KNN basado en Rating
def recommend_movies_knn(movie_title, num_recommendations=5):
    # Buscar la película seleccionada
    selected_movie = df[df['Title'].str.contains(movie_title, case=False, na=False)]

    if selected_movie.empty:
        print("Película no encontrada.")
        return

    selected_movie = selected_movie.iloc[0]
    print(f"Película seleccionada: {selected_movie['Title']} (Rating: {selected_movie['Rating']})\n")

    # Seleccionar las características de las películas (Rating en este caso)
    X = df[['Rating']].values

    # Crear un modelo KNN
    model = NearestNeighbors(n_neighbors=num_recommendations + 1, metric='euclidean')
    model.fit(X)

    # Buscar las películas más cercanas a la seleccionada
    distance, indices = model.kneighbors([selected_movie[['Rating']].values])

    print(f"Recomendaciones basadas en '{movie_title}':\n")
    for i in range(1, len(indices[0])):  # Comienza en 1 para evitar la película seleccionada
        similar_movie = df.iloc[indices[0][i]]
        print(f"- {similar_movie['Title']} (Rating: {similar_movie['Rating']})")


# Ejemplo de uso
movie_name = input("Ingresa el nombre de la película: ")
recommend_movies_knn(movie_name)
