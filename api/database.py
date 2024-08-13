import json
import pymongo
from bson.objectid import ObjectId
from bson.json_util import dumps
from image import Image

cluster = pymongo.MongoClient(
    "mongodb+srv://db_user:9L9JWU5oWBVxK3LU@cluster0.dnxkd.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
db = cluster.get_database('api_test')
collection = db.get_collection('image')


class PyMongo:
    """
    Classe responsável por executar a comunicação e iterações com banco de dados MongoDB
    """

    def __init__(self):
        pass

    def get_image_by_id(self, id):
        """
        Retorna a imagem do id informado
        :param id:
        :return: json_data
        """
        try:
            resp = collection.find_one({'_id': ObjectId(id)})
            json_data = json.loads(dumps(resp))
            return json_data
        except Exception as e:
            error = json.loads(dumps({'status': 'Erro: Problema ao acessar a imagem '+str(id)}))
            return error

    def get_images(self):
        """
        Retorna lista de todas as imagens salvas
        :return:
        """
        try:
            resp = collection.find({})
            list_resp = list(resp)
            json_data = json.loads(dumps(list_resp))
            return json_data
        except Exception as e:
            error = json.loads(dumps({'status': 'Erro: Problema ao acessar as imagens.'}))
            return error

    def insert_image(self, image):
        """
        Retorna lista de todas as imagens salvas
        :return:
        """
        msg: str
        try:
            dt = {
                'name': image.name,
                'data': image.data
            }
            collection.insert_one(dt)
            msg = json.loads(dumps({'status': 'Imagem ' + image.name + ' salva com sucesso!'}))
            return msg
        except Exception as e:
            error = json.loads(dumps({'status': 'Erro: Imagem ' + image.name + ' não foi salva.'}))
            return error


if __name__ == '__main__':
    bd = PyMongo()

    # Teste de consultas
    # resp = bd.get_image_by_id("66bac80f607c263326f8a5d4")
    resp = bd.get_images()

    # Teste insert
    i = Image()
    i.name = 'teste3'
    i.data = 'KHKIDHW*&¨#@BKJHD*&E'
    # resp = bd.insert_image(i)
    print(resp)
    print(type(resp))
