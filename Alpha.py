import pandas as pd
import statsmodels.formula.api as smf


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
print(factor.info())

#### Regressão

rsquared = pd.DataFrame()
fama_df = pd.DataFrame()

for i in funds.columns:
    rsquared[i] = smf.ols(formula=f'{i} ~ Market_Factor + HML + SMB + WML', data=factor)
    rsquared[i] = rsquared[i].fit()
    fama_df[i] = rsquared[i].rsquared_adj

print(fama_df)





