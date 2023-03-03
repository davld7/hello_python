# Segundo ejemplo del profesor (optimizado).

import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt

# Preparar los datos
fahrenheit = np.array([])
celcius = np.array([])
for x in range(-40, 150):
    fahrenheit = np.append(fahrenheit, x)
    gradosCelcius = ((x-32)/1.8)
    celcius = np.append(celcius, gradosCelcius)
    print("Grados fahrenheit: "+str(x)+" = a " +
          str(gradosCelcius) + " Grados Celcius")

# Definir el modelo
entrada = tf.keras.layers.Input(shape=1)
densa_1 = tf.keras.layers.Dense(1, activation='relu')(entrada)
salida = tf.keras.layers.Dense(1, activation='linear')(densa_1)

# Compilar el modelo
model = tf.keras.models.Model(inputs=entrada, outputs=salida)
model.compile(optimizer=tf.keras.optimizers.Adam(
    0.09), loss='mean_squared_error')

# Entrenar el modelo
epochs_hist = model.fit(fahrenheit, celcius, epochs=250)

plt.xlabel('Número de Epocas')
plt.ylabel("Magnitud")
plt.plot(epochs_hist.history['loss'])
plt.show()

# Evaluar el modelo
print("Modelo después de entrenar: ")
print(model.predict([40.0]))

# Usar el modelo
prediction = model.predict([100])
print("Predicción en grados Celsius: {}".format(prediction[0][0]))
