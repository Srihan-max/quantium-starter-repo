import pandas as pd
from dash import Dash, dcc, html
import plotly.express as px

df = pd.read_csv("formatted_sales.csv")

df['date'] = pd.to_datetime(df['date'])

daily_sales = df.groupby('date')['sales'].sum().reset_index()

daily_sales = daily_sales.sort_values('date')

fig = px.line(
    daily_sales,
    x='date',
    y='sales',
    title='Pink Morsel Sales Over Time',
    labels={'date': 'Date', 'sales': 'Total Sales ($)'}

)

app = Dash(__name__)

app.layout = html.Div(children=[
    html.H1("Soul Foods Pink Morsel Sales Visualizer", style={'textAlign': 'center'}),
    dcc.Graph(figure=fig)
])


if __name__ == '__main__':
    app.run(debug=True)

