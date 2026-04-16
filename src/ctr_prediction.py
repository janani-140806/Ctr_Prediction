import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split


def train_ctr_model(csv_path: str = "ads.csv", verbose: bool = True):
    """Load data, train a logistic regression model, and report test accuracy."""
    df = pd.read_csv(csv_path)

    feature_columns = ["age", "daily_time_spent", "area_income"]
    X = df[feature_columns]
    y = df["clicked"]

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.2,
        random_state=42,
        stratify=y,
    )

    model = LogisticRegression(max_iter=1000)
    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)

    if verbose:
        print("CTR model trained successfully")
        print(f"Test Accuracy: {accuracy:.2f}")

    return model, accuracy


def get_user_input():
    """Collect feature values for a single user from the console."""
    print("\nEnter user details to predict click-through behavior:")
    age = int(input("Age: "))
    daily_time_spent = float(input("Daily Time Spent: "))
    area_income = float(input("Area Income: "))
    return pd.DataFrame(
        [[age, daily_time_spent, area_income]],
        columns=["age", "daily_time_spent", "area_income"],
    )


def predict_click(model, user_features: pd.DataFrame):
    """Predict class and probability of ad click."""
    predicted_class = model.predict(user_features)[0]
    click_probability = model.predict_proba(user_features)[0][1]

    print(f"\nPredicted CTR Probability: {click_probability:.2%}")
    if predicted_class == 1:
        print("Prediction: User will CLICK the ad")
    else:
        print("Prediction: User will NOT click the ad")


if __name__ == "__main__":
    ctr_model, _ = train_ctr_model("ads.csv")
    user_data = get_user_input()
    predict_click(ctr_model, user_data)