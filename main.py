import numpy as np
import matplotlib.pyplot as plt
from data_generator import DataGenerator
from model import Model

def main():
    independent_experiment = 500
    feature_dim = 4
    rff_dim = 200
    learning_rate = 0.75
    num_iterations = 1000

    mse_values_all_trials = np.zeros(num_iterations)

    for _ in range(independent_experiment):
        data_gen = DataGenerator(num_iterations, feature_dim)
        data_gen.generate_parameters()
        x, y = data_gen.generate_data()
        
        model = Model(feature_dim, rff_dim, learning_rate)
        mse_values_per_iteration = model.train(x, y, num_iterations)
        
        mse_values_all_trials += mse_values_per_iteration

    mse_values_all_trials /= independent_experiment
    mse_values_all_trials /= max(mse_values_all_trials)
    mse_value_all_trials = 10 * np.log10(mse_values_all_trials)

    plt.plot(mse_value_all_trials)
    plt.xlabel('Iteration')
    plt.ylabel('MSE (dB)')
    plt.title('MSE over iterations')
    plt.show()

if __name__ == "__main__":
    main()
