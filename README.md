# data-science-study-hours

# Project Overview
This project analyzes the relationship between student study hours and exam scores using linear regression. The dataset contains records of hours studied and corresponding test scores.

# Folder Structure
```
project-root/
├── data/                # Contains the dataset (score.csv)
├── scripts/             # Python scripts for data processing, analysis, and modeling
├── outputs/             # Processed data, models, and results
├── requirements.txt     # Required dependencies
├── README.md            # Project documentation
```


# Usage

## 1. Setup the Project:
Clone the repository.
Ensure you have Python installed.
Install required dependencies using the requirements.txt file:
```sh
pip install -r requirements.txt
```

## 2. Run Data Preprocessing
```sh
python scripts/01_data_preprocessing.py
```
This will clean the dataset and save the processed file in `outputs/cleaned_data.csv`.

## 3. Perform Exploratory Analysis
```sh
python scripts/02_exploratory_analysis.py
```
This script generates statistical summaries and visualizations, saving plots in `outputs/`.

## 4. Train the Regression Model
```sh
python scripts/03_regression_model.py
```
This script trains a linear regression model and saves it in `outputs/regression_model.pkl`.

## 5. Evaluate the Model
```sh
python scripts/04_model_evaluation.py
```
This script calculates performance metrics and saves them in `outputs/evaluation_results.txt`.

## 6. Generate Predictions
```sh
python scripts/05_generate_predictions.py
```
This script predicts student scores based on input study hours and saves results in `outputs/predictions.csv`.

# Requirements
- Python 3.x
- pandas
- matplotlib
- seaborn
- scikit-learn
- joblib

# Acknowledgments
dataset name: Student Study Hours

dataset author: Himanshu Nakrani
dataset source: https://www.kaggle.com/datasets/himanshunakrani/student-study-hours

