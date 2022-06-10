import dash_bootstrap_components as dbc
from dash import Output, Input, html, dcc


class ReportPage(object):
    @staticmethod
    def get_html_components():
        return dbc.CardBody([
            html.H4("Report for Carbon Market Data", className="card-title"),
            html.Div(children=[
                html.Article(children=[
                    html.Section(children=[
                        html.H5("Conclusions", className="card-title"),
                        html.P(
"""The carbon markets have been developed in a mainly voluntary way (goals for reducing and offsetting emissions from companies that voluntarily decide to buy carbon credits for corporate social responsibility and to demonstrate some type of commitment to offsetting their emissions), which means that carbon markets are not standardized and those are very different from each other and it is difficult to account for their robustness.
Sectorized analysis of the carbon credit market
Comparison with the carbon emission according to the sample we take

ToDo""",
                            className="card-text", style={'white-space': 'pre-wrap'}
                        )
                    ]),
                ]),

            ])]
        )
