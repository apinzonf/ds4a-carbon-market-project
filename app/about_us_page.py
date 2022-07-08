import dash_bootstrap_components as dbc
from dash import Output, Input, html, dcc


class AboutUsPage(object):
    def __init__(self, app):
        self.app = app

    def describe_person(self, name, description, profile_photo, text_link, url_link):
        return dbc.Card(
            [
                dbc.Row(
                    [
                        dbc.Col(
                            dbc.CardImg(
                                src=self.app.get_asset_url(profile_photo),
                                className="img-fluid rounded-start",
                            ),
                            className="col-md-4",
                        ),
                        dbc.Col(
                            dbc.CardBody(
                                [
                                    html.H4(name, className="card-title"),
                                    html.P(description,className="card-text"),
                                    dbc.CardLink(text_link, href=url_link)
                                ]
                            ),
                            className="col-md-8",
                        ),
                    ],
                    className="g-0 d-flex align-items-center",
                )
            ],
            className="mb-3",
            style={"maxHeight": "250px", "minHeight": "250px"}
        )

    def get_html_components(self):
        return dbc.CardBody([
            dbc.Row([
                dbc.Col(
                    self.describe_person(
                        name='Alexander Pinzon Fernandez',
                        profile_photo='profile_photos/alexander_pinzon_fernandez.jpg',
                        text_link='www.linkedin.com/in/alexander-pinzon-fernandez-9031138b',
                        url_link='https://www.linkedin.com/in/alexander-pinzon-fernandez-9031138b/',
                        description = """
                        Master of Computer Science and Software Engineer. 
                        Senior Software Engineer at Kinesso."""
                    )
                ),
                dbc.Col(
                    self.describe_person(
                        name='Mateo Orozco Jimenez',
                        profile_photo='profile_photos/mateo_orozco.jpg',
                        text_link='https://www.linkedin.com/in/mateo-orozco-jimenez-3307b977/',
                        url_link='https://www.linkedin.com/in/mateo-orozco-jimenez-3307b977/',
                        description = """
                        Administrative engineer and specialist in artificial intelligence with 5 years of experience working in corporate finance, 
                        capital markets, project evaluation and data analysis. Professional with technical skills in programming, 
                        management of office automation tools and C1 certification in English. 
                        Person with high capacity for problem solving, analytical and attention to detail."""
                    )
                ),
            ]),
            dbc.Row([
                dbc.Col(
                    self.describe_person(
                        name='Iván Herney Hernández León',
                        profile_photo='profile_photos/ivan_herney.jpg',
                        text_link='www.linkedin.com/in/ivan-herney-hernandez-leon',
                        url_link='https://www.linkedin.com/in/ivan-herney-hernandez-leon',
                        description = """
                        Production and operations engineer at Holcim, 
                        Industrial engineer specialized in production and operations engineering with 14 years of experience in different industries
                        including fertilizers, refractories, alternative fuels and cement, 
                        passionate about data science and machine learning in which I permanent formation meeting
                        """
                    )
                ),
                dbc.Col(
                    self.describe_person(
                        name='Katherin Parra',
                        profile_photo='profile_photos/katherin_parra.jpg',
                        text_link='www.linkedin.com/in/katherin-parra/',
                        url_link='https://www.linkedin.com/in/katherin-parra/',
                        description = """
                        Mechatronic Engineer, specialist in Commercial Management. 
                        11 years of work experience in the commercial area with a solid technical background, 
                        development and maintenance of new markets"""
                    )
                )
            ]),
            dbc.Row([
                dbc.Col(
                    self.describe_person(
                        name='Luis David Villarreal Muñoz',
                        profile_photo='profile_photos/david_villarreal.jpg',
                        text_link='www.linkedin.com/in/ludavim/',
                        url_link='https://www.linkedin.com/in/ludavim/',
                        description = """
                        I’m an electrical and electronic engineer from the Universidad Nacional de Colombia. 
                        I’m currently working at El Dorado International Airport in the Telecommunications Area."""
                    )
                ),
                dbc.Col(
                    self.describe_person(
                        name='Esteban Salamanca Vasquez',
                        profile_photo='profile_photos/esteban_salamanca.jpg',
                        text_link='www.linkedin.com/in/esteban-salamanca-vasquez-1959b4138',
                        url_link='https://www.linkedin.com/in/esteban-salamanca-vasquez-1959b4138/',
                        description = """
                        Ingeniero de Control. 
                        Big Data Developer en Tata Consultancy Services."""
                    )
                )
            ]),
            dbc.Row([
                dbc.Col(
                    self.describe_person(
                        name='Laura Paola Goyeneche Gomez',
                        profile_photo='profile_photos/laura_goyeneche.jpg',
                        text_link='www.linkedin.com/in/laura-paola-goyeneche-17b35b190',
                        url_link='https://www.linkedin.com/in/laura-paola-goyeneche-17b35b190/',
                        description = """
                        Bachelor degree in Telecommunications Engineering.
                        Telecommunications Engineer at Whale Cloud."""
                    )
                ),
                dbc.Col(
                    self.describe_person(
                        name='Team 74',
                        profile_photo='profile_photos/team74.png',
                        text_link='carbon-market-analysis.azurewebsites.net',
                        url_link='https://carbon-market-analysis.azurewebsites.net/',
                        description = """
                        DS4A Team 74. 
                        Colombia 2022."""
                    )
                )
            ])


        ])
