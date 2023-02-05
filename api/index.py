import openai
import os
from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)
openai.api_key = os.getenv("API_KEY")

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


@app.route("/question_to_code", methods=('GET', 'POST'))
def queston_to_code():
    if request.method == "POST":
        animal = request.form['user_input']
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=animal,
            temperature=0.7,
            max_tokens=4000,
        )
        return redirect(url_for('queston_to_code', result=response.choices[0].text))
    result = request.args.get("result")
    return render_template('code.html', result=result)

@app.route('/image_generation', methods=('GET', 'POST'))
def image_generation():
    if request.method == "POST":
        animal = request.form['user_input']
        response = openai.Image.create(
          prompt=animal,
          n=3,
          size="256x256",
        )
        return redirect(url_for('image_generation', result=response['data'][0]['url']))
    result = request.args.get("result")
    return render_template('image.html', result=result)



if __name__ == "__main__":
    app.run(debug=True)
