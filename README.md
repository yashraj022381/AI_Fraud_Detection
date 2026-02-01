[![Python](https://img.shields.io/badge/Python-3.10-blue)](https://www.python.org/)
[![Gradio](https://img.shields.io/badge/UI-Gradio-orange)](https://gradio.app/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

# AI_Fraud_Detection

- A simple AI-powered app to detect credit card fraud using Isolation Forest (anomaly detection) and rule-based checks. Built with Gradio for an interactive UI.

1. ## Features
- Input transaction details (amount, hour, distance, international, PIN/chip use, merchant category)
- ML-based anomaly detection
- Rule-based warnings for suspicious patterns (high amount, strange time, international)
- Adjustable anomaly threshold slider for sensitivity tuning

2. ## Setup
i) Clone the repo:
    git clone https://github.com/yourusername/AI-Fraud-Detection.git
    cd AI-Fraud-Detection

ii) Install dependencies:
   pip install -r requirements.txt
     - Python
     - Scikit-learn (Isolation Forest)
     - Gradio (UI)
     - Pandas, Joblib

iii). Run the app:
    python app.py

iv). Open the local URL in your browser (e.g., http://127.0.0.1:7860)

3. ## Usage
   - Enter transaction details
   - Adjust threshold slider (lower = more sensitive to fraud)
   - Click "Check for Fraud"
   - See result, anomaly score, and any rule warnings

4. ## Screenshots
   
   - Overview UI
     ![IMG_20260201_142715738](https://github.com/user-attachments/assets/1b58e61b-6aaa-478e-a4c3-9969a8a4217c)
     ![IMG_20260201_142618501](https://github.com/user-attachments/assets/c0ba1f5c-9d03-45f0-beb3-55b1e2937735)

   - Test Name
     
     (1) Normal Daytime low amount:
         ![IMG_20260201_143141910_HDR](https://github.com/user-attachments/assets/ce423922-dcc4-4bfe-9199-977781233409)
         ![IMG_20260201_143154839_HDR](https://github.com/user-attachments/assets/3aa4022c-0cbf-47ad-bc15-795cc1b8704f)

     (2) Normal nighttime low amount:
         ![IMG_20260201_143559665_HDR](https://github.com/user-attachments/assets/cd5b3eab-328e-4da3-b056-4379a6de987d)
         ![IMG_20260201_143615525_HDR](https://github.com/user-attachments/assets/76948461-967c-4060-8081-51ba3894511a)

     (3) Rule suspicious - strange time:
         ![IMG_20260201_144826656_HDR](https://github.com/user-attachments/assets/3fef7316-d743-42ef-bd3d-52b9df117b98)
         ![IMG_20260201_144859805_HDR](https://github.com/user-attachments/assets/5d984794-a26c-4748-988d-31f50f981e98)

     (4) Rule suspicious - high amount:
         ![IMG_20260201_145117975_HDR](https://github.com/user-attachments/assets/c3ea2e91-b8ee-4b0c-a57a-9f8dfb2faedf)
         ![IMG_20260201_145157220_HDR](https://github.com/user-attachments/assets/0fe09259-f2be-4548-ae27-e1bba6a6781e)

     (5) Rule suspicious - international:
         ![IMG_20260201_145354369_HDR](https://github.com/user-attachments/assets/dd3bb79d-aed2-4c58-ae95-437e185070e5)
         ![IMG_20260201_145423245_HDR](https://github.com/user-attachments/assets/22e77739-2a4a-4d6a-9dc6-c0e732b78289)

     (6) Multiple rules triggered:
         ![IMG_20260201_145654927_HDR](https://github.com/user-attachments/assets/fb42c857-01d8-4b89-aae7-a7bf2ad7092e)
         ![IMG_20260201_145715407_HDR](https://github.com/user-attachments/assets/ab6dfc28-fb50-4a94-b8f4-c68f37218f86)

     (7) Borderline ML fraud (low threshold):
         ![IMG_20260201_150026027_HDR](https://github.com/user-attachments/assets/60a8cb6a-9ebb-451e-bbfa-9d3424682106)
         ![IMG_20260201_150046275_HDR](https://github.com/user-attachments/assets/c73ddc70-22d8-49fa-9a4e-f5b68be249fd)

     (8) Same input - strict threshold:
         ![IMG_20260201_150259819_HDR](https://github.com/user-attachments/assets/157c97be-e4eb-4522-b4b4-cd4666d7d6f1)
         ![IMG_20260201_150343423_HDR](https://github.com/user-attachments/assets/f6660724-f1e8-4f75-a5c2-1819146173e5)

     (9) Extreme fraud case:
         ![IMG_20260201_150603161_HDR](https://github.com/user-attachments/assets/1011a920-5c56-4574-9633-ea1d56405bbf)
         ![IMG_20260201_150617084_HDR](https://github.com/user-attachments/assets/5f36d9f1-e291-44fe-a0d3-16067340c8ef)

     (10) After test Clear History:
          ![IMG_20260201_150841638_HDR](https://github.com/user-attachments/assets/39c7917b-f556-47e5-be8d-68c17253e681)
          ![IMG_20260201_150850846_HDR](https://github.com/user-attachments/assets/a24d263f-cb14-4341-8d3e-1813dcb496c5)

5. ## Technologies
   - Python
   - Scikit-learn (Isolation Forest)
   - Gradio (UI)
   - Pandas
   - Joblib
  
6. ## Live Demo
    

## Future Improvements

- Integrate with real API for live data

Developed by Yashraj — Mumbai, India
