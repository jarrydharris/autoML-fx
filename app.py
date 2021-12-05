import dash
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from dash import dcc, html
# from dash.dependencies import Input, Output, State
from plotly.tools import mpl_to_plotly
from waitress import serve
import pickle

PICKLE_PATH = "model/predictions.pickle"
with open(PICKLE_PATH, "rb") as f:
    plot_df = pickle.load(f)

fig, ax = plt.subplots(dpi=300, figsize=(4, 3))
# TODO: This needs to filter by the last two weeks
plot_df[plot_df.index >= '2021-11-01'].plot(ax=ax)

print("Models finished.")

fig = mpl_to_plotly(fig)

app = dash.Dash(__name__)

app.layout = html.Div(
    [
        dcc.Graph(id="graph", figure=fig)
    ]
)

if __name__ == '__main__':
    app.run_server(debug=True)
    # serve(app.server, host="0.0.0.0", port=8080)
