from dash import Dash, html, dcc, Input, Output
import dash_bootstrap_components as dbc
import plotly.express as px
import pandas as pd

from co2_emitted_by_country import Co2EmittedByCountry
from boxplot_analysis import BoxPlotAnalysis

app = Dash(__name__,
           meta_tags=[{'name': 'viewport', 'content': 'width=device-width, height=device-height, initial-scale=1.0'}],
           external_stylesheets=[dbc.themes.CERULEAN])
app.title = 'Carbon-Market analysis'

# Load data frames
df = pd.read_csv("../data/carbon-market.csv.zip")
df_co2 = pd.read_csv("../data/merged_project_worldbank.csv.zip")

# Load plots tab class managers
box_plot_analysis = BoxPlotAnalysis(df)
co2_emitted_by_country = Co2EmittedByCountry(df_co2)


@app.callback(co2_emitted_by_country.get_output(), co2_emitted_by_country.get_input())
def update_line_chart(countries=co2_emitted_by_country.country_list):
    return co2_emitted_by_country.line_plot_fig(countries)


@app.callback(box_plot_analysis.get_output(), box_plot_analysis.get_inputs())
def box_plot_analysis_slider_interaction(x_value='region', y_value='credits_issued', semilogy=["SemiLogY"]):
    return box_plot_analysis.boxplot_fig(x_value, y_value, semilogy)


def get_tab_style():
    return {
        'display': 'flex',
        'flex-direction': 'row',
        'flex': '70%',
        'margin': '10px',
        'backgroundColor': '#FFFF10'
    }


app.layout = html.Div(
    children=[
        dbc.CardHeader(children=[
            html.H4(children='Carbon-Market analysis', className="card-title"),
            html.P(children='Team 74', className="card-text")
        ], style={
            'flex': '1',
            'max-height': '80px',
            'min-height': '80px'}),
        dbc.CardBody(
            dbc.Tabs([
                dbc.Tab(label='Boxplot Analysis', children=box_plot_analysis.get_html_components()),
                dbc.Tab(label='CO2_emitted', children=co2_emitted_by_country.get_html_components()),
                dbc.Tab(label='Other 2'),
                dbc.Tab(label='About Us')
            ])),
        dbc.CardFooter("Data Science For All DS4A - Colombia 2022", style={
            'flex': '1',
            'max-height': '50px',
            'min-height': '50px'})
    ]
    ,
    style={
        'display': 'flex',
        'flex-direction': 'column',
        'height': '100vh',
        'min-height': '100vh'
    }
    )

if __name__ == '__main__':
    app.run_server(debug=True)
