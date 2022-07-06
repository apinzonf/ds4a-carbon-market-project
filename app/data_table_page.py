import dash_bootstrap_components as dbc
from dash import Output, Input, html, dcc


class DataTablePage(object):
    def __init__(self, df):
        self.df = df

    def generate_table(self, max_rows=20):
        dataframe = self.df
        return dbc.Table([
            html.Thead(
                html.Tr([html.Th(col) for col in dataframe.columns])
            ),
            html.Tbody([
                html.Tr([
                    html.Td(dataframe.iloc[i][col]) for col in dataframe.columns
                ]) for i in range(min(len(dataframe), max_rows))
            ])
        ])

    def get_html_components(self):
        return self.generate_table()
