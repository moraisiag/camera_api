from flask import Flask, make_response, jsonify, request
from database import PyMongo
from image import Image

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
    image = Image()
    image.name = request.json['name']
    image.data = request.json['data']
    return make_response(
        jsonify(bd.insert_image(image))
    )

app.run()
