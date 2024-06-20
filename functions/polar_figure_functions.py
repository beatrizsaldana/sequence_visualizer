import plotly.graph_objects as go
from typing import List
import pandas as pd


def create_polar_plot(sequence: List[int], vertex_selection_method: str, divisor: int) -> go.Figure:
    d = len(set(sequence)) if vertex_selection_method == 'unique_values_in_set' else divisor
    r_dataset = [3] * len(sequence)
    theta_dataset = [x*(360/d) for x in sequence]
    fig_layout = go.Layout(
        title={'text': str(divisor), 'x': 0.5, 'xanchor': 'center'},
        updatemenus=[dict(
            type="buttons",
            buttons=[{
                "label": "Play",
                "method": "animate",
                "args": [None]
            }]
        )],
        template='simple_white',
        showlegend = False,
        polar = dict(
            angularaxis = dict(
                showline=False,
                ticks='',
                showticklabels=False,
                rotation = 90,
                direction = "clockwise"
            ),
            radialaxis = dict(
                showline = False,
                ticks='',
                showticklabels=False,
            )
        ),
        margin_t = 40,
        margin_b = 0
    )

    fig = go.Figure(
        data=[go.Scatterpolar(
            r = r_dataset,
            theta = theta_dataset[0:2],
            mode = 'markers+lines',
            line_width = 3,
            marker_size = 6
        )],
        layout=fig_layout,
        frames=[go.Frame(
            data=[go.Scatterpolar(
                r = r_dataset,
                theta = theta_dataset[0:x],
                mode = 'markers+lines',
                line_width = 3,
                marker_size = 6
            )]
        ) for x in range(2, len(theta_dataset)+1)]
    )

    return fig

