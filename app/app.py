from dash import Dash, html, dcc,Input, Output
import plotly.express as px
import pandas as pd

app = Dash(__name__, meta_tags=[{'name':'viewport', 'content':'width=device-width, height=device-height, initial-scale=1.0'}])
app.title = 'Carbon-Market analysis'

# assume you have a "long-form" data frame
# see https://plotly.com/python/px-arguments/ for more options
df = pd.read_csv("../data/carbon-market_and_co2-emissions.csv.zip")
df = df.drop(['Unnamed: 0'], axis=1)

def generate_table(dataframe, max_rows=10):
    return html.Table([
        html.Thead(
            html.Tr([html.Th(col) for col in dataframe.columns])
        ),
        html.Tbody([
            html.Tr([
                html.Td(dataframe.iloc[i][col]) for col in dataframe.columns
            ]) for i in range(min(len(dataframe), max_rows))
        ])
    ])


fig = px.scatter(
    df,
    x="year",
    y="credits_issued",
    color="region",
    hover_data=["co2_emitted", "credits_issued", "region"],
)


box_x_cols = ['voluntary_registry', 'arb_project', 'voluntary_status', 'scope', 'type', 'reduction_removal',
              'methodology_protocol', 'region', 'country', 'state', 'project_type', 'year']
box_x_cols.sort()
box_y_cols = ['credits_issued', 'credits_retired', 'registry_issued_credits', 'credits_remaining', 'co2_emitted']
box_y_cols.sort()

cols_names = ['credits_issued', 'credits_retired', 'registry_issued_credits', 'credits_remaining', 'co2_emitted']
cols_names.sort()
col_items = {i[0]: i[1] for i in list(zip(range(len(cols_names)), cols_names))}

def update_scatter_plot(y_value):
    return px.scatter(
        df,
        x="year",
        y=y_value,
        color="region"
    )

@app.callback(Output('scatter-graph', 'figure'), [Input('fig-drop-down', 'value')])
def slider_interaction(slider_val):
    if slider_val == 0:
        fig = update_scatter_plot(slider_val)
    else:
        fig = update_scatter_plot(slider_val)

    return fig


@app.callback(Output('box-graph', 'figure'),
              [Input('id-box-drop-down-x', 'value'),
               Input('id-box-drop-down-y', 'value'),
               Input('id-box-drop-down-semilogy', 'value')])
def slider_interaction(x_value='region', y_value='co2_emitted', semilogy=["SemiLogY"]):
    fig_box = px.box(df, x=x_value, y=y_value, height=600)
    if semilogy:
        fig_box.update_yaxes(type="log")
    return fig_box


app.layout = html.Div(
    children=[
        html.Header(children=[
            html.H1(children='Carbon-Market analysis'),
            html.Div(children='''Team 74''')
        ], style={
            'backgroundColor': '#EEEEEE',
            'flex': '1'}),

        html.Main(
            children=[
                html.Nav(children=[
                    dcc.Dropdown(options=box_x_cols,value='region',id='id-box-drop-down-x'),
                    dcc.Dropdown(options=box_y_cols,value='co2_emitted',id='id-box-drop-down-y'),
                    dcc.Checklist(options=["SemiLogY"], value=["SemiLogY"], id='id-box-drop-down-semilogy')

                ], style={ 'min-width': '200px'}),
                html.Article(dcc.Graph( id='box-graph', figure=slider_interaction()),
                             style={'height': '100%', 'flex': '70%'})
            ],
            style={
                'display': 'flex',
                'flex-direction': 'row',
                'flex': '70%',
                'margin': '10px',
                'backgroundColor': '#FFFF10'
            }),
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

