from flask import Flask, redirect, url_for, render_template, jsonify
import random

app= Flask(__name__)
lower_limit= 0
upper_limit= 100

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/addition")
def addition():
    return render_template("addition_test.html")

@app.route('/get_numbers_and_sum', methods=['GET'])
def get_numbers_and_sum():
    # Retrieve the numbers and sum from your data source or perform any necessary calculations
    num1 = random.randint(lower_limit, upper_limit)
    num2 = random.randint(lower_limit, upper_limit)

    result= num1+num2

    # Return the numbers as a JSON response
    return jsonify({'num1': num1, 'num2': num2, 'result': result})

@app.route("/n_back")
def nback():
    return "<h1>this is n back task</h1>"

@app.route("/stroop")
def stroop():
    return "<h1>this is stroop task</h1>"

@app.route("/texting")
def texting():
    return "<h1>this is texting task</h1>"

@app.route("/reading")
def reading():
    return "<h1>this is reading task</h1>"

if __name__ == "__main__":
    app.run(debug=True)