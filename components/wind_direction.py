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


# @app.callback(Output('wind_direction_value', 'children'),
#               [Input('update_value', 'n_intervals')])
# def weather_value(n_intervals):
#     header_list = ['Date Time', 'Humidity', 'Rain', 'Photo Resistor Value', 'Photo Resistor LED', 'Revolution', 'RPM',
#                    'Wind Speed KPH', 'Wind Degree', 'Wind Direction', 'CO2 Level', 'Temperature', 'Air Pressure']
#     df = pd.read_csv('weather_data.csv', names = header_list)
#
#     # engine = sqlalchemy.create_engine('mysql+pymysql://vo73ww2oq1t3byst:tw4syv8irwcxd5iv@d3y0lbg7abxmbuoi.chr7pe7iynqr.eu-west-1.rds.amazonaws.com:3306/eqgk9pk342vfu3vx')
#     # df = pd.read_sql_table('accuweather', engine)
#
#     # degree_value = [112.5, 67.5, 90, 157.5, 135, 202.5, 180, 22.5, 45, 247.5, 225, 337.5, 0, 292.5, 315, 270]
#     # direction_value = ["ESE", "ENE", "E", "SSE", "SE", "SSW", "S", "NNE", "NE", "WSW", "SW", "NNW", "N", "WNW", "NW",
#     #                    "W"]
#     # dictionary_degree_direction = {'Degree': degree_value, 'Direction': direction_value}
#     # df2 = pd.DataFrame(dictionary_degree_direction)
#     # df2['Degree'] = df2['Degree'].astype(float)
#     # df2['Direction'] = df2['Direction'].astype(str)
#     # merge_df = pd.merge(left = df,
#     #                     right = df2,
#     #                     how = 'inner',
#     #                     left_on = ['Wind Direction'],
#     #                     right_on = ['Degree'])
#
#     get_wind_direction = df['Wind Direction'].tail(1).iloc[0]
#
#     return [
#             html.Div([
#                 html.Img(src = app.get_asset_url('compass.png'),
#                          className = 'compass_image'
#                          ),
#                 html.Div([
#                     html.P('WIND DIRECTION',
#                            className = 'w_d_value'
#                            ),
#                     html.P(get_wind_direction,
#                            className = 'w_d_number_value'
#                            ),
#                 ], className = 'w_d_number_value_row'),
#             ], className = 'w_d_number_value_column'),
#         ]

def wind_direction_graph(n_intervals):
    header_list = ['Date Time', 'Humidity', 'Rain', 'Photo Resistor Value', 'Photo Resistor LED', 'Revolution', 'RPM',
                   'Wind Speed KPH', 'Wind Degree', 'Wind Direction', 'CO2 Level', 'Temperature', 'Air Pressure']
    df = pd.read_csv('weather_data.csv', names = header_list)
    # r_value = [112.5,67.5,90,157.5,135,202.5,180,22.5,45,247.5,225,337.5,0,292.5,315,270]
    # theta_value = ["ESE","ENE","E","SSE","SE","SSW","S","NNE","NE","WSW","SW","NNW","N","WNW","NW","W"]
    # r_value = [0,22.5,45,67.5,90,112.5,135,157.5,180,202.5,225,247.5,270,292.5,315,337.5]
    # theta_value = ['N','NNE','NE','ENE','E','ESE','SE','SSE','S','SSW','SW','WSW','W','WNW','NW','NNW']
    r_value = [90, 67.5, 45, 22.5, 0, 337.5, 315, 292.5, 270, 247.5, 225, 202.5, 180, 157.5, 135, 112.5]
    theta_value = ['E', 'ENE', 'NE', 'NNE', 'N', 'NNW', 'NW', 'WNW', 'W', 'WSW', 'SW', 'SSW', 'S', 'SSE', 'SE', 'ESE']

    return {
        'data': [go.Scatterpolar(
            r = r_value,
            theta = theta_value,
            fill = 'toself',
            mode = 'markers+lines',
            marker = dict(color = 'rgb(111, 231, 219)',
                          size = 5,
                          line = dict(color = 'rgba(111, 231, 219, .1)',
                                      width = 1)),
            hoverinfo = 'skip',
        ),
            go.Scatterpolar(
                r = df['Wind Degree'].tail(1),
                theta = df['Wind Direction'].tail(1),
                mode = 'markers',
                marker = dict(color = 'orange',
                              size = 10),
                hoverinfo = 'text',
                hovertext =
                '<b>Degree</b>: ' + df['Wind Degree'].tail(1).astype(str) + '<br>' +
                '<b>Direction</b>: ' + df['Wind Direction'].tail(1).astype(str) + '<br>'
            )],
        'layout': go.Layout(polar = dict(radialaxis = dict(visible = False),
                                         bgcolor = 'rgba(255, 255, 255, 0)',
                                         angularaxis = dict(showline = True,
                                                            linecolor = 'white',
                                                            tickcolor = 'white')),
                            showlegend = False,
                            paper_bgcolor = 'rgba(255, 255, 255, 0)',
                            plot_bgcolor = 'rgba(255, 255, 255, 0)',
                            font = dict(color = 'white'),
                            ),
    }
