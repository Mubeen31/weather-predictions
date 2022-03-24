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


def sun_set_status_value(n_intervals):
    now = datetime.now()
    day = now.strftime('%a')
    date = now.strftime('%d/%m/%Y')
    time_name = now.strftime('%H:%M:%S')
    header_list = ['Date Time', 'Humidity', 'Rain', 'Photo Resistor Value', 'Photo Resistor LED', 'Revolution', 'RPM',
                   'Wind Speed KPH', 'Wind Degree', 'Wind Direction', 'CO2 Level', 'Temperature', 'Air Pressure']
    df = pd.read_csv('weather_data.csv', names = header_list)
    df['Date Time'] = pd.to_datetime(df['Date Time'])
    df['Date'] = df['Date Time'].dt.date
    df['Date'] = pd.to_datetime(df['Date'])
    df['Time'] = df['Date Time'].dt.time
    unique_date = df['Date'].unique()
    filter_led_date_2 = df[df['Date'] == unique_date[-2]][['Date', 'Photo Resistor LED', 'Time']]
    sun_set_time_2 = filter_led_date_2[(filter_led_date_2['Photo Resistor LED'] == ' LED OFF ')]['Time'].tail(1).iloc[0]
    filter_led_date_1 = df[df['Date'] == unique_date[-1]][['Date', 'Photo Resistor LED', 'Time']]

    if time_name >= '00:00:00' and time_name <= '16:45:00':
        return [
            html.Div([
                html.Img(src = app.get_asset_url('sunset.png'),
                         className = 'sunset_image'
                         ),
                html.P('SUNSET',
                       className = 'sunset_value'
                       ),
                html.P(
                    # '16:36:29',
                    sun_set_time_2,
                    className = 'sunset_text_value'
                ),
            ], className = 'sunset_column'),
        ]
    elif time_name > '16:45:00' and time_name <= '23:59:59':
        sun_set_time_1 = \
        filter_led_date_1[(filter_led_date_1['Photo Resistor LED'] == ' LED OFF ')]['Time'].tail(1).iloc[0]

        return [
            html.Div([
                html.Img(src = app.get_asset_url('sunset.png'),
                         className = 'sunset_image'
                         ),
                html.P('SUNSET',
                       className = 'sunset_value'
                       ),
                html.P(
                    # '16:36:29',
                    sun_set_time_1,
                    className = 'sunset_text_value'
                ),
            ], className = 'sunset_column'),
        ]
