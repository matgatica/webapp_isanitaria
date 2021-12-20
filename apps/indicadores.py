import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
from pandas.io.formats import style
from app import app
import plotly.express as px
import pandas as pd
from datetime import date
from epiweeks import Week
from urllib.request import urlopen
import json


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


with urlopen('https://raw.githubusercontent.com/caracena/chile-geojson/master/13.geojson') as response:
    geojason = json.load(response)

for dict in geojason["features"]:
    dict["id"]=dict["properties"]["Comuna"]

df_indicadores=pd.read_excel("DATA/df_resumendata.xlsx").drop(columns=["Unnamed: 0","Unnamed: 10"])


df_indicadores["fecha"]=pd.to_datetime(df_indicadores["source"].str[:20].str[12:],format='%Y%m%d')
df_indicadores["SE"]=df_indicadores["fecha"].apply(lambda x: Week.fromdate(x, system="iso").week)


lista_comunas_ind=[]
for i in df_indicadores.Comuna.unique():
    mini_dict={'label':f'{i}',"value":f"{i}"}
    lista_comunas_ind.append(mini_dict)


content_second_row_ind5 = dbc.Row(
    [
        
            dcc.Graph(id='graph_indicador_5'),

        dcc.Dropdown(
            id='id_comuna_ind5',
            options=lista_comunas_ind,
            value=['Santiago'],
            multi=True     
        ),
        dcc.RangeSlider(
            id='slider_ind5',
            min=0,
            max=100,
            step=1,
            value=[5, 50],
            marks={
            1: '1',
            10:'10',
            20: '20',
            30: '30',
            40: '40',
            50: '50'
            }
        )]

        )
        

content_third_row_ind5 = dbc.Row(
    [
            dcc.Graph(id="geograph_indicador_5"),

        dcc.Slider(
        id='slider_SE_5',
        min=0,
        max=50,
        step=1,
        value=30,
        marks={
            1: '1',
            10:'10',
            20: '20',
            30: '30',
            40: '40',
            50: '50'
            }
        )]

        )

content_ind5 = html.Div(
    [
        html.Br(),
        html.P(children='''Indicador 5: Oportunidad de la investigación epidemiológica y registro del primer seguimiento de casos: proporción de casos confirmados, en los cuales se inicia la investigación epidemiológica e
identificación de contactos estrechos antes de 48 h.'''),
        content_second_row_ind5,
        content_third_row_ind5
        
    
    ]
)

content_second_row_ind6 = dbc.Row(
    [
        
            dcc.Graph(id='graph_indicador_6'),

        dcc.Dropdown(
            id='id_comuna_ind6',
            options=lista_comunas_ind,
            value=['Santiago'],
            multi=True     
        ),
        dcc.RangeSlider(
            id='slider_ind6',
            min=0,
            max=100,
            step=1,
            value=[5, 50],
            marks={
            1: '1',
            10:'10',
            20: '20',
            30: '30',
            40: '40',
            50: '50'
            }
        )]

        )
        
content_third_row_ind6 = dbc.Row(
    [
        
        dcc.Graph(id="geograph_indicador_6"),

        dcc.Slider(
        id='slider_SE_6',
        min=0,
        max=50,
        step=1,
        value=30,
        marks={
            1: '1',
            10:'10',
            20: '20',
            30: '30',
            40: '40',
            50: '50'
            }
        )]

        )
        

content_ind6 = html.Div(
    [
        html.Br(),
        html.P('''Indicador 6: Identificación de contactos: proporción de casos con al menos un contacto identificado.'''),
        content_second_row_ind6,
        content_third_row_ind6
        
    
    ],
    
)

content_second_row_ind7 = dbc.Row(
    [
        
            dcc.Graph(id='graph_indicador_7'),

        dcc.Dropdown(
            id='id_comuna_ind_7',
            options=lista_comunas_ind,
            value=['Santiago'],
            multi=True     
        ),
        dcc.RangeSlider(
            id='slider_ind_7',
            min=0,
            max=100,
            step=1,
            value=[5, 50],
            marks={
            1: '1',
            10:'10',
            20: '20',
            30: '30',
            40: '40',
            50: '50'
            }
        )]

        )
        
