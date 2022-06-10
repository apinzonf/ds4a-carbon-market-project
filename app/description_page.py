import dash_bootstrap_components as dbc
from dash import Output, Input, html, dcc


class DescriptionPage(object):
    @staticmethod
    def get_html_components():
        return dbc.CardBody([
            html.H4("Analyzing Carbon Market Data", className="card-title"),
            html.Div(children=[
                html.Article(children=[
                    html.Section(children=[
                        html.H5("Business Problem", className="card-title"),
                        html.P(
"""The PNUMA – Programa de Las Naciones Unidas para el Medio Ambiente look forward to increase confidence in carbon markets from a data analysis perspective considering the growing uncertainty regarding transparency in the generation of carbon credits.
                            
There is a high diversity of projects that search to achieve voluntary objectives through the implementation of emission reduction actions in various sectors of the economy, from the forestry sector to public transportation. This diversity of actors and methodologies used bring uncertainty to the companies that buy them, the civil society and the authorities.
        
The carbon markets have been developed in a mainly voluntary way (goals for reducing and offsetting emissions from companies that voluntarily decide to buy carbon credits for corporate social responsibility and to demonstrate some type of commitment to offsetting their emissions), which means that carbon markets are not standardized and those are very different from each other and it is difficult to account for their robustness.
        """,
                            className="card-text", style={'white-space': 'pre-wrap'}
                        )
                    ]),
                    html.Section(children=[
                        html.H5("Business Impact", className="card-title"),
                        html.P(
"""The impact of this analysis is to know if the generation of carbon credits in the voluntary market has effectively contributed to changing the emission trajectories in the countries that host the projects and if the differentiation of the projects could explain the quality or robustness of the projects. The questions we will solve with this analysis are as follow:
                                    """,className="card-text", style={'white-space': 'pre-wrap'}),
                        html.Ol(children=[
                            html.Li(html.P('In which sectors do carbon credits have a greater, lesser or no impact?')),
                            html.Li(html.P('Is there a relationship between the issuance of carbon credits and greenhouse gas emissions?')),
                            html.Li(html.P('In which regions, sectors or countries it is possible to see a better understanding of the impact?'))
                        ])
                    ])
                ]),

            ])]
        )