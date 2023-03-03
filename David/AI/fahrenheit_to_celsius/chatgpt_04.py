# Importamos la librería NumPy para trabajar con arrays y operaciones matemáticas
import numpy as np
# Importamos los módulos Keras y TensorFlow para crear y entrenar la red neuronal
from tensorflow import keras
# Importamos el módulo Matplotlib para crear gráficas del aprendizaje del modelo
import matplotlib.pyplot as plt

# Datos de entrada (grados Fahrenheit)
fahrenheit = np.array([-40, -10, 0, 8, 15, 22, 38, 48, 62, 70], dtype=float)
# Datos de salida (grados Celsius)
celsius = np.array([-40, -23.333, -17.778, -13.333, -
                   9.444, -5.556, 3.333, 8.889, 16.667, 21.111], dtype=float)

# Creamos el modelo
model = keras.Sequential([
    # Capa de entrada con una sola variable de entrada (grados Fahrenheit)
    keras.layers.Dense(units=1, input_shape=[1])
])

# Compilamos el modelo con el optimizador Adam y la función de pérdida de error cuadrático medio (MSE)
model.compile(optimizer=keras.optimizers.Adam(1), loss='mean_squared_error')

# Entrenamos el modelo con los datos de entrada y salida, y un número determinado de épocas (iteraciones)
# Utilizamos la opción verbose=True para que se muestre en la consola el avance del entrenamiento por cada época
history = model.fit(fahrenheit, celsius, epochs=300, verbose=True)

# Imprimimos la gráfica del aprendizaje del modelo
plt.plot(history.history['loss'])
plt.title('Aprendizaje del modelo')
plt.ylabel('Pérdida')
plt.xlabel('Época')
plt.show()

# Realizamos predicciones para algunos valores de grados Fahrenheit que no estaban en los datos de entrenamiento
fahrenheit_test = np.array([60, 70, 80, 90, 100], dtype=float)
celsius_test = model.predict(fahrenheit_test)

# Imprimimos las predicciones con una cadena de formato que muestra solo 3 decimales para los grados Celsius
for i in range(len(fahrenheit_test)):
    print('{:.1f} grados Fahrenheit = {:.3f} grados Celsius'.format(
        fahrenheit_test[i], celsius_test[i][0]))
