# Financial Information
import os

import dash
import dash_core_components as dcc
import dash_bootstrap_components as dbc
import dash_html_components as html
import plotly.express as px
from dash.dependencies import Input, Output, State, ClientsideFunction
import pandas as pd
import plotly.graph_objects as go

#-
df = pd.read_csv('Financial 2020.csv')
df = df.rename(columns={'Brand ': 'Brand', 'Size ': 'Size', 'Sold $ ': 'Sold', 'Total Profit $': 'Profit', 'Category': 'Type'})
df2 = pd.read_csv('2019 financial.csv')
df2 = df2.rename(columns={'Brand ': 'Brand', 'Category': 'Type'})
external_stylesheets = [dbc.themes.BOOTSTRAP]
app = dash.Dash(__name__, external_stylesheets=external_stylesheets, meta_tags=[
    {'name': 'Caretag 2020 Business Report',
     'content': 'This website is a dynamic business report for www.caretag.us.'
                'Please visit www.caretag.us to see all of our offerings'},
    {'charset': 'utf-8'},
    {'name': 'viewport',
     'content': 'width=device-width, initial-scale=0.95'},
], title='Caretag 2020 Business Report')
server = app.server
app.layout = html.Div([
    html.Div(id="output-clientside"),
    html.Div(children=[
        html.Header(children=[
           html.H1("2020 Caretag Business Report")
        ]),
    ]),
    html.Div(children=[
        html.Nav(className="disappear",
                 children=[
            html.Ul(children=[
                html.Li(children=[
                    html.A("Introduction", href="#section-1")
                ]),
                html.Li(children=[
                    html.A("Overview", href="#section-2")
                ]),
                html.Li(children=[
                    html.A("Looking Ahead", href="#section-3")
                ]),
                html.Li(children=[
                    html.A("Final Thoughts", href="#section-4")
                ]),
            ]),
            html.A(href="https://www.caretag.us/", children=[
                html.Img(className="image-hover",
                         alt="caretag",
                         src=app.get_asset_url("Logo.png"),
                         style={'height': '75px',
                                'width': '85px',
                                'display': 'block',
                                'margin-left': 'auto',
                                'margin-right': 'auto',
                                'filter': 'invert(1)'})])
        ], style={'display': 'inline-block', 'height': '100%', 'vertical-align': 'top'}),
        html.Main(children=[
            html.Section(
                id="section-1",
                children=[
                    html.H1("Introduction"),
                    html.P(["2020 has been a difficult year for the retail business and the second hand resale was no exception. "
                            "Not only were primary market supply chains disrupted, but so too were secondary market channels. "
                            "Furthermore, as purchasable bulk inventory decreased year-over-year, the cost of purchasing and transporting these same goods increased. "
                            "The secondary market can be viewed as an ecosystem which relies on a primary buyer individual or company who then becomes a secondary market seller via reselling channels such as Caretag.us,  marketplaces such as Grailed.com or consignment shops such as TheRealReal. "
                            "Resultant from 2020’s", html.A('disruption', className="no-underline", href='https://www.mdpi.com/1911-8074/13/8/173/pdf', style={'margin': '0.25rem', 'color': '#ffd11a'}), "of the manufacturing supply chain for high-end contemporary retail shops such as Ssense and MatchesFashion, many retailers could not procure enough high-demand inventory to satisfy the needs of consumers, thus many of these buyers began flocking to the secondary market. "
                            "This is most apparent in the", html.A('study', className="no-underline", href='https://drive.google.com/drive/folders/12D1SXDVeMyJFxRcY8HpDo0v4T0qHdcaN?usp=sharing', style={'margin': '0.25rem', 'color': '#ffd11a'}), "performed by Caretag.us between January and June tracking the price of Rick Owens Ramones in which over a six month period (pre-covid and during covid) The price of this sneaker increased 32 and 38% for diffusion and main-line pairs respectively. "
                            "The increase of buyers on the secondary market not only increased the price of such goods for consumers, but also inventory purchasing costs for Caretag.us."
                    ]),
                ]),
            html.Section(
                id="section-2",
                children=[
                    html.H1("Overview"),
                    html.P(["As of January 14th 2021, WWW.Caretag.us had sold and purchased 104 items between the period of January 1st 2020 to January 1st 2021. "
                            "This is a 32% decrease in transaction from the year before, but a nearly 100% increase in revenue. "
                            "Through a concerted shift toward specific brands and apparel categories Caretag has been able to satisfy our customers in an affordable and efficient way. "
                            "During 2019 Chanel was Caretags most sold brand accounting for 25% of sales, however, by 2020 it had been surpassed by Rick Owens which accounted for nearly 50% of all sales. "
                            "Moreover, in 2019 Caretag’s inventory was balanced between clothing, accessories/Jewelry, footwear and bags, however, by the end of 2020 footwear had grown 164% to account for 58.7% of all sales. "
                            "Because of scarcities within the primary market, Rick Owens footwear became  2020’s best selling inventory class and will likely remain so in 2021. Please see below for Caretag’s interactive sales dashboard."]),
                    html.Div([
                        html.H3('2020 & 2019 Sales Information'
                        ),
                    ]),
                    html.Div(children=[
                        html.Label('Filter by Attribute (2020)'),
                        dcc.Dropdown(
                            id='my_dropdown',
                            options=[
                                {'label': 'Brand', 'value': 'Brand'},
                                {'label': 'Size', 'value': 'Size'},
                                {'label': 'Category', 'value': 'Type'}
                            ],
                            value='Brand',
                            multi=False,
                            clearable=False,
                            style={"width": "48%", 'align': 'right', 'display': 'inline-block', 'color': '#000000'}
                        ),
                        html.Label(['Filter by Attribute (2019)'], style={'display': 'inline-block',}),
                        dcc.Dropdown(
                            id='my_dropdown_2',
                            options=[
                                {'label': 'Brand', 'value': 'Brand'},
                                {'label': 'Category', 'value': 'Type'}
                            ],
                            value='Brand',
                            multi=False,
                            clearable=False,
                            style={"width": "48%", 'align': 'left', 'display': 'inline-block', 'color': '#000000'}

                        )
                    ], style=dict(display='flex')),
                    html.Div(children=[
                        dcc.Loading(children=[
                            dcc.Graph(
                                id='2020-graph',
                                style={'width': '50%', 'align': 'right', 'display': 'inline-block'},
                                figure={'layout': go.Layout(
                                    paper_bgcolor='rgba(0,0,0,0)',
                                    plot_bgcolor='rgba(0,0,0,0)'
                                )}
                            ),
                            dcc.Graph(
                                id='2019-graph',
                                style={'width': '50%', 'align': 'left', 'display': 'inline-block'},
                                figure={'layout': go.Layout(
                                    paper_bgcolor='rgba(0,0,0,0)',
                                    plot_bgcolor='rgba(0,0,0,0)'
                                )}
                            )
                        ])
                    ])
                ]),
            html.Section(
                id="section-3",
                children=[
                    html.H1("Looking Ahead"),
                    html.P(["Caretag forecasts growth throughout 2021 with an increased consumer focus on difficult to find, low-production, pieces primarily from “Avante-Garde” designers (Rick Owens, Guidi, Carol Christian Poell, etc). "
                            "As “archive” buyers become more attuned to their own personal style many will begin to separate themselves from what they see as “archive Hypebeasts” and more mainstream “archive” consumers. "
                            "This sentiment has strongly proliferated through-out social media with instagram accounts such as", html.A('@GuidiCommunity', className="no-underline", href='https://www.instagram.com/guidi_community', style={'margin': '0.25rem', 'color': '#ffd11a'}), ",", html.A('@Geocasket', className="no-underline", href='https://www.instagram.com/geocasket/', style={'margin': '0.25rem', 'color': '#ffd11a'}), "and", html.A('@lucentement.', className="no-underline", href='https://www.instagram.com/lucentement/', style={'margin': '0.25rem', 'color': '#ffd11a'}),
                            "There must be a mention of technical outerwear and clothing as an extremely strong segment of the secondary market with brands including Kiko Kostadinov, Arc’teryx, Craig Green and Final Home. "
                            "Caretag will continue to have a strong position towards vintage Chanel pieces including the Sports diffusion and Jewelry line. "
                            "Furthermore, Caretag has a strong long-term position towards non-collaboration Kaws accessories and collectibles primarily from his OriginalFake and eponymous brands."
                            "As seen in 2020, legacy contemporary archive brands such Raf Simons, Undercover, (N)umber (N)ine and Jean Paul Gaultier will continue to struggle on the resell market aside from their most recognizable and coveted pieces."
                            " Lastly, business goals for 2021 include:",
                            html.Div(
                                html.Ul(children=[
                                    html.Li("Lower acquisition and shipping costs"),
                                    html.Li("Price inventory more efficiently"),
                                    html.Li("Forecast more efficiently"),
                                    html.Li("Increase customer retention"),
                                    html.Li("Increase Inventory"),
                                ], style={"margin": "0rem 1.5rem", "padding": "1rem"})
                            )
                    ])
                ]),
            html.Section(
                id="section-4",
                children=[
                    html.H1("Final Thoughts"),
                    html.P(["Caretag looks forward to the next year with great optimism and expects to continue growing via the current sales and pricing strategy as well as lowering overhead costs. "
                            "Caretag would like to personally thank all customers, followers and business partners for their continued support. "
                            "If you have any questions about this report please feel free to reach out to the company at any time at:", html.A('Email', className="no-underline", href="mailto:caretagus@gmail.com", style={'margin': '0.25rem', 'color': '#ffd11a'})])
                ]),
        ],style={'display': 'inline-block', 'width': '85%', 'height': '100%'}),
    ], style=dict(display='flex', position='absolute')),
])


