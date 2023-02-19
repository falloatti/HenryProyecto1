# HENRY LABS
#### PROYECTO INDIVIDUAL I -- Machine Learning Operations (MLOps)

##### Fernando Alloatti

------------

##### Temática

El proyecto consistía en situarse en el rol de Data Engineer, a quien como miembro del equipo de una empresa, el Tech Lead le solicita realizar un proceso de ETL sobre cuatro datasets proporcionados, conteniendo información relativa a los catálogos de series y películas de cuatro plataformas de streaming (Netflix, Hulu, Amazon Prime Video y Disney).

Como segunda parte del requerimiento, se solicitaba elaborar una API a efectos de disponibilizar los datos de manera online, los cuales debían ser accedidos mediante cinco consultas predefinidas.

Por último, se solicita documentar todo el proceso y el funcionamiento de la API, y efectuar un video que sería remitido al Tech Lead que nos encargó el proyecto para que nos efectúe un feedback sobre el mismo.
![texto alternativo](https://github.com/falloatti/HenryProyectoUno/blob/main/plataformas.png)

#### Propuesta de trabajo

##### Transformaciones: 
Para este MVP no necesitas perfección, ¡necesitas rapidez! ⏩ Vas a hacer estas, y solo estas, transformaciones a los datos:

Generar campo id: Cada id se compondrá de la primera letra del nombre de la plataforma, seguido del show_id ya presente en los datasets (ejemplo para títulos de Amazon = as123)

Los valores nulos del campo rating deberán reemplazarse por el string “G” (corresponde al maturity rating: “general for all audiences”

De haber fechas, deberán tener el formato AAAA-mm-dd

Los campos de texto deberán estar en minúsculas, sin excepciones

El campo duration debe convertirse en dos campos: duration_int y duration_type. El primero será un integer y el segundo un string indicando la unidad de medición de duración: min (minutos) o season (temporadas)


#####  Desarrollo API: 
Propones disponibilizar los datos de la empresa usando el framework FastAPI. Las consultas que propones son las siguientes:

Película con mayor duración con filtros opcionales de AÑO, PLATAFORMA Y TIPO DE DURACIÓN. (la función debe llamarse get_max_duration(year, platform, duration_type))

Cantidad de películas por plataforma con un puntaje mayor a XX en determinado año (la función debe llamarse get_score_count(platform, scored, year))

Cantidad de películas por plataforma con filtro de PLATAFORMA. (La función debe llamarse get_count_platform(platform))

Actor que más se repite según plataforma y año. (La función debe llamarse get_actor(platform, year))


##### Deployment: 
Se utiliza Deta para hacer el deployment de aplicaciones. 

#### Análisis exploratorio de los datos: (Exploratory Data Analysis-EDA)
El análisis exploratorio de datos (EDA) se realizó mediante una inspección de los datos de las columnas.
En el archivo EDA.py se encuentra el desarrollo completo. A modo de resumen se comenta que entre otras cosas se encontraron, post depuración de valores repetidos:

userId int64 Valores no nulos:  11013823
score float64 Valores no nulos:  11013823
timestamp datetime64[ns] Valores no nulos:  11013823
id object Valores no nulos:  11013823
type object Valores no nulos:  11013823
title object Valores no nulos:  11013823
director object Valores no nulos:  7056968
cast object Valores no nulos:  8465400
country object Valores no nulos:  5509022
date_added datetime64[ns] Valores no nulos:  6440690
year int64 Valores no nulos:  11013823
rating object Valores no nulos:  11013823
listed_in object Valores no nulos:  11013823
platform object Valores no nulos:  11013823
duration_int int64 Valores no nulos:  11013823
duration_type object Valores no nulos:  10924436
scored float64 Valores no nulos:  11013823
 
- 115077 usuarios únicos, donde el 80.0% del total de visualizaciones, corrsponde a 30549 usuarios, es decir, solo el 26.55% de ellos. 
- 22998 id de películas únicos. 
- los valores de score van en un rango de 1 a 5, con una media de 3.53.
- del total de datos, el 71.63% corresponde a movies y el 28.37% corresponde a tv show. 
- existen 22042 valores únicos para 'title', se vericaron casos aleatorios y el motivo de no coincidencia con la cantidad de 'id' es que se trata de películas con el mismo nombre o lanzadas en distintas plataformas. 
- el top 5 de directores es 'mark knight', 'cannis holder', 'jay chapman', 'moonbug entertainment', 'arthur van merwijk', se realiza un split de los datos de la columna, se calcularon los que mas frecuencia tienen, se generan variables dummies de estos y se elimina la columna. 
- se procesaron las clasificaciones y se obtuvo que el genero mas visto es drama con el 15.16%, seguido de comedias con el 8.14% y documentales con el 6.23%. 

En el archivo pueden verse el resto de los datos, las transformaciones realizadas y la variables nuevas que fueron creadas. 
##### Sistema de recomendación:

Una vez que toda la data es consumible por la API ya lista para consumir para los departamentos de Analytics y de Machine Learning, y nuestro EDA bien realizado entendiendo bien los datos a los que tenemos acceso, es hora de entrenar nuestro modelo de machine learning para armar un sistema de recomendación de películas para usuarios, donde dado un id de usuario y una película, nos diga si la recomienda o no para dicho usuario.

##### Instrucciones para el uso de la API: 
La API se encuentra alojada en el siguiente link [Links](https://deta.space/discovery/r/r7fa4opjkhn7gj1a)

En la API se encontraran con la siguiente imagen, luego se debe hacer click en 'Consultas generales'.
![texto alternativo](https://github.com/falloatti/HenryProyectoUno/blob/main/plataformas.png)


