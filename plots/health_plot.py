"""
Health indicator Plotly figure factory.

Generates an interactive line chart of the health indicator over time,
with a dashed horizontal threshold line. Supports light and dark themes;
dark mode is partially implemented but not yet exposed in the UI.
"""

import numpy as np
import plotly.graph_objects as go


def create_health_plot(
    health: np.ndarray,
    time: np.ndarray,
    threshold: float = 1.0,
    theme: str = "light",
) -> go.Figure:
    """
    Create an interactive health degradation plot.

    Parameters
    ----------
    health : np.ndarray
        Health indicator values (1-D).
    time : np.ndarray
        Time stamps corresponding to health values.
    threshold : float
        Failure threshold (horizontal dashed line).
    theme : str
        UI theme: "light" or "dark". Only light is fully wired in v0.1.0.

    Returns
    -------
    go.Figure
        Plotly figure ready for embedding in Dash.
    """
    if len(health) != len(time):
        raise ValueError("health and time must have the same length")

    if theme == "dark":
        bg = "#121212"
        text = "#FFFFFF"
        grid = "#444444"
        health_color = "#56B4E9"
        threshold_color = "#D55E00"
    else:
        bg = "#FFFFFF"
        text = "#000000"
        grid = "#E5E5E5"
        health_color = "#0072B2"
        threshold_color = "#D55E00"

    fig = go.Figure()

    fig.add_trace(go.Scatter(
        x=time,
        y=health,
        mode="lines+markers",
        name="Health Indicator",
        line=dict(color=health_color, width=2),
        marker=dict(size=6, color=health_color),
        hovertemplate="Time: %{x:.2f}<br>Health: %{y:.3f}<extra></extra>",
    ))

    fig.add_hline(
        y=threshold,
        line=dict(color=threshold_color, dash="dash", width=2),
        annotation_text=f"Threshold ({threshold:.2f})",
        annotation_position="top right",
    )

    fig.update_layout(
        title=dict(
            text="Health Monitoring (PCA-based)",
            x=0.5,
            font=dict(size=18, color=text),
        ),
        xaxis=dict(
            title="Time (units)",
            gridcolor=grid,
            linecolor=grid,
            tickfont=dict(color=text),
        ),
        yaxis=dict(
            title="Health Indicator",
            gridcolor=grid,
            linecolor=grid,
            tickfont=dict(color=text),
        ),
        paper_bgcolor=bg,
        plot_bgcolor=bg,
        font=dict(color=text),
        hovermode="x unified",
        height=500,
        margin=dict(l=60, r=40, t=60, b=40),
    )

    return fig
