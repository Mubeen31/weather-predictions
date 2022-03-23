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


def forecast_image_value(n_intervals):
    header_list = ['Date Time', 'Humidity', 'Rain', 'Photo Resistor Value', 'Photo Resistor LED', 'Revolution', 'RPM',
                   'Wind Speed KPH', 'Wind Degree', 'Wind Direction', 'CO2 Level', 'Temperature', 'Air Pressure']
    df = pd.read_csv('weather_data.csv', names = header_list)
    get_led_on = df['Photo Resistor LED'].tail(1).iloc[0]
    df['Air Pressure'] = df['Air Pressure'] / 100
    df2 = df[['Temperature', 'Air Pressure']].tail(1194)
    df2.dropna(inplace = True)
    df_x = df2.drop(['Air Pressure'], axis = 1)
    df_y = df2['Air Pressure']
    lr = linear_model.LinearRegression()
    lr.fit(df_x, df_y)
    y_predict = lr.predict(df_x)
    average_predicted_pressure = np.average(y_predict)

    if average_predicted_pressure < 1000 and get_led_on == ' LED ON ':
        return [
            html.Img(src = app.get_asset_url('night-rain.png'),
                     className = 'forecast_image'),
        ]
    if average_predicted_pressure > 1000 and get_led_on == ' LED ON ':
        return [
            html.Img(src = app.get_asset_url('night-cloud.png'),
                     className = 'forecast_image'),
        ]
    if average_predicted_pressure < 1000:
        return [
            html.Img(src = app.get_asset_url('rain.png'),
                     className = 'forecast_image'),
        ]
    elif average_predicted_pressure > 1000 and average_predicted_pressure < 1015:
        return [
            html.Img(src = app.get_asset_url('cloud.png'),
                     className = 'forecast_image'),
        ]
    elif average_predicted_pressure > 1015:
        return [
            html.Img(src = app.get_asset_url('sunny.png'),
                     className = 'forecast_image'),
        ]
