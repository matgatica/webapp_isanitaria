from dash import dcc
import dash
from dash import html
from dash.dependencies import Input, Output
import dash_auth
from apps import app1, centro_trazabilidad, indicadores, home, info_nacional, vacunas
from app import app,server

server=server

VALID_USERNAME_PASSWORD_PAIRS = {
    'isanitaria': 'Seremi1025'
}
auth = dash_auth.BasicAuth(
    app,
    VALID_USERNAME_PASSWORD_PAIRS
)

app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content')
])


@app.callback(Output('page-content', 'children'),
              Input('url', 'pathname'))
              
def display_page(pathname):
    if pathname == '/apps/app1':
        return app1.layout
    elif pathname == '/apps/indicadores':
        return indicadores.layout
    elif pathname == '/apps/centro_trazabilidad':
        return centro_trazabilidad.layout
    elif pathname == '/apps/info_nacional':
        return info_nacional.layout
    elif pathname == '/apps/vacunas':
        return vacunas.layout
    else:
        return home.layout

if __name__ == '__main__':
    app.run_server(debug=True)
