# 🩺 Diabetes Prediction using Machine Learning

This project uses machine learning to predict whether a person is likely to have diabetes based on diagnostic health data. It leverages the Pima Indians Diabetes Dataset and applies various classification algorithms to build an accurate prediction model.


## 📊 Dataset

- **Source:** Pima Indians Diabetes Database
- **Attributes Used:**
  - Pregnancies
  - Glucose
  - BloodPressure
  - SkinThickness
  - Insulin
  - BMI
  - DiabetesPedigreeFunction
  - Age
  - Outcome (1: Diabetic, 0: Non-Diabetic)


## 💻 Technologies Used

- Python 🐍
- Pandas & NumPy
- Scikit-learn
- Matplotlib & Seaborn
- Jupyter Notebook

## ⚙️ Machine Learning Models Implemented

- Logistic Regression
- K-Nearest Neighbors (KNN)
- Decision Tree
- Random Forest
- Support Vector Machine (SVM)



## 📈 Model Evaluation

Each model is evaluated using:

- Accuracy Score
- Confusion Matrix
- Classification Report
- ROC Curve


## 🚀 How to Run

1. **Clone the repo:**
   ```bash
   git clone https://github.com/divyaredii/Diabetes-prediction.git
   cd Diabetes-prediction
````

2. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Jupyter Notebook:**

   ```bash
   jupyter notebook
   ```

4. Open `diabetes_prediction.ipynb` and run the cells.


## 🧠 Insights

* Feature correlation was analyzed to identify the most influential health factors.
* Random Forest and SVM achieved the highest accuracy in this experiment.
* Data normalization and handling of missing values helped improve performance.



## 📌 Future Improvements

* Integrate with a simple web interface using Streamlit or Flask.
* Add support for real-time prediction using user input.
* Optimize hyperparameters using Grid Search.



## 🙋‍♀️ Author

**Divya Reddy**
[GitHub Profile](https://github.com/divyaredii)



## 📄 License

This project is licensed under the MIT License. See the `LICENSE` file for details.




Let me know if you'd like me to generate a `requirements.txt` file, add images or graphs to the README, or create a `Streamlit` web version of the model.

