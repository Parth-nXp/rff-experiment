# Random Fourier Features Model Kernel Least Mean Square Algorithm

This project simulates an experiment using Random Fourier Features (RFF) to approximate a non-linear function. The experiment is repeated multiple times, and the mean squared error (MSE) is calculated and plotted over iterations.

This simulation is inspired by the work of J. Dong, Y. Zheng, and B. Chen, titled "A Unified Framework of Random Feature KLMS Algorithms and Convergence Analysis," presented at the 2018 International Joint Conference on Neural Networks (IJCNN) in Rio de Janeiro, Brazil. [Read the paper](https://doi.org/10.1109/IJCNN.2018.8489498).

## Project Structure

The project is divided into three main scripts:

1. **data_generator.py**
   - Contains the `DataGenerator` class, which generates synthetic data for the experiment.

2. **model.py**
   - Contains the `Model` class, which represents the RFF model and performs training.

3. **main.py**
   - The main script that runs the experiment, collects MSE values, and plots the results.

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/Parth-nXp/rff-experiment.git
    cd rff-experiment
    ```

2. Create a virtual environment and activate it:
    ```bash
    python -m venv rff-klms
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

Run the main script to start the experiment:
```bash
python main.py
```

## Troubleshooting

If you encounter any issues or errors while running the project, please check the following:

- Ensure all dependencies are installed correctly by running `pip install -r requirements.txt`.
  
- Make sure you are using a compatible version of Python (e.g., Python 3.6 or higher).
 
- If you encounter issues related to missing files or incorrect paths, verify that you are in the correct directory (`rff-experiment`).

If problems persist, feel free to open an issue on GitHub.

## Contributing

Contributions are welcome! If you have suggestions for improvements or bug fixes, please follow these steps:

1. Fork the repository.

2. Create a new branch (`git checkout -b feature-branch`).

3. Make your changes and commit them (`git commit -m 'Add some feature'`).

4. Push to the branch (`git push origin feature-branch`).

5. Open a pull request.

Please ensure your code follows the existing style and includes appropriate tests.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE.txt) file for details.

