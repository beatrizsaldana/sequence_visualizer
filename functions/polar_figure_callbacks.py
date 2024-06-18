from functions.sequence_class import Series
from functions.polar_figure_functions import create_polar_plot
from functions.get_sequences_functions import get_fibonacci_sequence

from dash import Input, Output, callback

from assets.config import SERIES_LENGTH


@callback(
    Output('polar_figure', 'figure'),
    [
        Input('series_select_single_polar', 'value'),
        Input('divisor_input', 'value')
    ]
)
def update_polar_figure(selected_series, divisor):
    series = Series.from_known_sequence(name=selected_series, length=SERIES_LENGTH)
    mod_sequence = series.get_mod_sequence(divisor=divisor)
    return create_polar_plot(sequence=mod_sequence, divisor=divisor)
