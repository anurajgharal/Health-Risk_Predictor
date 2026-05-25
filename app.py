from flask import Flask, render_template, request

app = Flask(__name__)

# ==========================================
# HOME PAGE
# ==========================================

@app.route("/")
def home():
    return render_template("index.html")


# ==========================================
# PREDICTION
# ==========================================

@app.route("/predict", methods=["POST"])
def predict():

    # GET VALUES

    gender = request.form["gender"]
    age = int(request.form["age"])
    occupation = request.form["occupation"]

    sleep_duration = float(
        request.form["sleep_duration"]
    )

    quality_of_sleep = int(
        request.form["quality_of_sleep"]
    )

    physical_activity = int(
        request.form["physical_activity"]
    )

    stress_level = int(
        request.form["stress_level"]
    )

    bmi_category = request.form["bmi_category"]

    blood_pressure = request.form["blood_pressure"]

    heart_rate = int(
        request.form["heart_rate"]
    )

    daily_steps = int(
        request.form["daily_steps"]
    )

    # ======================================
    # HEALTH SCORE LOGIC
    # ======================================

    score = 0

    # Sleep Duration

    if sleep_duration >= 7:
        score += 20
    else:
        score -= 10

    # Sleep Quality

    score += quality_of_sleep * 3

    # Physical Activity

    score += physical_activity * 2

    # Stress Level

    score -= stress_level * 2

    # Heart Rate

    if 60 <= heart_rate <= 100:
        score += 15
    else:
        score -= 10

    # Daily Steps

    if daily_steps >= 7000:
        score += 20
    else:
        score -= 5

    # BMI

    if bmi_category == "Normal":
        score += 15

    elif bmi_category == "Overweight":
        score -= 5

    else:
        score -= 15

    # Blood Pressure

    if blood_pressure == "Normal":
        score += 10

    else:
        score -= 10

    # Age

    if age > 50:
        score -= 10
  

    if score > 100:
       score = 100

    if score < 0:
       score = 0

    # ======================================
    # FINAL RESULT
    # ======================================

    if score >= 70:

        result = "✅ Healthy Lifestyle"

    elif score >= 40:

        result = "⚠️ Moderate Lifestyle Risk"

    else:

        result = "🚨 Poor Lifestyle Health"

    # ======================================
    # SUGGESTIONS
    # ======================================

    suggestions = []

    if sleep_duration < 7:
        suggestions.append(
            "Improve your sleep duration."
        )

    if stress_level > 6:
        suggestions.append(
            "Try meditation and stress management."
        )

    if daily_steps < 7000:
        suggestions.append(
            "Walk more daily."
        )

    if bmi_category == "Obese":
        suggestions.append(
            "Maintain healthy body weight."
        )

    if blood_pressure != "Normal":
        suggestions.append(
            "Monitor your blood pressure regularly."
        )

    return render_template(
        "index.html",
        prediction_text=result,
        score=score,
        suggestions=suggestions,
        form_data=request.form
    )


# ==========================================
# RUN APP
# ==========================================

if __name__ == "__main__":
    app.run(debug=True)
