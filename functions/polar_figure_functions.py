import plotly.graph_objects as go
from typing import List
import pandas as pd


def create_polar_plot(sequence: List[int], divisor: int) -> go.Figure:
    fig = go.Figure()
    fig.add_trace(go.Scatterpolar(
        r = [3] * len(sequence),
        theta = [x*(360/len(set(sequence))) for x in sequence],
        mode = 'markers+lines',
        name = 'Test',
        line_color = 'blue'
    ))
    fig.update_layout(
        title={'text': str(divisor), 'x': 0.5, 'xanchor': 'center'},
        template='simple_white',
        showlegend = False,
        polar = dict(
            angularaxis = dict(
                showline=False,
                ticks='',
                showticklabels=False,
                rotation = 90
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
    return fig

