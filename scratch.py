import datetime
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
from datetime import datetime as dt

app = dash.Dash()

year_min = 1900
year_max = 2100
year_step = int((year_max - year_min) / 10)
month_step = 1
day_step = 3

app.layout = html.Div([
    dcc.Slider(
        id='birth-year-slider',
        min=year_min,
        max=year_max,
        step=1,
        value=2019,
        marks={i:str(i) for i in range(year_min, year_max+1, year_step)},
        updatemode='drag',
    ),
    html.Div([html.Br()]),
    dcc.Slider(
        id='birth-month-slider',
        min=1,
        max=12,
        step=1,
        value=6,
        marks={i:str(i) for i in range(1, 13, month_step)},
        updatemode='drag',
    ),
    html.Div([html.Br()]),
    dcc.Slider(
        id='birth-day-slider',
        min=1,
        max=31,
        step=1,
        value=15,
        marks={i:str(i) for i in range(1, 32, day_step)},
        updatemode='drag',
    ),
    html.Div([html.Br()]),
    dcc.DatePickerSingle(
        id='birth-date',
        date=dt(2019, 6, 15),
    ),
    html.Div([html.Br()]),

    dcc.Slider(
        id='birth-hour-slider',
        min=0,
        max=23,
        step=1,
        value=12,
        marks={i:str(i) for i in range(0, 24, 2)},
        updatemode='drag',
    ),
    html.Div([html.Br()]),
    dcc.Slider(
        id='birth-minute-slider',
        min=0,
        max=59,
        step=1,
        value=30,
        marks={i:str(i) for i in range(0, 60, 5)},
        updatemode='drag',
    ),
    html.Div([html.Br()]),
    html.Div(id="birth-time"),
    html.Div([html.Br()]),
])

@app.callback(
    Output('birth-date', 'date'),
    [Input('birth-year-slider', 'value'),
     Input('birth-month-slider', 'value'),
     Input('birth-day-slider', 'value')]
)
def update_birth_date(year, month, day):
    return datetime.date(year=year, month=month, day=day)

@app.callback(
    Output('birth-time', 'children'),
    [Input('birth-hour-slider', 'value'),
     Input('birth-minute-slider', 'value')]
)
def update_birth_time(hour, minute):
    return "{:02}:{:02}".format(hour, minute)


if __name__ == '__main__':
    app.run_server(debug=True)