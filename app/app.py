from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)

@app.route("/")
def index():
    df = pd.read_csv("data/processed/features.csv")
    score = round(df["tiger_index"].mean(), 2)
    return render_template("index.html", score=score)

if __name__ == "__main__":
    app.run(debug=True)