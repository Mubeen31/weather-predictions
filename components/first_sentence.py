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

html.Div([
    dcc.Interval(id = 'update_value',
                 interval = 6000,
                 n_intervals = 0),
]),


def first_sentence_value(n_intervals):
    header_list = ['Date Time', 'Humidity', 'Rain', 'Photo Resistor Value', 'Photo Resistor LED', 'Revolution', 'RPM',
                   'Wind Speed KPH', 'Wind Degree', 'Wind Direction', 'CO2 Level', 'Temperature', 'Air Pressure']
    df = pd.read_csv('weather_data.csv', names = header_list)
    df['Air Pressure'] = df['Air Pressure'] / 100
    get_pressure = df['Air Pressure'].tail(1).iloc[0]
    get_photo_resistor_value = df['Photo Resistor Value'].tail(1).iloc[0].astype(float)
    get_rain_value = df['Rain'].tail(1).iloc[0].astype(float)
    get_led_on = df['Photo Resistor LED'].tail(1).iloc[0]
    get_air_pressure = df['Air Pressure'].tail(1).iloc[0].astype(float)
    convert_pa_to_mb = get_air_pressure / 100
    now = datetime.now()
    day = now.strftime('%a')
    date = now.strftime('%d/%m/%Y')
    time = now.strftime('%H:%M:%S')

    if get_pressure > 1000 and get_led_on == ' LED ON ':
        return [
            html.P('The skies will be cloudy.',
                   className = 'status_paragraph_format'),
        ]
    if get_pressure < 1000 and get_led_on == ' LED ON ':
        return [
            html.P('Rain is expected during the night.',
                   className = 'status_paragraph_format'),
        ]
    if get_pressure > 1000 and get_rain_value >= 800.0 and get_rain_value <= 900.0 and get_led_on == ' LED ON ':
        return [
            html.P('Rain is expected during the night.',
                   className = 'status_paragraph_format'),
        ]
    if get_pressure > 1000 and get_rain_value <= 800.0 and get_led_on == ' LED ON ':
        return [
            html.P('Rain is expected during the night.',
                   className = 'status_paragraph_format'),
        ]
    if get_pressure < 1000 and get_rain_value <= 800.0 and get_led_on == ' LED ON ':
        return [
            html.P('Rain is expected during the night.',
                   className = 'status_paragraph_format'),
        ]
    if get_rain_value <= 800.0:
        return [
            html.P('Rain is expected during the day.',
                   className = 'status_paragraph_format'),
        ]
    elif get_photo_resistor_value < 300.0:
        return [
            html.P('The skies will be cleared.',
                   className = 'status_paragraph_format'),
        ]
    elif get_photo_resistor_value < 300.0 and convert_pa_to_mb > 1002.00 and convert_pa_to_mb <= 1005.00:
        return [
            html.P('The skies will be cleared.',
                   className = 'status_paragraph_format'),
        ]
    elif get_photo_resistor_value < 300.0 and convert_pa_to_mb >= 1000.00 and convert_pa_to_mb < 1002.00:
        return [
            html.P('The skies will be foggy.',
                   className = 'status_paragraph_format'),
        ]
    elif get_photo_resistor_value >= 300.0 and get_photo_resistor_value <= 800.0:
        return [
            html.P('The skies wil be cloudy.',
                   className = 'status_paragraph_format'),
        ]
    elif get_photo_resistor_value > 800.0 and get_photo_resistor_value <= 900.0:
        return [
            html.P('The skies wil be partly cloudy.',
                   className = 'status_paragraph_format'),
        ]
    elif get_photo_resistor_value > 900.0:
        return [
            html.P('The skies wil be sunny.',
                   className = 'status_paragraph_format'),
        ]
