import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import joblib

def load_data(file_path):
    """Load the dataset from CSV file."""
    df = pd.read_csv(file_path)
    print(f"Dataset loaded with shape: {df.shape}")
    return df

def preprocess_data(df):
    """Preprocess the data: handle missing values, scale features."""
    print("Missing values before preprocessing:")
    print(df.isnull().sum())

    numerical_cols = df.select_dtypes(include=['float64', 'int64']).columns
    df[numerical_cols] = df[numerical_cols].fillna(df[numerical_cols].mean())

    
    if 'clicked' in df.columns:
        X = df.drop('clicked', axis=1)
        y = df['clicked']
    else:
        X = df
        y = None

    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    print("Preprocessing completed.")
    return X_scaled, y, scaler

def train_model(X, y):
    """Train RandomForest model."""
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    print(f"Model Accuracy: {accuracy:.2f}")
    print("Classification Report:")
    print(classification_report(y_test, y_pred))

    return model, accuracy

def save_model(model, scaler, model_path='models/ctr_model.pkl', scaler_path='models/scaler.pkl'):
    """Save the trained model and scaler."""
    joblib.dump(model, model_path)
    joblib.dump(scaler, scaler_path)
    print("Model and scaler saved.")

if __name__ == "__main__":
    df = load_data('data/ads.csv')

    
    X, y, scaler = preprocess_data(df)

    model, accuracy = train_model(X, y)

    save_model(model, scaler)
