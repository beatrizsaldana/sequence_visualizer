from dash import html, dcc
import dash_bootstrap_components as dbc

from assets.config import KNOWN_SERIES
from functions.global_functions import blank_figure


layout = html.Div([
    dcc.Loading(
        [
            dcc.Graph(
                id='many_polar_figures',
                figure=blank_figure(),
                config={'displaylogo': False},
                style={'height': '150vh'}
            )
        ],
        id='many_polar_figures_loading',
        type='circle'
    )
])