content_third_row_ind7 = dbc.Row(
    [
        
        dcc.Graph(id="geograph_indicador_7"),

        dcc.Slider(
        id='slider_SE_7',
        min=0,
        max=50,
        step=1,
        value=30,
        marks={
            1: '1',
            10:'10',
            20: '20',
            30: '30',
            40: '40',
            50: '50'
            }
        )]

        )
        

content_ind7 = html.Div(
    [
        html.Br(),
        html.P('''Indicador 7: Oportunidad de la investigación epidemiológica y registro del primer seguimiento de en
contactos: proporción de contactos nuevos en los cuales se inicia la investigación epidemiológica antes de 48 h.'''),
        content_second_row_ind7,
        content_third_row_ind7
        
    ],
    
)

tabs_styles = {
    'height': '44px'
}
tab_style = {
    'borderBottom': '1px solid #d6d6d6',
    'padding': '6px',
    'fontWeight': 'bold',
    'marginLeft':'auto'
}

tab_selected_style = {
    'borderTop': '1px solid #d6d6d6',
    'borderBottom': '1px solid #d6d6d6',
    'backgroundColor': '#119DFF',
    'color': 'white',
    'padding': '6px'
}


tabs=dbc.Tabs(
    [
        dbc.Tab(content_ind5, label="INDICADOR 5",style=tab_style, active_tab_style=tab_selected_style,tabClassName="flex-grow-1 text-center"),
        dbc.Tab(content_ind6, label="INDICADOR 6",style=tab_style, active_tab_style=tab_selected_style,tabClassName="flex-grow-1 text-center"),   
        dbc.Tab(content_ind7, label="INDICADOR 7",style=tab_style, active_tab_style=tab_selected_style,tabClassName="flex-grow-1 text-center"),   
    ],
    style=tabs_styles
)

cuerpo=html.Div([dbc.Row(
    dbc.Col([
        html.H2('INDICADORES', style=TEXT_STYLE),
        html.H6('<Inteligencia Sanitaria>', style=TEXT_STYLE),
        tabs,
    ])),
    ],
    style=CONTENT_STYLE
    )

layout = html.Div([sidebar, cuerpo,html.Footer(children='<Inteligencia Sanitaria>',style=TEXT_STYLE)])


@app.callback(
    Output('graph_indicador_5', 'figure'),
    [
    Input('id_comuna_ind5', 'value'),
    Input('slider_ind5', 'value'),
    
    ]
)

def update_graph_5(value_comuna,value_ind):

    df=df_indicadores
    df=df[df.Comuna.isin(value_comuna)]
    dff = df[(df.SE>=value_ind[0])&(df.SE<=value_ind[1])]
    fig5 = px.line(dff,x='SE',y='Indicador 5',color='Comuna',template='plotly_dark')
    fig5.update_layout(margin={'l': 40, 'b': 40, 't': 10, 'r': 0}, hovermode='closest')

    return fig5



@app.callback(
    Output('geograph_indicador_5', 'figure'),
    [
    Input('slider_SE_5', 'value'),
    ]
)

def update_geograph_5(value_ind):
    df=df_indicadores

    dff = df[(df.SE==value_ind)]
    dff = dff[(dff.Comuna!='Total')]
    dff.fillna('0',inplace=True)
    dff['Indicador 5']=dff['Indicador 5'].astype(float)

    
    fig6=px.choropleth_mapbox(dff, geojson=geojason, locations='Comuna', color='Indicador 5',
                           #color_continuous_scale="Viridis",
                           range_color=(0, 1),
                           mapbox_style="carto-positron",
                           template='plotly_dark',
                           width=1500,
                           height=1000,
                           center={"lat": -33.4691199, "lon": -70.641997},
                           zoom=8,
                           opacity=0.3,
                           labels={'SE':'SE',
                               'Indicador 5':'Indicador 5'}
                          )


    fig6.update_layout(mapbox_style="open-street-map")
    fig6.update_geos(fitbounds="locations")
    fig6.update_geos(
        visible=False, resolution=110,
        showcountries=True, countrycolor="Black",
        scope="south america",
        showsubunits=True, subunitcolor="Blue",
        
    )
    fig6.update_layout(margin={'l': 0, 'b': 0, 't': 0, 'r': 0}, hovermode='closest')

    return fig6



