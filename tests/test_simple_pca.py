"""
Unit-test suite for the PCA health indicator backend.

Run with:
    pytest tests/test_simple_pca.py -v
"""

import numpy as np
import pytest

from backend.simple_pca import compute_health_indicator, generate_synthetic_data


def test_generate_synthetic_data_shape():
    """Synthetic data generator must return the requested shape."""
    X = generate_synthetic_data(n_measurements=30, n_features=5)
    assert X.shape == (30, 5)


def test_compute_health_indicator_basic():
    """PCA output must contain expected keys and valid arrays."""
    X = generate_synthetic_data(n_measurements=50, n_features=4)
    result = compute_health_indicator(X, n_components=1)

    assert "health" in result
    assert "explained_variance" in result
    assert "components" in result

    health = result["health"]
    assert health.shape == (50,)
    assert np.isfinite(health).all()
    assert 0.0 <= result["explained_variance"] <= 1.0


def test_compute_health_indicator_monotonic_trend():
    """
    Health indicator must be monotonically increasing for synthetic data
    because a positive degradation trend is injected into the first feature.
    """
    X = generate_synthetic_data(n_measurements=50, n_features=4, seed=123)
    result = compute_health_indicator(X)
    health = result["health"]

    slope = np.polyfit(np.arange(len(health)), health, 1)[0]
    assert slope > 0


def test_invalid_input_raises():
    """Invalid inputs must raise ValueError."""
    with pytest.raises(ValueError):
        compute_health_indicator(np.array([1, 2, 3]))

    with pytest.raises(ValueError):
        compute_health_indicator(np.array([[1, 2]]))
