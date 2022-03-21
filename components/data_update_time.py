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


def last_data_update_time(n_intervals):
    header_list = ['Date Time', 'Humidity', 'Rain', 'Photo Resistor Value', 'Photo Resistor LED', 'Revolution', 'RPM',
                   'Wind Speed KPH', 'Wind Degree', 'Wind Direction', 'CO2 Level', 'Temperature', 'Air Pressure']
    df = pd.read_csv('weather_data.csv', names = header_list)
    df['Date Time'] = pd.to_datetime(df['Date Time'])
    df['Date'] = df['Date Time'].dt.date
    df['Date'] = pd.to_datetime(df['Date'])
    df['Time'] = df['Date Time'].dt.time
    df['Time'] = df['Time'].astype(str)
    get_dat_time = str(df['Date Time'].tail(1).iloc[0].strftime("%d-%m-%Y %H:%M:%S"))

    return [
        html.P('Last Updated Time: ' + get_dat_time,
               className = 'updated_time_value'
               ),
    ]
