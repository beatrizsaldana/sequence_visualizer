import dash
import dash_bootstrap_components as dbc
from layout import serve_layout

app = dash.Dash(__name__, external_stylesheets = [dbc.themes.BOOTSTRAP])

server = app.server

app.layout = serve_layout()

if __name__ == '__main__':
    app.run_server(debug=True)
