from dash import html, dcc
import dash_bootstrap_components as dbc

from assets.config import KNOWN_SERIES, VERTEX_SELECTION_METHODS
from functions.global_functions import blank_figure, create_options


def create_toolbar():
    toolbar = dbc.Row([
        dbc.Col(
            dbc.InputGroup([
                dbc.InputGroupText('Series'),
                dbc.Select(
                    id='series_select_single_polar',
                    options=create_options(KNOWN_SERIES),
                    value=create_options(KNOWN_SERIES)[0]['value'],
                    disabled=True
                ),
            ])
        ),
         dbc.Col(
            dbc.InputGroup([
                dbc.InputGroupText('Vertex Selection'),
                dbc.Select(
                    id='vertex_selection_single_polar',
                    options=create_options(VERTEX_SELECTION_METHODS),
                    value=create_options(VERTEX_SELECTION_METHODS)[0]['value'],
                    disabled=True
                ),
            ])
        ),
        dbc.Col(
            dbc.InputGroup([
                dbc.InputGroupText('Divisor'),
                dbc.Input(id='divisor_input', value=5, type="number"),
            ])
        )
    ], style={'marginBottom': 15})
    return toolbar


def create_repeating_sequence_text():
    sequence_text=html.Div(id="repeating_sequence_text")
    return sequence_text


def create_figure_layout():
    figure = html.Div([
        dcc.Loading(
            [
                dcc.Graph(
                    id='polar_figure',
                    figure=blank_figure(),
                    config={'displaylogo': False},
                    style={'height': '70vh'}
                )
            ],
            id='polar_figure_loading',
            type='circle'
        )
    ])
    return figure


layout = html.Div([
    create_toolbar(),
    create_repeating_sequence_text(),
    create_figure_layout()
])
