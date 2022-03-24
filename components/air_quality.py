import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output
import plotly.graph_objs as go
from dash.exceptions import PreventUpdate
import pandas as pd
from datetime import datetime, date, time
import numpy as np
from datetime import datetime, date, time
from sklearn import linear_model
import sqlalchemy
from dash import dash_table as dt
import time

font_awesome = "https://use.fontawesome.com/releases/v5.10.2/css/all.css"
meta_tags = [{"name": "viewport", "content": "width=device-width"}]
external_stylesheets = [meta_tags, font_awesome]

app = dash.Dash(__name__, external_stylesheets = external_stylesheets)

html.Div([
    dcc.Interval(id = 'update_value',
                 interval = 6000,
                 n_intervals = 0),
]),


def air_quality_value(n_intervals):
    header_list = ['Date Time', 'Humidity', 'Rain', 'Photo Resistor Value', 'Photo Resistor LED', 'Revolution', 'RPM',
                   'Wind Speed KPH', 'Wind Degree', 'Wind Direction', 'CO2 Level', 'Temperature', 'Air Pressure']
    df = pd.read_csv('weather_data.csv', names = header_list)
    get_air_quality = df['CO2 Level'].tail(1).iloc[0].astype(float)

    if get_air_quality >= 250.0 and get_air_quality <= 400.0:
        return [
            html.Div([
                html.Img(src = app.get_asset_url('air-quality.png'),
                         className = 'quality_image'
                         ),
                html.Div([
                    html.P('AIR QUALITY',
                           className = 'air_quality_text_value'
                           ),
                    html.Div([
                        html.P('{0:,.0f} ppm'.format(get_air_quality),
                               className = 'quality_value'
                               ),
                        html.P('Excellent',
                               className = 'air_quality_text_status')
                    ], className = 'air_quality_text_status_row')
                ], className = 'air_quality_text_quality_value')
            ], className = 'air_quality_text_quality_value_row'),

        ]

    elif get_air_quality > 400.0 and get_air_quality <= 1000.0:
        return [
            html.Div([
                html.Img(src = app.get_asset_url('air-quality.png'),
                         className = 'quality_image'
                         ),
                html.Div([
                    html.P('AIR QUALITY',
                           className = 'air_quality_text_value'
                           ),
                    html.Div([
                        html.P('{0:,.0f} ppm'.format(get_air_quality),
                               className = 'quality_value'
                               ),
                        html.P('Good',
                               className = 'air_quality_text_status')
                    ], className = 'air_quality_text_status_row')
                ], className = 'air_quality_text_quality_value')
            ], className = 'air_quality_text_quality_value_row'),

        ]
    elif get_air_quality > 1000.0 and get_air_quality <= 2000.0:
        return [
            html.Div([
                html.Img(src = app.get_asset_url('air-quality.png'),
                         className = 'quality_image'
                         ),
                html.Div([
                    html.P('AIR QUALITY',
                           className = 'air_quality_text_value'
                           ),
                    html.Div([
                        html.P('{0:,.0f} ppm'.format(get_air_quality),
                               className = 'quality_value'
                               ),
                        html.P('Poor',
                               className = 'poor_air_quality_text_status')
                    ], className = 'air_quality_text_status_row')
                ], className = 'air_quality_text_quality_value')
            ], className = 'air_quality_text_quality_value_row'),

        ]
    elif get_air_quality > 2000.0 and get_air_quality <= 5000.0:
        return [
            html.Div([
                html.Img(src = app.get_asset_url('air-quality.png'),
                         className = 'quality_image'
                         ),
                html.Div([
                    html.P('AIR QUALITY',
                           className = 'air_quality_text_value'
                           ),
                    html.Div([
                        html.P('{0:,.0f} ppm'.format(get_air_quality),
                               className = 'quality_value'
                               ),
                        html.P('Dangerous',
                               className = 'poor_air_quality_text_status')
                    ], className = 'air_quality_text_status_row')
                ], className = 'air_quality_text_quality_value')
            ], className = 'air_quality_text_quality_value_row'),

        ]
