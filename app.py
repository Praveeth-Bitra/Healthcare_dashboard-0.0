from flask import Flask, render_template
import pandas as pd
import os

app = Flask(__name__, template_folder=os.path.abspath('templates'))

csv_file = "healthcare_dataset.csv"

@app.route('/')
def home():
    try:
        df = pd.read_csv(csv_file)

        # Count number of patients per Blood Type
        blood_counts = df["Blood Type"].value_counts()

        blood_types = blood_counts.index.tolist()
        patients = blood_counts.values.tolist()

        print("🔹 Blood Types:", blood_types)
        print("🔹 Patient Counts:", patients)

    except Exception as e:
        blood_types = ["Error"]
        patients = [0]
        print("⚠️ CSV Load Error:", e)

    return render_template("index.html", hospitals=blood_types, patients=patients)

if __name__ == '__main__':
    app.run(debug=True)
