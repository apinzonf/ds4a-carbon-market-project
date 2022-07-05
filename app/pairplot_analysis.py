import plotly.express as px
from dash import Output, Input, html, dcc
import dash_bootstrap_components as dbc
import plotly.graph_objects as go
import plotly.io as pio
pio.templates.default = "simple_white"
import pycountry

class animations(object):
    def __init__(self, df):
        self.df = df
        self.country_list = df.country.unique()
        self.scope_list = df.scope.unique()
        self.region_list = df.region.unique()
        self.project_list = df.project_type.unique()
        self.reduction_list = df.reduction_removal.unique()       
    
    
    def graphics(self, country = 'Colombia', type_analysis = 'scope', credit = 'credits_issued' ):
                               
        def get_code(loc):
            try:
                return pycountry.countries.get(name = loc).alpha_3
            except:
                return None
        
        df = self.df.copy()          
        df_credits = df.groupby(["year", 'country'])[credit].sum().reset_index()
        df_credits['code'] = df_credits['country'].apply( lambda x: get_code(x))
                        
        includes= ['United States', 'China', 'Germany', 'India','Brazil', 'Mexico', 'Argentina', 'Peru', 'Colombia']
        df_selected=df_credits[df_credits['country'].isin(includes)] 
        
        usa = df_selected[df_selected['country'].isin(['United States'])]
        china = df_selected[df_selected['country'].isin(['China'])]
        Germany = df_selected[df_selected['country'].isin(['Germany'])]
        india = df_selected[df_selected['country'].isin(['India'])]
        brazil = df_selected[df_selected['country'].isin(['Brazil'])]
        mexico = df_selected[df_selected['country'].isin(['Mexico'])]
        colombia = df_selected[df_selected['country'].isin(['Colombia'])]
        
        
        t_usa = go.Scatter(x=usa['year'][:2],
                            y=usa[credit][:2],                            
                            mode='lines',                                                         
                            name='USA',
                            line=dict(width=1.5),
                            stackgroup = 'one',)
        t_brazil = go.Scatter(x = brazil['year'][:2],
                            y = brazil[credit][:2],
                            mode='lines',
                            name= 'Brazil',
                            line=dict(width=1.5),
                            stackgroup = 'one',)
        t_india = go.Scatter(x = india['year'][:2],
                            y = india[credit][:2],
                            mode='lines',
                            name= 'India',
                            line=dict(width=1.5),
                            stackgroup = 'one',)
        t_china = go.Scatter(x = china['year'][:2],
                            y = china[credit][:2],
                            mode='lines',
                            name= 'China',
                            line=dict(width=1.5),
                            stackgroup = 'one',)
        
        t_colombia = go.Scatter(x = colombia['year'][:2],
                            y = colombia[credit][:2],
                            mode='lines',
                            name= 'Colombia',
                            line=dict(width=1.5),
                            stackgroup = 'one',)
        
        frames = [dict(data= [dict(type='scatter',
                           x=usa['year'][:k+1],
                           y=usa[credit][:k+1],                           
                           ),                              
                      dict(type='scatter',
                           x=brazil['year'][:k+1],
                           y=brazil[credit][:k+1]),
                      dict(type='scatter',
                           x=india['year'][:k+1],
                           y=india[credit][:k+1]),
                      dict(type='scatter',
                           x=china['year'][:k+1],
                           y=china[credit][:k+1]),
                      dict(type='scatter',
                           x=colombia['year'][:k+1],
                           y=colombia[credit][:k+1]),         
                     ],
               traces= [0, 1, 2, 3, 4],  
              )for k  in  range(1, len(usa)-1)]
              
        layout = go.Layout( #showlegend=False,
                            title='trend',
                            height=350,
                            hovermode='x unified',
                            updatemenus=[
                                dict(                                    
                                    type='buttons', 
                                    y=-0.33,
                                    x=-0.1,
                                    xanchor='left',
                                    yanchor='bottom',
                                    pad=dict(t=0, r=10),
                                    buttons=[dict(label='Play',
                                    method='animate',
                                    args=[None, 
                                          dict(frame=dict(duration=500, 
                                                          redraw=False),
                                                          transition=dict(duration=0),
                                                          fromcurrent=True,
                                                          mode='immediate')]
                                    )]
                                ),                                  
                                dict(
                                    type = "buttons",
                                    y= -0.15,
                                    x= 0.15,
                                    xanchor='left',
                                    yanchor='top',
                                    pad=dict(t=0, r=10),
                                    direction = "left",
                                    buttons=list([
                                        dict(
                                            args=[{"yaxis.type": "linear"}],
                                            label="linear",
                                            method="relayout"
                                            ),
                                        dict(
                                            args=[{"yaxis.type": "log"}],
                                            label="log",
                                            method="relayout"
                                            )
                                        ]),
                                    ),
                             ])
        
        layout.update(xaxis =dict(range=['1996', '2020'], autorange=False),
                      yaxis =dict(range=[0, 120000000], autorange=False));
            
            
        fig_countries = go.Figure(data=[t_usa, t_brazil, t_india, t_china, t_colombia], frames=frames, layout=layout)
        
        fig_geo = px.choropleth(df_credits, locations = 'code',
                    animation_frame = 'year',
                    color = credit,                    
                    hover_name = 'country',                   
                    color_continuous_scale = 'temps_r'
                    )
        fig_geo.update_layout( height=350, )
        
        
        df_country = df[df['country'] == country ]        
        selection = df_country.groupby(['year',type_analysis ]).sum().reset_index().sort_values(by = 'year') 
        
        credit_by_selection = (sum(df_country.groupby(['country'])[credit].sum()))/1000000
        credit_by_selection = f'{credit_by_selection:.2f}' + 'M Tons'
        
        projects_by_selection = sum(df_country.groupby(['country'])[credit].count())        
        
        fig_pie = px.pie(selection, values=credit,names=type_analysis, title='pie chart')
        fig_pie.update_layout(legend_x=-0.3,
                              legend_y=-0.4,                                
                              height=400
                             )       
        fig_bar = px.bar(selection, x= 'year', y = credit, color = type_analysis)
        fig_bar.update_layout(showlegend=False,
                             height=300
                             )
        
        simulation = px.bar(
                selection, x=  type_analysis, y = credit,
                animation_frame = 'year',
                animation_group = type_analysis,    
                color= type_analysis,
                hover_name = type_analysis,
                range_y=[0,10000000],
                title = 'behavior of scope by type of projects' )
        simulation.update_layout(showlegend=False)
        
        return fig_countries, fig_geo, fig_pie, fig_bar, simulation, credit_by_selection, projects_by_selection
    

    @staticmethod
    def get_output():
        return [Output('country-chart', 'figure'),
                Output('geo-chart', 'figure'),
                Output('pie-chart', 'figure'),
                Output('bar-chart', 'figure'),
                Output('simulation', 'figure'),
                Output('num_credits', 'children'),
                Output('num_projects', 'children')
                ]

    @staticmethod
    def get_inputs():
        return [ Input('id_country', 'value'),                 
                 Input('id_analysis', 'value'),
                 Input('id_credits', 'value'),]
       
    @staticmethod
    def get_credits():
        type_credits = ['credits_issued', 'credits_retired', 'registry_issued_credits', 'credits_remaining']
        type_credits.sort()
        return type_credits
    
    @staticmethod
    def get_analysis():
        analysis = [ 'voluntary_status', 'scope', 'type', 'reduction_removal', 'methodology_protocol', 'project_type']
        analysis.sort()
        return analysis          
    
    def get_html_components(self):
        return dbc.CardBody([
            
            dbc.Row(
                dbc.Col(
                html.Div("Fast view of carbon market"),
                width={"size": 6, "offset": 4},
                className='h4',
                style = {'justify':'center'}    
                    
                       )
                   ),

            dbc.Row([                
                dbc.Col([
                    dcc.Graph(id='geo-chart', config={}, figure = self.graphics()[1])
                        ], width=6),                
                
                dbc.Col([                    
                    dcc.Graph(id='country-chart', config={}, figure = self.graphics()[0])
                ], width=6),                
            ]),

            dbc.Row([
                dbc.Col(
                html.Div("custom visualization"),                                
                )],
                style = {"background-color": "#EEFFD6",
                         'height':'35px',                            
                         'border-radius': '5px',
                         'padding': '5px 0px',
                         'text-align': 'left',
                        }     
                   ),
            dbc.Row([
                dbc.Col([                    
                    html.Label('country', className='card-tittle'),
                    dcc.Dropdown([x for x in sorted(self.df['country'].unique())],
                                 value = 'Colombia',
                                 id='id_country'),
                    
                    html.Label('type analysis', className='card-tittle'),
                    dcc.Dropdown(options=animations.get_analysis(),
                                 value='scope',
                                 id="id_analysis"),
                    
                    html.Label('Type credits', className='card-tittle'),
                    dcc.Dropdown(options=animations.get_credits(),
                                 value=animations.get_credits()[0],                                 
                                 id='id_credits'),
                    ],
                    style = {
                            'width': '224px',                            
                            'background-color': '##EEFFD6', 
                            'border-radius': '5px',
                            'margin-top': '50px',
                            'margin-bottom': '10px', 
                             },
                    width="300px"),
                
                dbc.Col([
                    
                    html.Label('Number of credits', className='card-tittle'),
                    html.H4(id='num_credits'),
                    html.Label('Number of projects', className='card-tittle'),
                    html.H4(id='num_projects')],
                    style = {                            
                            'border-radius': '5px',
                            'margin-top': '50px',
                            'padding': '41px 0 0 62px' 
                             },
                    width=3),
                dbc.Col([
                    dcc.Graph(id='bar-chart', config={'displayModeBar':False}, figure = self.graphics()[3])
                ], width=6),
            ]),
        
            
            dbc.Row([
                dbc.Col([html.Label("Visualization by country", className="align-middle")])
            ], style = {"background-color": "#EEFFD6",
                        'height':'35px',                            
                        'border-radius': '5px',
                        'padding': '5px 0px',
                        'text-align': 'left',
                       }     
                ),

            dbc.Row([
                dbc.Col([
                    dcc.Graph(id='pie-chart', config={'displayModeBar':False}, figure = self.graphics()[2])                    
                ], width=5),
                dbc.Col([
                   dcc.Graph(id='simulation', config={'displayModeBar':False}, figure = self.graphics()[4])
                ], width=7)
            ])
        ])
  
        return  
