from functions.sequence_class import Series
from functions.polar_figure_functions import create_polar_plot
from functions.get_sequences_functions import get_fibonacci_sequence

from dash import html, Input, Output, callback
import dash_bootstrap_components as dbc

from assets.config import SERIES_LENGTH


@callback(
    [
        Output('polar_figure', 'figure'),
        Output('repeating_sequence_single_polar', 'data'),
    ],
    [
        Input('series_select_single_polar', 'value'),
        Input('divisor_input', 'value')
    ]
)
def update_polar_figure(selected_series, divisor):
    series = Series.from_known_sequence(name=selected_series, length=SERIES_LENGTH)
    mod_sequence = series.get_mod_sequence(divisor=divisor)
    figure = create_polar_plot(sequence=mod_sequence, divisor=divisor)
    return [figure, mod_sequence]


@callback(
    Output('repeating_sequence_text', 'children'),
    [
        Input('repeating_sequence_single_polar', 'data')
    ]
)
def update_repeating_sequence_single_polar(repeating_sequence):
    children = [
        dbc.Card(
            dbc.CardBody(
                html.P(str(repeating_sequence))
            )
        )
    ]
    return children
