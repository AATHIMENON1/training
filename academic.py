import dash
from dash import Dash, html, dcc, callback, Output, Input
import plotly.express as px
import pandas as pd

df = pd.read_csv('C:/Users/athir/OneDrive/Desktop/kaggle/input/origin.csv')
df.head(10)
app = Dash(__name__)

app.layout = html.Div([
    html.H1(children='Countries', style={'textAlign':'center'}),
    dcc.Dropdown(df.origin_region.unique(), 'Caribbean', id='dropdown-selection'),
    dcc.Graph(id='graph-content')
])

@callback(
    Output('graph-content', 'figure'),
    Input('dropdown-selection', 'value')
)
def update_graph(value):
    dff = df[df.origin_region==value]
    return px.histogram(dff, x='academic_type', y='students')

if __name__ == '__main__':
    app.run(debug=True)
