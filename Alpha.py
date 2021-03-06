import pandas as pd
import numpy as np
from statsmodels import regression
import statsmodels.api as smf
from statsmodels.tools.tools import add_constant


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
print(factor.columns)

#### Regressão


def reg(y):
    X = add_constant(factor[['Market_Factor', 'HML', 'SMB', 'WML']])
    Y = y
    fit = smf.OLS(Y, X).fit()
    alpha_an = ((1+fit.params[0])**252)-1
    var = {'p_values': fit.pvalues['const'],
            'r_2': fit.rsquared_adj,
            'alpha': alpha_an}
    return var

dict = {}

for i in funds.columns:
    x = reg(factor[i])
    dict[i] = x
    
alfa = pd.DataFrame(dict)

alfa.to_excel('Alfa.xlsx')
