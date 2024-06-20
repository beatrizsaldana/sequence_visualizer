from dash import html, dcc
import dash_bootstrap_components as dbc

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
                        dcc.Markdown('''
                            This is a visualization of the repeating patterns that arise when dividing every number of a series by an integer and then taking the remainder. For example, if we look at the fibonacci sequence:
                            ```
                            0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765, 10946, 17711, ...
                            ```
                            and divide each number by `3` and capture the remainder, we get :
                            ```
                            0, 1, 1, 2, 0, 2, 2, 1, 0, 1, 1, 2, 0, 2, 2, 1, 0, 1, 1, 2, 0, 2, 2, 1, ...
                            ```
                            The repeating sequence here is `0, 1, 1, 2, 0, 2, 2, 1`.

                            The polar figure will then display this pattern by drawing a line between each of the numbers. In this case it will place the `0` at the `0,360` position on the circle, and `1` at the `120` position and the `2` at the `240` position. All equidistant from eachother.
                        ''')
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
                        tab_id='polar_figure_tab',
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
            dcc.Store(id='repeating_sequence_single_polar', data=None)
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
