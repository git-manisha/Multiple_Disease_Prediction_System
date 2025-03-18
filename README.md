# Multiple Disease Prediction System

## Introduction
The **Multiple Disease Prediction System** is a machine learning-based web application developed using **Streamlit**. This project allows users to predict the likelihood of having Diabetes, Heart Disease, or Parkinson's Disease based on input medical parameters. The system is built using **Support Vector Machine (SVM) and Logistic Regression models**.

## Models Used
1. **Diabetes Prediction** - Support Vector Machine (SVM)
2. **Heart Disease Prediction** - Logistic Regression
3. **Parkinson's Disease Prediction** - Support Vector Machine (SVM)

## Features
- User-friendly web interface built with **Streamlit**.
- Machine learning models trained on medical datasets.
- Real-time predictions based on user input.
- Uses **pickle** files to load trained models.

## Installation and Setup
Follow these steps to set up and run the project:

### 1. Clone the Repository
```sh
git clone https://github.com/git-manisha/Multiple_Disease_Prediction_System.git
cd Multiple_Disease_Prediction_System
```

### 2. Create and Activate a Virtual Environment
#### For Windows:
```sh
python -m venv streamlit_env
streamlit_env\Scripts\activate
```
#### For macOS/Linux:
```sh
python3 -m venv streamlit_env
source streamlit_env/bin/activate
```

### 3. Install Required Dependencies
```sh
pip install -r requirements.txt
```

### 4. Run the Streamlit App
```sh
streamlit run "C:\Users\manis\PycharmProjects\Multiple_Disease_Prediction\streamlit_env\multiple_disease_pred.py"
```

## File Structure
```
Multiple-Disease-Prediction-System/
│── models/
│   ├── diabetes_model.sav
│   ├── heart_disease_model.sav
│   ├── parkinsons_model.sav
│── streamlit_env/
│   ├── multiple_disease_pred.py  # Main Streamlit application
│── datasets/
│   ├── diabetes.csv
│   ├── heart.csv
│   ├── parkinsons.csv
│── requirements.txt
│── README.md
```

## Dependencies
Ensure the following libraries are installed:
```sh
streamlit
scikit-learn
pandas
numpy
pickle
```

## Usage
1. Open the **Multiple Disease Prediction System** in your web browser.
2. Select the disease you want to predict (Diabetes, Heart Disease, or Parkinson's Disease).
3. Enter the required medical parameters.
4. Click the "Predict" button to get the result.

## Contributing
Contributions are welcome! If you'd like to improve the project, please follow these steps:
1. Fork the repository.
2. Create a new branch (`feature-branch`).
3. Commit your changes.
4. Push to your branch and submit a pull request.

## License
This project is licensed under the **MIT License**.

---
**Author:** Manisha Soni  
**Contact:** git-manisha

