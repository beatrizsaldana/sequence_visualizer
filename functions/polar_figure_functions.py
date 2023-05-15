import plotly.graph_objects as go
from typing import List
import pandas as pd


def create_polar_plot(sequence: List[int]):
    fig = go.Figure()
    fig.add_trace(go.Scatterpolar(
        r = [3] * len(sequence),
        theta = [x*(360/len(set(sequence))) for x in sequence],
        mode = 'markers+lines',
        name = 'Test',
        line_color = 'violet'
    ))
    fig.update_layout(
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
    )
    return fig

