import pandas as pd
import yfinance as yf
from datetime import date
import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression

def calculate_beta(df,nifty):
    # Calculate the daily returns of the stock
    df['Returns'] = df['Close'].pct_change()

    # Replace 'benchmark_column' with the actual column name from the dataframe
    nifty['Nifty_Returns'] = nifty['Close'].pct_change()
    # Separate the independent variables (features) and the dependent variable (target)
    df = df.dropna()
    X = nifty['Nifty_Returns']
    y = df['Returns']

    # Fit a linear regression model
    model = LinearRegression()
    model.fit(X, y)

    # Get the beta coefficient (slope)
    beta = model.coef_[0]

    # Add the beta column to the DataFrame
    df['Beta'] = beta

    return df