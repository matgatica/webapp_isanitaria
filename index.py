from dash import dcc
import dash
from dash import html
from dash.dependencies import Input, Output
import dash_auth
from apps import app1, app2, home, app3, app4, app5
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
    elif pathname == '/apps/app2':
        return app2.layout
    elif pathname == '/apps/app3':
        return app3.layout
    elif pathname == '/apps/app4':
        return app4.layout
    elif pathname == '/apps/app5':
        return app5.layout
    else:
        return home.layout

if __name__ == '__main__':
    app.run_server(debug=True)
