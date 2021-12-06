import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
from app import app
import plotly.express as px
import pandas as pd
from datetime import date
from epiweeks import Week

# the style arguments for the sidebar.
SIDEBAR_STYLE = {
    'position': 'fixed',
    'top': 0,
    'left': 0,
    'bottom': 0,
    'width': '20%',
    'padding': '20px 10px',
    'background-color': '#f8f9fa'
}

# the style arguments for the main content page.
CONTENT_STYLE = {
    'margin-left': '25%',
    'margin-right': '5%',
    'padding': '20px 10p',
    'background-image': 'url(“assets/fondo3-1.png”)'
}

TEXT_STYLE = {
    'textAlign': 'center',
    'color': '#191970'
}

CARD_TEXT_STYLE = {
    'textAlign': 'center',
    'color': '#0074D9'
}

controls = dbc.Form(
    [
        html.Br(),
        
        dcc.Link(html.H3('Go To Trazabilidad'), href='/apps/app3'),
        dcc.Link(html.H3('Go To Home'), href='/'),
         
    ]
)

sidebar = html.Div(
    [
        html.H2('MENU', style=TEXT_STYLE),
        html.Hr(),
        controls
    ],
    style=SIDEBAR_STYLE,
)   


df_indicadores=pd.read_excel("DATA/df_resumendata.xlsx").drop(columns=["Unnamed: 0","Unnamed: 10"])
df_indicadores["fecha"]=pd.to_datetime(df_indicadores["source"].str[:20].str[12:],format='%Y%m%d')
df_indicadores["SE"]=df_indicadores["fecha"].apply(lambda x: Week.fromdate(x, system="iso").week)

lista_comunas_ind=[]
for i in df_indicadores.Comuna.unique():
    mini_dict={'label':f'{i}',"value":f"{i}"}
    lista_comunas_ind.append(mini_dict)



content_second_row = dbc.Row(
    [
        dbc.Col(children=[
            html.H2(children='Indicador 5'),
            dcc.Graph(id='graph_indicadores'),

        dcc.Dropdown(
            id='id_comuna_ind',
            options=lista_comunas_ind,
            value=['Santiago'],
            multi=True     
        ),
        dcc.RangeSlider(
            id='slider_ind',
            min=0,
            max=100,
            step=1,
            value=[5, 50]
        )]

        )
        
    ]
)





content = html.Div(
    [
        html.H2('INDICADORES', style=TEXT_STYLE),
        html.H6('<Inteligencia Sanitaria>', style=TEXT_STYLE),
        html.Hr(),
        content_second_row,
        
    
    ],
    style=CONTENT_STYLE
)

layout = html.Div([sidebar, content])


@app.callback(
    Output('graph_indicadores', 'figure'),
    [
    Input('id_comuna_ind', 'value'),
    Input('slider_ind', 'value')
    ]
)

def update_graph_4(value_comuna,value_ind):
    df=df_indicadores
    
    df=df[df.Comuna.isin(value_comuna)]
    dff = df[(df.SE>=value_ind[0])&(df.SE<=value_ind[1])]
    
    fig5 = px.line(dff,x='SE',y='Indicador 5',color='Comuna')

    fig5.update_layout(margin={'l': 40, 'b': 40, 't': 10, 'r': 0}, hovermode='closest')

    return fig5