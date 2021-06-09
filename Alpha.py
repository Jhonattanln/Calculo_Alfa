import pandas as pd
import numpy as np
from statsmodels import regression
import statsmodels.api as smf


#### Importando os dados
funds = pd.read_excel('economatica.xlsx', parse_dates=True, index_col=0)
hml = pd.read_excel('HML_Factor.xlsx', parse_dates=True, index_col=0)
mark = pd.read_excel('Market_Factor.xlsx', parse_dates=True, index_col=0)
smb = pd.read_excel('SMB_Factor.xlsx', parse_dates=True, index_col=0)
wml = pd.read_excel('WML_Factor.xlsx', parse_dates=True, index_col=0)


##### Ajustando nomes das colunas

def columns(df):
    df.columns = df.columns.str[43:]
columns(funds)

#### Concatenando dados
funds = funds.pct_change()
factor = pd.concat([mark, hml, smb, wml, funds], axis=1).dropna()
#print(factor.head())

#### Regressão
funds_name = funds.columns



def reg(y):
    alfa = regression.linear_model.OLS(y, smf.add_constant(np.column_stack((factor['Market_Factor'], factor['HML'], 
    factor['SMB'], factor['WML'])))).fit()
    print(alfa.summary())

reg(factor['Zenith Fc FIA'])
