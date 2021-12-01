import dash
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from autots import AutoTS
from dash import dcc, html
from dash.dependencies import Input, Output, State
from plotly.tools import mpl_to_plotly
from waitress import serve

DATA_PATH = "data/raw.csv"

model = AutoTS(
    forecast_length=14,
    frequency='D',
    prediction_interval=0.9,
    ensemble='simple', #simple
    model_list="fast", #fast
    transformer_list="fast",  #fast 
    drop_most_recent=1,
    max_generations=10, #10
    num_validations=3, #3
    validation_method="backwards"
)

df = pd.read_csv(DATA_PATH)

model = model.fit(
    df,
    date_col='dates',
    value_col='price'
)

prediction = model.predict()
forecasts_df = prediction.forecast  
forecasts_upper_df = prediction.upper_forecast
forecasts_lower_df = prediction.lower_forecast

col = model.df_wide_numeric.columns[-1]  

plot_df = pd.DataFrame(
    {
        col: model.df_wide_numeric[col],
        "up_forecast": forecasts_upper_df[col],
        "low_forecast": forecasts_lower_df[col],
        "forecast": forecasts_df[col],
    }
)
plot_df[plot_df == 0] = np.nan
plot_df.interpolate(method="cubic", inplace=True)
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
    # app.run_server(debug=True)
    serve(app.server, host="0.0.0.0", port=8080)
