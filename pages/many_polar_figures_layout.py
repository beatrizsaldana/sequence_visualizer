from dash import html, dcc
import dash_bootstrap_components as dbc

from assets.config import NUMBER_OF_PLOTS, MANY_POLAR_FIGURES_START_VH
from functions.global_functions import blank_figure, create_options


def get_vh(start_vh: int = MANY_POLAR_FIGURES_START_VH, numbe_of_plots: int = NUMBER_OF_PLOTS) -> str:
    '''Get the vertical height of the compotent containing the figures'''
    vh = start_vh
    if numbe_of_plots > 40:
        x = numbe_of_plots - 40
        n, r = divmod(x, 10)
        num = n + 1 if r > 0 else n
        vh = vh + (num*25)
    return f'{vh}vh'


def create_toolbar():
    toolbar = dbc.Row([
        dbc.Col(
            dbc.InputGroup([
                dbc.InputGroupText('Series'),
                dbc.Select(id='series_select_multiple_polar', options=create_options(), value=create_options()[0]['value']),
            ])
        ),
        dbc.Col(
            dbc.InputGroup([
                dbc.InputGroupText('Number of Figures'),
                dbc.Input(id='number_of_figures', value=NUMBER_OF_PLOTS, type="number"),
            ])
        )
    ], style={'marginBottom': 15})
    return toolbar


layout = html.Div([
    create_toolbar(),
    dcc.Loading(
        [
            dcc.Graph(
                id='many_polar_figures',
                figure=blank_figure(),
                config={'displaylogo': False},
                style={'height': get_vh()}
            )
        ],
        id='many_polar_figures_loading',
        type='circle'
    )
])