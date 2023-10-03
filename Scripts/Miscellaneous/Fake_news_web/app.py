from feature import *
from flask import Flask, render_template, request
from sklearn.externals import joblib

pipeline = joblib.load("pipeline.sav")

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/api", methods=["POST"])
def get_delay():
    result = request.form
    query_title = result["title"]
    query_author = result["author"]
    query_text = result["maintext"]
    print(query_text)
    query = get_all_query(query_title, query_author, query_text)
    ##user_input = {'query':query}
    pred = pipeline.predict(query)
    print(pred)
    dic = {1: "real", 0: "fake"}
    return f'<html><body><h1>{dic[pred[0]]}</h1> <form action="/"> <button type="submit">back </button> </form></body></html>'


if __name__ == "__main__":
    app.run(port=8080, debug=True)