@app.callback(
    Output('graph_indicador_6', 'figure'),
    [
    Input('id_comuna_ind6', 'value'),
    Input('slider_ind6', 'value'),
    
    ]
)

def update_graph_6(value_comuna,value_ind):

    df=df_indicadores
    df=df[df.Comuna.isin(value_comuna)]
    dff = df[(df.SE>=value_ind[0])&(df.SE<=value_ind[1])]
    fig5 = px.line(dff,x='SE',y='Indicador 6',color='Comuna',template='plotly_dark')
    fig5.update_layout(margin={'l': 40, 'b': 40, 't': 10, 'r': 0}, hovermode='closest')

    return fig5



@app.callback(
    Output('geograph_indicador_6', 'figure'),
    [
    Input('slider_SE_6', 'value'),
    ]
)

def update_geograph_6(value_ind):

    df=df_indicadores

    dff = df[(df.SE==value_ind)]
    dff = dff[(dff.Comuna!='Total')]
    dff.fillna('0',inplace=True)
    dff['Indicador 6']=dff['Indicador 6'].astype(float)

    fig6=px.choropleth_mapbox(dff, geojson=geojason, locations='Comuna', color='Indicador 6',
                           #color_continuous_scale="Viridis",
                           range_color=(0, 1),
                           mapbox_style="carto-positron",
                           template='plotly_dark',
                           width=1500,
                           height=1000,
                           center={"lat": -33.4691199, "lon": -70.641997},
                           zoom=8,
                           opacity=0.3,
                           labels={'SE':'SE',
                               'Indicador 6':'Indicador 6'}
                          )


    fig6.update_layout(mapbox_style="open-street-map")
    fig6.update_geos(fitbounds="locations")
    fig6.update_geos(
        visible=False, resolution=110,
        showcountries=True, countrycolor="Black",
        scope="south america",
        showsubunits=True, subunitcolor="Blue",
        
    )
    fig6.update_layout(margin={'l': 0, 'b': 0, 't': 0, 'r': 0}, hovermode='closest')

    return fig6


@app.callback(
    Output('graph_indicador_7', 'figure'),
    [
    Input('id_comuna_ind_7', 'value'),
    Input('slider_ind_7', 'value'),
    
    ]
)

def update_graph_7(value_comuna,value_ind):

    df=df_indicadores
    df=df[df.Comuna.isin(value_comuna)]
    dff = df[(df.SE>=value_ind[0])&(df.SE<=value_ind[1])]
    fig7 = px.line(dff,x='SE',y='Indicador 7',color='Comuna',template='plotly_dark')
    fig7.update_layout(margin={'l': 40, 'b': 40, 't': 10, 'r': 0}, hovermode='closest')

    return fig7



@app.callback(
    Output('geograph_indicador_7', 'figure'),
    [
    Input('slider_SE_7', 'value'),
    ]
)

def update_geograph_7(value_ind):

    df=df_indicadores

    dff = df[(df.SE==value_ind)]
    dff = dff[(dff.Comuna!='Total')]
    dff.fillna('0',inplace=True)
    dff['Indicador 7']=dff['Indicador 7'].astype(float)

    fig6=px.choropleth_mapbox(dff, geojson=geojason, locations='Comuna', color='Indicador 7',
                           #color_continuous_scale="Viridis",
                           range_color=(0, 1),
                           mapbox_style="carto-positron",
                           template='plotly_dark',
                           width=1500,
                           height=1000,
                           center={"lat": -33.4691199, "lon": -70.641997},
                           zoom=8,
                           opacity=0.3,
                           labels={'SE':'SE',
                               'Indicador 7':'Indicador 7'}
                          )


    fig6.update_layout(mapbox_style="open-street-map")
    fig6.update_geos(fitbounds="locations")
    fig6.update_geos(
        visible=False, resolution=110,
        showcountries=True, countrycolor="Black",
        scope="south america",
        showsubunits=True, subunitcolor="Blue",
        
    )

    return fig6
