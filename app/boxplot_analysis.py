import plotly.express as px
from dash import Output, Input, html, dcc


class BoxPlotAnalysis(object):
    def __init__(self, df):
        self.df = df

    def boxplot_fig(self, x_value='region', y_value='credits_issued', semilogy=["SemiLogY"]):
        fig_box = px.box(self.df, x=x_value, y=y_value, height=600)
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
        return [
            html.Nav(children=[
                dcc.Dropdown(
                    options=BoxPlotAnalysis.get_box_x_cols(),
                    value=BoxPlotAnalysis.get_box_x_cols()[0],
                    id='id-box-drop-down-x'),
                dcc.Dropdown(
                    options=BoxPlotAnalysis.get_box_y_cols(),
                    value=BoxPlotAnalysis.get_box_y_cols()[0],
                    id='id-box-drop-down-y'),
                dcc.Checklist(
                    options=["SemiLogY"],
                    value=["SemiLogY"],
                    id='id-box-drop-down-semilogy')
            ], style={ 'min-width': '200px'}),
            html.Article(dcc.Graph( id='box-graph', figure=self.boxplot_fig()),
                         style={'height': '100%', 'flex': '70%'})
        ]