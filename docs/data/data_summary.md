## Reporte de Datos

Este documento contiene los resultados del análisis exploratorio de datos.

### Resumen general de los datos

Este conjunto de datos contiene información relacionado con las pruebas fisco-quimicas del cemento:

### Variables Quimicas

<img src = "https://drive.google.com/uc?export=view&id=1s74zfnm24m_YwTAFb8bM8Hd0MRCunD4d" alt = "Encabezado Proyecto" width = "70%">  </img>

**Descripción**: Datos obtenidos apartir de analisis por Fluorecensia de rayos X

### Variables Fisicas

<img src = "https://drive.google.com/uc?export=view&id=1MjsUbqVohbBGbtM4Z4bFx44fZ2LClahj" alt = "Encabezado Proyecto" width = "70%">  </img>

**Descripción**: Datos obtenidos apartir de ensayos realizados de acuerdo a la norma **NTC 121**

[NTC-121:2021 | Norma Tecnica Colombiana - Especificación de desempeño para cemento hidráulico](https://tienda.icontec.org/gp-especificacion-de-desempeno-para-cemento-hidraulico-ntc121-2021.html "NTC-121")



## Resumen de calidad de los datos

En esta sección se presenta un resumen de la calidad de los datos. Se describe la cantidad y porcentaje de valores faltantes, valores extremos, errores y duplicados. También se muestran las acciones tomadas para abordar estos problemas.

- **Total de registros:** 106893
- **Numero de columnas:** 29
- **Objetivos:** 4
- **Caracteristicas:** 25

La siguiente visualización muestra la proporción de datos faltantes por variable

<img src = "https://drive.google.com/uc?export=view&id=1AYfREnfctA3eijUJQ-AH1xLdUVzutqew" alt = "Encabezado Proyecto" width = "100%">  </img>

lo que hizo necesario realizar procesos de limpieza para obtener los conjuntos de datos a trabajar

Los pasos realizados fueron los siguientes:
- Eliminación de datos faltantes
- seleción de localizaciones de interes (molinos de cemento (3) y despacho), puesto que se contaba con data de pruebas de investigación no relevantes para el objetivo buscado en este modelado
- Eliminación de datos atipicos, se aplico en esto un filtrado usando 1.5 veces el rango intercuartilico

```python
def filtrar_por_iqr(df, var):
    Q1 = df[var].quantile(0.25)
    Q3 = df[var].quantile(0.75)
    IQR = Q3 - Q1
    filtro = (df[var] >= (Q1 - 1.5 * IQR)) & (df[var] <= (Q3 + 1.5 * IQR))
    return df[filtro]
```

Finalmente se obtuvo lo siguiente:

Matriz de variables y localizaciones elegidas:

<img src = "https://drive.google.com/uc?export=view&id=1fIZDU7u00JuWytlwjHLKlGBj0YNJgMyV" alt = "Encabezado Proyecto" width = "30%">  </img>

Si datos faltantes o nulos:

<img src = "https://drive.google.com/uc?export=view&id=17jgKs9Y_9IftY-8epumA-1B6LLliRkCj" alt = "Encabezado Proyecto" width = "100%">  </img>

- **Total de registros:** 1556
- **Numero de columnas:** 24
- **Objetivos:** 1 / una por cada edad objetivo
- **Caracteristicas:** 23

## Variable objetivo

Cada conjunto de datos preprocesado contiene una variable objetivo

| conjunto | variable objetivo |
| ---- | ---- |
| df_R1 | R1 |
| df_R3 | R3 |
| df_R7 | R7 |
| df_R28 | R28 |

## Variables individuales

Se realizo un analisis por cada variable identificando su tendencia, histograma y diagrama de caja por localización, esto permitio determinar comportamientos individuales en función de la localización y a su vez identificar datos atipicos en conversación con los responsables del control de proceso

algunas muestras de ellos son las siguientes:

### Propiedad Quimica: 

Contenido de calicio (**var = CaO_AVG**) 
<img src = "https://drive.google.com/uc?export=view&id=1Zm0g-WqRFt_4EkwBiYPbH2LBmgBliqvp" alt = "Encabezado Proyecto" width = "100%">  </img>


### Propiedad Fisica
Finura (**var = R45**)
<img src = "https://drive.google.com/uc?export=view&id=1T-x16E8YZWkzDlvnqFyv0MWga9O6khyQ" alt = "Encabezado Proyecto" width = "100%">  </img>

## Ranking de variables

Utilizando un analisis de correlaciones se obtuvo los ranking por variables para realizar la predicción de cada una de las edades.

>Ranking obtenido  
<img src = "https://drive.google.com/uc?export=view&id=1aOujoojMOrQfH5uavrWAvXoiVqkuWAYt" alt = "Encabezado Proyecto" width = "10%">  </img>


## Relación entre variables explicativas y variable objetivo

### Matiriz de correlaciones
<img src = "https://drive.google.com/uc?export=view&id=1GSdvoZRaujiBz613UYLifjNr8XCq-2TU" alt = "Encabezado Proyecto" width = "60%">  </img>

las variables fisicas tiene una posición dominante en el ranking, si embargo dado la diversidad de localizaciones y tipos de cementos esto puede generar alteraciones no vistas en este análisis

### Modelado
Se realizo un modelado inicial con un model de regresion lineal multivariables

obteniendo los siguientes resultados:

<img src = "https://drive.google.com/uc?export=view&id=18KRHZknja1arrDvcfkwR0aMakaeyun6r" alt = "Encabezado Proyecto" width = "100%">  </img>

Si bien se observa un buen comportamiento entre el valor real y el valor predicho, las metricas obtenidas fueron las siguientes

<img src = "https://drive.google.com/uc?export=view&id=1hC1iaFeEIYZBOEZO6c5hREK8z8Sfi80I" alt = "Encabezado Proyecto" width = "20%">  </img>

valores muy positivos para los conjuntos de entrenamiento y prueba, de manera similar la metrica de evaluación **MAE**

Al realizar una extracción de los coeficiones de cada una de las variables se obtuvo lo sguiente:

<img src = "https://drive.google.com/uc?export=view&id=1xS76cL8tSKQf-I0nVSVKgnM-qXNFP_Q0" alt = "Encabezado Proyecto" width = "30%">  </img>

En este punto podemos detallar que si bien se obtienen buenas predicciones los valores con mas peso en el modelo lineal basico estan siendo puestos por las variables categoricas (transformadas con **OneHotEncoder**) mientras que las demas variables tienen pesos poco significativos, podria inducirse por un fuerte nivel de multicolinearidad, puesto que muchas de las variables estan correlacionadas entre si.

Se abordaron diferentes tipos de modelos y tenicas para aboradar este tema