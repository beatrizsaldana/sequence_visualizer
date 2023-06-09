from dash import html, dcc
import dash_bootstrap_components as dbc

from global_files.app import app
from pages import polar_figure_layout, many_polar_figures_layout


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
                    'paddingTop':0,
                    'background-color':'#FFFFFF',
                    'border-color':'#FFFFFF',
                    'color':'grey'
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
                        dbc.Card(dbc.CardBody([many_polar_figures_layout.layout])),
                        label='Many Polar Figures',
                        className='tab-content',
                        tab_id='many_porlar_figures_tab',
                        label_style={'color': 'grey'}
                    ),
                    dbc.Tab(
                        dbc.Card(dbc.CardBody([polar_figure_layout.layout])),
                        label='Single Polar Figure',
                        className='tab-content',
                        tab_id='porlar_figure_tab',
                        label_style={'color': 'grey'}
                    )
                ],
                id='page_tabs',
                active_tab='many_porlar_figures_tab'
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
