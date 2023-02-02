import openai
import os
from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)
openai.api_key = os.environ.get('API_KEY')

@app.route("/", methods=("GET", "POST"))
def index():
    if request.method == "POST":
        animal = request.form["user_input"]
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt= animal,
            temperature=0.7,
            max_tokens=4000,
        )
        return redirect(url_for("index", result=response.choices[0].text))

    result = request.args.get("result")
    return render_template("index.html", result=result)


if __name__ == "__main__":
    app.run(debug=False)
