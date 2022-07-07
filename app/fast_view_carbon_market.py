import dash_bootstrap_components as dbc
import plotly.express as px
import plotly.graph_objects as go
import plotly.io as pio
import pycountry
from dash import Output, Input, html, dcc

pio.templates.default = "simple_white"


def get_code(loc):
    try:
        return pycountry.countries.get(name=loc).alpha_3
    except:
        return None


class FastViewForCarbonMarket(object):
    def __init__(self, df):
        self.df = df
        self.df = df
        self.country_list = df.country.unique()
        self.scope_list = df.scope.unique()
        self.project_list = df.project_type.unique()
        self.reduction_list = df.reduction_removal.unique()

    def callback_update_fig_countries(self, credit='credits_issued'):
        df_credits = self.df.groupby(["year", 'country'])[credit].sum().reset_index()
        df_credits['code'] = df_credits['country'].apply(lambda x: get_code(x))

        countries_names_selection = ['United States', 'China', 'Germany', 'India', 'Brazil', 'Mexico', 'Argentina',
                                     'Peru', 'Colombia']
        df_selected = df_credits[df_credits['country'].isin(countries_names_selection)]

        countries_df_list = [df_selected[df_selected['country'] == country_name] for country_name in
                             countries_names_selection]
        country_go_scatters = []
        for index in range(len(countries_names_selection)):
            df_country = countries_df_list[index]
            country_name = countries_names_selection[index]
            country_scatter = go.Scatter(mode='lines', name=country_name, line=dict(width=1.5), stackgroup='one',
                                         x=df_country['year'][:2],
                                         y=df_country[credit][:2])
            country_go_scatters.append(country_scatter)

        frames_data_list = []
        for time_frame in range(1, len(countries_df_list[0]) - 1):
            country_data_list = []
            for df_country in countries_df_list:
                country_data = dict(type='scatter', x=df_country['year'][:time_frame + 1],
                                    y=df_country[credit][:time_frame + 1])
                country_data_list.append(country_data)
            frames_data = dict(data=country_data_list, traces=list(range(len(countries_df_list))))
            frames_data_list.append(frames_data)

        layout = go.Layout(title='trend', height=350, hovermode='x unified', updatemenus=[
            dict(type='buttons', y=-0.33, x=-0.1, xanchor='left', yanchor='bottom', pad=dict(t=0, r=10),
                 buttons=[
                     dict(label='Play', method='animate', args=[
                         None,
                         dict(frame=dict(duration=500, redraw=False), transition=dict(duration=0), fromcurrent=True,
                              mode='immediate')])
                 ]),
            dict(type="buttons", y=-0.15, x=0.15, xanchor='left', yanchor='top', pad=dict(t=0, r=10), direction="left",
                 buttons=[
                     dict(args=[{"yaxis.type": "linear"}], label="linear", method="relayout"),
                     dict(args=[{"yaxis.type": "log"}], label="log", method="relayout")
                 ]),
        ])
        layout.update(xaxis=dict(range=['1996', '2020'], autorange=False),
                      yaxis=dict(range=[0, 120000000], autorange=False))

        fig_countries = go.Figure(data=country_go_scatters, frames=frames_data_list, layout=layout)

        fig_geo = px.choropleth(df_credits,
                                locations='code',
                                animation_frame='year',
                                color=credit,
                                hover_name='country',
                                color_continuous_scale='temps_r')
        fig_geo.update_layout(height=350, )

        return {
            'id-out-fvcm-country-chart': fig_countries,
            'id-out-fvcm-geo-chart': fig_geo
        }



    def callback_update_get_figures(self, country='Colombia', type_analysis='scope', credit='credits_issued'):
        df_country = self.df[self.df['country'] == country]
        selection = df_country.groupby(['year', type_analysis]).sum().reset_index().sort_values(by='year')

        credit_by_selection = (sum(df_country.groupby(['country'])[credit].sum())) / 1000000
        credit_by_selection = f'{credit_by_selection:.2f}' + 'M Tons'

        projects_by_selection = sum(df_country.groupby(['country'])[credit].count())

        fig_pie = px.pie(selection, values=credit, names=type_analysis, title='pie chart')
        fig_pie.update_layout(legend_x=-0.3, legend_y=-0.4, height=400)

        fig_bar = px.bar(selection, x='year', y=credit, color=type_analysis)
        fig_bar.update_layout(showlegend=False, height=300)

        simulation = px.bar(
            selection, x=type_analysis, y=credit,
            animation_frame='year',
            animation_group=type_analysis,
            color=type_analysis,
            hover_name=type_analysis,
            range_y=[0, 10000000],
            title='behavior of scope by type of projects')
        simulation.update_layout(showlegend=False)

        return {
            'id-out-fvcm-pie-chart': fig_pie,
            'id-out-fvcm-bar-chart': fig_bar,
            'id-out-fvcm-simulation': simulation,
            'id-out-fvcm-num-credits': credit_by_selection,
            'id-out-fvcm-num-projects': projects_by_selection
        }

    def callback_of_components_by_id(self, country='Colombia', type_analysis='scope', credit='credits_issued'):
        response = self.callback_update_fig_countries(credit)
        response.update(self.callback_update_get_figures(country, type_analysis, credit))
        response
        return response

    def callback(self, country='Colombia', type_analysis='scope', credit='credits_issued'):
        response = self.callback_of_components_by_id(country, type_analysis, credit)
        return [response[key] for key in response]

    @staticmethod
    def get_output():
        return [Output('id-out-fvcm-country-chart', 'figure'),
                Output('id-out-fvcm-geo-chart', 'figure'),
                Output('id-out-fvcm-pie-chart', 'figure'),
                Output('id-out-fvcm-bar-chart', 'figure'),
                Output('id-out-fvcm-simulation', 'figure'),
                Output('id-out-fvcm-num-credits', 'children'),
                Output('id-out-fvcm-num-projects', 'children')]

    @staticmethod
    def get_inputs():
        return [Input('id-in-fvcm-country', 'value'),
                Input('id-in-fvcm-analysis', 'value'),
                Input('id-in-fvcm-credits', 'value'), ]

    @staticmethod
    def get_credits():
        type_credits = ['credits_issued', 'credits_retired', 'registry_issued_credits', 'credits_remaining']
        type_credits.sort()
        return type_credits

    @staticmethod
    def get_analysis():
        analysis = ['voluntary_status', 'scope', 'type', 'reduction_removal', 'methodology_protocol', 'project_type']
        analysis.sort()
        return analysis

    def get_html_components(self):
        return dbc.CardBody(
            [
                dbc.Row([dbc.Col([html.Label("Overall view", className="align-middle")])],
                        style={"background-color": "#EEFFD6",
                               'height': '35px', 'border-radius': '5px', 'padding': '5px 0px', 'text-align': 'left', }
                        ),
                dbc.Row([
                    dbc.Col([dcc.Graph(
                        id='id-out-fvcm-geo-chart',
                        config={},
                        figure=self.callback_of_components_by_id()['id-out-fvcm-geo-chart']
                    )], width=6),
                    dbc.Col([dcc.Graph(
                        id='id-out-fvcm-country-chart',
                        config={},
                        figure=self.callback_update_fig_countries()['id-out-fvcm-country-chart']
                    )], width=6),
                ]),
                dbc.Row([dbc.Col(html.Div("Custom visualization"))],
                        style={"background-color": "#EEFFD6",
                               'height': '35px', 'border-radius': '5px', 'padding': '5px 0px', 'text-align': 'left', }
                        ),
                dbc.Row([
                    dbc.Col([html.Label('country', className='card-tittle'),
                             dcc.Dropdown(
                                 [x for x in sorted(self.country_list)],
                                 value='Colombia',
                                 id='id-in-fvcm-country'),
                             html.Label('type analysis', className='card-tittle'),
                             dcc.Dropdown(
                                 options=FastViewForCarbonMarket.get_analysis(),
                                 value='scope',
                                 id="id-in-fvcm-analysis"),
                             html.Label('Type credits', className='card-tittle'),
                             dcc.Dropdown(
                                 options=FastViewForCarbonMarket.get_credits(),
                                 value=FastViewForCarbonMarket.get_credits()[0],
                                 id='id-in-fvcm-credits'),
                             ],
                            style={'width': '224px', 'background-color': '##EEFFD6', 'border-radius': '5px',
                                   'margin-top': '50px', 'margin-bottom': '10px'},
                            width="300px"),
                    dbc.Col([
                        html.Label('Number of credits', className='card-tittle'),
                        html.H4(
                            children=self.callback_of_components_by_id()['id-out-fvcm-num-credits'],
                            id='id-out-fvcm-num-credits'
                        ),
                        html.Label('Number of projects', className='card-tittle'),
                        html.H4(
                            children=self.callback_of_components_by_id()['id-out-fvcm-num-projects'],
                            id='id-out-fvcm-num-projects'
                        )],
                        style={'border-radius': '5px', 'margin-top': '50px', 'padding': '41px 0 0 62px'},
                        width=3),
                    dbc.Col([
                        dcc.Graph(
                            id='id-out-fvcm-bar-chart',
                            config={'displayModeBar': False},
                            figure=self.callback_of_components_by_id()['id-out-fvcm-bar-chart']
                        )
                    ], width=6),
                ]),
                dbc.Row([dbc.Col([html.Label("Visualization by country", className="align-middle")])],
                        style={"background-color": "#EEFFD6",
                               'height': '35px', 'border-radius': '5px', 'padding': '5px 0px', 'text-align': 'left'}
                        ),
                dbc.Row([
                    dbc.Col([
                        dcc.Graph(
                            id='id-out-fvcm-pie-chart',
                            config={'displayModeBar': False},
                            figure=self.callback_of_components_by_id()['id-out-fvcm-pie-chart']
                        )
                    ],
                        width=5),
                    dbc.Col([
                        dcc.Graph(
                            id='id-out-fvcm-simulation',
                            config={'displayModeBar': False},
                            figure=self.callback_of_components_by_id()['id-out-fvcm-simulation']
                        )
                    ], width=7)
                ])
            ])
