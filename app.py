from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def home():
    return open("index.html").read()

@app.route("/age", methods=["POST"])
def age():
    age = int(request.form.get("age"))

    if age >= 18:
        return "Kirish mumkin"
    else:
        return "Kirish mumkin emas"

app.run(debug=True)
