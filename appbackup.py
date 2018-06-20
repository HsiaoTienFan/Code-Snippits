import dash
from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
pd.core.common.is_list_like = pd.api.types.is_list_like
from pandas_datareader import data as web
from datetime import datetime as dt
import plotly.graph_objs as go

app = dash.Dash()
Now = pd.read_csv("C:/Users/Fanhsiao/Downloads/new.csv")
labelNames = pd.read_csv("C:/Users/Fanhsiao/Desktop/Dash/formattedLabels.csv")
for i in range(0,len(labelNames.columns)):
    options = [{'label':labelNames.columns[i], 'value':labelNames.columns[i]}]
app.layout = html.Div([
    dcc.Dropdown(
        id='vsIn',
        options = [{'label':labelNames.columns[i], 'value':labelNames.columns[i]} for i in range(0,len(labelNames.columns))],
        value=options[0]['label'],
        clearable=False,
        placeholder="Select a variable"
    ),
    html.Div([
        html.H1('Mozz1 vs Mozz2'),
        dcc.Graph(id='vsOut'),
        html.H1('Histogram'),
        dcc.Graph(id='histOut')
    ])
])

@app.callback(Output('vsOut', 'figure'), [Input('vsIn', 'value')])
def update_graph(selected_dropdown_value):
    getVariable = [{'label': i, 'value': i} for i in labelNames[selected_dropdown_value]]
    df = Now
    # Create traces
    trace0 = go.Scatter(
        x = df.sample_dt,
        y = df[getVariable[0]['label']],
        mode = 'lines',
        name = 'Mozz1'
    )
    trace1 = go.Scatter(
        x = df.sample_dt,
        y = df[getVariable[1]['label']],
        mode = 'lines',
        name = 'Mozz2'
    )   
    return {
        'data': [trace0, trace1]
    }


@app.callback(Output('histOut', 'figure'), [Input('vsIn', 'value')])
def update_graph(selected_dropdown_value):
    getVariable = [{'label': i, 'value': i} for i in labelNames[selected_dropdown_value]]
    df = Now
    # Create traces
    trace0 = go.Histogram(
        x = df[getVariable[0]['label']],
        opacity=0.75,
        name = 'Mozz1'
    )
    trace1 = go.Histogram(
        x = df[getVariable[1]['label']],
        opacity=0.75,
        name = 'Mozz2'
    )
    
    return {
        'data': [trace0, trace1],
        'layout' : 
        go.Layout(barmode='overlay')
    }


if __name__ == '__main__':
    app.run_server()
    
    
    