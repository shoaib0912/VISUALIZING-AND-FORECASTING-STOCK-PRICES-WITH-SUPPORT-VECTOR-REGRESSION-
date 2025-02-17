import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd

# Create a sample dataset
df = pd.DataFrame({
    'Month': ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun'],
    'Sales': [100, 120, 110, 130, 140, 150]
})

# Create the Dash app
app = dash.Dash(__name__)
app.css.append_css({"external_url": "header.css"})

# Define the app layout
app.layout = html.Div(children=[
    html.H1(children='Sales Dashboard'),

    html.Div(children='''
        Select a month to see the sales data:
    '''),

    dcc.Dropdown(
        id='month-dropdown',
        options=[{'label': i, 'value': i} for i in df['Month'].unique()],
        value='Jan'
    ),

    dcc.Graph(id='sales-graph')
])

# Define the callback function
@app.callback(
    Output('sales-graph', 'figure'),
    Input('month-dropdown', 'value')
)
def update_graph(selected_month):
    filtered_df = df[df['Month'] == selected_month]
    fig = px.line(filtered_df, x='Month', y='Sales')
    return fig

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)