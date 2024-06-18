import plotly.graph_objects as go
from dash import Input, Output

from assets.config import KNOWN_SERIES

def blank_figure() -> go.Figure:
    fig = go.Figure(go.Scatter(x=[],y=[]))
    fig.update_layout(template=None),
    fig.update_xaxes(showgrid=False, showticklabels=False, zeroline=False)
    fig.update_yaxes(showgrid=False, scaleanchor='x', showticklabels=False, zeroline=False)
    return fig

def create_options():
    return [{'label': x.capitalize(), 'value': x} for x in KNOWN_SERIES]
