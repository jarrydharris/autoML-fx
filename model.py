from autots import AutoTS
import numpy as np
import pandas as pd
import pickle

DATA_PATH = "data/raw.csv"
PICKLE_PATH = "model/predictions.pickle"

df = pd.read_csv(DATA_PATH)

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

with open(PICKLE_PATH, 'wb') as f:
    pickle.dump(plot_df, f)