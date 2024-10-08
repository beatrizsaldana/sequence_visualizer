from functions.sequence_class import Series
from functions.polar_figure_functions import create_polar_plot
from assets.config import SERIES_LENGTH

from dash import html, Input, Output, callback
import dash_bootstrap_components as dbc


@callback(
    [
        Output('polar_figure', 'figure'),
        Output('repeating_sequence_single_polar', 'data'),
    ],
    [
        Input('series_select_single_polar', 'value'),
        Input('vertex_selection_single_polar', 'value'),
        Input('divisor_input', 'value') 
    ]
)
def update_polar_figure(selected_series, vertex_selection_method, divisor):
    series = Series.from_known_sequence(name=selected_series, length=SERIES_LENGTH)
    mod_sequence = series.get_mod_sequence(divisor=divisor)
    figure = create_polar_plot(sequence=mod_sequence, vertex_selection_method=vertex_selection_method, divisor=divisor)
    return [figure, mod_sequence]


@callback(
    Output('repeating_sequence_text', 'children'),
    [
        Input('repeating_sequence_single_polar', 'data')
    ]
)
def update_repeating_sequence_single_polar(repeating_sequence):
    children = [
        html.P(f"Repeating Sequence: {repeating_sequence}"),
        html.P(f"Repeating Sequence Length: {len(repeating_sequence)}")
    ]
    return children
