import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
from app import app
import plotly.express as px
import pandas as pd
from datetime import date
from dash import dash_table



vacunas = pd.read_csv('https://raw.githubusercontent.com/MinCiencia/Datos-COVID19/master/output/producto81/vacunacion_comuna_edad_2daDosis.csv').drop(columns=["Codigo region","Codigo comuna"])

columnas=[x for x in vacunas.columns if x.isnumeric()]



# the style arguments for the sidebar.
SIDEBAR_STYLE = {
    'position': 'fixed',
    'top': 0,
    'left': 0,
    'bottom': 0,
    'width': '15%',
    'padding': '20px 10px',
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

tabla_vacuna = html.Div(
    className="row",
    children=[
        html.Div(
            dash_table.DataTable(
                id='table-paging-with-graph',
                columns=[

                    {"name": ["EDAD",i], "id": i} if i.isnumeric() else {"name": ["",i], "id": i}  for i in vacunas.columns
                ],
                page_current=0,
                page_size=20,
                page_action='custom',

                filter_action='custom',
                filter_query='',

                sort_action='custom',
                sort_mode='multi',
                sort_by=[],
                fixed_columns={'headers': True, 'data': 3},
                style_table={'minWidth': '100%'},
                style_cell={
                            # all three widths are needed
                            'minWidth': '180px', 'width': '180px', 'maxWidth': '180px',
                            'overflow': 'hidden',
                            'textOverflow': 'ellipsis',
                        },
                        style_header={
                                        'backgroundColor': 'rgb(30, 30, 30)',
                                        'color': 'white'
                                    },
                        style_data={
                                    'backgroundColor': 'rgb(50, 50, 50)',
                                    'color': 'white'
                                    }
            ),
            #style={'height': 750, 'overflowY': 'scroll'},
            #className='six columns'
        ),
        html.Div(
            id='table-paging-with-graph-container',
            className="five columns"
        )
    ]
)

operators = [['ge ', '>='],
             ['le ', '<='],
             ['lt ', '<'],
             ['gt ', '>'],
             ['ne ', '!='],
             ['eq ', '='],
             ['contains '],
             ['datestartswith ']]


def split_filter_part(filter_part):
    for operator_type in operators:
        for operator in operator_type:
            if operator in filter_part:
                name_part, value_part = filter_part.split(operator, 1)
                name = name_part[name_part.find('{') + 1: name_part.rfind('}')]

                value_part = value_part.strip()
                v0 = value_part[0]
                if (v0 == value_part[-1] and v0 in ("'", '"', '`')):
                    value = value_part[1: -1].replace('\\' + v0, v0)
                else:
                    try:
                        value = float(value_part)
                    except ValueError:
                        value = value_part

                # word operators need spaces after them in the filter string,
                # but we don't want these later
                return name, operator_type[0].strip(), value

    return [None] * 3


content = html.Div(
    [
        html.H2('VACUNAS NACIONAL', style=TEXT_STYLE),
        html.H6('<Inteligencia Sanitaria>', style=TEXT_STYLE),
        html.Hr(),
        html.P(children="""
        Datos que corresponden a los vacunados en cada una de las comunas de Chile, según residencia y edad.
        Estos datos provienen del Departamento de Estadísticas e Información Sanitaria (DEIS) del Ministerio de Salud del país.
        El DEIS hace mejoras al registro de vacunación a medida que analiza diversas fuentes de datos.
        Se entiende por comuna de residencia la comuna que se declaró la vivienda del paciente.
        """),
        tabla_vacuna,   
        
    ],
    style=CONTENT_STYLE
)

layout = html.Div([sidebar, content,html.Footer(
    children=[
        dbc.Row([
    html.A(html.Img(src='assets/paso-a-paso-logo.png'),style={'textAlign': 'center'})])
    ],className="mb-4")
    
    ])
@app.callback(
    Output('table-paging-with-graph', "data"),
    Input('table-paging-with-graph', "page_current"),
    Input('table-paging-with-graph', "page_size"),
    Input('table-paging-with-graph', "sort_by"),
    Input('table-paging-with-graph', "filter_query"))
def update_table(page_current, page_size, sort_by, filter):
    filtering_expressions = filter.split(' && ')
    dff = vacunas
    for filter_part in filtering_expressions:
        col_name, operator, filter_value = split_filter_part(filter_part)

        if operator in ('eq', 'ne', 'lt', 'le', 'gt', 'ge'):
            # these operators match pandas series operator method names
            dff = dff.loc[getattr(dff[col_name], operator)(filter_value)]
        elif operator == 'contains':
            dff = dff.loc[dff[col_name].str.contains(filter_value)]
        elif operator == 'datestartswith':
            # this is a simplification of the front-end filtering logic,
            # only works with complete fields in standard format
            dff = dff.loc[dff[col_name].str.startswith(filter_value)]

    if len(sort_by):
        dff = dff.sort_values(
            [col['column_id'] for col in sort_by],
            ascending=[
                col['direction'] == 'asc'
                for col in sort_by
            ],
            inplace=False
        )

    return dff.iloc[
        page_current*page_size: (page_current + 1)*page_size
    ].to_dict('records')



@app.callback(
    Output('table-paging-with-graph-container', "children"),
    Input('table-paging-with-graph', "data"))
def update_graph(rows):
    dff = pd.DataFrame(rows)
    dff['total']=dff[columnas].sum(axis=1)
    return html.Div(
        [
            dcc.Graph(
                id="columna",
                figure=px.bar(dff, x='Comuna', y='total',template='plotly_dark')
            )
        ]
    )
