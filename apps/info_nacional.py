import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
from app import app
import plotly.express as px
import pandas as pd
from datetime import date


pcr_por_region=pd.read_csv("https://raw.githubusercontent.com/MinCiencia/Datos-COVID19/master/output/producto7/PCR.csv")
pcr_unpivoted = pcr_por_region.melt(id_vars=['Region'], var_name='date', value_name='cuenta')
lista_regiones_pcr=[]
for i in pcr_por_region.Region.unique():
    mini_dict={'label':f'{i}',"value":f"{i}"}
    lista_regiones_pcr.append(mini_dict)

totales_por_region=pd.read_csv("https://raw.githubusercontent.com/MinCiencia/Datos-COVID19/master/output/producto3/TotalesPorRegion.csv")
totales_unpivoted = totales_por_region.melt(id_vars=['Region','Categoria'], var_name='date', value_name='cuenta')
lista_regiones_totales=[]
for i in totales_por_region.Region.unique():
    mini_dict={'label':f'{i}',"value":f"{i}"}
    lista_regiones_totales.append(mini_dict)

lista_categorias_totales=[]
for i in totales_por_region.Categoria.unique():
    mini_dict={'label':f'{i}',"value":f"{i}"}
    lista_categorias_totales.append(mini_dict)


ventiladores=pd.read_csv("DATA/ventiladores_nacional.csv",sep=',').drop(columns=["Unnamed: 0"])
ventiladores_unpivoted = ventiladores.melt(id_vars=['Ventiladores'], var_name='date', value_name='cuenta')
lista_ventiladores=[
                    {'label':'total',"value":"total"},
                    {'label':"disponibles","value":"disponibles"},
                    {'label':"ocupados","value":"ocupados"}
                    ]

residencias=pd.read_csv("DATA/residencias_nacional.csv",sep=',').drop(columns=["Unnamed: 0"])
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
    'margin-left': '20%',
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
        dcc.Link(dbc.Button("Go To Trazabilidad", color="danger", className="d-grid gap-2 col-6 mx-auto",size='lg'), href='/apps/centro_trazabilidad'),
        html.Br(),
        dcc.Link(dbc.Button("Go To Indicadores", color="danger", className="d-grid gap-2 col-6 mx-auto",size='lg'), href='/apps/indicadores'),
        html.Br(),
        dcc.Link(dbc.Button("Go To Info Nacional", color="danger", className="d-grid gap-2 col-6 mx-auto",size='lg'), href='/apps/info_nacional'),
        html.Br(),
        dcc.Link(dbc.Button("Go To Vacunas Nacional", color="danger", className="d-grid gap-2 col-6 mx-auto",size='lg'), href='/apps/vacunas'),
        html.Br(),
        dcc.Link(dbc.Button("Go To Home", color="danger", className="d-grid gap-2 col-6 mx-auto",size='lg'), href='/')    
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



content_pcr = dbc.Row(
    [
        
        html.H2(children='PCR NACIONAL'),
        dcc.Graph(id='pcr_nacional'),

        dcc.Dropdown(
            id='id_regiones_pcr',
            options=lista_regiones_pcr,
            value=['Metropolitana'],
            multi=True     
        ),
        dcc.DatePickerRange(
            id='date_range_pcr',
            min_date_allowed=date(1995, 8, 5),
            max_date_allowed=date(2022, 1, 1),
            initial_visible_month=date(2020, 6, 1),
            end_date=date(2021, 12 , 1),
            start_date=date(2020, 6, 1)
        )]
        )

content_totales = dbc.Row(
    [
        
        html.H2(children='TOTALES NACIONAL'),
        dcc.Graph(id='totales_nacional'),

        dcc.Dropdown(
            id='id_regiones_totales',
            options=lista_regiones_totales,
            value=['Metropolitana'],
            multi=True     
        ),
        dcc.Dropdown(
            id='id_categorias_totales',
            options=lista_categorias_totales,
            value='Casos acumulados',
               
        ),
        dcc.DatePickerRange(
            id='date_range_totales',
            min_date_allowed=date(1995, 8, 5),
            max_date_allowed=date(2022, 1, 1),
            initial_visible_month=date(2020, 6, 1),
            end_date=date(2021, 12 , 1),
            start_date=date(2020, 6, 1)
        )]
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
        content_totales,
        content_pcr,
        content_ventiladores,
        content_residencias
    
        
    ],
    style=CONTENT_STYLE
)

layout = html.Div([sidebar, content,html.Footer(children='<Inteligencia Sanitaria>',style=TEXT_STYLE)])



@app.callback(
    Output('pcr_nacional', 'figure'),
    [
    Input('id_regiones_pcr', 'value'),
    Input('date_range_pcr', 'start_date'),
    Input('date_range_pcr', 'end_date'),
    ]
    )

def update_graph(regiones_pcr,startdate,enddate):               
    df=pcr_unpivoted
    
    df=df[(df.Region.isin(regiones_pcr))]
    dff = df[(df.date>=startdate)&(df.date<=enddate)]
    fig3 = px.line(dff,x='date',y='cuenta',color='Region',template='plotly_dark')

    fig3.update_layout(margin={'l': 40, 'b': 40, 't': 10, 'r': 0}, hovermode='closest')

    return fig3










@app.callback(
    Output('totales_nacional', 'figure'),
    [
    Input('id_regiones_totales', 'value'),
    Input('id_categorias_totales', 'value'),
    Input('date_range_totales', 'start_date'),
    Input('date_range_totales', 'end_date'),
    ]
    )

def update_graph(regiones_totales,categorias_totales,startdate,enddate):               
    df=totales_unpivoted
    
    df=df[(df.Region.isin(regiones_totales))&(df.Categoria==categorias_totales)]
    dff = df[(df.date>=startdate)&(df.date<=enddate)]
    fig3 = px.line(dff,x='date',y='cuenta',color='Region',template='plotly_dark')

    fig3.update_layout(margin={'l': 40, 'b': 40, 't': 10, 'r': 0}, hovermode='closest')

    return fig3





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
    fig2 = px.line(dff,x='date',y='cuenta',color='Ventiladores',template='plotly_dark')

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
    fig3 = px.line(dff,x='date',y='cuenta',color='Region',template='plotly_dark')

    fig3.update_layout(margin={'l': 40, 'b': 40, 't': 10, 'r': 0}, hovermode='closest')

    return fig3