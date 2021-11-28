import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output, State
from waitress import serve

app = dash.Dash(__name__)

if __name__ == '__main__':
    serve(app.server, host="0.0.0.0", port=8080)