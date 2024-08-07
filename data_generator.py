import numpy as np

class DataGenerator:
    """Class to generate synthetic data for the experiment."""
    
    def __init__(self, num_iterations, feature_dim):
        self.num_iterations = num_iterations
        self.feature_dim = feature_dim

    def generate_parameters(self):
        """Generate random parameters for the experiment."""
        self.theta_k = np.random.uniform(0.2, 0.9)
        self.mu_k = np.random.uniform(-0.2, 0.2)
        self.sigma2_uk = np.random.uniform(0.2, 1.2)
        self.sigma2_nuk = np.random.uniform(0.005, 0.03)
        self.uk = np.random.normal(self.mu_k, np.sqrt(self.sigma2_uk), (self.num_iterations, self.feature_dim))
        self.nuk = np.random.normal(0, np.sqrt(self.sigma2_nuk), (self.num_iterations, 1))

    def generate_data(self):
        """Generate x and y data based on the generated parameters."""
        x = np.zeros((self.num_iterations, self.feature_dim))
        y = np.zeros((self.num_iterations, 1))
        x[0] = self.uk[0]  # Initial value

        for n in range(1, self.num_iterations):
            x[n] = self.theta_k * x[n-1] + np.sqrt(1 - self.theta_k**2) * self.uk[n]
            y[n] = (np.sqrt(x[n, 0]**2 + np.sin(np.pi * x[n, 3])**2) + 
                    (0.8 - 0.5 * np.exp(-x[n, 1]**2)) * x[n, 2] + self.nuk[n])
        
        return x, y
