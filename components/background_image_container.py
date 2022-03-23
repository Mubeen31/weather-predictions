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

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

html.Div([
    dcc.Interval(id='update_value',
                 interval=6000,
                 n_intervals=0),
]),


def background_image_and_container(n_intervals):
    header_list = ['Date Time', 'Humidity', 'Rain', 'Photo Resistor Value', 'Photo Resistor LED', 'Revolution', 'RPM',
                   'Wind Speed KPH', 'Wind Degree', 'Wind Direction', 'CO2 Level', 'Temperature', 'Air Pressure']
    df = pd.read_csv('weather_data.csv', names=header_list)
    get_photo_resistor_value = df['Photo Resistor Value'].tail(1).iloc[0].astype(float)
    get_rain_value = df['Rain'].tail(1).iloc[0].astype(float)
    get_led_on = df['Photo Resistor LED'].tail(1).iloc[0]

    if get_rain_value <= 800.0 and get_led_on == ' LED ON ':
        return [
            html.Div(style={'background-image': 'url("/assets/night-rain.jpg")',
                            'background-repeat': 'no-repeat',
                            'background-size': 'auto'
                            },
                     className='background_image_container'),
        ]

    if get_rain_value >= 800.0 and get_rain_value <= 900.0 and get_led_on == ' LED ON ':
        return [
            html.Div(style={'background-image': 'url("/assets/night-rain.jpg")',
                            'background-repeat': 'no-repeat',
                            'background-size': 'auto'
                            },
                     className='background_image_container'),
        ]
    if get_rain_value >= 800.0 and get_rain_value <= 900.0:
        return [
            html.Div(style={'background-image': 'url("/assets/rain.jpg")',
                            'background-repeat': 'no-repeat',
                            'background-size': 'auto'
                            },
                     className='background_image_container'),
        ]
    if get_rain_value < 800.0:
        return [
            html.Div(style={'background-image': 'url("/assets/rain.jpg")',
                            'background-repeat': 'no-repeat',
                            'background-size': 'auto'
                            },
                     className='background_image_container'),
        ]

    elif get_photo_resistor_value < 300.0:
        return [
            html.Div(style={'background-image': 'url("/assets/night.jpg")',
                            'background-repeat': 'no-repeat',
                            'background-size': 'auto'
                            },
                     className='background_image_container'),
        ]

    elif get_photo_resistor_value >= 300.0 and get_photo_resistor_value <= 800.0:
        return [
            html.Div(style={'background-image': 'url("/assets/cloudy-day.jpg")',
                            'background-repeat': 'no-repeat',
                            'background-size': 'auto'
                            },
                     className='background_image_container'),
        ]
    elif get_photo_resistor_value > 800.0 and get_photo_resistor_value <= 900.0:
        return [
            html.Div(style={'background-image': 'url("/assets/partly-cloudy.jpg")',
                            'background-repeat': 'no-repeat',
                            'background-size': 'auto'
                            },
                     className='background_image_container'),
        ]
    elif get_photo_resistor_value > 900.0:
        return [
            html.Div(style={'background-image': 'url("/assets/sunny.jpg")',
                            'background-repeat': 'no-repeat',
                            'background-size': 'auto'
                            },
                     className='background_image_container'),
        ]
