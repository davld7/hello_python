import numpy as np
import tensorflow as tf
from tensorflow import keras
import matplotlib.pyplot as plt

# Datos de entrada y salida
fahrenheit = np.array([-40, -30, -20, -10, 0, 10, 20, 30, 40, 50])
celsius = np.array([-40, -34, -29, -23, -18, -12, -6, 1, 7, 12])

# Modelo de red neuronal
model = keras.Sequential([
    keras.layers.Dense(units=1, input_shape=[1])
])
model.compile(optimizer=tf.optimizers.Adam(1), loss='mean_squared_error')

# Entrenamiento del modelo
history = model.fit(fahrenheit, celsius, epochs=1500, verbose=False)

# Gráfico del aprendizaje del modelo
plt.plot(history.history['loss'])
plt.title('Aprendizaje del modelo')
plt.ylabel('Error')
plt.xlabel('Época')
plt.show()

# Predicción de la conversión de grados Fahrenheit a Celsius
fahrenheit_test = np.array([100])
celsius_test = model.predict(fahrenheit_test)
print(celsius_test)
