import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

dataset = pd.read_csv("C:/Users/VISHU/3D Objects/Machine Learning/Datasets/boston.csv")

X = dataset.drop('TAX', axis=1)
Y = dataset['TAX']

import pickle
from sklearn.model_selection import KFold
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
poly = PolynomialFeatures(degree = 3, include_bias = True)
X_poly = poly.fit_transform(X)
Regression = LinearRegression()
Regression.fit(X, Y)
pickle.dump(Regression, open('model.pkl', 'wb'))
model = pickle.load(open('model.pkl', 'rb'))