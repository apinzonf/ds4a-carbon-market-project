import dash_bootstrap_components as dbc
from dash import Output, Input, html, dcc


class DescriptionModels(object):
    @staticmethod
    def get_html_components():
        return dbc.CardBody([
            html.H4("Models Used", className="card-title"),
            html.Div(children=[
                html.Article(children=[
                    html.Section(children=[
                        html.H5("CNN-LSTM", className="card-title"),
                        html.P(
"""An LSTM (long-short term memory network) is a type of recurrent neural network that allows for the accounting of sequential dependencies in a time series.

A convolutional neural network is one that applies a process known as convolution in determining the relationships between two functions. e.g. given two functions f and g, the convolution integal expresses how the shape of one function is modified by the other. Such networks are traditionally used for image classification, and do not account for sequential dependencies in the way that a recurrent neural network is able to do.

However, the main advantage of CNNs that make them suited to forecasting time series is that of dilated convolutions - or the ability to use filters to compute dilations between each cell. That is to say, the size of the space between each cell, which in turn allows the neural network to better understand the relationships between the different observations in the time series.

For this reason, LSTM and CNN layers are often combined when forecasting a time series. This allows for the LSTM layer to account for sequential dependencies in the time series, while the CNN layer further informs this process through the use of dilated convolutions.
        """,
                            className="card-text", style={'white-space': 'pre-wrap'}
                        ),
                        html.A("""More info
                                    """,
                               href="https://towardsdatascience.com/cnn-lstm-predicting-daily-hotel-cancellations-e1c75697f124",
                               ),
                    ]),
                    html.Section(children=[
                        html.H5("Support Vector Machine (SVR)", className="card-title"),
                        html.P(
"""In machine learning, Support Vector Machines are supervised learning models with associated learning algorithms that analyze data used for classification and regression analysis. In Support Vector Regression, the straight line that is required to fit the data is referred to as hyperplane.
        """,
                            className="card-text", style={'white-space': 'pre-wrap'}
                        ),
                        html.A("""More info
                                            """,
                               href="https://towardsdatascience.com/unlocking-the-true-power-of-support-vector-regression-847fd123a4a0",
                               ),
                    ])
                ]),

            ])]
        )
