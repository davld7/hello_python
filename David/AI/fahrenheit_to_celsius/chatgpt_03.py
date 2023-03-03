import numpy as np
import matplotlib.pyplot as plt
from keras.models import Sequential
from keras.layers import Dense
from keras.optimizers import Adam

# Datos de entrada y salida
# Datos de entrada: grados Fahrenheit
fahrenheit = np.array([-40, -30, -20, -10, 0, 10, 20, 30, 40, 50], dtype=float)
# Datos de salida: grados Celsius
celsius = np.array([-40, -34.44, -28.89, -23.33, -17.78, -12.22, -
                   6.67, -1.11, 4.44, 10], dtype=float)

# Crear el modelo de la red neuronal
model = Sequential()  # Inicializar el modelo
# Agregar una capa densa con una neurona y una entrada de tamaño 1 (solo hay una variable de entrada)
model.add(Dense(1, input_shape=[1]))

# Compilar el modelo con la función de pérdida de error cuadrático medio y el optimizador Adam con una tasa de aprendizaje de 0.1
model.compile(loss='mean_squared_error', optimizer=Adam(0.1))

# Entrenar el modelo con los datos de entrada y salida, durante 500 épocas
history = model.fit(fahrenheit, celsius, epochs=700)

# Visualizar el aprendizaje del modelo
# Graficar la historia de la pérdida del modelo durante el entrenamiento
plt.plot(history.history['loss'])
plt.title('Gráfico de aprendizaje del modelo')  # Titular el gráfico
plt.xlabel('Época')  # Etiquetar el eje x con "Época"
plt.ylabel('Pérdida')  # Etiquetar el eje y con "Pérdida"
plt.show()  # Mostrar el gráfico

# Hacer predicciones con el modelo
# Datos de prueba: grados Fahrenheit
fahrenheit_test = np.array([60, 70, 80, 90, 100], dtype=float)
# Hacer predicciones con el modelo para los datos de prueba
celsius_test = model.predict(fahrenheit_test)

# Mostrar las predicciones
for i in range(len(fahrenheit_test)):  # Recorrer los datos de prueba
    # Mostrar las predicciones en pantalla, redondeando a un decimal los grados Fahrenheit y a tres decimales los grados Celsius
    print('{:.1f} grados Fahrenheit = {:.3f} grados Celsius'.format(
        fahrenheit_test[i], celsius_test[i][0]))
