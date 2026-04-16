# CTR Prediction System

## Project Description

This is an AI/ML project for predicting Click Through Rate (CTR) using machine learning models. The system loads advertisement data, preprocesses it, trains a RandomForest classifier, and provides a web interface for making predictions.

## Features

- Data loading and preprocessing (handling missing values, feature scaling)
- RandomForest model training and evaluation
- Model persistence (save/load trained models)
- Streamlit web app for user-friendly predictions
- Beginner-friendly code with detailed comments

## Tech Stack

- **Programming Language:** Python
- **Libraries:** Pandas, Scikit-learn, Joblib, Streamlit
- **Model:** RandomForest Classifier

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/janani-140806/CTR-PREDICTION.git
   cd CTR-PREDICTION
   ```

2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Train the model:
   ```bash
   python main.py
   ```

2. Run the Streamlit app:
   ```bash
   streamlit run app.py
   ```

3. Open the browser and enter user details to get CTR predictions.

## Example Code

```python
# Load and preprocess data
df = load_data('data/ads.csv')
X, y, scaler = preprocess_data(df)

# Train model
model, accuracy = train_model(X, y)

# Make prediction
input_data = [[25, 60, 50000]]  # age, daily_time_spent, area_income
input_scaled = scaler.transform(input_data)
prediction = model.predict(input_scaled)
probability = model.predict_proba(input_scaled)[0][1]
print(f"CTR Probability: {probability:.2%}")
```

## Project Structure

```
CTR_prediction/
├── data/
│   ├── ads.csv
│   └── engagement_data.csv
├── models/
│   ├── ctr_model.pkl
│   └── scaler.pkl
├── src/
│   └── ctr_prediction.py
├── notebook/
├── app/
├── main.py
├── app.py
├── requirements.txt
└── README.md
```

## Step-by-Step: Run the Project

### 1) Install dependencies

```bash
npm install
```

### 2) Start MongoDB locally

Start your MongoDB service (example on Windows if installed as a service):

```bash
net start MongoDB
```

If your setup is different, run MongoDB using your normal method.

### 3) Start the backend server

```bash
npm start
```

You should see logs like:

- `Connected to MongoDB: ctrDB`
- `Server running at http://localhost:3000`

### 4) Open the application

Visit:

```text
http://localhost:3000
```

### 5) Test prediction flow

1. Fill out all form fields.
2. Click **Predict CTR**.
3. See predicted CTR on screen.
4. Confirm data saved in MongoDB (`ctrDB`, `predictions` collection).

---

## API Endpoint

### `POST /predict`

**Request JSON:**

```json
{
  "age": 25,
  "gender": "Female",
  "device": "Mobile",
  "category": "Tech",
  "time": "Evening"
}
```

**Response JSON (success):**

```json
{
  "success": true,
  "ctr": 75.0,
  "message": "CTR predicted and saved successfully."
}
```

---

## Notes

- Prediction logic is intentionally simple and rule-based for learning/demo purposes.
- You can later replace the logic with a trained ML model while keeping the same API flow.




=======
# CTR-PREDICTION
>>>>>>> ac54f3e7b4b6208fb1adb42d404708fa4c0d54d6
