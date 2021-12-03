import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
from app import app
import plotly.express as px
import pandas as pd
from datetime import date


df_inv_res = pd.read_csv('DATA/casos_inv_comuna_res.csv',sep=",",parse_dates=True,infer_datetime_format=True)

df_inv_estab = pd.read_csv('DATA/casos_inv_comuna_estab.csv',sep=",",parse_dates=True,infer_datetime_format=True)

df_inv_res.fillna(0,inplace=True)
df_inv_estab.fillna(0,inplace=True)


df_inv_res_unpivoted = df_inv_res.melt(id_vars=['cont_comuna'], var_name='date', value_name='cuenta')
df_inv_estab_unpivoted = df_inv_estab.melt(id_vars=['comuna_estab_deis'], var_name='date', value_name='cuenta')


lista_comunas=[]
for i in df_inv_res.cont_comuna.unique():
    mini_dict={'label':f'{i}',"value":f"{i}"}
    lista_comunas.append(mini_dict) 

lista_comunas_estab=[]
for i in df_inv_estab.comuna_estab_deis.unique():
    mini_dict={'label':f'{i}',"value":f"{i}"}
    lista_comunas_estab.append(mini_dict)


df_casos_seg_res = pd.read_csv('DATA/casos_seg_comuna_res_prev.csv',sep=",",parse_dates=True,infer_datetime_format=True)
df_casos_seg_res.fillna(0,inplace=True)
df_casos_seg_res_unpivoted = df_casos_seg_res.melt(id_vars=['cont_comuna','prevision'], var_name='date', value_name='cuenta')

lista_comunas_seg_res=[]
for i in df_casos_seg_res.cont_comuna.unique():
    mini_dict={'label':f'{i}',"value":f"{i}"}
    lista_comunas_seg_res.append(mini_dict)


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
        html.P('Dropdown', style={
            'textAlign': 'center'
        }),
        dcc.Dropdown(
            id='dropdown',
            options=[{
                'label': 'Value One',
                'value': 'value1'
            }, {
                'label': 'Value Two',
                'value': 'value2'
            },
                {
                    'label': 'Value Three',
                    'value': 'value3'
                }
            ],
            value=['value1'],  # default value
            multi=True
        ),
        html.Br(),
        html.P('Range Slider', style={
            'textAlign': 'center'
        }),
        dcc.RangeSlider(
            id='range_slider',
            min=0,
            max=20,
            step=0.5,
            value=[5, 15]
        ),
        html.P('Check Box', style={
            'textAlign': 'center'
        }),
        dbc.Card([dbc.Checklist(
            id='check_list',
            options=[{
                'label': 'Value One',
                'value': 'value1'
            },
                {
                    'label': 'Value Two',
                    'value': 'value2'
                },
                {
                    'label': 'Value Three',
                    'value': 'value3'
                }
            ],
            value=['value1', 'value2'],
            inline=True
        )]),
        html.Br(),
        html.P('Radio Items', style={
            'textAlign': 'center'
        }),
        dbc.Card([dbc.RadioItems(
            id='radio_items',
            options=[{
                'label': 'Value One',
                'value': 'value1'
            },
                {
                    'label': 'Value Two',
                    'value': 'value2'
                },
                {
                    'label': 'Value Three',
                    'value': 'value3'
                }
            ],
            value='value1',
            style={
                'margin': 'auto'
            }
        )]),
        html.Br(),
        dbc.Button(
            id='submit_button',
            n_clicks=0,
            children='Submit',
            color='primary',
            
        ),
    ]
)

sidebar = html.Div(
    [
        html.H2('Parameters', style=TEXT_STYLE),
        html.Hr(),
        controls
    ],
    style=SIDEBAR_STYLE,
)

content_first_row = dbc.Row([
    dbc.Col(
        dbc.Card(
            [

                dbc.CardBody(
                    [
                        html.H4(id='card_title_1', children=['Card Title 1'], className='card-title',
                                style=CARD_TEXT_STYLE),
                        html.P(id='card_text_1', children=['Sample text.'], style=CARD_TEXT_STYLE),
                    ]
                )
            ]
        ),
        md=3
    ),
    dbc.Col(
        dbc.Card(
            [

                dbc.CardBody(
                    [
                        html.H4('Card Title 2', className='card-title', style=CARD_TEXT_STYLE),
                        html.P('Sample text.', style=CARD_TEXT_STYLE),
                    ]
                ),
            ]

        ),
        md=3
    ),
    dbc.Col(
        dbc.Card(
            [
                dbc.CardBody(
                    [
                        html.H4('Card Title 3', className='card-title', style=CARD_TEXT_STYLE),
                        html.P('Sample text.', style=CARD_TEXT_STYLE),
                    ]
                ),
            ]

        ),
        md=3
    ),
    dbc.Col(
        dbc.Card(
            [
                dbc.CardBody(
                    [
                        html.H4('Card Title 4', className='card-title', style=CARD_TEXT_STYLE),
                        html.P('Sample text.', style=CARD_TEXT_STYLE),
                    ]
                ),
            ]
        ),
        md=3
    )
])

