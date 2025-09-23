'''
Puesta en Producción de un Modelo de Machine Learning con Flask
Este script crea una API RESTful usando Flask para servir un modelo de machine learning previamente entrenado
y serializado con pickle. La API permite hacer predicciones enviando datos en formato JSON.
'''

# Importar Paquetes
from flask import Flask, request, jsonify
import pickle
import numpy as np

# Cargar Modelo
modelo = None

# Cargar el modelo
with open("archivo_estimador.pkl", 'rb') as file:
    modelo = pickle.load(file)

# Crear la Aplicación Flask
app = Flask(__name__)

@app.route('/predecir', methods=['POST'])
def predict():
    # obtener json
    data = request.get_json(force=True)
    
    # convertir los datos a un arreglo de Numpy
    input_data = np.array(data['input']).reshape(1, -1)
    
    # Hacer predicción
    prediccion = modelo.predict(input_data)
    
    # regresar predicción en formato json
    return jsonify({'prediccion': int(prediccion[0])})

if __name__ == '__main__':
    app.run(debug=True)

