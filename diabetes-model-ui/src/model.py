import pandas as pd
import joblib
import os

def preprocess_data(input_data):
    # Implement data preprocessing steps here
    # For example, scaling or encoding categorical variables
    return processed_data

def train_model(X_train, y_train):
    from sklearn.ensemble import RandomForestClassifier
    model = RandomForestClassifier()
    model.fit(X_train, y_train)
    return model

def predict(model, input_data):
    # Use the trained model to make predictions
    prediction = model.predict(input_data)
    return prediction

def load_model():
    import joblib
    model = joblib.load('diabetes_model.pkl')  # Load a pre-trained model
    return model

def save_model(model, best_model, label_encoder):
    import joblib
    joblib.dump(model, 'diabetes_model.pkl')  # Save the trained model for future use
    joblib.dump(best_model, 'best_model.pkl')
    joblib.dump(label_encoder, 'label_encoder.pkl')

def predict_diabetes(input_data):
    # Get the directory where model.py is located
    current_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Load the model and label encoder
    model = joblib.load(os.path.join(current_dir, '..', '..', 'best_model.pkl'))
    label_encoder = joblib.load(os.path.join(current_dir, '..', '..', 'label_encoder.pkl'))
    
    # Preprocess input data
    input_data['Gender'] = label_encoder.transform([input_data['gender']])[0]
    
    # Convert to proper format
    input_df = pd.DataFrame([[
        float(input_data['age']),
        input_data['Gender'],
        float(input_data['bmi']),
        float(input_data['glucose']),
        float(input_data['insulin']),
        float(input_data['bp']),
        float(input_data['pedigree']),
        input_data['activity'],
        input_data['smoker'],
        input_data['family'],
        float(input_data['hba1c'])
    ]], columns=['Age', 'Gender', 'BMI', 'Glucose', 'Insulin', 'BloodPressure', 'DiabetesPedigree',
                 'ActivityLevel', 'Smoker', 'FamilyHistory', 'HbA1c'])
    
    # One-hot encoding
    input_df = pd.get_dummies(input_df, columns=['ActivityLevel', 'Smoker', 'FamilyHistory'], drop_first=True)
    
    # Ensure all required columns are present
    expected_columns = model.feature_names_in_
    for col in expected_columns:
        if col not in input_df.columns:
            input_df[col] = 0
    
    # Reorder columns to match training data
    input_df = input_df[expected_columns]
    
    # Make prediction
    prediction = model.predict(input_df)
    
    # Convert prediction back to label
    result = label_encoder.inverse_transform(prediction)[0]
    
    return result