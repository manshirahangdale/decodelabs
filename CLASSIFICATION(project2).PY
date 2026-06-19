import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
from sklearn.impute import SimpleImputer

# Load data
df = pd.read_csv('exoplanets.csv')
print(df.head())
print(df.info())
print(df.shape)

print(df['Discovery method'].value_counts())

# Keep only top 4 methods with reasonable sample sizes
top_methods = ['transit', 'radial vel.', 'microlensing', 'imaging']
df = df[df['Discovery method'].isin(top_methods)]

print(df.shape)
print(df['Discovery method'].value_counts())

# Convert numeric columns (stored as text) to actual numbers
numeric_cols = ['Mass (MJ)', 'Radius (RJ)', 'Period (days)', 
                 'Semi-major axis (AU)', 'Temp. (K)', 
                 'Host star mass (M☉)', 'Host star temp. (K)']

for col in numeric_cols:
    df[col] = pd.to_numeric(df[col], errors='coerce')

print(df[numeric_cols].info())
print(df[numeric_cols].isnull().sum())

# Select features - dropping Temp. (K) and Mass (MJ) due to too many missing values
features = ['Radius (RJ)', 'Period (days)', 'Semi-major axis (AU)', 
            'Host star mass (M☉)', 'Host star temp. (K)']

X = df[features]
y = df['Discovery method']

# Impute missing values with median instead of dropping rows
# This keeps minority classes (microlensing, radial vel.) intact
imputer = SimpleImputer(strategy='median')
X_imputed = pd.DataFrame(imputer.fit_transform(X), columns=features)

print("Final dataset shape:", X_imputed.shape)
print(y.value_counts())

# Split into train and test sets
X_train, X_test, y_train, y_test = train_test_split(
    X_imputed, y, test_size=0.2, random_state=42, stratify=y
)

print("Train shape:", X_train.shape)
print("Test shape:", X_test.shape)

# Train Random Forest model
# class_weight='balanced' helps the model pay more attention to minority classes
model = RandomForestClassifier(n_estimators=100, random_state=42, class_weight='balanced')
model.fit(X_train, y_train)

# Predict on test set
y_pred = model.predict(X_test)

# Evaluate
accuracy = accuracy_score(y_test, y_pred)
print(f"\nModel Accuracy: {accuracy:.2%}")

print("\nClassification Report:")
print(classification_report(y_test, y_pred, zero_division=0))

# Check feature importance
importance = pd.Series(model.feature_importances_, index=features)
print("\nFeature Importance:")
print(importance.sort_values(ascending=False))