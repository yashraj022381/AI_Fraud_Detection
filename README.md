# AI_Fraud_Detection

A simple AI-powered app to detect credit card fraud using Isolation Forest (anomaly detection) and rule-based checks. Built with Gradio for an interactive UI.

## Features
- Input transaction details (amount, hour, distance, international, PIN/chip use, merchant category)
- ML-based anomaly detection
- Rule-based warnings for suspicious patterns (high amount, strange time, international)
- Adjustable anomaly threshold slider for sensitivity tuning

## Setup
1. Clone the repo:
    git clone https://github.com/yourusername/AI-Fraud-Detection.git
    cd AI-Fraud-Detection

2. Install dependencies:
   pip install -r requirements.txt
     - Python
     - Scikit-learn (Isolation Forest)
     - Gradio (UI)
     - Pandas, Joblib

4. Run the app:
    python app.py

5. Open the local URL in your browser (e.g., http://127.0.0.1:7860)

    ## Usage
    - Enter transaction details
    - Adjust threshold slider (lower = more sensitive to fraud)
    - Click "Check for Fraud"
    - See result, anomaly score, and any rule warnings

    ## Screenshots
    ### Overview UI
    ![UI Overview](screenshots/ui-overview.png)

    ### Normal Transaction
    ![Normal Result](screenshots/normal-result.png)

    ### Fraud Alert
    ![Fraud Alert](screenshots/fraud-alert.png)

    ## Technologies
     - Python
     - Scikit-learn (Isolation Forest)
     - Gradio (UI)
     - Pandas, Joblib

## Future Improvements
- Add more features (e.g. user history)
- Integrate with real API for live data

Developed by Yashraj — Mumbai, India
