import dash_bootstrap_components as dbc
from dash import html
from dash import dcc

layout = html.Div(
    [
        dbc.Row(html.H1(
    children = 'Inteligencia Sanitaria',
    style = {
      'textAlign': 'center',
      'color': '#7FDBFF'
    }
  )),
        dbc.Row(dcc.Link('Go to App 1', href='/apps/app1')),
        dbc.Row(dcc.Link('Go to App 2', href='/apps/app2'))
    ]
)
