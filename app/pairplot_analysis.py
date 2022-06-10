import plotly.express as px
from dash import Output, Input, html, dcc
import dash_bootstrap_components as dbc


class PairPlotAnalysis(object):
    def __init__(self, df):
        self.df = df

    def get_html_components(self):
        fig = px.scatter_matrix(self.df, title='PairPlot of carbon-market credits with co2 emissions')
        return html.Div(
            html.Article(dcc.Graph(id='pair-plot-graph',figure=fig),style={'flex': '90%'}),
            style={
                'display': 'flex',
                'flex-direction': 'row',
                'flex': '70%',
                'margin': '10px'
            })
