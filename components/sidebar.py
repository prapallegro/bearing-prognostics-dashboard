"""
Sidebar component with interactive controls.

Provides a dataset info card, a threshold slider, and an about card.
All interactive elements expose IDs that are targeted by callbacks
registered in app.py.
"""

from dash import html, dcc
import dash_bootstrap_components as dbc


def create_sidebar():
    """Build the control sidebar."""
    return dbc.Col(md=3, children=[
        html.Div([
            dbc.Card([
                dbc.CardHeader("Dataset", className="fw-bold"),
                dbc.CardBody([
                    html.P("Synthetic demo data (v0.1.0)", className="text-muted small"),
                    html.Hr(),
                    html.Div("Measurements:", className="fw-bold small"),
                    html.Div(id="measurement-count", children="50"),
                ])
            ], className="mb-3"),

            dbc.Card([
                dbc.CardHeader("Threshold", className="fw-bold"),
                dbc.CardBody([
                    dcc.Slider(
                        id="threshold-slider",
                        min=0.5,
                        max=3.0,
                        step=0.1,
                        value=1.5,
                        marks={0.5: "0.5", 1.5: "1.5", 3.0: "3.0"},
                    ),
                ])
            ], className="mb-3"),

            dbc.Card([
                dbc.CardHeader("About", className="fw-bold"),
                dbc.CardBody([
                    html.P(
                        "v0.1.0-alpha MVP. RUL prediction and "
                        "advanced features coming in future releases.",
                        className="small text-muted",
                    ),
                    html.A(
                        "View Roadmap →",
                        href="https://github.com/prapallegro/bearing-prognostics-dashboard/issues",
                        target="_blank",
                        className="small",
                    ),
                ])
            ]),
        ], className="mt-4")
    ], className="m-0")
