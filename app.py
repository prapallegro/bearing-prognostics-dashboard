"""
Bearing Prognostics Dashboard — v0.1.0-alpha (MVP)

Main application entry point. Initializes the Dash web server,
constructs the UI layout, and registers the interactive callback that
recomputes the health indicator and regenerates the plot whenever the
user adjusts the threshold slider.
"""

import numpy as np
import dash
import dash_bootstrap_components as dbc
from dash import Input, Output, dcc, html

from components.layout import create_layout
from backend.simple_pca import compute_health_indicator, generate_synthetic_data
from plots.health_plot import create_health_plot


# Synthetic demo data — stand-in until real dataset loaders are implemented
FEATURE_MATRIX = generate_synthetic_data(n_measurements=50, n_features=4)
TIME = np.arange(50)


# Dash application instance
app = dash.Dash(
    __name__,
    external_stylesheets=[dbc.themes.BOOTSTRAP],
    suppress_callback_exceptions=True,
)
app.title = "Bearing Prognostics Dashboard"
app.layout = create_layout()


@app.callback(
    Output("health-plot-container", "children"),
    Output("measurement-count", "children"),
    Input("threshold-slider", "value"),
)
def update_dashboard(threshold):
    """
    Recompute the PCA health indicator and redraw the plot when the user
    moves the threshold slider.
    """
    result = compute_health_indicator(FEATURE_MATRIX, n_components=1)
    health = result["health"]

    fig = create_health_plot(
        health=health,
        time=TIME,
        threshold=threshold,
        theme="light",
    )

    return dcc.Graph(figure=fig), str(len(health))


if __name__ == "__main__":
    app.run(debug=True, port=8050)
