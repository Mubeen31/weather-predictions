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


def third_sentence_value(n_intervals):
    header_list = ['Date Time', 'Humidity', 'Rain', 'Photo Resistor Value', 'Photo Resistor LED', 'Revolution', 'RPM',
                   'Wind Speed KPH', 'Wind Degree', 'Wind Direction', 'CO2 Level', 'Temperature', 'Air Pressure']
    df = pd.read_csv('weather_data.csv', names = header_list)
    get_temp = df['Temperature'].tail(1).iloc[0].astype(float)
    get_temp_add = df['Temperature'].tail(1).iloc[0].astype(float) + 3.00
    get_temp_subtract = df['Temperature'].tail(1).iloc[0].astype(float) - 3.00
    get_photo_resistor_value = df['Photo Resistor Value'].tail(1).iloc[0].astype(float)
    get_rain_value = df['Rain'].tail(1).iloc[0].astype(float)
    get_led_on = df['Photo Resistor LED'].tail(1).iloc[0]
    now = datetime.now()
    day = now.strftime('%a')
    date_now = now.strftime('%d/%m/%Y')
    time_now = now.strftime('%H:%M:%S')

    if get_temp >= 1.00 and get_temp <= 3.00:
        return [
            html.P('Temperatures near freezing.',
                   className = 'status_paragraph_format'),
        ]
    else:
        return [
            html.P('-',
                   className = 'status_paragraph_format1'),
        ]
