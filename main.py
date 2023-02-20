from fastapi import FastAPI
import pandas as pd
import os
import numpy as np
from typing import List
from fastapi.responses import HTMLResponse
app= FastAPI()
@app.get("/", response_class=HTMLResponse)
async def main():
    html_content = """
    <html>
    <head>
        <style>
            body {
                background-color: #FFFF00; /* Amarillo fuerte */
                text-align: center;
                position: relative;
            }
            img {
                position: absolute;
                bottom: 0;
                left: 50%;
                transform: translate(-50%);
            }
            .big-img {
                width: 60%;
            }
            .btn {
                padding: 10px 18px;
                font-weight: bold;
                font-size: 18px;
                color: white;
                background-color: #4286f4; /* Azul claro */
                border: none;
                border-radius: 5px;
                margin: 10px;
            }
            .btn:hover {
                background-color: #366ec8; /* Azul oscuro */
                cursor: pointer;
            }
            .logo-img {
                position: absolute;
                top: 10px;
                left: 10px;
                height: 100px;
                weight: 100px;
                margin: 100px;
                padding: 100 px;
                rigth: 50 px;
            }
            .title {
                font-size: 24px;
                font-weight: bold;
            }
        </style>
    </head>
    <body>
        <div>
            <img class="logo-img" src="https://drive.google.com/uc?id=1GXYR9ERrB5DGFp3IcQBjlRgZk-SJa5ZW" alt="Logo de Google">
        </div>
        <h1 class="title">PROYECTO INDIVIDUAL I -- Machine Learning Operations (MLOps)</h1>
        <form>
            <button class="btn" formaction="/docs">Consultas generales</button>
            <button class="btn" formaction="/salir">Salir</button>
        </form>
        <div style="text-align: center;">
            <img class="big-img" src="https://drive.google.com/uc?id=1dddwFe-i09mfrzPLoLpT9rFtXD0vAkkn" alt="Descripción de la imagen">
        </div>
    </body>
    </html>
    """
    return html_content


   
@app.get("/get_score_count/{platform}/{scored}/{year}")
def get_score_count(platform: str, scored: float, year: int):
    # Generar el diccionario de combinaciones de letras para cada plataforma
    platform_dict = {}
    for plat, combos in {'netflix': ['n', 'ne', 'net', 'netf', 'netfl', 'netfli', 'netflix'],
                            'disney': ['d', 'di', 'dis', 'disn', 'disne', 'disney'],
                            'hulu': ['h', 'hu', 'hul', 'hulu'],
                            'amazon': ['a', 'am', 'ama', 'amaz', 'amazo', 'amazon']}.items():
        for combo in combos:
            platform_dict[combo] = plat

    # Buscar la plataforma correspondiente en el diccionario
    platform_full = platform_dict.get(platform, platform)

    # Cargar el archivo CSV en un DataFrame de Pandas
    df = pd.read_csv('df_plataformas_final.csv')

    # Contar el número de veces que se cumple la condición
    cantidad = np.count_nonzero(np.where((df["platform"] == platform_full) & (df["scored"] >scored) & (df["year"] == year), True, False))

    # Devolver la cantidad de veces que se cumple la condición
    return cantidad


@app.get("/get_actor/{platform}/{release_year}")
def get_actor(platform: str, release_year: int):
    # Generar el diccionario de combinaciones de letras para cada plataforma
    platform_dict = {}
    for plat, combos in {'netflix': ['n', 'ne', 'net', 'netf', 'netfl', 'netfli', 'netflix'],
                         'disney': ['d', 'di', 'dis', 'disn', 'disne', 'disney'],
                         'hulu': ['h', 'hu', 'hul', 'hulu'],
                         'amazon': ['a', 'am', 'ama', 'amaz', 'amazo', 'amazon']}.items():
        for combo in combos:
            platform_dict[combo] = plat

    # Buscar la plataforma correspondiente en el diccionario
    platform_full = platform_dict.get(platform, platform)

    # Cargar el archivo CSV en un DataFrame de Pandas
    df = pd.read_csv('df_plataformas_final.csv')

    # Filtrar por año y plataforma
    filtered_df = df[(df['platform'] == platform_full) & (df['year'] == release_year)]

    # Contar la cantidad de veces que aparece cada actor en la columna 'cast'
    actor_count = filtered_df['cast'].str.split(',').explode().str.strip().value_counts()

    # Devolver el actor que más se repite
    if actor_count.empty:
        return None
    else:
        return actor_count.index[0]
    
@app.get("/get_count_platform/{platform}")
def get_count_platform(platform: str):
    # Generar el diccionario de combinaciones de letras para cada plataforma
    platform_dict = {}
    for plat, combos in {'netflix': ['n', 'ne', 'net', 'netf', 'netfl', 'netfli', 'netflix'],
                         'disney': ['d', 'di', 'dis', 'disn', 'disne', 'disney'],
                         'hulu': ['h', 'hu', 'hul', 'hulu'],
                         'amazon': ['a', 'am', 'ama', 'amaz', 'amazo', 'amazon']}.items():
        for combo in combos:
            platform_dict[combo] = plat

    # Buscar la plataforma correspondiente en el diccionario
    platform_full = platform_dict.get(platform, platform)

    # Cargar el archivo CSV en un DataFrame de Pandas
    df = pd.read_csv('df_plataformas_final.csv')

    # Contar el número de veces que se cumple la condición
    cantidad = np.count_nonzero((df["platform"] == platform_full))

    # Devolver la cantidad de veces que se cumple la condición
    return cantidad


@app.get("/get_max_duration")
def get_max_duration(year: int = None, platform: str = None, duration_type: str = None):
    # Generar los diccionarios de combinaciones de letras para cada opción
    platform_dict = {}
    for plat, combos in {'netflix': ['n', 'ne', 'net', 'netf', 'netfl', 'netfli', 'netflix'],
                         'disney': ['d', 'di', 'dis', 'disn', 'disne', 'disney'],
                         'hulu': ['h', 'hu', 'hul', 'hulu'],
                         'amazon': ['a', 'am', 'ama', 'amaz', 'amazo', 'amazon']}.items():
        for combo in combos:
            platform_dict[combo] = plat

    duration_dict = {'min': ['min', 'mi', 'm'], 'season': ['season', 's', 'se', 'sea', 'seas', 'seaso']}

    # Buscar la plataforma correspondiente en el diccionario
    platform_full = platform_dict.get(platform, platform)

    # Buscar el tipo de duración correspondiente en el diccionario
    duration_type_full = duration_type
    for duration, combos in duration_dict.items():
        if duration_type in combos:
            duration_type_full = duration

    # Cargar el archivo CSV en un DataFrame de Pandas
    df = pd.read_csv('df_plataformas_final.csv')

    # Filtrar el DataFrame
    if duration_type_full is not None:
        filtered_df = df[df['duration_type'] == duration_type_full]
    else:
        filtered_df = df.copy()
    if year is not None:
        filtered_df = filtered_df[filtered_df['year'] == year]
    if platform_full is not None:
        filtered_df = filtered_df[filtered_df['platform'] == platform_full]

    # Ordenar el DataFrame y obtener la fila con la duración máxima
    sorted_df = filtered_df.sort_values(by='duration_int', ascending=False)
    max_duration = sorted_df.iloc[0][['title']]
    
    return max_duration


   