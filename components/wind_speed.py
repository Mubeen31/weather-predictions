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


def wind_speed_graph(n_intervals):
    header_list = ['Date Time', 'Humidity', 'Rain', 'Photo Resistor Value', 'Photo Resistor LED', 'Revolution', 'RPM',
                   'Wind Speed KPH', 'Wind Degree', 'Wind Direction', 'CO2 Level', 'Temperature', 'Air Pressure']
    df = pd.read_csv('weather_data.csv', names = header_list)
    get_wind_speed = df['Wind Speed KPH'].tail(1).iloc[0].astype(float)

    if get_wind_speed <= 20.00:
        return {
            'data': [go.Indicator(
                mode = 'gauge',
                value = get_wind_speed,
                gauge = {'axis': {'range': [None, 20], 'tickcolor': "white"},
                         'bar': {'color': "rgba(0, 255, 255, 0.3)", 'thickness': 1},
                         'bordercolor': "rgb(0, 255, 255)",
                         'borderwidth': 0.5,
                         # 'threshold': {'line': {'color': "white", 'width': 2},
                         #               'thickness': 1, 'value': 7}
                         },
                # number = {'valueformat': '.2f',
                #           'font': {'size': 20},
                #           },
                domain = {'y': [0, 1], 'x': [0, 1]})],
            'layout': go.Layout(
                title = {'text': 'Wind Speed and Direction',
                         'y': 0.75,
                         'x': 0.5,
                         'xanchor': 'center',
                         'yanchor': 'top'
                         },
                font = dict(color = 'white',
                            size = 10),
                paper_bgcolor = 'rgba(255, 255, 255, 0)',
                plot_bgcolor = 'rgba(255, 255, 255, 0)',
            ),
        }
    elif get_wind_speed > 20.00 and get_wind_speed <= 30.00:
        return {
            'data': [go.Indicator(
                mode = 'gauge',
                value = get_wind_speed,
                gauge = {'axis': {'range': [None, 30], 'tickcolor': "white"},
                         'bar': {'color': "rgba(0, 255, 255, 0.3)", 'thickness': 1},
                         'bordercolor': "rgb(0, 255, 255)",
                         'borderwidth': 0.5,
                         # 'threshold': {'line': {'color': "white", 'width': 2},
                         #               'thickness': 1, 'value': 7}
                         },
                # number = {'valueformat': '.2f',
                #           'font': {'size': 20},
                #           },
                domain = {'y': [0, 1], 'x': [0, 1]})],
            'layout': go.Layout(
                title = {'text': '',
                         'y': 0.8,
                         'x': 0.5,
                         'xanchor': 'center',
                         'yanchor': 'top'
                         },
                font = dict(color = 'white'),
                paper_bgcolor = 'rgba(255, 255, 255, 0)',
                plot_bgcolor = 'rgba(255, 255, 255, 0)',
            ),
        }
    elif get_wind_speed > 30.00 and get_wind_speed <= 40.00:
        return {
            'data': [go.Indicator(
                mode = 'gauge',
                value = get_wind_speed,
                gauge = {'axis': {'range': [None, 40], 'tickcolor': "white"},
                         'bar': {'color': "rgba(0, 255, 255, 0.3)", 'thickness': 1},
                         'bordercolor': "rgb(0, 255, 255)",
                         'borderwidth': 0.5,
                         # 'threshold': {'line': {'color': "white", 'width': 2},
                         #               'thickness': 1, 'value': 7}
                         },
                # number = {'valueformat': '.2f',
                #           'font': {'size': 20},
                #           },
                domain = {'y': [0, 1], 'x': [0, 1]})],
            'layout': go.Layout(
                title = {'text': '',
                         'y': 0.8,
                         'x': 0.5,
                         'xanchor': 'center',
                         'yanchor': 'top'
                         },
                font = dict(color = 'white'),
                paper_bgcolor = 'rgba(255, 255, 255, 0)',
                plot_bgcolor = 'rgba(255, 255, 255, 0)',
            ),
        }
    elif get_wind_speed > 40.00 and get_wind_speed <= 50.00:
        return {
            'data': [go.Indicator(
                mode = 'gauge',
                value = get_wind_speed,
                gauge = {'axis': {'range': [None, 50], 'tickcolor': "white"},
                         'bar': {'color': "rgba(0, 255, 255, 0.3)", 'thickness': 1},
                         'bordercolor': "rgb(0, 255, 255)",
                         'borderwidth': 0.5,
                         # 'threshold': {'line': {'color': "white", 'width': 2},
                         #               'thickness': 1, 'value': 7}
                         },
                # number = {'valueformat': '.2f',
                #           'font': {'size': 20},
                #           },
                domain = {'y': [0, 1], 'x': [0, 1]})],
            'layout': go.Layout(
                title = {'text': '',
                         'y': 0.8,
                         'x': 0.5,
                         'xanchor': 'center',
                         'yanchor': 'top'
                         },
                font = dict(color = 'white'),
                paper_bgcolor = 'rgba(255, 255, 255, 0)',
                plot_bgcolor = 'rgba(255, 255, 255, 0)',
            ),
        }
    elif get_wind_speed > 50.00 and get_wind_speed <= 60.00:
        return {
            'data': [go.Indicator(
                mode = 'gauge',
                value = get_wind_speed,
                gauge = {'axis': {'range': [None, 60], 'tickcolor': "white"},
                         'bar': {'color': "rgba(0, 255, 255, 0.3)", 'thickness': 1},
                         'bordercolor': "rgb(0, 255, 255)",
                         'borderwidth': 0.5,
                         # 'threshold': {'line': {'color': "white", 'width': 2},
                         #               'thickness': 1, 'value': 7}
                         },
                # number = {'valueformat': '.2f',
                #           'font': {'size': 20},
                #           },
                domain = {'y': [0, 1], 'x': [0, 1]})],
            'layout': go.Layout(
                title = {'text': '',
                         'y': 0.8,
                         'x': 0.5,
                         'xanchor': 'center',
                         'yanchor': 'top'
                         },
                font = dict(color = 'white'),
                paper_bgcolor = 'rgba(255, 255, 255, 0)',
                plot_bgcolor = 'rgba(255, 255, 255, 0)',
            ),
        }
    elif get_wind_speed > 60.00:
        return {
            'data': [go.Indicator(
                mode = 'gauge',
                value = get_wind_speed,
                gauge = {'axis': {'range': [None, get_wind_speed + 50.00], 'tickcolor': "white"},
                         'bar': {'color': "rgba(0, 255, 255, 0.3)", 'thickness': 1},
                         'bordercolor': "rgb(0, 255, 255)",
                         'borderwidth': 0.5,
                         # 'threshold': {'line': {'color': "white", 'width': 2},
                         #               'thickness': 1, 'value': 7}
                         },
                # number = {'valueformat': '.2f',
                #           'font': {'size': 20},
                #           },
                domain = {'y': [0, 1], 'x': [0, 1]})],
            'layout': go.Layout(
                title = {'text': '',
                         'y': 0.8,
                         'x': 0.5,
                         'xanchor': 'center',
                         'yanchor': 'top'
                         },
                font = dict(color = 'white'),
                paper_bgcolor = 'rgba(255, 255, 255, 0)',
                plot_bgcolor = 'rgba(255, 255, 255, 0)',
            ),
        }
