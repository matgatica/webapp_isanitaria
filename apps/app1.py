import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import dash
import pandas as pd
import plotly.express as px
import datetime as dt
from app import app
from datetime import date

df_inv = pd.read_csv('DATA/CASOS_INV.csv',dtype=str,sep=";")
df_inv["_id.dia_seg"]=pd.to_datetime(df_inv["_id.dia_seg"],format="%d-%m-%Y")

#available_indicators = df['Indicator Name'].unique()

layout = html.Div([
    html.H1(children='Casos Investigación'),
    # html.Div([
    #     html.Div([
    #         dcc.Dropdown(
    #             id='xaxis-column',
    #             options=[{'label': i, 'value': i} for i in available_indicators],
    #             value='Fertility rate, total (births per woman)'
    #         ),
    #        
    #     ], style={'width': '48%', 'display': 'inline-block'}),
    #     html.Div([
    #         dcc.Dropdown(
    #             id='yaxis-column',
    #             options=[{'label': i, 'value': i} for i in available_indicators],
    #             value='Life expectancy at birth, total (years)'
    #         ),
    #      
    #     ], style={'width': '48%', 'float': 'right', 'display': 'inline-block'})
    # ]),

    dcc.Graph(id='indicator-graphic'),

     dcc.DatePickerRange(
        id='my-date-picker-range',
        min_date_allowed=date(1995, 8, 5),
        max_date_allowed=date(2022, 1, 1),
        initial_visible_month=date(2021, 1, 1),
        end_date=date(2021, 6 ,1),
        start_date=date(2021, 1, 1)
     ),
     
     html.H1(children='Casos Investigación'),

     dcc.Graph(id='indicator-graphic_2'),

     dcc.DatePickerRange(
        id='my-date-picker-range_2',
        min_date_allowed=date(1995, 8, 5),
        max_date_allowed=date(2022, 1, 1),
        initial_visible_month=date(2021, 1, 1),
        end_date=date(2021, 6 ,1),
        start_date=date(2021, 1, 1)
     )
])

@app.callback(
    Output('indicator-graphic', 'figure'),
    
    # Input('xaxis-column', 'value'),
    # Input('yaxis-column', 'value'),
    [Input('my-date-picker-range', 'start_date'),
    Input('my-date-picker-range', 'end_date'),
    ]
)

def update_graph(#xaxis_column_name, yaxis_column_name,
                 startdate,enddate):
    df=df_inv            
    dff = df[(df['_id.dia_seg'] >= startdate) & (df['_id.dia_seg'] <= enddate)]

    fig = px.scatter(data_frame=dff,x="_id.dia_seg",
                     y=[dff["count"]])
                     #hover_name="CASOS INVESTIGACION")

    fig.update_layout(margin={'l': 40, 'b': 40, 't': 10, 'r': 0}, hovermode='closest')

    # fig.update_xaxes(title=xaxis_column_name
    #                 )

    # fig.update_yaxes(title=yaxis_column_name
    #                 )

    return fig


@app.callback(
    Output('indicator-graphic_2', 'figure'),
    # Input('xaxis-column', 'value'),
    # Input('yaxis-column', 'value'),
    [
    Input('my-date-picker-range_2', 'start_date'),
    Input('my-date-picker-range_2', 'end_date'),
    ]
)


def update_graph_2(#xaxis_column_name, yaxis_column_name,
                 startdate,enddate):
    df=df_inv            
    dff = df[(df['_id.dia_seg'] >= startdate) & (df['_id.dia_seg'] <= enddate)]

    fig = px.scatter(data_frame=dff,x="_id.dia_seg",
                     y=[dff["count"]])
                     #hover_name="CASOS INVESTIGACION")

    fig.update_layout(margin={'l': 40, 'b': 40, 't': 10, 'r': 0}, hovermode='closest')

    # fig.update_xaxes(title=xaxis_column_name
    #                 )

    # fig.update_yaxes(title=yaxis_column_name
    #                 )

    return fig