@app.callback(
    Output(component_id='2020-graph', component_property='figure'),
    [Input(component_id='my_dropdown', component_property='value')]
)

def graph_2020(my_dropdown):
  dff = df
  piechart = px.pie(
      data_frame=dff,
      names=my_dropdown,
      title='2020',
      color_discrete_sequence=px.colors.sequential.Plotly3,
      #hole=.1,
      )
  piechart.layout.showlegend = False
  return(piechart)

@app.callback(
    Output(component_id='2019-graph', component_property='figure'),
    [Input(component_id='my_dropdown_2', component_property='value')]
)

def graph_2019(my_dropdown_2):
  dfff = df2
  piechart2 = px.pie(
      data_frame=dfff,
      names=my_dropdown_2,
      title='2019',
      color_discrete_sequence=px.colors.sequential.Plotly3,
      #hole=.3,
      )
  piechart2.layout.showlegend = False
  return(piechart2)

app.clientside_callback(
    ClientsideFunction(namespace="clientside", function_name="resize"),
    Output("output-clientside", "children"),
    [Input("yourGraph_ID", "figure")],
)
if __name__=="__main__":
    app.run(debug=True)
    #app.run_server(host=os.getenv('IP', '0.0.0.0'),
            #port=int(os.getenv('PORT', 4444)))

