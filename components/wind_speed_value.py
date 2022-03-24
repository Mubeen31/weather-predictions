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


def wind_speed_value_value(n_intervals):
    header_list = ['Date Time', 'Humidity', 'Rain', 'Photo Resistor Value', 'Photo Resistor LED', 'Revolution', 'RPM',
                   'Wind Speed KPH', 'Wind Degree', 'Wind Direction', 'CO2 Level', 'Temperature', 'Air Pressure']
    df = pd.read_csv('weather_data.csv', names = header_list)
    get_wind_speed = df['Wind Speed KPH'].tail(1).iloc[0].astype(float)

    return [
        html.Div([
            html.P('WIND SPEED',
                   className = 'w_s_value'
                   ),
            html.P('{0:,.2f} kph'.format(get_wind_speed),
                   className = 'w_s_number_value'
                   ),
        ], className = 'w_s_number_value_column'),
    ]
