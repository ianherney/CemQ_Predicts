
# Diccionario de datos

# Base de datos 1 | datos crudos
Este conjunto de datos contiene información relacionado con las pruebas quimicas realizadas a los cementos, tanto en etapas de desarrollo como en etapas de producción, La siguiente tabla describe el listado de pruebas:

## Descripción

RangeIndex: 106893 entries, 1 to 106893
Data columns (total 29 columns):

| # |  Column     |  Non-Null Count |  Dtype  | 
| --- |  ------   |      --------------  | -----  |
| 0 |  Start Time |   106893 | non-null |  datetime64[ns] |
| 1 |  Sortname   |    106893 | non-null | category    |
| 2 |  Location   |    106893 | non-null | category    |
| 3 |  CaO_AVG    |    79174 | non-null |  object        
| 4 |  SiO2_AVG   |    79309 | non-null |  object        
| 5 |  Al2O3_AVG  |    79309 | non-null |  object        
| 6 |  Fe2O3_AVG  |    79309 | non-null |  object        
| 7 |  MgO_AVG    |    53720 | non-null  | object        
| 8 |  NO.SO3.P_AVG  |  31791 | non-null |  object        
| 9 |  LOI.P_AVG  |    31695 | non-null  | object        
| 10 | Na2O.P_AVG  |   31701 | non-null  | object        
| 11 | K2O.P_AVG  |    31702 | non-null  | object        
| 12 | TiO2_AVG   |    45848 | non-null  | object        
| 13 | P2O5_AVG   |    44403 | non-null  | object        
| 14 | Mn2O3_AVG  |    34426 | non-null  | object        
| 15 | Cl_AVG     |    33250 | non-null  | object        
| 16 | Cr2O3_AVG  |    31643 | non-null  | object        
| 17 | NO.R45_AVG |    53239 | non-null  | object        
| 18 | R38_AVG    |    3380 | non-null   | object        
| 19 | NO.BLAINE_AVG  |  17630 | non-null |  object        
| 20 | WC_AVG    |     5235 | non-null   | object        
| 21 | WR_AVG    |     4715 | non-null  |  object        
| 22 | SETINI_AVG  |    4722 | non-null |   object        
| 23 | SETFIN_AVG  |   4722 | non-null  |  object        
| 24 | FLOW_AVG   |   5222 | non-null   | object        
| 25 | NO.1CSA_AVG   |  5158 | non-null |   object        
| 26 | NO.3CSA_AVG  |   5238 | non-null   | object        
| 27 | NO.7CSA_AVG   |   5204 | non-null   | object        
| 28 | NO.28CSA_AVG  |  5109 | non-null   | object        

| dtypes | num | 
| --- | --- |
| category | (2)|
| datetime64[ns] | (1) |
| object | (26) |


**memory usage:** 22.2+ MB


# Base de datos 2,3,4,5 | datos preprocesados
Estos conjunto de datos se obtienen despues de realizado el preproceso a los datos crudos, se separaron conjuntos para las distintas edades a predecir en los conjuntos se hablara de **target** para esta variable. 

## Descripción

RangeIndex: 1556 entries, 0 to 1555
Data columns (total 24 columns):

| # |  Column  | description  |     Non-Null Count | Dtype  | 
| --- |   ------ | ---  |     -------------- | ----- |  
| 0  | Start Time | Marcaje de tiempo en el cual se realizo el ensayo  |  1556 non-null |  object  |
| 1  | Sortname | tipo de cemento  |  1556 non-null |  category |
| 2  | Location | Punto donde se toma la muestra  |  1556 non-null |  category |
| 3  | CaO_AVG  | % Oxido de Calcio    |  1556 non-null |  float64 | 
| 4  | SiO2_AVG | % Oxido de Silice   |  1556 non-null |  float64 | 
| 5  | Al2O3_AVG | % Oxido de Aluminio  |  1556 non-null |  float64 | 
| 6  | Fe2O3_AVG | % Oxido de Hierro   |  1556 non-null |  float64 | 
| 7  | MgO_AVG  | % Oxido de Magnesio   |  1556 non-null |  float64 | 
| 8  | NO.SO3.P_AVG | % Oxido de azufre |  1556 non-null |   float64 | 
| 9  | Na2O.P_AVG | % Oxido de Sodio  |  1556 non-null |  float64 |
| 10 | K2O.P_AVG | % Oxido de Potasio  |  1556 non-null |  float64 |
| 11 | TiO2_AVG  | % Oxido de titanio  |  1556 non-null |  float64 | 
| 12 | P2O5_AVG  | % Oxido de Fosforo  |  1556 non-null |  float64 | 
| 13 | Mn2O3_AVG | % Oxido de Manganeso  |  1556 non-null |  float64 | 
| 14 | Cl_AVG  | % Cloruros    |  1556 non-null |  float64 |  
| 15 | Cr2O3_AVG | % Oxido de Cromo   |  1556 non-null |  float64 | 
| 16 | LOI.P_AVG | % perdida al fuego  |  1556 non-null |  float64 | 
| 17 | NO.R45_AVG | % retenido 45  |  1556 non-null |  float64 | 
| 18 | WC_AVG  | Relación agua - cemento   |  1556 non-null |  float64 | 
| 19 | WR_AVG  | Relación consumo de agua    |  1556 non-null |  float64 | 
| 20 | SETINI_AVG | Tiempo marcha inicial |  1556 non-null |  int64 |   
| 21 | SETFIN_AVG | Tiempo marcha final |  1556 non-null |  int64 |   
| 22 | FLOW_AVG  |  Consisitencia   |  1556 non-null |  float64 | 
| 23 | **R1 ( target )** | Resistencia a 1 día |  1556 non-null |  float64 | 

| dtypes | num | 
| --- | --- |
| category | (2)|
| float64 | (19) |
| int64 | (2) |
| object | (1) |

**memory usage:** 270.9+ KB

Los demas conjuntos son simialres a este pero filtrados para las variables objetivo o target de **R3**, **R7** y **R28**