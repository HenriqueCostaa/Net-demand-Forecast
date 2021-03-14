import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objects as go
import pandas as pd
import numpy as np

# Dataset 'Processing'

df_emissions = pd.read_csv('BC2_HotelCancelations_NetDemand.csv')

def add_country(x):
  return 'Portugal'
df_emissions['country_name'] = df_emissions['NetDemand'].apply(add_country)

df_emission_0 = df_emissions

# Building our Graphs (nothing new here)

data_choropleth = dict(type='choropleth',
                       locations=df_emission_0['country_name'],  #There are three ways to 'merge' your data with the data pre embedded in the map
                       locationmode='country names',
                       z=df_emission_0['GrossDemand'],
                       text=df_emission_0['country_name'],
                       colorscale='inferno',
                       colorbar=dict(title='GrossDemand')
                      )

layout_choropleth = dict(geo=dict(scope='world',  #default
                                  projection=dict(type='orthographic'
                                                 ),
                                  #showland=True,   # default = True
                                  landcolor='black',
                                  lakecolor='white',
                                  showocean=True,   # default = False
                                  oceancolor='azure'
                                 ),
                         
                         title=dict(text='World Choropleth Map',
                                    x=.5 # Title relative position according to the xaxis, range (0,1)
                                   )
                        )

fig = go.Figure(data=data_choropleth, layout=layout_choropleth)



# The App itself

app = dash.Dash(__name__)

server = app.server




app.layout = html.Div(children=[
    html.H1(children='My First DashBoard'),

    html.Div(children='''
        Example of html Container
    '''),

    dcc.Graph(
        id='example-graph',
        figure=fig
    )
])




if __name__ == '__main__':
    app.run_server(debug=True)
