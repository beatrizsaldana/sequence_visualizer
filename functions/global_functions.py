import plotly.graph_objects as go
from global_files.app import app
from dash import Input, Output


def blank_figure() -> go.Figure:
    fig = go.Figure(go.Scatter(x=[],y=[]))
    fig.update_layout(template=None),
    fig.update_xaxes(showgrid=False, showticklabels=False, zeroline=False)
    fig.update_yaxes(showgrid=False, scaleanchor='x', showticklabels=False, zeroline=False)
    return fig


@app.callback(
    Output('information_modal', 'is_open'),
    [
        Input('information_button', 'n_clicks')
    ],
    prevent_initial_call=True
)
def open_information_modal(information_button_click):
    return True

