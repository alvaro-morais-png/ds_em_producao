import pandas as pd
import json
import requests
from flask import Flask, Response, request

#loading test dataset
df10 = pd.read_csv('/home/alvaro/Documentos/alvaro/comunidadeds/projetos/ds_em_producao_main/datasets/test.csv')
df_store_raw = pd.read_csv('/home/alvaro/Documentos/alvaro/comunidadeds/projetos/ds_em_producao_main/datasets/store.csv')

#merge test dataset +store
df_test = pd.merge(df10, df_store_raw, how='left', on='Store')

#choose store for predicion_ apenas uma loja para exemplificar o processo
df_test = df_test[df_test['Store']== 22 ]

#remove closed days
df_test = df_test[df_test['Open'] != 0]
df_test = df_test[~df_test['Open'].isnull()]
df_test = df_test.drop('Id', axis=1)


#conver dataframe to json
data = json.dumps(df_test.to_dict( orient='records' ))
data

# API Call
#porta local # url = 'http://0.0.0.0:5000/rossmann/predict'
url = 'https://rossmann-predict-luat.onrender.com/rossmann/predict'
header = {'Content-type': 'application/json'}
data = data

r = requests.post(url, data = data, headers=header)
print( 'Status Code {}'.format(r.status_code))
print(f'Status Code: {r.status_code}')
print(f'Erro: {r.text}')  # ← mostra o erro retornado pela API

d1 = pd.DataFrame(r.json(), columns=r.json()[0].keys() )

d2 = d1[['store', 'prediction']].groupby( 'store' ).sum().reset_index()

for i in range(len(d2)):
    print('Store Number {} will sell R$ {:,.2f} in the next six weeks'.format(
        d2.loc[i, 'store'], 
        d2.loc[i, 'prediction'] ) )