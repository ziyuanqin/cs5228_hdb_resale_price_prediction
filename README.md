# cs5228_hdb_resale_price_prediction

## Task Description

The resale market of HDB flats is big business in Singapore. To find a good prices as either a buyer or a seller, it is important to have good understanding of what affects the market value of a HDB flat. Most people would accept that attributes such as the size and type of flat, its floor, but also its location to nearby amenities (e.g., MRT stations, parks, malls, commercial centers) influence the resale price of the flat. However, it is not obvious which attributes are indeed most important in a quantified sense.

The goal of this project is to predict the resale price of a HDB flat based on its properties (e.g., size, #rooms, type, model, location). It is therefore first and foremost a regression task. Besides to prediction outcome in terms of a dollar value, other useful results include the importance of different attributes, the evaluation and comparison of different regression techniques, an error analysis and discussion about limitations and potential extensions, etc.

## Evaluation

The evaluation metric for this competition is Root Mean Squared Error (RSME). The RSME is a common metric to evaluate regression tasks. We use the RSME (instead of the Mean Squared Error) so that the error values have the correct unit, which is SGD for this task.

## Code Structure

This project trains and evaluates multiple regression models on a given dataset.
It includes both classical linear models (Linear Regression, Lasso, Ridge) and modern ensemble and non-parametric methods (LightGBM, XGBoost, Random Forest, CatBoost, KNN, and Neural Networks).

The best-performing models for each approach are saved automatically in the best_models/ directory for later comparison and reuse.

```graphql
project/
│
├── dataset/                           # Dataset directory
│   ├── original/                      # Original data files
│   │   ├── train.csv
│   │   └── test.csv
│   │
│   ├── auxiliary-data/                # Auxiliary or external supporting data
│   │
│   └── processed-data/                # Preprocessed data used for training
│
├── best_models/                       # Stores the best-performing models from each algorithm
│
├── eda.ipynb                          # Exploratory Data Analysis (EDA)
│
├── data_preprocessing.ipynb           # Data cleaning and feature engineering
│
├── regression_LGBM_XGB.ipynb          # Implements regression models:
│                                      # Linear Regression, Lasso, Ridge, LightGBM, XGBoost
│
├── RandomForest_CatBoost.ipynb        # Implements Random Forest and CatBoost models
│
├── models_without_auxdata.ipynb       # Models without auxiliary data
│
├── KNN_NN.ipynb                       # Implements K-Nearest Neighbors (KNN) and Neural Network models
│
└── README.md                          # Project documentation

```
