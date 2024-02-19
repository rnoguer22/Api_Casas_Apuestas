import pandas as pd
from sklearn.ensemble import RandomForestClassifier

class Prediction:

    def __init__(self, data_path):
        self.data_path = data_path

    
    def make_predictions(self, prediction_data_path):
        df = pd.read_csv(self.data_path, encoding='utf-8')
        df.drop(['Squad', 'id'], inplace=True, axis=1)
        X = df.iloc[:, 1:].values
        y = df.iloc[:, 0].values
        clf = RandomForestClassifier(n_estimators=100, criterion='entropy')
        clf.fit(X, y)

        prediction_data = pd.read_csv(prediction_data_path, encoding='utf-8')
        teams = prediction_data['Squad'].values
        prediction_data.drop(['Squad', 'id'], inplace=True, axis=1)
        X_pred = prediction_data.iloc[:, 1:]
        y_pred = clf.predict(X_pred)
        prediction_df = pd.DataFrame({'Squad':teams, 'Prediction':y_pred})
        return prediction_df
