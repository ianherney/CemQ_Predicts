# Reporte del Modelo Final

## Resumen Ejecutivo

El modelo final seleccionado, XGBoost, ha demostrado un rendimiento destacado:

**score**: 	0.9625
**error cuadrático medio (MSE)**: de 1.255

 Estos resultados fueron obtenidos después de realizar alrededor de 300 pruebas utilizando la optimización automática de hiperparámetros con Optuna. XGBoost superó a otros modelos considerados en términos de puntaje y capacidad predictiva.

## Descripción del Problema
El problema abordado se centra en la construcción de un modelo predictivo eficaz. El contexto y los objetivos del problema deben ser claramente delineados. En este caso, la meta era desarrollar un modelo que ofreciera altas métricas de evaluación, minimizando la multicolinealidad. La elección de XGBoost como modelo final se basó en su capacidad para abordar este desafío y proporcionar un rendimiento sobresaliente.

## Descripción del Modelo

El modelo final implementado es XGBoost, un algoritmo de ensamble que ha demostrado ser efectivo en diversos problemas de regresión. La metodología incluyó la optimización de hiperparámetros utilizando Optuna, lo que permitió explorar una variedad de configuraciones y seleccionar aquellas que maximizaran el rendimiento del modelo.

Se realizaron distintas prueba con ayuda de MLFlow y optuna, en donde se eligieron los siguientes modelos

- **Linear_model**: Modelo base de implementación

- **Lasso**: usando la regularización Lasso que penaliza la suma del valor absolutos de los coeficientes de regresión a esta penalización se le conoce como l1 y tiene el efecto de forzar a que los coeficientes de los predictores tiendan a cero

- **Ridge**: usaado la regularización Ridge que penaliza la suma de los coeficientes elevados al cuadrado, a esta penalización se le conoce como l2 y tiene el efecto de reducir de forma proporcional el valor de todos los coeficientes del modelo pero sin que estos lleguen a cero

- **Random Forest (RF)**: Random Forest es un modelo de conjunto que combina múltiples árboles de decisión. Cada árbol en el bosque vota por una predicción y la predicción final es el promedio (en regresión) de las predicciones individuales. RF es conocido por su capacidad para manejar conjuntos de datos grandes y complejos.

- **Gradient Boosting Regressor (GBR)**: GBR también es un modelo de conjunto que construye árboles de decisión de forma secuencial. A diferencia de Random Forest, cada árbol se construye para corregir los errores del modelo existente. GBR es eficaz para mejorar la precisión predictiva.

- **Xtreme Gradient Boosting Regressor (XGBoost)**: XGBoost es una implementación eficiente y escalable de algoritmos de Gradient Boosting. Combina características como la regularización, la poda de árboles y la gestión de la velocidad de aprendizaje para mejorar la precisión y la generalización del modelo. Es particularmente útil en competiciones de ciencia de datos y se ha convertido en una elección popular para problemas de regresión y clasificación.

### Experimentos:

<img src = "https://drive.google.com/uc?export=view&id=1pvv17xU22Wk2yexvwceoeW7VxifjL8bf" alt = "Encabezado Proyecto" width = "60%">  </img>

Una vista en comparación con los otros modelos se evidencia en la siguiente grafica

<img src = "https://drive.google.com/uc?export=view&id=14tusDvN3ITJT9yY7KK9jDwP4Or_sOerx" alt = "Encabezado Proyecto" width = "60%">  </img>

## Parametros obtenidos

Una vista de los parametros vistos durante la optimización se detalla a continuación

<img src = "https://drive.google.com/uc?export=view&id=1F8j8LB2zvQ8R3g_ZoNU5L7zr8UJMd0JN" alt = "Encabezado Proyecto" width = "60%">  </img>

Obteniendo finalmente los siguientes:

<img src = "https://drive.google.com/uc?export=view&id=19oGgIykh-V_EVVC7TuAS4zOmXJMvCnzz" alt = "Encabezado Proyecto" width = "20%">  </img>



## Evaluación del Modelo

El rendimiento del modelo se evaluó utilizando métricas clave, donde se alcanzó un adecuado score y un MSE. Estos resultados indican que el modelo es capaz de realizar predicciones precisas y tiene una capacidad predictiva significativa. La elección de XGBoost se justifica no solo por sus excelentes métricas, sino también por su capacidad para manejar la multicolinealidad, proporcionando una solución robusta y generalizable.

**Metricas obtenidas**

<img src = "https://drive.google.com/uc?export=view&id=165oVRJJfOl8WC_ChscIkA8F4jofd9rjI" alt = "Encabezado Proyecto" width = "20%">  </img>


## Conclusiones y Recomendaciones

El modelo final, basado en XGBoost, ha superado las expectativas en términos de rendimiento predictivo. Sus fortalezas incluyen una alta capacidad predictiva y una resistencia a la multicolinealidad. Sin embargo, es esencial tener en cuenta las limitaciones del modelo y su aplicabilidad en diferentes contextos. Se recomienda realizar validación adicional en entornos específicos antes de su implementación definitiva.

## Referencias

Las decisiones y configuraciones del modelo se basaron en la literatura existente sobre los algoritmos utilizados, así como en la documentación oficial de las bibliotecas y herramientas empleadas (XGBoost, Optuna). Además, se consideraron los conocimientos previos sobre el problema específico abordado y la experiencia previa en modelado predictivo.
