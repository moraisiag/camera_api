import json
from bson.json_util import dumps

from PIL import Image
import requests
import base64
URL = 'http://127.0.0.1:5000'

class APIClientTest:
    """
    Classe para testar a consulta e salvamento das imagens
    """
    def __init__(self):
        pass

    def get_images(self):
        """
        Consulta imagens
        :return:
        """
        resp = requests.get(URL + '/images')
        print(resp.json())

    def save_image(self):
        """
        Carrega uma imagem exemplo, converte em base64 e envia para a API de salvamento
        :return:
        """
        # foto = Image.open("C:\\Users\\Marcos\\Downloads\\Desenhos\\1008357-flip.jpg")
        # foto.show()
        with open('C:\\Users\\Marcos\\Downloads\\Desenhos\\1008357-flip.jpg', 'rb') as foto:
            encoded_data = base64.b64encode(foto.read())
        # print(encoded_data)
        dados = {
            'name': 'teste base64',
            'data': encoded_data
        }
        dados_json = json.loads(dumps(dados))
        #print(dados_json)
        #print(type(dados_json))
        resp = requests.post(URL+'/insert_image', json=dados_json)
        print(resp.json())


if __name__ == '__main__':
    im = APIClientTest()
    #im.save_image()
    im.get_images()
