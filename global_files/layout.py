from dash import html, dcc
import dash_bootstrap_components as dbc

from global_files.app import app
from pages import polar_figure_layout


def serve_layout():
    dashboard_title = html.Div(
        [
            html.H4('Sequence Visualizer', style={'display': 'inline-block'}),
            dbc.Button(
                '\u24d8',
                id = 'information_button',
                size = 'lg',
                style = {
                    'display': 'inline-block',
                    'paddingTop':0
                }
            )
        ]
    )

    information_modal = html.Div(
        dbc.Modal(
            [
                dbc.ModalHeader(dbc.ModalTitle('\u24d8 Dashboard Information')),
                dbc.ModalBody(
                    [
                        html.P("USER INFORMATION GOES HERE")
                    ]
                )
            ],
            id='information_modal',
            scrollable=True,
            size='xl',
            is_open=False
        )
    )

    content_tabs = html.Div(
        [
            dbc.Tabs(
                [
                    dbc.Tab(
                        dbc.Card(dbc.CardBody([polar_figure_layout.layout])),
                        label='Polar Figure',
                        className='tab-content',
                        tab_id='porlar_figure_tab',
                    )
                ],
                id='page_tabs',
                active_tab='porlar_figure_tab'
            )
        ]
    )

    store_components = html.Div(
        [
            dcc.Store(id='tmp', data=None)
        ]
    )

    return html.Div(
        [
            dashboard_title,
            information_modal,
            content_tabs,
            store_components
        ]
    )


app.layout = serve_layout()
