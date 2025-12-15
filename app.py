
import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import pandas as pd
import plotly.express as px

# Use the pre-processed formatted_sales.csv
df = pd.read_csv("formatted_sales.csv")


app = dash.Dash(__name__)
app.title = "Pink Morsels Sales Visualiser"

app.layout = html.Div(
    className="container",
    children=[
        html.H1("Pink Morsels Sales by Region"),

        
        dcc.RadioItems(
            id="region-radio",
            options=[
                {"label": "All", "value": "all"},
                {"label": "North", "value": "north"},
                {"label": "East", "value": "east"},
                {"label": "South", "value": "south"},
                {"label": "West", "value": "west"},
            ],
            value="all",
            className="radio-group",
            inline=True
        ),

        dcc.Graph(id="sales-line-chart")
    ]
)

@app.callback(
    Output("sales-line-chart", "figure"),
    Input("region-radio", "value")
)
def update_chart(selected_region):
    if selected_region == "all":
        filtered_df = df
    else:
        filtered_df = df[df["region"] == selected_region]

    fig = px.line(
        filtered_df,
        x="date",
        y="sales",
        color="region",
        title="Pink Morsels Sales Over Time"
    )

    fig.update_layout(template="plotly_white")
    return fig


if __name__ == "__main__":
    app.run_server(debug=True)
