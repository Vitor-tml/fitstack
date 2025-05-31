from src.data_processing import load_users, load_checkins
from src.feature_engineering import generate_features
from src.model import train_model
import matplotlib.pyplot as plt
import pandas as pd

# Carregar dados
users = load_users(num_users=50)
checkins = load_checkins(num_checkins=50, existing_users=users) 

# Gerar features
features = generate_features(users, checkins)

# Tratar NaN
numeric_features = features.select_dtypes(include=['number'])
features[numeric_features.columns] = features[numeric_features.columns].fillna(numeric_features.mean()) # Imputação pela média

#  Treinar modelo
model, score, columns = train_model(features)

print(f'R² no teste: {score:.2f}')

#  Importância das features
importancia = pd.Series(model.feature_importances_, index=columns)
importancia.sort_values().plot(kind='barh')
plt.title('Importância das Features')
plt.show()