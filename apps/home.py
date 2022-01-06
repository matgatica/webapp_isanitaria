import dash_bootstrap_components as dbc
from dash import html
from dash import dcc
from app import app
import pandas as pd

totales=pd.read_csv("https://raw.githubusercontent.com/MinCiencia/Datos-COVID19/master/output/producto3/TotalesPorRegion.csv")

casos_activos_confirmados=totales.loc[(totales["Region"]=="Metropolitana")&(totales["Categoria"]=="Casos activos confirmados")]
casos_activos_confirmados=casos_activos_confirmados.loc[:,casos_activos_confirmados.columns[-1]].values[0]

casos_activos_probables=totales.loc[(totales["Region"]=="Metropolitana")&(totales["Categoria"]=="Casos activos probables")]
casos_activos_probables=casos_activos_probables.loc[:,casos_activos_probables.columns[-1]].values[0]

casos_nuevos_totales=totales.loc[(totales["Region"]=="Metropolitana")&(totales["Categoria"]=="Casos nuevos totales")]
casos_nuevos_totales=casos_nuevos_totales.loc[:,casos_nuevos_totales.columns[-1]].values[0]

casos_nuevos_con_sintomas=totales.loc[(totales["Region"]=="Metropolitana")&(totales["Categoria"]=="Casos nuevos con sintomas")]
casos_nuevos_con_sintomas=casos_nuevos_con_sintomas.loc[:,casos_nuevos_con_sintomas.columns[-1]].values[0]

casos_nuevos_sin_sintomas=totales.loc[(totales["Region"]=="Metropolitana")&(totales["Categoria"]=="Casos nuevos sin sintomas")]
casos_nuevos_sin_sintomas=casos_nuevos_sin_sintomas.loc[:,casos_nuevos_sin_sintomas.columns[-1]].values[0]

casos_nuevos_nose_sintomas=casos_nuevos_totales-casos_nuevos_con_sintomas-casos_nuevos_sin_sintomas

casos_nuevos_antigeno=totales.loc[(totales["Region"]=="Metropolitana")&(totales["Categoria"]=="Casos nuevos confirmados por antigeno")]
casos_nuevos_antigeno=casos_nuevos_antigeno.loc[:,casos_nuevos_antigeno.columns[-1]].values[0]

fallecidos_totales=totales.loc[(totales["Region"]=="Metropolitana")&(totales["Categoria"]=="Fallecidos totales")]
fallecidos_totales=fallecidos_totales.loc[:,fallecidos_totales.columns[-1]].values[0]




card_activos_confirmados = [
    dbc.CardHeader(f"Región Metropolitana  al {totales.columns[-1]}"),
    dbc.CardBody(
        [
            html.H5(f"Casos Activos Confirmados: {casos_activos_confirmados}", className="card-title"),
            html.P(
                "Fuente: Ministerio de Salud. Ver en: https://www.minsal.cl/nuevo-coronavirus-2019-ncov/casos-confirmados-en-chile-covid-19/",
                className="card-text",
                style={"fontSize":12}
            ),
        ]
    ),
]

card_activos_probables = [
    dbc.CardHeader(f"Región Metropolitana  al {totales.columns[-1]}"),
    dbc.CardBody(
        [
            html.H5(f"Casos Activos Probables: {casos_activos_probables}", className="card-title"),
            html.P(
                "Fuente: Ministerio de Salud. Ver en: https://www.minsal.cl/nuevo-coronavirus-2019-ncov/casos-confirmados-en-chile-covid-19/",
                className="card-text",
                style={"fontSize":12}
            ),
        ]
    ),
]

card_fallecidos_totales = [
    dbc.CardHeader(f"Región Metropolitana  al {totales.columns[-1]}"),
    dbc.CardBody(
        [
            html.H5(f"Fallecidos Totales: {fallecidos_totales}", className="card-title"),
            html.P(
                "Fuente: Ministerio de Salud. Ver en: https://www.minsal.cl/nuevo-coronavirus-2019-ncov/casos-confirmados-en-chile-covid-19/",
                className="card-text",
                style={"fontSize":12}
            ),
        ]
    ),
]

card_nuevos_totales = [
    dbc.CardHeader(f"Región Metropolitana  al {totales.columns[-1]}"),
    dbc.CardBody(
        [
            html.H5(f"Casos Nuevos Totales: {casos_nuevos_totales}", className="card-title"),
            html.P(
                "Fuente: Ministerio de Salud. Ver en: https://www.minsal.cl/nuevo-coronavirus-2019-ncov/casos-confirmados-en-chile-covid-19/",
                className="card-text",
                style={"fontSize":12}
            ),
        ]
    ),
]

card_nuevos_con_sintomas = [
    dbc.CardHeader(f"Región Metropolitana  al {totales.columns[-1]}"),
    dbc.CardBody(
        [
            html.H5(f"Casos Nuevos con Sintomas: {casos_nuevos_con_sintomas}", className="card-title"),
            html.P(
                "Fuente: Ministerio de Salud. Ver en: https://www.minsal.cl/nuevo-coronavirus-2019-ncov/casos-confirmados-en-chile-covid-19/",
                className="card-text",
                style={"fontSize":12}
            ),
        ]
    ),
]

