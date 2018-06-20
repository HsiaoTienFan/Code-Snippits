from initialisation import *

Now = pd.read_csv("C:/Users/Fanhsiao/Downloads/new.csv")
labelNames = pd.read_csv("C:/Users/Fanhsiao/Downloads/Mozz/formattedLabels.csv")
for i in range(0,len(labelNames.columns)):
    options = [{'label':labelNames.columns[i], 'value':labelNames.columns[i]}]

app = dash.Dash()
app.config['suppress_callback_exceptions']=True
app.scripts.config.serve_locally = True
vertical = True

app.layout = html.Div([
    html.H1('Variable Comparison'),
        dcc.Dropdown(
            id='dropIn',
            options = [{'label':labelNames.columns[i], 'value':labelNames.columns[i]} for i in range(0,len(labelNames.columns))],
            value=options[0]['label'],
            clearable=False,
            placeholder="Select a variable"
        ),
    html.H1(''),
    html.Div(
        dcc.Tabs(
            tabs=[
                {'label': 'Mozz1 vs Mozz2', 'value': 'scatter'},
                {'label': 'Histogram', 'value': 'histogram'},
                {'label': 'Predictions', 'value': 'scatter'},
                {'label': 'Target Pricing', 'value': 'scatter'},
            ],
            value='scatter',
            id='tabs',
            vertical=vertical,
            style={
                'height': '100vh',
                'borderRight': 'thin lightgrey solid',
                'textAlign': 'left'
            }
        ),
        style={'width': '20%', 'float': 'left'}
    ),
    html.Div(
        html.Div(id='tab-output'),
        style={'width': '80%', 'float': 'right'}
    ),
], style={
    'fontFamily': 'Sans-Serif',
    'margin-left': 'auto',
    'margin-right': 'auto',
})

    
@app.callback(Output('tab-output', 'children'), [Input('tabs', 'value'), Input('dropIn', 'value')])
def display_content(tabs, selected_dropdown_value):
    getVariable = ['sample_dt'] + [i for i in labelNames[selected_dropdown_value]]
    df = Now[getVariable]
    data = [
        {
            'x': df.sample_dt,
            'y': df[getVariable[1]],
            'type': tabs,
            'name' : 'Mozz1'
        },
        {
            'x': df.sample_dt,
            'y': df[getVariable[2]],
            'type': tabs,
            'name' : 'Mozz2'
        }
    ]
    if tabs == 'histogram':
        data = [
            {
                'x': df[getVariable[1]],
                'type': tabs,
                'name' : 'Mozz1',
                'opacity' : 0.75
            },
            {
                'x': df[getVariable[2]],
                'type': tabs,
                'name' : 'Mozz2',
                'opacity' : 0.75
            }
        ]

    return html.Div([
        dcc.Graph(
            id='graph',
            figure={
                'data': data,
                'layout' : go.Layout(barmode='overlay')
                }
        ),
    ])


if __name__ == '__main__':
    app.run_server(debug=True)