import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
from app import app
import plotly.express as px
import pandas as pd
from datetime import date

ventiladores=pd.read_csv("C:/Users/gaticam/Documents/GitHub/PROYECTO_WEB_APP_INTSANITARIA/DATA/ventiladores_nacional.csv",sep=',').drop(columns=["Unnamed: 0"])
ventiladores_unpivoted = ventiladores.melt(id_vars=['Ventiladores'], var_name='date', value_name='cuenta')
lista_ventiladores=[
                    {'label':'total',"value":"total"},
                    {'label':"disponibles","value":"disponibles"},
                    {'label':"ocupados","value":"ocupados"}
                    ]

residencias=pd.read_csv("C:/Users/gaticam/Documents/GitHub/PROYECTO_WEB_APP_INTSANITARIA/DATA/residencias_nacional.csv",sep=',').drop(columns=["Unnamed: 0"])
residencias_unpivoted = residencias.melt(id_vars=['Region','Categoria'], var_name='date', value_name='cuenta')

lista_regiones_residencias=[]
for i in residencias.Region.unique():
    mini_dict={'label':f'{i}',"value":f"{i}"}
    lista_regiones_residencias.append(mini_dict)

lista_categorias_residencias=[]
for i in residencias.Categoria.unique():
    mini_dict={'label':f'{i}',"value":f"{i}"}
    lista_categorias_residencias.append(mini_dict)

# the style arguments for the sidebar.
SIDEBAR_STYLE = {
    'position': 'fixed',
    'top': 0,
    'left': 0,
    'bottom': 0,
    'width': '20%',
    'padding': '20px 10px',
    
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
  
}

CARD_TEXT_STYLE = {
    'textAlign': 'center',
    'color': '#0074D9'
}

controls = dbc.Form(
    [
        html.Br(),
        
        dcc.Link(html.H3('Go To Trazabilidad'), href='/apps/app3'),
        dcc.Link(html.H3('Go To Indicadores'), href='/apps/app2'),
        dcc.Link(html.H3('Go To Info Nacional'), href='/apps/app4'),
        dcc.Link(html.H3('Go To Vacunas Nacional'), href='/apps/app5'),
        dcc.Link(html.H3('Go To Home'), href='/')
            
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

content_ventiladores = dbc.Row(
    [
        
        html.H2(children='VENTILADORES NACIONAL'),
        dcc.Graph(id='ventiladores_nacional'),

        dcc.Dropdown(
            id='id_ventiladores',
            options=lista_ventiladores,
            value=['total','disponibles','ocupados'],
            multi=True     
        ),
        dcc.DatePickerRange(
            id='date_range_ventiladores',
            min_date_allowed=date(1995, 8, 5),
            max_date_allowed=date(2022, 1, 1),
            initial_visible_month=date(2021, 1, 1),
            end_date=date(2021, 12 , 1),
            start_date=date(2021, 1, 1)
        )]
        )
    
content_residencias = dbc.Row(
    [
        
        html.H2(children='RESIDENCIAS NACIONAL'),
        dcc.Graph(id='residencias_nacional'),

        dcc.Dropdown(
            id='id_regiones_residencias',
            options=lista_regiones_residencias,
            value=['Metropolitana'],
            multi=True     
        ),
        dcc.Dropdown(
            id='id_categorias_residencias',
            options=lista_categorias_residencias,
            value='cupos totales',
               
        ),
        
        dcc.DatePickerRange(
            id='date_range_residencias',
            min_date_allowed=date(1995, 8, 5),
            max_date_allowed=date(2022, 1, 1),
            initial_visible_month=date(2021, 1, 1),
            end_date=date(2021, 12 , 1),
            start_date=date(2021, 1, 1)

        )]
        )

content = html.Div(
    [
        html.H2('INFO NACIONAL', style=TEXT_STYLE),
        html.H6('<Inteligencia Sanitaria>', style=TEXT_STYLE),
        html.Hr(),
        content_ventiladores,
        content_residencias
    
        
    ],
    style=CONTENT_STYLE
)

layout = html.Div([sidebar, content])


@app.callback(
    Output('ventiladores_nacional', 'figure'),
    [
    Input('id_ventiladores', 'value'),
    Input('date_range_ventiladores', 'start_date'),
    Input('date_range_ventiladores', 'end_date'),
    ]
    )

def update_graph(value,startdate,enddate):               
    df=ventiladores_unpivoted
    
    df=df[df.Ventiladores.isin(value)]
    dff = df[(df.date>=startdate)&(df.date<=enddate)]
    fig2 = px.line(dff,x='date',y='cuenta',color='Ventiladores')

    fig2.update_layout(margin={'l': 40, 'b': 40, 't': 10, 'r': 0}, hovermode='closest')

    return fig2

    
@app.callback(
    Output('residencias_nacional', 'figure'),
    [
    Input('id_regiones_residencias', 'value'),
    Input('id_categorias_residencias', 'value'),
    Input('date_range_residencias', 'start_date'),
    Input('date_range_residencias', 'end_date'),
    ]
    )

def update_graph(regiones_residencias,categorias_residencias,startdate,enddate):               
    df=residencias_unpivoted
    
    df=df[(df.Region.isin(regiones_residencias))&(df.Categoria==categorias_residencias)]
    dff = df[(df.date>=startdate)&(df.date<=enddate)]
    fig3 = px.line(dff,x='date',y='cuenta',color='Region')

    fig3.update_layout(margin={'l': 40, 'b': 40, 't': 10, 'r': 0}, hovermode='closest')

    return fig3