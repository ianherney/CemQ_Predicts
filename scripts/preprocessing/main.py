## Librerias
import pandas as pd
import joblib
import numpy as np
from pathlib import Path
from 

## Functions
# funcion para categorizar variables y eliminar datos anomalos 
def categorizar(df):
    var_numericas = df.columns[3:]
    df = df.replace( {'Error 3000': np.nan, '<NA>': np.nan} )
    df = df.convert_dtypes()
    return df

#funcion para eliminar datos atipicos 
def filtrar_por_iqr(df, var):
    Q1 = df[var].quantile(0.25)
    Q3 = df[var].quantile(0.75)
    IQR = Q3 - Q1
    filtro = (df[var] >= (Q1 - 1.5 * IQR)) & (df[var] <= (Q3 + 1.5 * IQR))
    return df[filtro]

# funcion para obtener dataframes por edades de desempeño 
def obtener_dataframe(df, target):

    sortnames = [ 'BOYT1',
                  'ESP2',
                  'ESP',
                  'ESP+',
                  'CTO.REACT',
                  'ECOART',
                  'ART.F',
                  'BASE1.BOYT1.MS',
                  'BASE2.BOYT1.MS',
                  'BOYT1.MS',
                ]

    categoricas = ['Start Time', 'Sortname', 'Location']

    var_quimicas = [ 'CaO_AVG',
                     'SiO2_AVG',
                     'Al2O3_AVG',
                     'Fe2O3_AVG',
                     'MgO_AVG',
                     'NO.SO3.P_AVG',
                     'Na2O.P_AVG',
                     'K2O.P_AVG',
                     'TiO2_AVG',
                     'P2O5_AVG',
                     'Mn2O3_AVG',
                     'Cl_AVG',
                     'Cr2O3_AVG'
                  ]

    var_fisicas = [
                    'LOI.P_AVG',
                    'NO.R45_AVG',
                    'WC_AVG',
                    'WR_AVG',
                    'SETINI_AVG',
                    'SETFIN_AVG',
                    'FLOW_AVG'
                   ]

    resistencias = ['R1',
                    'R3',
                    'R7',
                    'R28'
                   ]

    dict_resistencias = {
                          'NO.1CSA_AVG': 'R1' ,
                          'NO.3CSA_AVG' : 'R3',
                          'NO.7CSA_AVG' : 'R7',
                          'NO.28CSA_AVG' : 'R28'
                        }

    var_numericas = df.columns[3:]
    df = df.replace( {'Error 3000': np.nan, '<NA>': np.nan} )
    df = df.convert_dtypes()

    df = df[df['Sortname'].isin(sortnames)]
    df = df[ ( df['Location'] == 'NO.561.d' ) | ( df['Location'] == 'NO.562.d' ) | ( df['Location'] == 'NO.563.d' ) | ( df['Location'] == 'NO.630.d' ) ]
    df = df.drop(columns=['NO.BLAINE_AVG', 'R38_AVG']).dropna()
    features = df.columns[3:]

    for var in features:
      df = filtrar_por_iqr(df, var)

    df = df.rename(columns = dict_resistencias)
    df = df[ categoricas + var_quimicas + var_fisicas + resistencias[:resistencias.index(target)+1]]

    path= f'./data/data_{target}.csv'
    df.to_csv(path, index = False)

    return df

def features_target(df, drop_cols, y):
    features = df.drop(drop_cols, axis = 1)
    target = df[y]
    return features, target

def load_from_excel(path, sheet_name, engine):
    df = pd.read_excel(path,
                       sheet_name = sheet_name,
                       engine  = engine)[1:]
    return df
    
# Dataframes
data = load_from_excel( './data/data_raw.xlsx', 
                                  'quimicos',
                                  'openpyxl'
                                 )

df_R1 = obtener_dataframe(data, 'R1')
df_R3 = obtener_dataframe(data, 'R3')
df_R7 = obtener_dataframe(data, 'R7')
df_R28 = obtener_dataframe(data, 'R28')

if __name__ == '__main__':
    df_R1 = load_from_csv( './data/data_R1.csv')
    features, target = features_target(df_R1, ['Start Time', 'Sortname', 'Location', 'R1'], 'R1')
    print (df_R1.columns)
