import plotly.graph_objects as GOES


def blank_figure() -> go.Figure:
    fig = go.Figure(go.Scatter(x=[],y=[]))
    fig.update_layout(template=None),
    fig.update_xaxes(showgrid=False, showticklabels=False, zeroline=False)
    fig.update_yaxes(showgrid=False, scaleanchor='x', showticklabels=False, zeroline=False)
    return fig