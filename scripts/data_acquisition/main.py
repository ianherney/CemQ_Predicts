## Librerias
import pandas as pd
import joblib
import numpy as np
from pathlib import Path

## Functions

# funcion de carga de datos formato excel
def load_from_excel(path, sheet_name, engine):
    df = pd.read_excel(path,
                       sheet_name = sheet_name,
                       engine  = engine)[1:]
    return df

# funcion de carga de datos formato csv
def load_from_csv(path):
    return pd.read_csv(path)

# funcion de carga de datos formato sql - por definir
def load_sql():
    pass


if __name__ == '__main__':
    # obtener Dataframe
    data = load_from_excel( '/content/CemQ_Predicts/data/data_raw.xlsx',
                                      'quimicos',
                                      'openpyxl'
                                    )

