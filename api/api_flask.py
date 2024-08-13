import os.path

from flask import Flask, make_response, jsonify, request, redirect,  flash
from database import PyMongo
from foto import Foto
from PIL import Image

app = Flask(__name__)
bd = PyMongo()


@app.route('/images', methods=['GET'])
def get_images():
    """
    Obtem todas as imagens salvas
    :return: get_images
    """
    return make_response(
        jsonify(bd.get_images())
    )


@app.route('/image_id', methods=['POST'])
def get_image():
    """
    Obtem imagem do id informado
    :return: get_image_by_id
    """
    id = request.json['id']
    return make_response(
        jsonify(bd.get_image_by_id(id))
    )


@app.route('/insert_image', methods=['POST'])
def insert_image():
    """
    Insere imagem no banco de dados
    :return: status_insert
    """
    foto = Foto()
    foto.name = request.json['name']
    foto.data = request.json['data']
    return make_response(
        jsonify(bd.insert_image(foto))
    )

@app.route('/save_image', methods=['POST'])
def save_image():
    """
    Insere imagem no banco de dados
    :return: status_insert
    """
    if 'file' not in request.files:
       flash('No file part')
       return redirect(request.url)
    file = request.files['file']
    file.save('imagem/')
    # return make_response(
    #     jsonify(bd.save_images(file))
    # )


if __name__ == '__main__':
    app.run(debug=True)
