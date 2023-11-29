import pandas as pd
import numpy as np
import joblib
from pathlib import Path  

from sklearn.linear_model import ( LinearRegression, Lasso, Ridge, ElasticNet, RANSACRegressor, HuberRegressor )
from sklearn.ensemble import ( GradientBoostingRegressor, RandomForestRegressor)
from sklearn.model_selection import GridSearchCV
    
def load_from_csv(path):
    return pd.read_csv(path)

# funcion de separación de caracteristicas y variable objetivo
def features_target(df, drop_cols, y):
    features = df.drop(drop_cols, axis = 1)
    target = df[y]
    return features, target

def model_export(model, score):
        print(score)
        joblib.dump(model, f'./best_model{score}.pkl')


regressors = {            
            'Lasso' : Lasso(alpha = 0.1),
            'Ridge' : Ridge(alpha = 0.3),
            'ElasticNET':  ElasticNet(random_state = 42),
            'GBR' : GradientBoostingRegressor(random_state = 42),
            'RFR' : RandomForestRegressor(random_state = 42)                        
        }
        
params = {
           'Lasso' : {'alpha' : [0.01, 0.1, 0.3, 0.5, 1, 10, 100] },
            'Ridge' : {'alpha' : [0.01, 0.1, 0.3, 0.5, 1, 10, 100] },
            'ElasticNET': {'alpha' : [0.01, 0.1, 0.3, 0.5, 1, 10, 100] },
            'GBR' : {
                'loss': ['squared_error', 'absolute_error'],
                'learning_rate' : [ 0.01, 0.05, 0.1 ],
                'n_estimators' : [100, 500, 1000, 1500],
                'max_depth'    : [4, 6, 8, 10]
            },
            'RFR' : {
                'max_depth': [80, 90, 100, 110],
                'n_estimators': [50, 100, 200, 300, 1000]
            }
                
        }


def grid_training(features, target):

  best_score = 999
  best_model = None
            
  for regressor, regressors in regressors.items():

    grid_reg = GridSearchCV(regressors, params[regressor], cv=5).fit(features, target.values.ravel())
    score = np.abs(grid_reg.best_score_)
            
    if score < best_score:
      best_score = score
      best_model = grid_reg.best_estimator_
                
  model_export(best_model, best_score)


df_R1 = load_from_csv( './data/data_R1.csv')   
features, target = features_target(df_R1, ['Start Time', 'Sortname', 'Location', 'R1'], 'R1')   
grid_training(features, target)
            
        
                
                