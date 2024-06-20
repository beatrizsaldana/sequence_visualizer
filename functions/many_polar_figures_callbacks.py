from functions.sequence_class import Series
from functions.many_polar_figures_functions import create_many_polar_plots
from assets.config import SERIES_LENGTH, NUMBER_OF_PLOTS

from dash import Input, Output, callback


@callback(
    Output('many_polar_figures', 'figure'),
    [
        Input('series_select_single_polar', 'value'),
        Input('vertex_selection_multiple_polar', 'value')
    ]
)
def update_polar_figure(selected_series, vertex_selection_method):
    series = Series.from_known_sequence(name=selected_series, length=SERIES_LENGTH)
    return create_many_polar_plots(series=series, number_of_plots=NUMBER_OF_PLOTS, vertex_selection_method=vertex_selection_method)
