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


def accu_dew_point_value(n_intervals):
    acc_header_list = ['Temperature', 'Wind Direction', 'Wind Speed', 'Humidity', 'Dew Point', 'Atmospheric Pressure']
    df1 = pd.read_csv('acc_weather_data.csv', names = acc_header_list)
    acc_dew_point = df1['Dew Point'].tail(1).iloc[0]
    header_list = ['Date Time', 'Humidity', 'Rain', 'Photo Resistor Value', 'Photo Resistor LED', 'Revolution', 'RPM',
                   'Wind Speed KPH', 'Wind Degree', 'Wind Direction', 'CO2 Level', 'Temperature', 'Air Pressure']
    df = pd.read_csv('weather_data.csv', names = header_list)
    get_temp = df['Temperature'].tail(1).iloc[0].astype(float)
    get_humidity = df['Humidity'].tail(1).iloc[0].astype(float)
    dew_point = get_temp - ((100 - get_humidity) / 5)
    difference_data = dew_point - acc_dew_point

    if dew_point == acc_dew_point:
        return [
            html.Div([
                html.P('Dew Point', className = 'acc_text'),
                html.Div([
                    html.P('{0:,.2f}°C'.format(acc_dew_point), className = 'acc_value'),
                    html.Div([
                        html.I(className = "far fa-check-circle fa-lg"),
                    ], className = 'acc_image'),
                ], className = 'acc_value_image_row')
            ], className = 'acc_value_image_column'),
        ]
    elif difference_data >= 0.01 and difference_data <= 0.49:
        return [
            html.Div([
                html.P('Dew Point', className = 'acc_text'),
                html.Div([
                    html.P('{0:,.2f}°C'.format(acc_dew_point), className = 'acc_value'),
                    html.Div([
                        html.I(className = "far fa-check-circle fa-lg"),
                    ], className = 'acc_image'),
                ], className = 'acc_value_image_row')
            ], className = 'acc_value_image_column'),
        ]
    elif difference_data <= -0.01 and difference_data >= -0.50:
        return [
            html.Div([
                html.P('Dew Point', className = 'acc_text'),
                html.Div([
                    html.P('{0:,.2f}°C'.format(acc_dew_point), className = 'acc_value'),
                    html.Div([
                        html.I(className = "far fa-check-circle fa-lg"),
                    ], className = 'acc_image'),
                ], className = 'acc_value_image_row')
            ], className = 'acc_value_image_column'),
        ]
    elif dew_point != acc_dew_point:
        return [
            html.Div([
                html.P('Dew Point', className = 'acc_text'),
                html.Div([
                    html.P('{0:,.2f}°C'.format(acc_dew_point), className = 'acc_value'),
                    html.Div([
                        html.I(className = "far fa-times-circle fa-lg"),
                    ], className = 'not_equal_acc_image'),
                ], className = 'acc_value_image_row')
            ], className = 'acc_value_image_column'),
        ]