card_nuevos_sin_sintomas = [
    dbc.CardHeader(f"Región Metropolitana  al {totales.columns[-1]}"),
    dbc.CardBody(
        [
            html.H5(f"Casos Nuevos sin Sintomas: {casos_nuevos_sin_sintomas}", className="card-title"),
            html.P(
                "Fuente: Ministerio de Salud. Ver en: https://www.minsal.cl/nuevo-coronavirus-2019-ncov/casos-confirmados-en-chile-covid-19/",
                className="card-text",
                style={"fontSize":12}
            ),
        ]
    ),
]

# the style arguments for the sidebar.
SIDEBAR_STYLE = {
    'position': 'fixed',
    'top': 0,
    'left': 0,
    'bottom': 0,
    'width': '15%',
    'padding': '20px 10px'
    
}

# the style arguments for the main content page.
CONTENT_STYLE = {
    'margin-left': '15%',
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
        dcc.Link(dbc.Button("Trazabilidad", color="danger", className="d-grid gap-2 col-6 mx-auto",size='lg'), href='/apps/centro_trazabilidad'),
        html.Br(),
        dcc.Link(dbc.Button("Indicadores", color="danger", className="d-grid gap-2 col-6 mx-auto",size='lg'), href='/apps/indicadores'),
        html.Br(),
        dcc.Link(dbc.Button("Info Nacional", color="danger", className="d-grid gap-2 col-6 mx-auto",size='lg'), href='/apps/info_nacional'),
        html.Br(),
        dcc.Link(dbc.Button("Vacunas Nacional", color="danger", className="d-grid gap-2 col-6 mx-auto",size='lg'), href='/apps/vacunas'),
        html.Br(),
        dcc.Link(dbc.Button("Home", color="danger", className="d-grid gap-2 col-6 mx-auto",size='lg'), href='/')    
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

content = html.Div([

        
        html.H1('SEREMI de Salud - Departamento de Salud Pública', style=TEXT_STYLE),
        html.H6('<Inteligencia Sanitaria>', style=TEXT_STYLE),
        html.Hr(),

        dbc.Row([dbc.Col(
        html.A([html.Img(src='assets/SEREMISALUDMET.png',style={'height':'200px', 'width':'250px'})],href="https://seremi13.redsalud.gob.cl/"),
        ),
        dbc.Col(
        html.A([html.Img(src='assets/logo_ymv.png',style={'height':'150px', 'width':'250px'})],href="https://mevacuno.gob.cl/"),
        )]

        ),

        html.H1('CIFRAS REGION METROPOLITANA', style=TEXT_STYLE),
        

        dbc.Row([
            dbc.Col(dbc.Card(card_activos_confirmados, color="primary", inverse=True)),
            dbc.Col(dbc.Card(card_activos_probables, color="primary", inverse=True)),
            dbc.Col(dbc.Card(card_fallecidos_totales, color="primary", inverse=True)),
        ],
        className="mb-4"
        ),
        dbc.Row([
            dbc.Col(dbc.Card(card_nuevos_totales, color="primary", inverse=True)),
            dbc.Col(dbc.Card(card_nuevos_con_sintomas, color="primary", inverse=True)),
            dbc.Col(dbc.Card(card_nuevos_sin_sintomas, color="primary", inverse=True)),
            
        ],
        className="mb-4"
        ),



        dbc.Row([
        html.H1('<DASH - SALUD PUBLICA>'),
        
        html.P(children='''Términos y condiciones:

Este sitio utiliza datos estadísticos conforme a datos generados en la Unidad de Inteligencia Sanitaria y la base de datos del Ministerio de Ciencia, Tecnología, Conocimiento e Innovación disponibles en https://github.com/MinCiencia/Datos-COVID19; que se basa en el “Informe Epidemiológico” y el “Reporte Diario” emitido por el Ministerio de Salud de Chile, conforme las normas disponibles en www.minsal.cl específicamente las dispuestas para datos de carácter estadístico; las que, en todo caso para estos efectos se rigen conforme la Ley Nº 19.628 sobre protección a la vida privada y sus respectivas modificaciones posteriores, en lo que corresponda.
'''),
        html.P(children='''Este sitio web informa datos de carácter estadístico, únicamente con la finalidad de generar visualizaciones a nivel de mapas, gráficos y tableros interactivos durante el contexto de las medidas que la autoridad sanitaria ha adoptado a propósito del estado de catástrofe, por calamidad pública ocasionado por el COVID-19, utilizando para ello información que no puede ser asociada a un titular identificado o identificable. (Art. 2 letra e), Ley Nº 19.628)'''),
        
       
        ]   
        )
    ],
    style=CONTENT_STYLE
)

layout = html.Div([sidebar, content,html.Footer(
    children=[
        dbc.Row([
    html.A(html.Img(src='assets/paso-a-paso-logo.png'),style={'textAlign': 'center'})])
    ],className="mb-4")
    
    ])
