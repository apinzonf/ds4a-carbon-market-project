import plotly.express as px
from dash import Output, Input, html, dcc
import dash_bootstrap_components as dbc


class Co2EmittedByCountry(object):
    def __init__(self, df):
        self.df = df
        self.country_list = df.country.unique()

    def line_plot_fig(self, countries):
        mask = self.df.country.isin(countries)
        fig = px.line(self.df[mask],
                      x='year',
                      y='CO2_emitted',
                      color='country',
                      title='CO2 emitted by country',
                      height=540)
        return fig

    @staticmethod
    def get_output():
        return Output('line-plot', 'figure')

    @staticmethod
    def get_input():
        return Input('id-checklist-co2-line-plot', 'value')

    def get_html_components(self):
        return html.Div(
            children=[
                dbc.Nav(
                    children=
                    html.Div(children=[
                        dbc.FormText("Select countries"),
                        dcc.Dropdown(
                            id='id-checklist-co2-line-plot',
                            options=self.country_list,
                            value=['Colombia', 'China', 'United States'],
                            multi=True)
                    ],
                        style={
                            'min-width': '250px',
                            'max-width': '250px'
                        },
                        className="mb-4"
                    )
                ),
                dcc.Graph(
                    id='line-plot',
                    figure=self.line_plot_fig(self.country_list),
                    style={'height': '100%', 'flex': '70%'}
                )
            ],

            style={
                'display': 'flex',
                'flex-direction': 'row',
                'flex': '70%',
                'margin': '10px'
            })
