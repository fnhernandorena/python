import tensorflow as tf
import numpy as np

celsius = np.array([-40, -10, 0, 8, 15, 22, 38], dtype=float)
fahrenheit = np.array([-40, 14, 32, 46, 59, 72, 100], dtype=float)

oculta1 = tf.keras.layers.Dense(units=3, input_shape=[1])
oculta2 = tf.keras.layers.Dense(units=3)
salida = tf.keras.layers.Dense(units=1)
modelo = tf.keras.Sequential([oculta1, oculta2, salida])

modelo.compile(
    optimizer=tf.keras.optimizers.Adam(0.1),
    loss='mean_squared_error'
)

print("Starting training...\n")
historial = modelo.fit(celsius, fahrenheit, epochs=300, verbose=False)
print("Model trained!\n")

while True:
    try:
        
        print("Do a prediction!\n")
        value = input('\x1b[1;33m'+'Insert value to convert \n\n Press a letter to finish\n\n')
        newvalue = float(value)
        realvalue = newvalue*1.8+32
        entrada = np.array([newvalue])
        resultado = modelo.predict(entrada.reshape(-1, 1))
        print("\n AI result is " + str(resultado[0][0]) + " fahrenheit! \n")
        print(f"Math result {realvalue} \n")
        
    except ValueError:
        break
    
print("App finished!")