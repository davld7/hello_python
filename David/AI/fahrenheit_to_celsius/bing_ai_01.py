# Importamos las librerías necesarias
import numpy as np
import tensorflow as tf
from tensorflow import keras
import matplotlib.pyplot as plt

# Creamos unos datos de ejemplo
x_train = np.array([1, 5, 7, 17, 24, 40, -10])
y_train = np.array([-17.222222, -15, -13.8888889, -8.33333333, -4.44444444, 4.44444444, -23.3333333])

# Creamos el modelo con una capa densa con una sola neurona y función lineal
model = keras.Sequential([
    keras.layers.Dense(units=1, input_shape=[1], activation='linear')
])

# Compilamos el modelo con la función de pérdida MSE y el optimizador Adam
model.compile(loss='mean_squared_error', optimizer='adam')

# Entrenamos el modelo con los datos de ejemplo durante 500 épocas y guardamos el historial de entrenamiento
history = model.fit(x_train, y_train, epochs=800)

# Probamos el modelo con un dato nuevo: ¿Qué temperatura en celsius corresponde a 100 farenheit?
x_test = np.array([100])
y_pred = model.predict(x_test)
print("La temperatura en celsius es:", y_pred)

# Graficamos la curva de pérdida en función de las épocas usando matplotlib
plt.style.use('ggplot')  # Elegimos un estilo predefinido
# Usamos los datos del historial de entrenamiento para dibujar la curva con estilo rojo discontinuo y puntos circulares
plt.plot(history.history['loss'], 'r--o', label='Pérdida')
plt.xlabel('Época')  # Añadimos una etiqueta al eje x
plt.ylabel('Pérdida')  # Añadimos una etiqueta al eje y
plt.title('Curva de aprendizaje del modelo')  # Añadimos un título al gráfico
plt.grid(True)  # Añadimos una cuadrícula al gráfico
plt.legend()  # Añadimos una leyenda al gráfico
plt.show()  # Mostramos el gráfico en pantalla
