import pickle
from surprise import SVD
from surprise import Dataset
from surprise.model_selection import cross_validate
import pandas as pd
from typing import List
from fastapi.responses import HTMLResponse
import pickle
from fastapi import FastAPI
import os
import numpy as np

app= FastAPI()


with open('mi_modelo_entrenado.pkl', 'rb') as archivo_pickle:
    modelo = pickle.load(archivo_pickle)

archivo_pickle.close()

with open('mi_modelo_entrenado.pkl', 'rb') as archivo_pickle:
    datos = pickle.load(archivo_pickle)
archivo_pickle.close()

@app.get("/prediccion")
async def obtener_prediccion(userId: int, id: str):
    prediccion = modelo.predict(userId, id)
    if prediccion.est >= 4:
        mensaje = "Tenes que verla!!", prediccion.est
    elif prediccion.est >= 3 and prediccion.est < 4:
        mensaje = "Te la recomendamos!", prediccion.est
    else:
        mensaje = "La neta wey? No la veas!", prediccion.est

    return {"mensaje": mensaje}
    