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
    dcc.Interval(id='update_time',
                 interval=1000,
                 n_intervals=0),
]),


def current_time_value(n_intervals):
    header_list = ['Date Time', 'Humidity', 'Rain', 'Photo Resistor Value', 'Photo Resistor LED', 'Revolution', 'RPM',
                   'Wind Speed KPH', 'Wind Degree', 'Wind Direction', 'CO2 Level', 'Temperature', 'Air Pressure']
    df = pd.read_csv('weather_data.csv', names=header_list)
    get_temp = df['Temperature'].tail(1).iloc[0].astype(float)
    now = datetime.now()
    day = now.strftime('%a')
    date = now.strftime('%d/%m/%Y')
    time = now.strftime('%H:%M:%S')

    return [
        html.Div([
            html.Div([
                html.P('CURRENT WEATHER'),
            ], className='current_weather'),
            html.P(time,
                   className='current_time'
                   ),
        ], className='current_weather_time'),
    ]
