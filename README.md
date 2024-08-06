# Random Fourier Features Model Experiment

This project simulates an experiment using Random Fourier Features (RFF) to approximate a non-linear function. The experiment is repeated multiple times, and the mean squared error (MSE) is calculated and plotted over iterations.

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
