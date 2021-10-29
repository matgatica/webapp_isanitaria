import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import dash
import pandas as pd
import plotly.express as px
import datetime as dt
from app import app
from datetime import date

df_inv = pd.read_csv('DATA/CASOS_INV.csv',dtype=str,sep=";")
df_inv["_id.dia_seg"]=pd.to_datetime(df_inv["_id.dia_seg"],format="%d-%m-%Y")
df_inv["count"]=df_inv["count"].astype(int)
df_inv.sort_values(by="_id.dia_seg",inplace=True)


layout = html.Div([
    html.H1(children='Casos Investigación'),

    dcc.Graph(id='indicator-graphic'),

     dcc.DatePickerRange(
        id='my-date-picker-range',
        min_date_allowed=date(1995, 8, 5),
        max_date_allowed=date(2022, 1, 1),
        initial_visible_month=date(2021, 1, 1),
        end_date=date(2021, 6 ,1),
        start_date=date(2021, 1, 1)
     ),
     
     html.H1(children='Casos Investigación'),

     dcc.Graph(id='indicator-graphic_2'),

     dcc.DatePickerRange(
        id='my-date-picker-range_2',
        min_date_allowed=date(1995, 8, 5),
        max_date_allowed=date(2022, 1, 1),
        initial_visible_month=date(2021, 1, 1),
        end_date=date(2021, 6 ,1),
        start_date=date(2021, 1, 1)
     )
])

@app.callback(
    Output('indicator-graphic', 'figure'),

    [Input('my-date-picker-range', 'start_date'),
    Input('my-date-picker-range', 'end_date'),
    ]
)

def update_graph(
                 startdate,enddate):
    df=df_inv            
    dff = df[(df['_id.dia_seg'] >= startdate) & (df['_id.dia_seg'] <= enddate)]

    fig2 = px.scatter(data_frame=dff,x=dff["_id.dia_seg"],
                     y=dff["count"])


    fig2.update_layout(margin={'l': 40, 'b': 40, 't': 10, 'r': 0}, hovermode='closest')
    
                    

    return fig2


@app.callback(
    Output('indicator-graphic_2', 'figure'),

    [
    Input('my-date-picker-range_2', 'start_date'),
    Input('my-date-picker-range_2', 'end_date'),
    ]
)


def update_graph_2(
                 startdate,enddate):
    df=df_inv            
    dff = df[(df['_id.dia_seg'] >= startdate) & (df['_id.dia_seg'] <= enddate)]

    fig1 = px.scatter(data_frame=dff,x=dff["_id.dia_seg"],
                     y=[dff["count"]])

    fig1.update_layout(margin={'l': 40, 'b': 40, 't': 10, 'r': 0}, hovermode='closest')

    return fig1
