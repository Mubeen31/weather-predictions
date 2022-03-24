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


def accu_wind_direction_value(n_intervals):
    acc_header_list = ['Temperature', 'Wind Direction', 'Wind Speed', 'Humidity', 'Dew Point', 'Atmospheric Pressure']
    df1 = pd.read_csv('acc_weather_data.csv', names = acc_header_list)
    acc_wind_direction = df1['Wind Direction'].tail(1).iloc[0]
    header_list = ['Date Time', 'Humidity', 'Rain', 'Photo Resistor Value', 'Photo Resistor LED', 'Revolution', 'RPM',
                   'Wind Speed KPH', 'Wind Degree', 'Wind Direction', 'CO2 Level', 'Temperature', 'Air Pressure']
    df = pd.read_csv('weather_data.csv', names = header_list)

    # degree_value = [112.5, 67.5, 90, 157.5, 135, 202.5, 180, 22.5, 45, 247.5, 225, 337.5, 0, 292.5, 315, 270]
    # direction_value = ["ESE", "ENE", "E", "SSE", "SE", "SSW", "S", "NNE", "NE", "WSW", "SW", "NNW", "N", "WNW", "NW",
    #                    "W"]
    # dictionary_degree_direction = {'Degree': degree_value, 'Direction': direction_value}
    # df2 = pd.DataFrame(dictionary_degree_direction)
    # df2['Degree'] = df2['Degree'].astype(float)
    # df2['Direction'] = df2['Direction'].astype(str)
    # merge_df = pd.merge(left = df,
    #                     right = df2,
    #                     how = 'inner',
    #                     left_on = ['Wind Direction'],
    #                     right_on = ['Degree'])

    get_wind_direction = df['Wind Direction'].tail(1).iloc[0]

    if get_wind_direction == acc_wind_direction:
        return [
            html.Div([
                html.P('Wind Direction', className = 'acc_text'),
                html.Div([
                    html.P(acc_wind_direction, className = 'acc_value'),
                    html.Div([
                        html.I(className = "far fa-check-circle fa-lg"),
                    ], className = 'acc_image'),
                ], className = 'acc_value_image_row')
            ], className = 'acc_value_image_column'),
        ]
    elif get_wind_direction != acc_wind_direction:
        return [
            html.Div([
                html.P('Wind Direction', className = 'acc_text'),
                html.Div([
                    html.P(acc_wind_direction, className = 'acc_value'),
                    html.Div([
                        html.I(className = "far fa-times-circle fa-lg"),
                    ], className = 'not_equal_acc_image'),
                ], className = 'acc_value_image_row')
            ], className = 'acc_value_image_column'),
        ]
