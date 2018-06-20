# -*- coding: utf-8 -*-
"""
Created on Thu Jun 21 09:53:00 2018

@author: Fanhsiao
"""
import dash
from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
from datetime import datetime as dt
import plotly.graph_objs as go

Now = pd.read_csv("C:/Users/Fanhsiao/Downloads/new.csv")
labelNames = pd.read_csv("C:/Users/Fanhsiao/Downloads/Mozz/formattedLabels.csv")
    