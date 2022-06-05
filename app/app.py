import logging

from dash import Dash, callback, html, dcc, dash_table, Input, Output, State, MATCH, ALL  # , ClientsideFunction
import dash_bootstrap_components as dbc

import plotly.express as px
import pandas as pd
import json
import os
import pickle

from version import get_version

df = pd.read_csv("data/carbon-market_and_co2-emmisions.csv", sep=",")

# Create the Scatter_fig
Scatter_fig = px.scatter(
    df,
    x="co2_emitted",
    y="credits_issued",
    color="region",
    hover_data=["co2_emitted", "credits_issued", "region"],
)
Scatter_fig.update_layout(
    title="CO2 emitted vs. credits issued by region", paper_bgcolor="#F8F9F9"
)

################################################################################################
# Create the app
################################################################################################
request_path_prefix = None
workspace_user = os.getenv('JUPYTERHUB_USER')  # Get DS4A Workspace user name
if workspace_user:
    request_path_prefix = '/user/' + workspace_user + '/proxy/8050/'

app = Dash(__name__, requests_pathname_prefix='/carbon/', external_stylesheets=[dbc.themes.FLATLY],
           meta_tags=[{'name': 'viewport', 'content': 'width=device-width, initial-scale=1.0'}])

################################################################################################
# Create Layout
################################################################################################
app.layout = html.Div([
    html.H2("US Sales Map", id='title'),  # Creates the title of the app
    dcc.Graph(figure=Scatter_fig, id='main-figure'),
    dcc.Slider(min=0, max=1, marks={0: 'US Map', 1: 'Scatter Plot'}, value=0, id='fig-slider', )
])


@app.callback(Output('main-figure', 'figure'), [Input('fig-slider', 'value')])
def slider_interaction(slider_val):
    if slider_val == 0:
        fig = Scatter_fig
    else:
        fig = Scatter_fig

    return fig


logger = logging.getLogger()
logger.setLevel(logging.INFO)

if __name__ == "__main__":
    logger.info(f'Carbon-Market web application dsf4-carbon-market version: [{get_version()}] started')
    app.run_server(port='8050', debug=True)

logger.info(f'Carbon-Market web application dsf4-carbon-market version: [{get_version()}] started')
app.run_server(host='0.0.0.0', port='8050', debug=True)
