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
                        html.Ul(children=[
                            html.Li(html.P("""As a first approach to analysis, an artificial intelligence model based on the prediction of future time series was carried out. When performed in this way, the time series had different behaviors and did not yield a desirable value. For this reason, we decided to pass to the second stage of analysis. This second phase corresponds to the use of carbon credit data and CO2 emissions data, and by considering only these two variables, it is possible to predict that there is no improvement in the behavior of carbon emissions due to the issuance of carbon credits. We conclude that emissions are continuing growing although the credits issuance. """)),
                            html.Li(html.P("""Our analyses show that even if carbon credits mitigate in a certain way the amount of CO2 emitted, this activity does not have a great impact on the improvement of the global GHG emissions trend.""")),
                            html.Li(html.P("""Once it was discovered that the prediction showed a rising trend with no improvement, we proceeded with the third stage of analysis. It corresponds to reviewing the simulations and visualizations again but focusing our attention on the time series, this is another module that seeks to simulate future trends using the existing data of emissions observed (1992 - 2018). In this way, it was possible to understand why these trends could predict the increase of CO2 emissions. In this third stage of analysis, more data were used, including variables like GDP and the population of each country.""")),
                            html.Li(html.P("""By 2001 the uncertainty behind the performance of carbon credits did not allow the more emitting countries to standardize the carbon markets as a regulated instrument to reduce GHG emissions. At that moment the United States was at the top of the list. Later, in 2005, one of the hottest years globally and when climate change began to be a concern on the governments' agenda, carbon credits gained relevance as an international standard. At the same time, China was already beginning its trends of growing economy (according to 2005 GDP) and China became the largest contributor of CO2 emissions followed by the USA and India.""")),
                            html.Li(html.P("""In addition, the general understanding of carbon credits assumes that their purpose is to remove or eliminate CO2. Nevertheless in 2005  new GHG mitigation activities were created as a mixed category, including emissions reductions, removals and avoided emissions. This possibility of certifying avoided emissions as a consequence of the reduction of the deforestation rate creates doubts and concerns about the additionality and integrity of the credits resulting from these activities.""")),
                            html.Li(html.P("""In addition to these concerns, the projects with the biggest mitigation potential since 2010 are implementing mitigation activities related to the avoidance of emissions as result of reforestation activities. One of the most complex situations is that these activities are not sufficiently monitored and normally are implemented in countries where technical and technological capacities to monitor ecosystems are very poor. Therefore, the performance, quality and standardization of these activities cannot be guaranteed.""")),
                            html.Li(html.P("""From another point of view a positive trend could be identified in the reduction of GHG emissions of countries that started to implement mitigation projects in the non-conventional energies sector. For example, in the Berkeley database, the data for Ukraine reflects a behavior of quite high emissions but since 2018 (before the pandemic) this behavior begins to decrease. What has Ukraine done differently in this regard since 2018? Looking into the historical data of this country, it was possible to visualize that Ukraine reactivated the generation of energy through nuclear plants and left the energy sources with fossil fuels aside, managing to reduce its CO2 emissions.""")),
                            html.Li(html.P("""In this phase, what was carried out was an exploration of the countries that had outliers with a downward trend, evaluating their behavior and understanding the action they implemented to reduce emissions. If each country manages to find an outlier to reduce its net CO2 emissions they could make decisions in line with the global commitments in climate change. Apparently, countries and even carbon credits projects are not focusing their attention in attacking key emissions sources. """)),
                        ]),
                    ]),
                    html.Section(children=[
                        html.H5("Future Work", className="card-title"),
                        html.Ul(children=[
                            html.Li(html.P("""The analyses and artificial intelligence models developed by ANALITICO2 could be detailed at the level of specific sectors and mitigation activities according to national circumstances. The consideration of economic variables could inform better climate policies and could provide decision-makers with a better understanding of how carbon markets could be considered as realistic solutions.""")),
                            html.Li(html.P("""New regulatory instruments can be put in place to incentivize the generation of carbon credits in relevant sectors that could transform GHG emissions trends. """)),
                            html.Li(html.P("""Voluntary carbon markets are an instrument to motivate the private sector to transform their value chains, nevertheless, they need to move faster to a better carbon intensity performance. The use of carbon credits from nature-based approaches, mainly avoiding emissions, are not offering enough evidence to consider them as the preferent option of compensation.""")),
                            html.Li(html.P("""Deforestation is a huge problem for countries like Colombia, not only at the climate level but also in biodiversity and food security. Avoiding emissions from projects and programmes trying to reduce deforestation need to prove additionality, performance and environmental integrity of their contribution. Data science instruments should be considered as a source of solutions to strength monitoring capacities in Colombia."""))

                        ])
                    ])
                ]),

            ])]
        )
