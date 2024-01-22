import json
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    
    return render_template('index.html')

@app.route('/fnaf_pc')
def fnaf_pc():
    with open('app/static/data/datos.json', 'r') as file:
        datos = json.load(file)

    # Ordena los datos de mayor a menor según el valor
    datos_ordenados = sorted(datos, key=lambda x: x['valor'], reverse=True)

    # Extrae las variables deseadas
    juego_name_1 = datos_ordenados[0]['juego']
    juego_downloader_1 = datos_ordenados[0]['valor']

    juego_name_2 = datos_ordenados[1]['juego']
    juego_downloader_2 = datos_ordenados[1]['valor']

    juego_name_3 = datos_ordenados[2]['juego']
    juego_downloader_3 = datos_ordenados[2]['valor']

    return render_template('fnaf_pc.html',
                           juego_name_1=juego_name_1, juego_downloader_1=juego_downloader_1,
                           juego_name_2=juego_name_2, juego_downloader_2=juego_downloader_2,
                           juego_name_3=juego_name_3, juego_downloader_3=juego_downloader_3)

@app.route('/fnaf_android')
def fnaf_android():
    return render_template('fnaf_android.html')

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True, port=3000)
