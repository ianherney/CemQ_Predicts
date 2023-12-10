# Reporte del Modelo Baseline

Este documento contiene los resultados del modelo baseline.

## Descripción del modelo

Modelo de regresion lineal multiple

## Variables de entrada

Matriz de variables y localizaciones elegidas:

<img src = "https://drive.google.com/uc?export=view&id=1fIZDU7u00JuWytlwjHLKlGBj0YNJgMyV" alt = "Encabezado Proyecto" width = "30%">  </img>

## Variable objetivo

Resistencia a 1 día

## Evaluación del modelo

### Métricas de evaluación

Se tomaron dos metricas, siendo ellas el score (**R2**) y como funcion de perdida el **MSE**

### Resultados de evaluación

Los resultados obtenidos fueron los siguientes:

<img src = "https://drive.google.com/uc?export=view&id=1hC1iaFeEIYZBOEZO6c5hREK8z8Sfi80I" alt = "Encabezado Proyecto" width = "20%">  </img>

## Análisis de los resultados

valores muy positivos para los conjuntos de entrenamiento y prueba, de manera similar la metrica de evaluación **MAE**

Al realizar una extracción de los coeficiones de cada una de las variables se obtuvo lo sguiente:

<img src = "https://drive.google.com/uc?export=view&id=1xS76cL8tSKQf-I0nVSVKgnM-qXNFP_Q0" alt = "Encabezado Proyecto" width = "30%">  </img>

En este punto podemos detallar que si bien se obtienen buenas predicciones los valores con mas peso en el modelo lineal basico estan siendo puestos por las variables categoricas (transformadas con **OneHotEncoder**) mientras que las demas variables tienen pesos poco significativos, podria inducirse por un fuerte nivel de multicolinearidad, puesto que muchas de las variables estan correlacionadas entre si.

Se abordaron diferentes tipos de modelos y tenicas para aboradar este tema
## Conclusiones

Si bien se obtienen resultados entre las predicciones y los valores reales aparentemente optimos, el modelo presenta una fuerte incidencia o inclinacion por las variables categoricas dando a ellas unos pesos sobrepropocionados, desdibujando la importancia de las caracterisiticas fisico quimicas del cemento, lo que lleva a replantear el uso de este metodo.

## Referencias

[Sklearn - Linear_model ](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LinearRegression.html)
