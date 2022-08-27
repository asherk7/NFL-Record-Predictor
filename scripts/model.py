"""
Machine Learning model for the record prediction
"""

import glob
import os
import pandas as pd
from sklearn.tree import DecisionTreeRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error

#merging all csv files into one
csv_files = glob.glob(os.path.join('C:\\Users\\mashe\\Desktop\\NFL-Record-Predictor\\data\\clean', '*.csv'))
dataframes = []
for csvfile in csv_files:
    df = pd.read_csv(csvfile)
    dataframes.append(df)
result = pd.concat(dataframes, ignore_index=True)
#result.to_csv('C:\\Users\\mashe\\Desktop\\NFL-Record-Predictor\\data\\raw\\team_data.csv', index=False)

stat_file_path = 'C:\\Users\\mashe\\Desktop\\NFL-Record-Predictor\\data\\clean\\team_data.csv'
team_data = pd.read_csv(stat_file_path)

#split data to train model and validate prediction
train_X, val_X, train_y, val_y = train_test_split(team_data.drop(columns=['Average Age', 'Record Prediction', 'QB', 'RB', 'WR', 'OL', 'DL', 'LB', 'S', 'CB', 'Win Percentage'], axis=1), team_data['Win Percentage'], random_state=0)

data_model = DecisionTreeRegressor()
data_model.fit(train_X,train_y)
val_pred = data_model.predict(val_X)
mean_absolute_error(val_y, val_pred)