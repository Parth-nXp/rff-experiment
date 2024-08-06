import numpy as np

class Model:
    """Class to represent the RFF model and perform training."""

    def __init__(self, feature_dim, rff_dim, learning_rate):
        self.feature_dim = feature_dim
        self.rff_dim = rff_dim
        self.learning_rate = learning_rate
        self.W = np.random.randn(feature_dim, rff_dim)
        self.b = np.random.uniform(0, 2 * np.pi, rff_dim)
        self.model = np.random.randn(rff_dim)

    def compute_rff_features(self, x):
        """Compute Random Fourier Features."""
        return np.sqrt(2 / self.rff_dim) * np.cos(np.dot(x, self.W) + self.b)

    def train(self, x, y, num_iterations):
        """Train the model using the given data."""
        mse_values_per_iteration = np.zeros(num_iterations)
        z = self.compute_rff_features(x)

        for n in range(1, num_iterations):
            epsilon = y[n] - np.dot(self.model, z[n])
            self.model += self.learning_rate * z[n] * epsilon
            mse_values_per_iteration[n] = epsilon**2

        return mse_values_per_iteration
