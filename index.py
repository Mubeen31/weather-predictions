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
import pathlib
from components.data_update_time import last_data_update_time
from components.title_image_value import title_image_and_value
from components.background_image_container import background_image_and_container
from components.current_time import current_time_value

# engine = sqlalchemy.create_engine('mysql+pymysql://b54eb1e6af434b:181636f95f46e13@eu-cdbr-west-02.cleardb.net:3306/heroku_323e0ab91ec4d38')
# df = pd.read_sql_table('accuweather', engine)
# df1 = df.tail(1)
# print(df1)

# header_list = ['Date Time', 'Humidity', 'Rain', 'Photo Resistor Value', 'Photo Resistor LED', 'Revolution', 'RPM',
#                'Wind Speed KPH', 'Wind Degree', 'Wind Direction', 'CO2 Level', 'Temperature', 'Air Pressure']
# df5 = pd.read_csv('weather_data.csv', names = header_list)
# df6 = df5.tail(2)

font_awesome = "https://use.fontawesome.com/releases/v5.10.2/css/all.css"
meta_tags = [{"name": "viewport", "content": "width=device-width"}]
external_stylesheets = [meta_tags, font_awesome]

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
server = app.server
app.title = "Weather Sensor Data"

app.layout = html.Div([
    html.Div([
        dcc.Interval(id='update_value',
                     interval=6000,
                     n_intervals=0),
    ]),

    html.Div([
        dcc.Interval(id='update_time',
                     interval=1000,
                     n_intervals=0),
    ]),

    html.Div([
        html.Div([
            html.Div([
                html.Div(id='last_data_update_time'),
            ], className='last_data_update_time'),
            html.Div([
                html.Div([
                    html.Div([
                        html.I(className="fas fa-home"),
                    ], className='title_image'),
                    html.H6('Newtown Road, Worcester, England',
                            style={'color': 'white'},
                            className='title'
                            ),
                ], className='logo_title'),
                html.Div(id='title_image_value')
            ], className='title_image_value_row'),
            html.A(href='https://www.accuweather.com/en/gb/worcester/wr1-3/current-weather/331595',
                   target='_blank',
                   children=[html.P('AccuWeather Data: Worcester, Worcestershire, England', className='link')]),
        ], className='title_date_time_container')
    ], className='title_date_time_container_overlay'),

    html.Div([

        html.Div(id='background_image_container',
                 className='background_image'),
        html.Div([
            html.Div([
                html.Div([
                    html.Div([
                        html.Div(id='time_value')
                    ], className='current_weather_time_value'),
                ], className='current_weather_time_value_forecast_row'),
            ], className='background_image_current_weather_time_column'),
        ], className='background_image_current_weather_time_content_row')
    ], className='background_image_current_weather_time_column'),
])


@app.callback(Output('last_data_update_time', 'children'),
              [Input('update_value', 'n_intervals')])
def last_data_update_time_callback(n_intervals):
    last_data_update_time_data = last_data_update_time(n_intervals)

    return last_data_update_time_data


@app.callback(Output('title_image_value', 'children'),
              [Input('update_value', 'n_intervals')])
def title_image_and_value_callback(n_intervals):
    title_image_and_value_data = title_image_and_value(n_intervals)

    return title_image_and_value_data


@app.callback(Output('background_image_container', 'children'),
              [Input('update_value', 'n_intervals')])
def background_image_and_container_callback(n_intervals):
    background_image_and_container_data = background_image_and_container(n_intervals)

    return background_image_and_container_data


@app.callback(Output('time_value', 'children'),
              [Input('update_time', 'n_intervals')])
def current_time_value_callback(n_intervals):
    current_time_value_data = current_time_value(n_intervals)

    return current_time_value_data


if __name__ == "__main__":
    app.run_server(debug=True)
