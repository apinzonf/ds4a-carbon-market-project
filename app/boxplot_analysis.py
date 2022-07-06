import plotly.express as px
from dash import Output, Input, html, dcc
import dash_bootstrap_components as dbc


class BoxPlotAnalysis(object):
    def __init__(self, df):
        self.df = df

    def boxplot_fig(self, x_value='region', y_value='credits_issued', semilogy=["SemiLogY"]):
        fig_box = px.box(self.df,
                         x=x_value,
                         y=y_value,
                         title=f"Boxplot of {y_value} by {x_value}",
                         height=540)
        if semilogy:
            fig_box.update_yaxes(type="log")
        return fig_box

    @staticmethod
    def get_output():
        return Output('box-graph', 'figure')

    @staticmethod
    def get_inputs():
        return [Input('id-box-drop-down-x', 'value'),
                Input('id-box-drop-down-y', 'value'),
                Input('id-box-drop-down-semilogy', 'value')]

    @staticmethod
    def get_box_x_cols():
        box_x_cols = ['voluntary_registry', 'arb_project', 'voluntary_status', 'scope', 'type', 'reduction_removal',
                      'methodology_protocol', 'region', 'country', 'state', 'project_type', 'year']
        box_x_cols.sort()
        return box_x_cols

    @staticmethod
    def get_box_y_cols():
        box_y_cols = ['credits_issued', 'credits_retired', 'registry_issued_credits', 'credits_remaining']
        box_y_cols.sort()
        return box_y_cols

    def get_html_components(self):
        return dbc.CardBody([
            html.H4("Analyzing Carbon Market Data", className="card-title", 
                    style = {}),
            html.Div(
                children=[
                html.Article(
                    children=[
                    html.Section(children=[
                        html.Br(),
                        html.H5("Interactive graph", className="card-title"),
                        html.P( """In this section you can interactive with the diferent variables, only select the categories for the axis x and the numerical variables in the second input of the form""", 
                               className="card-text", style={'white-space': 'pre-wrap',
                                                             'padding':'10px',
                                                             "background-color": "#fafafa" }
                              )
                        ])
                ])
            ]), 
            html.Div(
                    children=[
                        dbc.Nav(children=[
                            html.Div(children=[
                                dbc.FormText("Select category for x axis"),
                                dcc.Dropdown(
                                    options=BoxPlotAnalysis.get_box_x_cols(),
                                    value=BoxPlotAnalysis.get_box_x_cols()[0],
                                    id='id-box-drop-down-x')],
                                className="mb-4"
                            ),
                            html.Div(children=[
                                dbc.FormText("Select numerical data for y axis"),
                                dcc.Dropdown(
                                    options=BoxPlotAnalysis.get_box_y_cols(),
                                    value=BoxPlotAnalysis.get_box_y_cols()[0],
                                    id='id-box-drop-down-y')],
                                className="mb-4"
                            ),
                            html.Div(children=[
                                dbc.FormText("Plot log scaling on the y axis"),
                                dcc.Checklist(
                                    options=["SemiLogY"],
                                    value=["SemiLogY"],
                                    id='id-box-drop-down-semilogy')],
                                className="mb-4")
                        ], style={
                            'min-width': '250px',
                            'padding': '1rem 2rem 1rem 1rem'
                        },
                            vertical="md"),
                        html.Article(dcc.Graph(id='box-graph', figure=self.boxplot_fig()),
                                     style={'height': '100%', 'flex': '70%'}
                                     )
                    ],
                    style={
                        'display': 'flex',
                        'flex-direction': 'row',
                        'flex': '70%',
                        'margin': '10px'
                    })
        ])
        return
