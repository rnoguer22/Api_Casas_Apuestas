import pandas as pd
from sklearn.ensemble import RandomForestClassifier

class Prediction:

    def __init__(self, data_path):
        self.data_path = data_path

    
    def make_predictions(self):
        df = pd.read_csv(self.data_path, encoding='utf-8')
        X = df.iloc[:, 2:].values
        y = df.iloc[:, 1].values
        clf = RandomForestClassifier(n_estimators=100, criterion='entropy')
        clf.fit(X, y)