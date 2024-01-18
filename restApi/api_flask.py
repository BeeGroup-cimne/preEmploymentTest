from flask import Flask, jsonify, request
from pymongo import MongoClient
import csv

app = Flask(__name__)

client = MongoClient('mongodb', 27017)
db = client['data']
coleccion = db['historico_kwh']

@app.route('/getKwh', methods=['GET'])
def getKwh():
    dia = request.args.get('dia')

    resultado = coleccion.find_one({'fecha': dia})

    if resultado:
        kwh = resultado['kwh']
        return jsonify({'msg': f'El dia {dia}: {kwh} Kwh'})
    else:
        return jsonify({'msg': f'No se encontraron datos para {dia}'}), 404



@app.route('/importCSV', methods=['POST'])
def importCSV():
    
    data = request.get_json()
    archivo_path = data['file']

    if archivo_path == '':
        return jsonify({'error': 'Nombre de archivo no válido'}), 400

    with open(archivo_path, 'r', encoding='utf-8') as archivo:
        lector_csv = csv.DictReader(archivo)
        for fila in lector_csv:
            fecha = fila['Date']
            kwh = fila['kwh']
            coleccion.insert_one({'fecha': fecha, 'kwh': kwh})
        
        return jsonify({'msg': 'Archivo CSV importado exitosamente'})


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')