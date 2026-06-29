"""
Minimal PCA-based health indicator backend.

Computes a scalar health indicator from a multivariate feature matrix
using Principal Component Analysis (PCA). The first principal component
score is used as the health indicator; its sign is flipped if necessary
to ensure a monotonically increasing degradation trend.
"""

import numpy as np
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
from typing import Dict, Any


def compute_health_indicator(
    feature_matrix: np.ndarray,
    n_components: int = 1,
) -> Dict[str, Any]:
    """
    Compute a health indicator from a feature matrix via PCA.

    Parameters
    ----------
    feature_matrix : np.ndarray
        Array of shape (n_samples, n_features). Each row is a temporal
        measurement; each column is an engineered feature.
    n_components : int
        Number of principal components to retain (default 1).

    Returns
    -------
    dict
        {
            "health": np.ndarray of shape (n_samples,),
            "explained_variance": float,
            "components": np.ndarray of shape (n_components, n_features),
        }
    """
    if feature_matrix.ndim != 2:
        raise ValueError("feature_matrix must be 2-D")

    n_samples, n_features = feature_matrix.shape
    if n_samples < 2 or n_features < 2:
        raise ValueError("Need at least 2 samples and 2 features")

    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(feature_matrix)

    pca = PCA(n_components=n_components)
    scores = pca.fit_transform(X_scaled)

    health = scores[:, 0].copy()

    if len(health) > 1:
        slope = np.polyfit(np.arange(len(health)), health, 1)[0]
        if slope < 0:
            health = -health

    return {
        "health": health,
        "explained_variance": float(pca.explained_variance_ratio_[0]),
        "components": pca.components_,
    }


def generate_synthetic_data(
    n_measurements: int = 50,
    n_features: int = 4,
    seed: int = 42,
) -> np.ndarray:
    """
    Generate synthetic vibration features for demonstration.

    Simulates bearing degradation by injecting a linear increasing trend
    into the first feature axis.
    """
    rng = np.random.default_rng(seed)
    X = rng.normal(loc=0.0, scale=1.0, size=(n_measurements, n_features))
    trend = np.linspace(0, 3.0, n_measurements)
    X[:, 0] += trend
    X += rng.normal(0, 0.2, X.shape)
    return X
