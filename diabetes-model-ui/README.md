# Diabetes Prediction Model UI

This project provides a web-based user interface for a diabetes prediction model. The model is implemented in Python and utilizes machine learning techniques to predict the likelihood of diabetes based on user input.

## Project Structure

```
diabetes-model-ui
├── src
│   ├── model.py        # Implementation of the diabetes prediction model
│   ├── app.py          # Main application file that serves the web interface
│   └── static
│       └── h.html      # HTML user interface for data input
├── requirements.txt     # List of dependencies for the project
└── README.md            # Documentation for the project
```

## Setup Instructions

1. **Clone the repository**:
   ```
   git clone <repository-url>
   cd diabetes-model-ui
   ```

2. **Install dependencies**:
   Create a virtual environment (optional but recommended) and install the required packages:
   ```
   pip install -r requirements.txt
   ```

3. **Run the application**:
   Execute the following command to start the web server:
   ```
   python src/app.py
   ```

4. **Access the application**:
   Open your web browser and navigate to `http://127.0.0.1:5000` to access the diabetes prediction interface.

## Usage

- Fill out the form with the required information, including age, gender, BMI, glucose level, insulin level, blood pressure, diabetes pedigree, activity level, smoking status, family history, and HbA1c.
- Click the "Submit" button to send the data to the model for prediction.

## Overview of the Model

The diabetes prediction model is designed to analyze user input and provide a prediction based on historical data. The model is trained using various features that are known to influence diabetes risk, and it outputs the likelihood of a user having diabetes based on the provided inputs.

## Acknowledgments

- This project utilizes Flask for the web framework and scikit-learn for machine learning functionalities.
- Special thanks to the contributors and the open-source community for their valuable resources and libraries.