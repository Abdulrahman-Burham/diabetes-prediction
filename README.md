# Diabetes Type Prediction Web Application

A Flask web application that predicts diabetes types using machine learning.

## Setup

1. Install requirements:
```bash
pip install -r requirements.txt
```

2. Run the application:
```bash
python diabetes-model-ui/src/app.py
```

## Project Structure
- `src/`
  - `app.py`: Flask application
  - `model.py`: ML model interface
  - `templates/`: HTML templates
  - `best_model.pkl`: Trained model
  - `label_encoder.pkl`: Label encoder