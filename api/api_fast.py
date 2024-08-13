# Colocar a API no Ar
# uvicorn api_fast:app --reload
from fastapi import FastAPI
from database import PyMongo
from pydantic import BaseModel

app = FastAPI()
bd = PyMongo()

"""
#######################################################
OBS:
Tive dificuldades de prossegiur com a FastAPI, então 
mudei para a Flask a qual consegui evoluir melhor
#######################################################
"""

@app.get("/images")
async def get_images():
    """
    Obtem todas as imagens salvas
    :return: get_images
    """
    resp = bd.get_images()
    return resp


class Image(BaseModel):
    name: str
    data: str


@app.post('/image_id')
async def get_image(img: Image):
    """
    Obtem imagem do id informado
    :return: get_image_by_id
    """
    id = '66bac1d3607c263326f8a5ce'
    return bd.get_image_by_id(id)
