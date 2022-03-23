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


def forecast_value_value(n_intervals):
    header_list = ['Date Time', 'Humidity', 'Rain', 'Photo Resistor Value', 'Photo Resistor LED', 'Revolution', 'RPM',
                   'Wind Speed KPH', 'Wind Degree', 'Wind Direction', 'CO2 Level', 'Temperature', 'Air Pressure']
    df = pd.read_csv('weather_data.csv', names = header_list)
    df2 = df[['Air Pressure', 'Temperature']].tail(1194)
    df2.dropna(inplace = True)
    df_x = df2.drop(['Temperature'], axis = 1)
    df_y = df2['Temperature']
    lr = linear_model.LinearRegression()
    lr.fit(df_x, df_y)
    y_predict = lr.predict(df_x)
    average_predicted_temperature = np.average(y_predict)

    return [
        html.P('{0:,.0f}°C'.format(average_predicted_temperature),
               className = 'predict_forecast_value'
               ),
    ]
