# Despliegue de modelos

## Infraestructura

- **Nombre del modelo:** QPredict_R1D
- **Plataforma de despliegue:** MLFlow - entorno local

### Requisitos técnicos:

### Version
| Key     | Value |
|---------|-------|
| VERSION | 1.0.0 |

### Software requirements
- python >= 3.7
- pip

### Librerias
- mlflow==2.9.1
- cloudpickle==3.0.0
- numpy==1.26.2
- packaging==23.2
- pandas==2.1.4
- psutil==5.9.6
- pyyaml==6.0.1
- scikit-learn==1.3.2
- scipy==1.11.4
- xgboost==2.0.2


### Requisitos de seguridad:
VPN compañia



## Código de despliegue

- **Archivo principal:** 'models:/QP_R1D/Production'

- **Rutas de acceso a los archivos:**  'models:/QP_R1D/Production'

- **Variables de entorno:** server configurado por ahora en local: mlflow.set_tracking_uri("http://localhost:5000")

## Documentación del despliegue

- **Instrucciones de instalación:** ejecución mediante la siguientes lineas

- Carga del modelo
```python
def load_model():    
    logged_model = 'models:/QP_R1D/Production'
    model = mlflow.pyfunc.load_model(logged_model)
    return model
```
- Prediciones:

```python
model = load_model()
y_pred = model.predict(features_test)
```

- **Instrucciones de uso:** si bien se desplegaron en forma local, se prepara un template estandar que contiene las variables usadas, las mismas seran enviadas al modelo y se devoveran las predicciones, el objetivo es levantar el servicio en un entorno de google colab

