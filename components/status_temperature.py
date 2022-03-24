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


def status_temperature_value(n_intervals):
    header_list = ['Date Time', 'Humidity', 'Rain', 'Photo Resistor Value', 'Photo Resistor LED', 'Revolution', 'RPM',
                   'Wind Speed KPH', 'Wind Degree', 'Wind Direction', 'CO2 Level', 'Temperature', 'Air Pressure']
    df = pd.read_csv('weather_data.csv', names = header_list)
    get_temp = df['Temperature'].tail(1).iloc[0].astype(float)
    convert_c_t_fahrenheit = (get_temp * 9 / 5) + 32
    get_wind_speed = df['Wind Speed KPH'].tail(1).iloc[0].astype(float)
    convert_kph_to_mph = get_wind_speed / 1.609344
    raise_power = convert_kph_to_mph ** 0.16
    feels_like = 35.74 + (0.6215 * convert_c_t_fahrenheit) - (35.75 * raise_power) + (
                0.4275 * convert_c_t_fahrenheit * raise_power)
    convert_f_t_c = (feels_like - 32) * 5 / 9
    get_photo_resistor_value = df['Photo Resistor Value'].tail(1).iloc[0].astype(float)
    get_rain_value = df['Rain'].tail(1).iloc[0].astype(float)
    get_led_on = df['Photo Resistor LED'].tail(1).iloc[0]
    get_air_pressure = df['Air Pressure'].tail(1).iloc[0].astype(float)
    convert_pa_to_mb = get_air_pressure / 100

    if get_rain_value <= 800.0 and get_led_on == ' LED ON ':
        return [
            html.Div([
                html.Div([
                    html.Img(src = app.get_asset_url('night-rain.png'),
                             className = 'image_position'),
                    html.P('{0:,.2f}°C'.format(get_temp),
                           className = 'status_temperature'
                           ),
                ], className = 'image_position_status_temperature'),

                html.Div([
                    html.P('Rain',
                           className = 'status_temperature_right'
                           ),
                    html.P('FEELS LIKE' + ' ' + ' ' + '{0:,.0f}°C'.format(convert_f_t_c),
                           className = 'status_temperature_right_temperature'
                           ),
                ], className = 'status_temperature_right_temperature_column')
            ], className = 'status_temperature_right_temperature_row'),
        ]

    if get_rain_value >= 800.0 and get_rain_value <= 900.0 and get_led_on == ' LED ON ':
        return [
            html.Div([
                html.Div([
                    html.Img(src = app.get_asset_url('night-rain.png'),
                             className = 'image_position'),
                    html.P('{0:,.2f}°C'.format(get_temp),
                           className = 'status_temperature'
                           ),
                ], className = 'image_position_status_temperature'),

                html.Div([
                    html.P('Showers',
                           className = 'status_temperature_right'
                           ),
                    html.P('FEELS LIKE' + ' ' + ' ' + '{0:,.0f}°C'.format(convert_f_t_c),
                           className = 'status_temperature_right_temperature'
                           ),
                ], className = 'status_temperature_right_temperature_column')
            ], className = 'status_temperature_right_temperature_row'),
        ]

    if convert_pa_to_mb > 1000 and get_led_on == ' LED ON ':
        return [
            html.Div([
                html.Div([
                    html.Img(src = app.get_asset_url('night-cloud.png'),
                             className = 'image_position'),
                    html.P('{0:,.2f}°C'.format(get_temp),
                           className = 'status_temperature'
                           ),
                ], className = 'image_position_status_temperature'),

                html.Div([
                    html.P('Cloudy',
                           className = 'status_temperature_right'
                           ),
                    html.P('FEELS LIKE' + ' ' + ' ' + '{0:,.0f}°C'.format(convert_f_t_c),
                           className = 'status_temperature_right_temperature'
                           ),
                ], className = 'status_temperature_right_temperature_column')
            ], className = 'status_temperature_right_temperature_row'),
        ]
    if convert_pa_to_mb < 1000 and get_rain_value > 900 and get_led_on == ' LED ON ':
        return [
            html.Div([
                html.Div([
                    html.Img(src = app.get_asset_url('night-cloud.png'),
                             className = 'image_position'),
                    html.P('{0:,.2f}°C'.format(get_temp),
                           className = 'status_temperature'
                           ),
                ], className = 'image_position_status_temperature'),

                html.Div([
                    html.P('Cloudy',
                           className = 'status_temperature_right'
                           ),
                    html.P('FEELS LIKE' + ' ' + ' ' + '{0:,.0f}°C'.format(convert_f_t_c),
                           className = 'status_temperature_right_temperature'
                           ),
                ], className = 'status_temperature_right_temperature_column')
            ], className = 'status_temperature_right_temperature_row'),
        ]

    if get_rain_value >= 800.0 and get_rain_value <= 900.0:
        return [
            html.Div([
                html.Div([
                    html.Img(src = app.get_asset_url('rain.png'),
                             className = 'image_position'),
                    html.P('{0:,.2f}°C'.format(get_temp),
                           className = 'status_temperature'
                           ),
                ], className = 'image_position_status_temperature'),

                html.Div([
                    html.P('Showers',
                           className = 'status_temperature_right'
                           ),
                    html.P('FEELS LIKE' + ' ' + ' ' + '{0:,.0f}°C'.format(convert_f_t_c),
                           className = 'status_temperature_right_temperature'
                           ),
                ], className = 'status_temperature_right_temperature_column')
            ], className = 'status_temperature_right_temperature_row'),
        ]

    if get_rain_value < 800.0:
        return [
            html.Div([
                html.Div([
                    html.Img(src = app.get_asset_url('rain.png'),
                             className = 'image_position'),
                    html.P('{0:,.2f}°C'.format(get_temp),
                           className = 'status_temperature'
                           ),
                ], className = 'image_position_status_temperature'),

                html.Div([
                    html.P('Rain',
                           className = 'status_temperature_right'
                           ),
                    html.P('FEELS LIKE' + ' ' + ' ' + '{0:,.0f}°C'.format(convert_f_t_c),
                           className = 'status_temperature_right_temperature'
                           ),
                ], className = 'status_temperature_right_temperature_column')
            ], className = 'status_temperature_right_temperature_row'),
        ]
    elif get_photo_resistor_value < 300.0:
        return [
            html.Div([
                html.Div([
                    html.Img(src = app.get_asset_url('moon.png'),
                             className = 'image_position'),
                    html.P('{0:,.2f}°C'.format(get_temp),
                           className = 'status_temperature'
                           ),
                ], className = 'image_position_status_temperature'),

                html.Div([
                    html.P('Clear',
                           className = 'status_temperature_right'
                           ),
                    html.P('FEELS LIKE' + ' ' + ' ' + '{0:,.0f}°C'.format(convert_f_t_c),
                           className = 'status_temperature_right_temperature'
                           ),
                ], className = 'status_temperature_right_temperature_column')
            ], className = 'status_temperature_right_temperature_row'),
        ]

    elif get_photo_resistor_value < 300.0 and convert_pa_to_mb > 1002.00 and convert_pa_to_mb <= 1005.00:
        return [
            html.Div([
                html.Div([
                    html.Img(src = app.get_asset_url('moon.png'),
                             className = 'image_position'),
                    html.P('{0:,.2f}°C'.format(get_temp),
                           className = 'status_temperature'
                           ),
                ], className = 'image_position_status_temperature'),

                html.Div([
                    html.P('Clear',
                           className = 'status_temperature_right'
                           ),
                    html.P('FEELS LIKE' + ' ' + ' ' + '{0:,.0f}°C'.format(convert_f_t_c),
                           className = 'status_temperature_right_temperature'
                           ),
                ], className = 'status_temperature_right_temperature_column')
            ], className = 'status_temperature_right_temperature_row'),
        ]
    elif get_photo_resistor_value < 300.0 and convert_pa_to_mb >= 1000.00 and convert_pa_to_mb < 1002.00:
        return [
            html.Div([
                html.Div([
                    html.Img(src = app.get_asset_url('fog-moon.png'),
                             className = 'image_position'),
                    html.P('{0:,.2f}°C'.format(get_temp),
                           className = 'status_temperature'
                           ),
                ], className = 'image_position_status_temperature'),

                html.Div([
                    html.P('Fog',
                           className = 'status_temperature_right'
                           ),
                    html.P('FEELS LIKE' + ' ' + ' ' + '{0:,.0f}°C'.format(convert_f_t_c),
                           className = 'status_temperature_right_temperature'
                           ),
                ], className = 'status_temperature_right_temperature_column')
            ], className = 'status_temperature_right_temperature_row'),
        ]
    elif get_photo_resistor_value >= 300.0 and get_photo_resistor_value <= 800.0:
        return [
            html.Div([
                html.Div([
                    html.Img(src = app.get_asset_url('cloud.png'),
                             className = 'image_position'),
                    html.P('{0:,.2f}°C'.format(get_temp),
                           className = 'status_temperature'
                           ),
                ], className = 'image_position_status_temperature'),

                html.Div([
                    html.P('Cloudy',
                           className = 'status_temperature_right'
                           ),
                    html.P('FEELS LIKE' + ' ' + ' ' + '{0:,.0f}°C'.format(convert_f_t_c),
                           className = 'status_temperature_right_temperature'
                           ),
                ], className = 'status_temperature_right_temperature_column')
            ], className = 'status_temperature_right_temperature_row'),
        ]

    elif get_photo_resistor_value > 800.0 and get_photo_resistor_value <= 900.0:
        return [
            html.Div([
                html.Div([
                    html.Img(src = app.get_asset_url('partly-cloud.png'),
                             className = 'image_position'),
                    html.P('{0:,.2f}°C'.format(get_temp),
                           className = 'status_temperature'
                           ),
                ], className = 'image_position_status_temperature'),

                html.Div([
                    html.P('Partly cloudy',
                           className = 'status_temperature_right'
                           ),
                    html.P('FEELS LIKE' + ' ' + ' ' + '{0:,.0f}°C'.format(convert_f_t_c),
                           className = 'status_temperature_right_temperature'
                           ),
                ], className = 'status_temperature_right_temperature_column')
            ], className = 'status_temperature_right_temperature_row'),
        ]

    elif get_photo_resistor_value > 900.0:
        return [
            html.Div([
                html.Div([
                    html.Img(src = app.get_asset_url('sunny.png'),
                             className = 'image_position'),
                    html.P('{0:,.2f}°C'.format(get_temp),
                           className = 'status_temperature'
                           ),
                ], className = 'image_position_status_temperature'),

                html.Div([
                    html.P('Sunny',
                           className = 'status_temperature_right'
                           ),
                    html.P('FEELS LIKE' + ' ' + ' ' + '{0:,.0f}°C'.format(convert_f_t_c),
                           className = 'status_temperature_right_temperature'
                           ),
                ], className = 'status_temperature_right_temperature_column')
            ], className = 'status_temperature_right_temperature_row'),
        ]
