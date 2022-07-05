from dash import Dash, html, dcc, Input, Output
import dash_bootstrap_components as dbc
import plotly.express as px
import pandas as pd
import pycountry

from app.about_us_page import AboutUsPage
from app.data_table_page import DataTablePage
from app.description_page import DescriptionPage
from app.co2_emitted_by_country import Co2EmittedByCountry
from app.boxplot_analysis import BoxPlotAnalysis
from app.pairplot_analysis import animations
from app.report_page import ReportPage

app = Dash(__name__,
           meta_tags=[{'name': 'viewport', 'content': 'width=device-width, height=device-height, initial-scale=1.0'}],
           external_stylesheets=[dbc.themes.CERULEAN])
app.title = 'Carbon-Market analysis'
app._favicon = ("carbon_market.ico")

# Load data frames
df = pd.read_csv("data/carbon-market.csv.zip")
df_co2 = pd.read_csv("data/merged_project_worldbank.csv.zip")

# Load page managers
carbon_market_data_table_page = DataTablePage(df)
co2_data_table_page = DataTablePage(df_co2)
box_plot_analysis = BoxPlotAnalysis(df)
co2_emitted_by_country = Co2EmittedByCountry(df_co2)
pair_plot_analysis = PairPlotAnalysis(df_co2)
about_us_page = AboutUsPage(app)


@app.callback(co2_emitted_by_country.get_output(), co2_emitted_by_country.get_input())
def update_line_chart(countries=co2_emitted_by_country.country_list):
    return co2_emitted_by_country.line_plot_fig(countries)


@app.callback(box_plot_analysis.get_output(), box_plot_analysis.get_inputs())
def box_plot_analysis_slider_interaction(x_value='region', y_value='credits_issued', semilogy=["SemiLogY"]):
    return box_plot_analysis.boxplot_fig(x_value, y_value, semilogy)

@app.callback(animations.get_output(), animations.get_inputs())
def simulation_interaction( countries  = animations.country_list, type_analysis = 'scope', credit = 'credits_issued'):    
    return animations.graphics( countries, type_analysis, credit )


def get_tab_style():
    return {
        'display': 'flex',
        'flex-direction': 'row',
        'flex': '70%',
        'margin': '10px',
        'backgroundColor': '#FFFF10'
    }


app.layout = dbc.Container(
    children=[
        dbc.CardHeader(children=[
            dbc.Row([
                dbc.Col([
                    html.H4(children='Carbon-Market analysis', className="card-title"),
                    html.P(children='Team 74', className="card-text")
                ]),
                dbc.Col(
                    dbc.CardImg(
                        src=app.get_asset_url("header_background.png"),
                        style={
                            "opacity": 0.9,
                            'max-height': '100px',
                            'min-height': '100px',
                            'max-width': '278px',
                            'min-width': '278px'
                        },
                    ),
                    style={
                        'text-align': 'right'
                    })
            ])
        ]),
        dbc.CardBody(
            dbc.Tabs([
                dbc.Tab(label='Carbon Market', children=DescriptionPage.get_html_components()),
                dbc.Tab(label='Data carbon-market', children=carbon_market_data_table_page.get_html_components(),
                        style={
                            'margin-top': '2%',
                            'height': '80vh',
                            'overflow': 'scroll'
                        }),
                dbc.Tab(label='Data CO2', children=co2_data_table_page.get_html_components(),
                        style={
                            'margin-top': '2%'
                        }),
                dbc.Tab(label='Boxplot Analysis', children=box_plot_analysis.get_html_components()),
                dbc.Tab(label='CO2_emitted', children=co2_emitted_by_country.get_html_components()),
                dbc.Tab(label='Pair Plot Analysis', children=pair_plot_analysis.get_html_components()),
                dbc.Tab(label='Report', children=ReportPage.get_html_components()),
                dbc.Tab(label='About Us', children=about_us_page.get_html_components())
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
    app.run(host="0.0.0.0", port="8050")
