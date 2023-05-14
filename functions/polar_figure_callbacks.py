from global_files.app import app
from sequence_class import Series
from polar_figure_functions import create_polar_plot


@app.callback(
    Output('polar_figure', 'figure'),
    [
        Input('series_select', 'value'),
        Input('length_input', 'value'),
        Input('divisor_input', 'value')
    ],
    prevent_initial_call=True
)
def update_polar_figure(selected_series, length, divisor):
    series = Series.from_known_sequence(name=selected_series, length=length)
    return create_polar_plot(sequence=series.get_mod_sequence(divisor=divisor))
    