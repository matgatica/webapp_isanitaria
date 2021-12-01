from dash import dcc
from dash import html
from dash.dependencies import Input, Output
import dash
import pandas as pd
import plotly.express as px
import datetime as dt
from app import app
from datetime import date
import dash_bootstrap_components as dbc
from datetime import datetime as dt
import numpy as np

df_inv_res = pd.read_csv('DATA/casos_inv_comuna_res.csv',sep=",",parse_dates=True,infer_datetime_format=True)

df_inv_estab = pd.read_csv('DATA/casos_inv_comuna_estab.csv',sep=",",parse_dates=True,infer_datetime_format=True)

df_inv_res.fillna(0,inplace=True)
df_inv_estab.fillna(0,inplace=True)




lista_comunas=[]
for i in df_inv_res.cont_comuna.unique():
    mini_dict={'label':f'{i}',"value":f"{i}"}
    lista_comunas.append(mini_dict) 

lista_comunas_estab=[]
for i in df_inv_estab.comuna_estab_deis.unique():
    mini_dict={'label':f'{i}',"value":f"{i}"}
    lista_comunas_estab.append(mini_dict) 



layout = html.Div([
    html.H1(children='Casos Investigación por comuna de residencia'),

    dcc.Graph(id='indicator-graphic'),

    dcc.Dropdown(
        id='id_comuna_residencia',
        options=lista_comunas,
        value=df_inv_res.cont_comuna.unique()[0]
    ),

     dcc.DatePickerRange(
        id='my-date-picker-range',
        min_date_allowed=date(1995, 8, 5),
        max_date_allowed=date(2022, 1, 1),
        initial_visible_month=date(2021, 11, 1),
        end_date=date(2021, 11 ,15),
        start_date=date(2021, 11, 1)
     ),
     
     html.H1(children='Casos Investigación por comuna de establecimiento'),

     dcc.Graph(id='indicator-graphic_2'),

     dcc.Dropdown(
        id='id_comuna_estab',
        options=lista_comunas_estab,
        value=df_inv_estab.comuna_estab_deis.unique()[0]
    ),

     dcc.DatePickerRange(
        id='my-date-picker-range_2',
        min_date_allowed=date(1995, 8, 5),
        max_date_allowed=date(2022, 1, 1),
        initial_visible_month=date(2021, 11, 1),
        end_date=date(2021, 11 ,15),
        start_date=date(2021, 11, 1)
     ),
     dbc.Row(dcc.Link('Go to App 2', href='/apps/app2')),
     dbc.Row(dcc.Link('Go to Home', href='/apps/'))

])

@app.callback(
    Output('indicator-graphic', 'figure'),

    [Input('id_comuna_residencia', 'value'),
    Input('my-date-picker-range', 'start_date'),
    Input('my-date-picker-range', 'end_date'),
    ]
)

def update_graph(value,startdate,enddate):               
    df=df_inv_res
    
    df=df[df.cont_comuna==value]
    dff = df[[x for x in df.columns if x>=startdate and x<=enddate]]
  
    dependiente=dff.values[0]
    
    independiente=np.array(dff.columns.map(lambda x: dt.strptime(x,"%Y-%m-%d").date()))
    
    fig2 = px.line(x=independiente,y=dependiente)

    fig2.update_layout(margin={'l': 40, 'b': 40, 't': 10, 'r': 0}, hovermode='closest')

    return fig2

@app.callback(
    Output('indicator-graphic_2', 'figure'),

    [
    Input('id_comuna_estab', 'value'),
    Input('my-date-picker-range_2', 'start_date'),
    Input('my-date-picker-range_2', 'end_date'),
    ]
)


def update_graph_2(value,startdate,enddate):
    df=df_inv_estab
    df=df[df.comuna_estab_deis==value]
    dff = df[[x for x in df.columns if x>=startdate and x<=enddate]]
    independiente=np.array(dff.columns.map(lambda x: dt.strptime(x,"%Y-%m-%d").date()))
    
    dependiente=dff.values[0]
    fig1 = px.line(x=independiente,y=dependiente)

    fig1.update_layout(margin={'l': 40, 'b': 40, 't': 10, 'r': 0}, hovermode='closest')

    return fig1
