import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
from sklearn.preprocessing import LabelEncoder

# Cargar el archivo CSV
try:
    df = pd.read_csv(r"C:\Users\POLVO\PycharmProjects\pythonProject\16k_Movies.csv")
except FileNotFoundError:
    print("El archivo no se encuentra en la ruta especificada. Por favor revisa la ubicación del archivo.")
    exit()

# Verificar si la columna 'Rating' existe en el DataFrame
if 'Rating' not in df.columns:
    print("La columna 'Rating' no se encuentra en el DataFrame. Revisa los nombres de las columnas.")
    exit()

# Revisar si hay valores nulos en la columna 'Rating'
if df['Rating'].isnull().sum() > 0:
    print(f"Se encontraron {df['Rating'].isnull().sum()} valores nulos en la columna 'Rating'")
    df = df.dropna(subset=['Rating'])

# Función de categorización con base en 'Rating'
def categorize_rating(rating):
    if rating >= 10:
        return 'Must Watch'
    elif 7 <= rating < 10:
        return 'Buena'
    elif 5 <= rating < 7:
        return 'Mediocre'
    elif rating < 4:
        return 'Tan mala que puede ser buena'
    else:
        return 'Mala'

# Aplicar la categorización
df['Category'] = df['Rating'].apply(categorize_rating)

# Codificar las categorías en números
le = LabelEncoder()
df['Category'] = le.fit_transform(df['Category'])

# Usar solo la columna 'Rating' para las características
X = df[['Rating']].values
y = df['Category']

# Dividir los datos en entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Crear el modelo KNN
knn = KNeighborsClassifier(n_neighbors=5)

# Entrenar el modelo
knn.fit(X_train, y_train)

# Realizar predicciones
y_pred = knn.predict(X_test)

# Evaluar el modelo
accuracy = accuracy_score(y_test, y_pred)
print(f'Accuracy: {accuracy:.2f}')

# Mostrar la matriz de confusión y el informe de clasificación
print(confusion_matrix(y_test, y_pred))
print(classification_report(y_test, y_pred))
