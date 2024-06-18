from dash import Input, Output, callback


@callback(
    Output('information_modal', 'is_open'),
    [
        Input('information_button', 'n_clicks'),
    ],
    prevent_initial_call=True,
)
def open_information_modal(n_clicks):
    if n_clicks:
        return True