content_second_row = dbc.Row(
    [
        dbc.Col(
            dcc.Graph(id='graph_1'), md=4
        ),
        dbc.Col(
            dcc.Graph(id='graph_2'), md=4
        ),
        dbc.Col(
            dcc.Graph(id='graph_3'), md=4
        )
    ]
)

content_third_row = dbc.Row(
    [
        dbc.Col(
            dcc.Graph(id='graph_4'), md=12,
        )
    ]
)

content_fourth_row = dbc.Row(
    [
        dbc.Col(children=[
            html.H2(children='Casos Investigación por comuna de establecimiento'),
            dcc.Graph(id='casos_inv_res'),

        dcc.Dropdown(
            id='id_comuna_residencia',
            options=lista_comunas,
            value=[df_inv_res.cont_comuna.unique()[0]],
            multi=True     
        ),
        dcc.DatePickerRange(
            id='my-date-picker-range',
            min_date_allowed=date(1995, 8, 5),
            max_date_allowed=date(2022, 1, 1),
            initial_visible_month=date(2021, 11, 1),
            end_date=date(2021, 11 ,15),
            start_date=date(2021, 11, 1)
        )],md=6
        ),

        dbc.Col(children=[
            html.H2(children='Casos Investigación por comuna de establecimiento'),

        dcc.Graph(id='casos_inv_estab'),

        dcc.Dropdown(
            id='id_comuna_estab',
            options=lista_comunas_estab,
            value=[df_inv_estab.comuna_estab_deis.unique()[0]],
            multi=True
        ),
        dcc.DatePickerRange(
            id='my-date-picker-range_2',
            min_date_allowed=date(1995, 8, 5),
            max_date_allowed=date(2022, 1, 1),
            initial_visible_month=date(2021, 11, 1),
            end_date=date(2021, 11 ,15),
            start_date=date(2021, 11, 1)
        )
        ],md=6)
    ]
)


content_fifth_row = dbc.Row(
    [
        dbc.Col(children=[
            html.H2(children='Casos Seguimiento por comuna de residencia y previsión'),
            dcc.Graph(id='casos_seg_res'),

        dcc.Dropdown(
            id='id_comuna_residencia_seg',
            options=lista_comunas_seg_res,
            value=[df_casos_seg_res.cont_comuna.unique()[0]],
            multi=True     
        ),
        dcc.DatePickerRange(
            id='my-date-picker-range_3',
            min_date_allowed=date(1995, 8, 5),
            max_date_allowed=date(2022, 1, 1),
            initial_visible_month=date(2021, 11, 1),
            end_date=date(2021, 11 ,15),
            start_date=date(2021, 11, 1)
        )],md=6
        )
    ]
)



content = html.Div(
    [
        html.H2('Dash Board I SANITARIA', style=TEXT_STYLE),
        html.Hr(),
        content_first_row,
        content_second_row,
        content_third_row,
        content_fourth_row,
        content_fifth_row
    ],
    style=CONTENT_STYLE
)

layout = html.Div([sidebar, content])


@app.callback(
    Output('graph_1', 'figure'),
    [Input('submit_button', 'n_clicks')],
    [State('dropdown', 'value'), State('range_slider', 'value'), State('check_list', 'value'),
     State('radio_items', 'value')
     ])
def update_graph_1(n_clicks, dropdown_value, range_slider_value, check_list_value, radio_items_value):
    print(n_clicks)
    print(dropdown_value)
    print(range_slider_value)
    print(check_list_value)
    print(radio_items_value)
    fig = {
        'data': [{
            'x': [1, 2, 3],
            'y': [3, 4, 5]
        }]
    }
    return fig


@app.callback(
    Output('graph_2', 'figure'),
    [Input('submit_button', 'n_clicks')],
    [State('dropdown', 'value'), State('range_slider', 'value'), State('check_list', 'value'),
     State('radio_items', 'value')
     ])
def update_graph_2(n_clicks, dropdown_value, range_slider_value, check_list_value, radio_items_value):
    print(n_clicks)
    print(dropdown_value)
    print(range_slider_value)
    print(check_list_value)
    print(radio_items_value)
    fig = {
        'data': [{
            'x': [1, 2, 3],
            'y': [3, 4, 5],
            'type': 'bar'
        }]
    }
    return fig


