from dash import Dash, html, dcc,Input, Output
import plotly.express as px
import pandas as pd

from boxplot_analysis import BoxPlotAnalysis

app = Dash(__name__, meta_tags=[{'name':'viewport', 'content':'width=device-width, height=device-height, initial-scale=1.0'}])
app.title = 'Carbon-Market analysis'


# Load data frame
df = pd.read_csv("../data/carbon-market.csv.zip")
df2 = pd.read_csv("../data/merged_project_worldbank.csv.zip")
country_list = df2.country.unique()

# Load box_plot tab class manager
box_plot_analysis = BoxPlotAnalysis(df)


@app.callback(Output('line-plot', 'figure'),
              Input('checklist', 'value',))
def update_line_chart(countries=country_list):
    mask = df2.country.isin(countries)
    fig_line = px.line(df2[mask],
                       x='year',
                       y='CO2_emitted',
                       color='country',
                       title='CO2 emitted by country')
    return fig_line

@app.callback(box_plot_analysis.get_output(),box_plot_analysis.get_inputs())
def box_plot_analysis_slider_interaction(x_value='region', y_value='credits_issued', semilogy=["SemiLogY"]):
    return box_plot_analysis.boxplot_fig(x_value, y_value, semilogy)


app.layout = html.Div(
    children=[
        html.Header(children=[
            html.H1(children='Carbon-Market analysis'),
            html.Div(children='''Team 74''')
        ], style={
            'backgroundColor': '#EEEEEE',
            'flex': '1'}),
        html.Main(
            dcc.Tabs([
                dcc.Tab(label='Boxplot Analysis', children=box_plot_analysis.get_html_components()),
                dcc.Tab(label='CO2_emitted', children=[
                    dcc.Graph(id='line-plot', figure=update_line_chart()),
                    dcc.Checklist(
                        id='checklist',
                        options=country_list,
                        value=['United States'],
                        inline=True
                    )
                ]),
                dcc.Tab(label='Other 2'),
                dcc.Tab(label='Other 3')
            ],
            style={
                'display': 'flex',
                'flex-direction': 'row',
                'flex': '70%',
                'margin': '10px',
                'backgroundColor': '#FFFF10'
            })),
        html.Footer("DS4A0100",style={'backgroundColor': '#AAAAFF','flex': '1'})
    ],
    style={
        'display': 'flex',
        'flex-direction': 'column',
        'height': '100vh',
        'min-height': '100vh'
    })


if __name__ == '__main__':
    app.run_server(debug=True)

