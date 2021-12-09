import dash_bootstrap_components as dbc
from dash import html
from dash import dcc
from app import app

# the style arguments for the sidebar.
SIDEBAR_STYLE = {
    'position': 'fixed',
    'top': 0,
    'left': 0,
    'bottom': 0,
    'width': '20%',
    'padding': '20px 10px'
    
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

content = html.Div([

        
        html.H1('SEREMI de Salud - Departamento de Salud Pública', style=TEXT_STYLE),
        html.H6('<Inteligencia Sanitaria>', style=TEXT_STYLE),
        html.Hr(),

        dbc.Row(dbc.Col(
        html.Img(src='assets/cropped-header-minsal_yo-me-vacuno_vertical.png',style={'height':'100%', 'width':'100%'}),
        md=3)
        ),

        dbc.Row(
        html.H1('asdasd')
        )
    ],
    style=CONTENT_STYLE
)

layout = html.Div([sidebar, content])