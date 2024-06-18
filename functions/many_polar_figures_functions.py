import plotly.graph_objects as go
from typing import List, Any
import pandas as pd
from plotly.subplots import make_subplots

from functions.sequence_class import Series


def create_subplot_specs(number_of_rows, number_of_columns, final_row_plot_num): 
    specs = [[{'type': 'polar'}]*number_of_columns]*number_of_rows
    if final_row_plot_num > 0:
        final_row = [{'type': 'polar'}]*final_row_plot_num
        final_row.extend([None]*(number_of_columns-final_row_plot_num))
        specs.append(final_row)
    return specs


def create_single_polar_plot(sequence: List[int], divisor: int, vertex_selection_method: str) -> go.Scatterpolar:
    d = len(set(sequence)) if vertex_selection_method == 'unique_values_in_set' else divisor
    return go.Scatterpolar(
        r = [3] * len(sequence),
        theta = [x*(360/d) for x in sequence],
        mode = 'markers+lines',
        line_color = 'blue',
        line_width = 1,
        marker_size = 2
    )


def create_empty_polar_plot() -> go.Scatterpolar:
    return go.Scatterpolar(
        r = [],
        theta = []
    )


def create_many_polar_plots(series: Series, vertex_selection_method: str, number_of_plots: int = 80, ) -> go.Figure:
    number_of_columns = 10
    number_of_rows, final_row_plot_num = divmod(number_of_plots, number_of_columns)
    fig = make_subplots(
        rows=number_of_rows+1 if final_row_plot_num>0 else number_of_rows,
        cols=number_of_columns,
        specs=create_subplot_specs(number_of_rows, number_of_columns, final_row_plot_num),
        subplot_titles=([str(i) for i in range(1,number_of_plots+1)])
    )
    divisor = 1
    for i in range(1, number_of_rows+1):
        for j in range(1, number_of_columns+1):
            sequence = series.get_mod_sequence(divisor=divisor)
            if sequence:
                fig.add_trace(
                    create_single_polar_plot(sequence, divisor, vertex_selection_method),
                    row = i,
                    col = j
                )
            divisor+=1
    if final_row_plot_num > 0:
        for j in range(1, final_row_plot_num+1):
            sequence = series.get_mod_sequence(divisor=divisor)
            if sequence:
                fig.add_trace(
                    create_single_polar_plot(sequence, divisor, vertex_selection_method),
                    row = number_of_rows+1,
                    col = j
                )
            divisor+=1

    fig.update_layout(
        template='simple_white',
        showlegend = False,
        margin_t = 40,
        margin_b = 0
    )
    fig.update_polars(
        angularaxis = dict(
            showline=True,
            ticks='',
            showticklabels=False,
            rotation = 90
        ),
        radialaxis = dict(
            showline = False,
            ticks='',
            showticklabels=False,
        )
    )
    return fig
