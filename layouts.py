import dash_bootstrap_components as dbc
from dash import dcc
from dash import html

def create_layout():
    return dbc.Container([
        dbc.NavbarSimple(
            brand= "🌦 Погодный дашборд 🌦",
            brand_href="#",
            color="dark",
            dark=True,
            brand_style={'text-align': 'center', 'width': '100%'},
            className="justify-content-center"
        ),


        dbc.Row([
            dbc.Col([
                html.Label("Выберите город:"),
                dbc.Input(id='city-input', value='Moscow', placeholder="Введите город", type='text', debounce=True, style={'width': '100%', 'padding': '8px'}),
            ], width=4, md=4, xs=12),
            dbc.Col([
               html.Label("Период:"),
            dbc.RadioItems(
                id='date-selector',
                options=[
                    {'label': '📍 Сегодня', 'value': 'today'},
                    {'label': '📅 Вчера', 'value': 'yesterday'},
                ],
                value='today',  
                inline=True,
                style={'margin-top': '5px'})
                ], width=4, md=4, xs=12),
            dbc.Col([
                dbc.Card(id='weather-output', body=True),
            ], width=4, md=4, xs=12),
        ], className="mb-3"),

        dbc.Row([
            dbc.Col(dcc.Graph(id='co-graph'), width=4, md=4, xs=12),
            dbc.Col(dcc.Graph(id='no2-graph'), width=4, md=4, xs=12),
            dbc.Col(dcc.Graph(id='o3-graph'), width=4, md=4, xs=12),
        ], className="mb-3"),

        dbc.Row([
            dbc.Col(dcc.Graph(id='so2-graph'), width=4, md=4, xs=12),
            dbc.Col(dcc.Graph(id='pm2_5-graph'), width=4, md=4, xs=12),
            dbc.Col(dcc.Graph(id='pm10-graph'), width=4, md=4, xs=12),
        ], className="mb-3")

    ], fluid=True)