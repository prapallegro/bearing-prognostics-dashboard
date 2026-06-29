"""
Root application layout factory.

Constructs the top-level Dash component tree: a Bootstrap navbar at the
top, a sidebar control panel on the left (25% width), and a main content
area on the right (75% width) where plots are rendered.
"""

from dash import html
import dash_bootstrap_components as dbc
from .sidebar import create_sidebar


def create_layout():
    """Build and return the main application layout."""
    return html.Div([
        dbc.Navbar(
            dbc.Container([
                dbc.NavbarBrand(
                    "Bearing Prognostics Dashboard",
                    className="fs-4 fw-bold",
                ),
            ], fluid=True),
            color="light",
            className="mb-3",
        ),
        dbc.Container(fluid=True, children=[
            dbc.Row([
                create_sidebar(),
                dbc.Col(md=9, children=[
                    html.Div(id="health-plot-container", className="p-3")
                ]),
            ])
        ]),
    ])
