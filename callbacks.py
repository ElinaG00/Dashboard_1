from utils.data_loader import load_data
import plotly.graph_objects as go
from dash import Input, Output, html
from datetime import date,  timedelta

def register_callbacks(app):
    
    @app.callback(
            [Output('weather-output', 'children'),
            Output('co-graph', 'figure'),
            Output('no2-graph', 'figure'),
            Output('o3-graph', 'figure'),
            Output('so2-graph', 'figure'),
            Output('pm2_5-graph', 'figure'),
            Output('pm10-graph', 'figure')],
            [Input('city-input', 'value'),
            Input('date-selector', 'value')]
    )


    def update_dashboard(city,date_period='today'):
        
        if date_period == 'today':
            selected_date = date.today().isoformat()
            date_display = "сегодня"
        elif date_period == 'yesterday':
            selected_date = (date.today() - timedelta(days=1)).isoformat()
            date_display = "вчера"
        else:
            selected_date = date.today().isoformat()
            date_display = "сегодня"

        data = load_data(city, selected_date)

        co_fig = go.Figure(
            data=[go.Scatter(x=data['hours'], y=data['co'], mode='lines+markers')],
            layout=go.Layout(title="Концентрация угарного газа по часам", 
                             xaxis_title='Время', 
                             yaxis_title='Концентрация CO (µg/m³)',
                             template='plotly_dark'
        ))

        no2_fig = go.Figure(
            data=[go.Scatter(x=data['hours'], y=data['no2'], mode='lines+markers')],
            layout=go.Layout(title="Концентрация диоксида азота по часам", 
                             xaxis_title='Время', 
                             yaxis_title='Концентрация NO2 (µg/m³)',
                             template='plotly_dark'
        ))

        o3_fig = go.Figure(
            data=[go.Scatter(x=data['hours'], y=data['o3'], mode='lines+markers')],
            layout=go.Layout(title="Концентрация озона по часам", 
                             xaxis_title='Время', 
                             yaxis_title='Концентрация O3 (µg/m³)',
                             template='plotly_dark'
        ))  

        so2_fig = go.Figure(
            data=[go.Scatter(x=data['hours'], y=data['so2'], mode='lines+markers')],
            layout=go.Layout(title="Концентрация сернистого газа по часам", 
                             xaxis_title='Время', 
                             yaxis_title='Концентрация SO2 (µg/m³)',
                             template='plotly_dark'
        ))

        pm2_5_fig = go.Figure(
            data=[go.Scatter(x=data['hours'], y=data['pm2_5'], mode='lines+markers')],
            layout=go.Layout(title="Концентрация мелкодисперсных частиц по часам", 
                             xaxis_title='Время', 
                             yaxis_title='Концентрация %',
                             template='plotly_dark'
        ))

        pm10_fig = go.Figure(
            data=[go.Scatter(x=data['hours'], y=data['pm10'], mode='lines+markers')],
            layout=go.Layout(title="Концентрация грубых частиц по часам", 
                             xaxis_title='Время', 
                             yaxis_title='Концентрация %',
                             template='plotly_dark'
        ))

        weather_output = html.Div([
            html.H4(f"{data['city_name']}", style={'margin-bottom': '10px'}),
            html.P(f"Дата: {selected_date}", style={'margin': '0', 'fontSize': '12px', 'color': '#666'}),
            html.Img(src=f"https:{data['icon']}", style={'width': '64px', 'height': '64px'}),
            html.H5(f"{data['temp']} C", style={'margin': '0'}),
            html.P(f"{data['condition']}", style={'margin': '0', 'fontSize': '14px'})
        ]
        )
        return weather_output, co_fig, no2_fig, o3_fig, so2_fig, pm2_5_fig, pm10_fig

