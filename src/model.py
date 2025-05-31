from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from lightgbm import LGBMRegressor
import pandas as pd

def train_model(features):
    le = LabelEncoder()
    features['gender_encoded'] = le.fit_transform(features['gender'])

    X = features[['gender_encoded', 'age', 'total_checkins', 'recency_days',
                  'avg_days_between', 'Summer', 'Autumn', 'Winter', 'Spring']]

    # Gerando um score simulado
    features['engagement_score'] = (
        features['total_checkins'] * 10
        - features['recency_days'] * 0.5
        - features['avg_days_between'] * 2
        + (features['Winter'] * 5)
    ) + pd.Series([5]*len(features))

    y = features['engagement_score']

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.3, random_state=42
    )

    model = LGBMRegressor()
    model.fit(X_train, y_train)
    score = model.score(X_test, y_test)

    return model, score, X.columns
