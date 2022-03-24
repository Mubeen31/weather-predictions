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


def air_pressure_value(n_intervals):
    header_list = ['Date Time', 'Humidity', 'Rain', 'Photo Resistor Value', 'Photo Resistor LED', 'Revolution', 'RPM',
                   'Wind Speed KPH', 'Wind Degree', 'Wind Direction', 'CO2 Level', 'Temperature', 'Air Pressure']
    df = pd.read_csv('weather_data.csv', names = header_list)
    df['Air Pressure'] = df['Air Pressure'] / 1
    df['Pressure_Difference'] = df['Air Pressure'].diff()
    pressure_difference = df['Pressure_Difference'].tail(1).iloc[0].astype(float)
    get_air_pressure = df['Air Pressure'].tail(1).iloc[0].astype(float)
    convert_pa_to_mb = get_air_pressure / 100

    # if pressure_difference < 0:
    return [
        html.Div([
            html.Img(src = app.get_asset_url('atmospheric-pressure.png'),
                     className = 'atmospheric_image'
                     ),
            html.Div([
                html.P('ATMOSPHERIC PRESSURE',
                       className = 'air_pressure_text_value'
                       ),

                html.P('{0:,.2f} mb'.format(convert_pa_to_mb),
                       className = 'air_value'
                       ),
                html.P('Falling',
                       className = 'falling_rising_value'
                       ),
            ], className = 'air_pressure_text_air_value')
        ], className = 'air_pressure_text_air_value_row'),

    ]

    # elif pressure_difference > 0:
    #     return [
    #         html.Div([
    #             html.Img(src = app.get_asset_url('atmospheric-pressure.png'),
    #                      className = 'atmospheric_image'
    #                      ),
    #             html.Div([
    #                 html.P('ATMOSPHERIC PRESSURE',
    #                        className = 'air_pressure_text_value'
    #                        ),
    #
    #                 html.P('{0:,.2f} mb'.format(convert_pa_to_mb),
    #                        className = 'air_value'
    #                        ),
    #                 html.P('Rising',
    #                        className = 'falling_rising_value'
    #                        ),
    #             ], className = 'air_pressure_text_air_value')
    #         ], className = 'air_pressure_text_air_value_row'),
    #
    #     ]
    # elif pressure_difference == 0:
    #     return [
    #         html.Div([
    #             html.Img(src = app.get_asset_url('atmospheric-pressure.png'),
    #                      className = 'atmospheric_image'
    #                      ),
    #             html.Div([
    #                 html.P('ATMOSPHERIC PRESSURE',
    #                        className = 'air_pressure_text_value'
    #                        ),
    #
    #                 html.P('{0:,.2f} mb'.format(convert_pa_to_mb),
    #                        className = 'air_value'
    #                        ),
    #                 html.P('',
    #                        className = 'falling_rising_value'
    #                        ),
    #             ], className = 'air_pressure_text_air_value')
    #         ], className = 'air_pressure_text_air_value_row'),
    #
    #     ]
