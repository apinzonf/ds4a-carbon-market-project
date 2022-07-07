import plotly.express as px
from dash import Output, Input, html, dcc
import dash_bootstrap_components as dbc


class Projections(object):
    def __init__(self, global_projections, colombia_projections):
        self.global_projections = global_projections
        self.colombia_projections = colombia_projections

    def line_plot_fig_global(self):
        fig = px.line(self.global_projections,
                      x='year',
                      y='CO2_emmited_kt',
                      color='prediction',
                      title='Global CO2 projection',
                      height=540)
        return fig

    def line_plot_fig_col(self):
        fig = px.line(self.colombia_projections,
                      x='year',
                      y='CO2_emmited_kt',
                      color='prediction',
                      title='Colombia CO2 projection',
                      height=540)
        return fig

    def get_html_components(self):
        return dbc.CardBody([
            html.H4("CNN LSTM model projection", className="card-title"),

            html.Div([
                html.Div([
                    html.Div([
                        html.H3('Column 1'),
                        dcc.Graph(
                            id='line-plot',
                            figure=self.line_plot_fig_global(),
                            style={'height': '100%', 'flex': '70%'}
                        )
                    ], className="six columns"),

                    html.Div([
                        html.H3('Column 2'),
                        dcc.Graph(
                            id='line-plot',
                            figure=self.line_plot_fig_col(),
                            style={'height': '100%', 'flex': '70%'}
                        )
                    ], className="six columns"),
                ], className="row")
            ])

        ])
