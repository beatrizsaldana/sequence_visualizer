from functions.sequence_class import Series
from functions.many_polar_figures_functions import create_many_polar_plots
from functions.get_sequences_functions import get_fibonacci_sequence

from dash import Input, Output, callback

from assets.config import SERIES_LENGTH, NUMBER_OF_PLOTS


@callback(
    Output('many_polar_figures', 'figure'),
    [
        Input('series_select', 'value')
    ]
)
def update_polar_figure(selected_series):
    series = Series.from_known_sequence(name=selected_series, length=SERIES_LENGTH)
    return create_many_polar_plots(series=series, number_of_plots=NUMBER_OF_PLOTS)
