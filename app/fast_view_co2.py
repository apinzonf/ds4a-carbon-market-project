import dash_bootstrap_components as dbc
import pandas as pd
import plotly.express as px
from dash import html, dcc
import plotly.io as pio
pio.templates.default = "simple_white"


class FastViewCo2(object):
    def __init__(self, data):
        self.df_co2 = data
        Un_Kt = 1000
        co2_country = data.groupby("name")['CO2'].sum()
        co2_country_acum = sum(co2_country)
        co2_country_df = pd.DataFrame(co2_country).reset_index()
        co2_country_df['% Representation'] = (co2_country_df['CO2'] / co2_country_acum) * 100
        co2_country_df['CO2'] = co2_country_df['CO2'] / Un_Kt
        co2_country_df = co2_country_df.sort_values(by='% Representation', ascending=False)

        co2_country_df['acumulado'] = co2_country_df['% Representation'].cumsum()
        co2_country_df = co2_country_df.reset_index()
        co2_country_df = co2_country_df

        ten_top = co2_country_df.iloc[10, 4]
        ten_top = str(f'{ten_top:.2f}' + '%')

        top_countries = list(co2_country_df['name'].head(8))
        g20_df = data[data['name'].isin(top_countries)]

        self.co2_country_df = co2_country_df
        self.ten_top = ten_top
        self.top_countries = top_countries
        self.g20_df = g20_df

    def get_fig_geo_co2(self):
        data = self.df_co2
        fig_geo_co2 = px.choropleth(data, locations='code',
                                    animation_frame='year',
                                    color='CO2',
                                    hover_name='name',
                                    color_continuous_scale='temps_r'
                                    )
        fig_geo_co2.update_layout(height=350)
        return fig_geo_co2

    def get_fig_countries_co2(self):
        fig_countries_co2 = px.area(self.g20_df.sort_values(by='CO2', ascending=False),
                                    x="year",
                                    y="CO2",
                                    color="name",
                                    line_group="name")
        fig_countries_co2.update_layout(height=350, )
        return fig_countries_co2

    def get_fig_pie_co2(self):
        fig_pie_co2 = px.pie(self.co2_country_df.head(10).sort_values(by='CO2', ascending=False),
                             values='% Representation', names='name',
                             hover_data=['name'], labels={'% Representation': '%'})
        fig_pie_co2.update_traces(textposition='inside', textinfo='label+value')
        return fig_pie_co2

    def get_fig_scatter(self):
        fig_scatter = px.scatter(
            self.df_co2, x='GDP', y='CO2',
            animation_frame='year',
            animation_group='CO2',
            size='pop',
            color='code_region',
            hover_name='name',
            log_x=True,
            range_x=[100, 100000],
            range_y=[100, 12000000]
        )
        return fig_scatter

    def get_fig_area_case_ukraine(self):
        case_ukraine = px.area(self.df_co2[self.df_co2['name'] == 'Ukraine'],
                               x="year",
                               y="CO2",
                               color="name",
                               line_group="name")
        return case_ukraine

    def get_html_components(self):
        return dbc.CardBody([
            dbc.Row([
                dbc.Col([html.Label("Overall view", className="align-middle")])],
                style={
                    "background-color": "#EEFFD6",
                    'height': '35px',
                    'border-radius': '5px',
                    'padding': '5px 0px',
                    'text-align': 'left'
                }
            ),
            dbc.Row([
                dbc.Col([dcc.Graph(id='id-geo-co2', figure=self.get_fig_geo_co2())], width=6),
                dbc.Col([dcc.Graph(id='id-area-country-co2', figure=self.get_fig_countries_co2())], width=6),
            ]),
            dbc.Row(
                [dbc.Col(html.Div('Comparative with other economics indicators'))],
                style={
                    "background-color": "#EEFFD6",
                    'height': '35px',
                    'border-radius': '5px',
                    'padding': '5px 0px',
                    'text-align': 'left',
                }
            ),
            dbc.Row([
                dbc.Col(
                    [
                        html.Label('% Emitions top ten', className='card-tittle'),
                        html.H4(self.ten_top)
                    ],
                    style={
                        'border-radius': '5px',
                        'margin-top': '30px',
                        'padding': '30px 0 0 30px'
                    },
                    width=2),
                dbc.Col(
                    [
                        dcc.Graph(
                            id='id-pie-co2',
                            config={'displayModeBar': False},
                            figure=self.get_fig_pie_co2())
                    ],
                    width=4),
                dbc.Col(
                    [
                        dcc.Graph(
                            id='id-scatter-co2',
                            config={'displayModeBar': False},
                            figure=self.get_fig_scatter())
                    ],
                    width=6),
            ]),
            dbc.Row([
                dbc.Col(html.Div('Case Ukraine'),)],
                style={
                    "background-color": "#EEFFD6",
                    'height': '35px',
                    'border-radius': '5px',
                    'padding': '5px 0px',
                    'text-align': 'left',
                }
            ),
            dbc.Row(
                [
                    dbc.Col(
                        [
                            dcc.Graph(
                                id='id-area-case-ukraine',
                                config={'displayModeBar': False},
                                figure=self.get_fig_area_case_ukraine())
                        ],
                        width=12),
            ]),
        ])