from flask import Flask, request, render_template, flash
import pickle

app = Flask(__name__)
app.config['SECRET_KEY'] = 'supersecret'

# Load scaler and model
scaler = pickle.load(open('scaler.pkl', 'rb'))
model = pickle.load(open('svm_model.pkl', 'rb'))

# Define acceptable input limits
LIMITS = {
    'gluc': (70, 200),       # Glucose
    'bp': (40, 130),         # Blood Pressure
    'insulin': (15, 276),    # Insulin
    'bmi': (10.0, 60.0),     # BMI
    'func': (0.05, 2.5),     # Diabetes Pedigree Function
    'age': (10, 120)         # Age
}

@app.route('/', methods=['GET', 'POST'])
def home():
    prediction = None
    result_message = ""

    if request.method == 'POST':
        try:
            pregs = int(request.form.get('pregs'))
            gluc = int(request.form.get('gluc'))
            bp = int(request.form.get('bp'))
            skin = int(request.form.get('skin'))
            insulin = float(request.form.get('insulin'))
            bmi = float(request.form.get('bmi'))
            func = float(request.form.get('func'))
            age = int(request.form.get('age'))

            # Input validation
            errors = []
            if not (LIMITS['gluc'][0] <= gluc <= LIMITS['gluc'][1]):
                errors.append(f"Glucose must be between {LIMITS['gluc'][0]} and {LIMITS['gluc'][1]}")
            if not (LIMITS['bp'][0] <= bp <= LIMITS['bp'][1]):
                errors.append(f"Blood Pressure must be between {LIMITS['bp'][0]} and {LIMITS['bp'][1]}")
            if not (LIMITS['insulin'][0] <= insulin <= LIMITS['insulin'][1]):
                errors.append(f"Insulin must be between {LIMITS['insulin'][0]} and {LIMITS['insulin'][1]}")
            if not (LIMITS['bmi'][0] <= bmi <= LIMITS['bmi'][1]):
                errors.append(f"BMI must be between {LIMITS['bmi'][0]} and {LIMITS['bmi'][1]}")
            if not (LIMITS['func'][0] <= func <= LIMITS['func'][1]):
                errors.append(f"Diabetes Pedigree Function must be between {LIMITS['func'][0]} and {LIMITS['func'][1]}")
            if not (LIMITS['age'][0] <= age <= LIMITS['age'][1]):
                errors.append(f"Age must be between {LIMITS['age'][0]} and {LIMITS['age'][1]}")

            if errors:
                for error in errors:
                    flash(error)
                return render_template('index.html', prediction=None, result_message=None)

            # Make prediction
            input_features = [[pregs, gluc, bp, skin, insulin, bmi, func, age]]
            input_scaled = scaler.transform(input_features)
            prediction = model.predict(input_scaled)[0]

            result_message = "The person is diabetic." if prediction == 1 else "The person is not diabetic."

        except (ValueError, TypeError):
            flash("Invalid input. Please enter valid numeric values.")
            return render_template('index.html', prediction=None, result_message=None)

    return render_template('index.html', prediction=prediction, result_message=result_message)

if __name__ == '__main__':
    app.run(debug=True)
