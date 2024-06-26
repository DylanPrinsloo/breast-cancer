import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix

# Step 1: Data Collection
data = pd.read_csv('sensor_data.csv')

# Step 2: Data Preprocessing
data = data.dropna()  # Remove missing values
# Normalize the data
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
scaled_data = scaler.fit_transform(data.drop('maintenance_needed', axis=1))

# Step 3: Feature Engineering
# (Assume feature engineering has been done and data is ready)

# Step 4: Model Selection
X = scaled_data
y = data['maintenance_needed']

# Step 5: Model Training
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Step 6: Model Evaluation
y_pred = model.predict(X_test)
print(confusion_matrix(y_test, y_pred))
print(classification_report(y_test, y_pred))

# Step 7: Model Deployment
# Save the model for deployment
import joblib
joblib.dump(model, 'predictive_maintenance_model.pkl')

# To load the model and make predictions:
# loaded_model = joblib.load('predictive_maintenance_model.pkl')
# new_data = scaler.transform(new_sensor_data)
# predictions = loaded_model.predict(new_data)
