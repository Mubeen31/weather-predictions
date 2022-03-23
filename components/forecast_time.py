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


def forecast_time_value(n_intervals):
    header_list = ['Date Time', 'Humidity', 'Rain', 'Photo Resistor Value', 'Photo Resistor LED', 'Revolution', 'RPM',
                   'Wind Speed KPH', 'Wind Degree', 'Wind Direction', 'CO2 Level', 'Temperature', 'Air Pressure']
    df = pd.read_csv('weather_data.csv', names = header_list)
    get_temp = df['Temperature'].tail(1).iloc[0].astype(float)
    now = datetime.now()
    day = now.strftime('%a')
    date = now.strftime('%d/%m/%Y')
    time_name = now.strftime('%H:%M:%S')

    if time_name > '13:00:00' and time_name <= '14:00:00':
        return [
            html.P('14:00',
                   className = 'forecast_time_value'
                   ),
        ]

    elif time_name > '14:00:00' and time_name <= '15:00:00':
        return [
            html.P('15:00',
                   className = 'forecast_time_value'
                   ),
        ]
    elif time_name > '15:00:00' and time_name <= '16:00:00':
        return [
            html.P('16:00',
                   className = 'forecast_time_value'
                   ),
        ]
    elif time_name > '16:00:00' and time_name <= '17:00:00':
        return [
            html.P('17:00',
                   className = 'forecast_time_value'
                   ),
        ]
    elif time_name > '17:00:00' and time_name <= '18:00:00':
        return [
            html.P('18:00',
                   className = 'forecast_time_value'
                   ),
        ]
    elif time_name > '18:00:00' and time_name <= '19:00:00':
        return [
            html.P('19:00',
                   className = 'forecast_time_value'
                   ),
        ]
    elif time_name > '19:00:00' and time_name <= '20:00:00':
        return [
            html.P('20:00',
                   className = 'forecast_time_value'
                   ),
        ]
    elif time_name > '20:00:00' and time_name <= '21:00:00':
        return [
            html.P('21:00',
                   className = 'forecast_time_value'
                   ),
        ]
    elif time_name > '21:00:00' and time_name <= '22:00:00':
        return [
            html.P('22:00',
                   className = 'forecast_time_value'
                   ),
        ]
    elif time_name > '22:00:00' and time_name <= '23:00:00':
        return [
            html.P('23:00',
                   className = 'forecast_time_value'
                   ),
        ]
    elif time_name > '23:00:00' and time_name <= '23:59:59':
        return [
            html.P('00:00',
                   className = 'forecast_time_value'
                   ),
        ]
    elif time_name >= '00:00:00' and time_name <= '01:00:00':
        return [
            html.P('01:00',
                   className = 'forecast_time_value'
                   ),
        ]
    elif time_name > '01:00:00' and time_name <= '02:00:00':
        return [
            html.P('02:00',
                   className = 'forecast_time_value'
                   ),
        ]
    elif time_name > '02:00:00' and time_name <= '03:00:00':
        return [
            html.P('03:00',
                   className = 'forecast_time_value'
                   ),
        ]
    elif time_name > '03:00:00' and time_name <= '04:00:00':
        return [
            html.P('04:00',
                   className = 'forecast_time_value'
                   ),
        ]
    elif time_name > '04:00:00' and time_name <= '05:00:00':
        return [
            html.P('05:00',
                   className = 'forecast_time_value'
                   ),
        ]
    elif time_name > '05:00:00' and time_name <= '06:00:00':
        return [
            html.P('06:00',
                   className = 'forecast_time_value'
                   ),
        ]
    elif time_name > '06:00:00' and time_name <= '07:00:00':
        return [
            html.P('07:00',
                   className = 'forecast_time_value'
                   ),
        ]
    elif time_name > '07:00:00' and time_name <= '08:00:00':
        return [
            html.P('08:00',
                   className = 'forecast_time_value'
                   ),
        ]
    elif time_name > '08:00:00' and time_name <= '09:00:00':
        return [
            html.P('09:00',
                   className = 'forecast_time_value'
                   ),
        ]
    elif time_name > '09:00:00' and time_name <= '10:00:00':
        return [
            html.P('10:00',
                   className = 'forecast_time_value'
                   ),
        ]
    elif time_name > '10:00:00' and time_name <= '11:00:00':
        return [
            html.P('11:00',
                   className = 'forecast_time_value'
                   ),
        ]
    elif time_name > '11:00:00' and time_name <= '12:00:00':
        return [
            html.P('12:00',
                   className = 'forecast_time_value'
                   ),
        ]
    elif time_name > '12:00:00' and time_name <= '13:00:00':
        return [
            html.P('13:00',
                   className = 'forecast_time_value'
                   ),
        ]
