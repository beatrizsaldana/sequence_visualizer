import plotly.graph_objects as go
from dash import Input, Output
from typing import List, Dict

def blank_figure() -> go.Figure:
    fig = go.Figure(go.Scatter(x=[],y=[]))
    fig.update_layout(template=None),
    fig.update_xaxes(showgrid=False, showticklabels=False, zeroline=False)
    fig.update_yaxes(showgrid=False, scaleanchor='x', showticklabels=False, zeroline=False)
    return fig


def create_options(list_of_options: List[str]) -> List[Dict[str,str]]:
    return [{'label': x.replace('_', ' ').capitalize(), 'value': x} for x in list_of_options]
