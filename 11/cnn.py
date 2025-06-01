# pip install tensorflow matplotlib

import matplotlib.pyplot as plt
from keras import Sequential
from keras.src.datasets import mnist
from keras.src.layers import Conv2D, MaxPooling2D, Flatten, Dense
from keras.src.utils import to_categorical

# 1. Cargar y preparar datos
(x_train, y_train), (x_test, y_test) = mnist.load_data()

# 2. Redimensionar a 28x28x1 y normalizar
x_train = x_train.reshape(-1, 28, 28, 1) / 255.0
x_test = x_test.reshape(-1, 28, 28, 1) / 255.0

# 3. One-hot encoding
y_train_cat = to_categorical(y_train, 10)
y_test_cat = to_categorical(y_test, 10)

# 4. Modelo CNN
model = Sequential([
    Conv2D(32, (3, 3), activation='relu', input_shape=(28, 28, 1)),
    MaxPooling2D((2, 2)),
    Flatten(),
    Dense(64, activation='relu'),
    Dense(10, activation='softmax')
])

# 5. Compilar y entrenar
model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
model.fit(x_train, y_train_cat, epochs=5, batch_size=32, validation_split=0.1)

# 6. Evaluar y predecir una imagen
loss, acc = model.evaluate(x_test, y_test_cat)
print(f"\nPrecisión en prueba: {acc:.2f}")

# Mostrar imagen y predicción
import numpy as np
imagen = x_test[0]
plt.imshow(imagen.squeeze(), cmap='gray')
plt.title('Imagen de prueba')
plt.axis('off')
plt.show()

pred = model.predict(np.array([imagen]))
print("Predicción:", np.argmax(pred))
print("Etiqueta real:", y_test[0])
