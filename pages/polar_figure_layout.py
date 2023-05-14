from dash import html, dcc
import dash_bootstrap_components as dbc

from config import KNOWN_SERIES
from functions.global_functions import blank_figure

def create_options():
    return [{'label': x.capitalize(), 'value': x} for x in KNOWN_SERIES]


def create_toolbar():
    toolbar = html.Div([
        dbc.InputGroup(
            dbc.InputGroupText('Series'),
            dbc.Select(id='series_select', options=create_options(), value=create_options()[0]['value']),
        ),
        dbc.InputGroup(
            dbc.InputGroupText('Length'),
            dbc.Input(id='length_input', value=30, type="number"),
        )
        dbc.InputGroup(
            dbc.InputGroupText('Divisor'),
            dbc.Input(id='divisor_input', value=3, type="number"),
        )
    ])
    return toolbar


def create_figure_layout():
    figure = html.Div([
        dcc.Loading(
            [
                dcc.Graph(
                    id='polar_figure',
                    figure=blank_figure(),
                    config={'displaylogo': False},
                    style={'height': '95vh'}
                )
            ],
            id='polar_figure_loading',
            type='circle'
        )
    ])
    return figure


layout = html.Div([
    dbc.Row(
        dbc.Col(create_toolbar(), width=3),
        dbc.Col(create_figure_layout(), width=9),
    )
])