@app.callback(
    Output('graph_3', 'figure'),
    [Input('submit_button', 'n_clicks')],
    [State('dropdown', 'value'), State('range_slider', 'value'), State('check_list', 'value'),
     State('radio_items', 'value')
     ])
def update_graph_3(n_clicks, dropdown_value, range_slider_value, check_list_value, radio_items_value):
    print(n_clicks)
    print(dropdown_value)
    print(range_slider_value)
    print(check_list_value)
    print(radio_items_value)
    df = px.data.iris()
    fig = px.density_contour(df, x='sepal_width', y='sepal_length')
    return fig


@app.callback(
    Output('graph_4', 'figure'),
    [Input('submit_button', 'n_clicks')],
    [State('dropdown', 'value'), State('range_slider', 'value'), State('check_list', 'value'),
     State('radio_items', 'value')
     ])
def update_graph_4(n_clicks, dropdown_value, range_slider_value, check_list_value, radio_items_value):
    print(n_clicks)
    print(dropdown_value)
    print(range_slider_value)
    print(check_list_value)
    print(radio_items_value)  # Sample data and figure
    df = px.data.gapminder().query('year==2007')
    fig = px.scatter_geo(df, locations='iso_alpha', color='continent',
                         hover_name='country', size='pop', projection='natural earth')
    fig.update_layout({
        'height': 600
    })
    return fig


@app.callback(
    Output('casos_inv_res', 'figure'),
    [Input('id_comuna_residencia', 'value'),
    Input('my-date-picker-range', 'start_date'),
    Input('my-date-picker-range', 'end_date'),
    ]
    )

def update_graph(value,startdate,enddate):               
    df=df_inv_res_unpivoted
    
    df=df[df.cont_comuna.isin(value)]
    dff = df[(df.date>=startdate)&(df.date<=enddate)]
    fig2 = px.line(dff,x='date',y='cuenta',color='cont_comuna')

    fig2.update_layout(margin={'l': 40, 'b': 40, 't': 10, 'r': 0}, hovermode='closest')

    return fig2


@app.callback(
    Output('casos_inv_estab', 'figure'),

    [
    Input('id_comuna_estab', 'value'),
    Input('my-date-picker-range_2', 'start_date'),
    Input('my-date-picker-range_2', 'end_date'),
    ]
)


def update_graph_2(value,startdate,enddate):
    df=df_inv_estab_unpivoted
    
    df=df[df.comuna_estab_deis.isin(value)]
    dff = df[(df.date>=startdate)&(df.date<=enddate)]
  
    
    fig1 = px.line(dff,x='date',y='cuenta',color='comuna_estab_deis')

    fig1.update_layout(margin={'l': 40, 'b': 40, 't': 10, 'r': 0}, hovermode='closest')

    return fig1


@app.callback(
    Output('casos_seg_res', 'figure'),

    [
    Input('id_comuna_residencia_seg', 'value'),
    Input('my-date-picker-range_3', 'start_date'),
    Input('my-date-picker-range_3', 'end_date'),
    ]
)

def update_graph_3(value,startdate,enddate):
    df=df_casos_seg_res_unpivoted
    
    df=df[df.cont_comuna.isin(value)]
    dff = df[(df.date>=startdate)&(df.date<=enddate)]
  
    
    fig3 = px.line(dff,x='date',y='cuenta',color='cont_comuna',symbol='prevision')

    fig3.update_layout(margin={'l': 40, 'b': 40, 't': 10, 'r': 0}, hovermode='closest')

    return fig3


@app.callback(
    Output('card_title_1', 'children'),
    [Input('submit_button', 'n_clicks')],
    [State('dropdown', 'value'), State('range_slider', 'value'), State('check_list', 'value'),
     State('radio_items', 'value')
     ])
def update_card_title_1(n_clicks, dropdown_value, range_slider_value, check_list_value, radio_items_value):
    print(n_clicks)
    print(dropdown_value)
    print(range_slider_value)
    print(check_list_value)
    print(radio_items_value)  # Sample data and figure
    return 'Card Tile 1 change by call back'


@app.callback(
    Output('card_text_1', 'children'),
    [Input('submit_button', 'n_clicks')],
    [State('dropdown', 'value'), State('range_slider', 'value'), State('check_list', 'value'),
     State('radio_items', 'value')
     ])
def update_card_text_1(n_clicks, dropdown_value, range_slider_value, check_list_value, radio_items_value):
    print(n_clicks)
    print(dropdown_value)
    print(range_slider_value)
    print(check_list_value)
    print(radio_items_value)  # Sample data and figure
    return 'Card text change by call back'