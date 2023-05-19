from flask import Flask, redirect, url_for, render_template, jsonify, request
import random

app= Flask(__name__)
lower_limit= 0
upper_limit= 100

@app.route("/")
def home():
    return render_template("index.html")

@app.route('/get_numbers', methods=['GET'])
def get_numbers():
    # Retrieve the numbers and sum from your data source or perform any necessary calculations
    num1 = random.randint(lower_limit, upper_limit)
    num2 = random.randint(lower_limit, upper_limit)

    sum= num1+num2

    # Return the numbers as a JSON response
    return jsonify({'num1': num1, 'num2': num2})

@app.route("/addition")
def addition():
    return render_template("addition_new.html")

@app.route("/n_back")
def nback():
    return "<h1>this is n back task</h1>"

@app.route("/stroop")
def stroop():
    return "<h1>this is stroop task</h1>"

@app.route("/texting_questions", methods=["GET"])
def fetch_random_question():
    question_list=["How are you doing today?",
                   "How is the weather outside?",
                   "Greetings, eleke",
                   "monday",
                   "tuesday",
                   "wednesday",
                   "thursday",
                   "friday",
                   "saturday",
                   "sunday"
                   ]
    
    rand_question= random.choice(question_list)

    return rand_question

# Define a list to store the conversation history
conversation = []

@app.route('/get_question', methods=['GET'])
def get_question():
    # Fetch a random question from your data source
    question = fetch_random_question()

    # Return the question and conversation history in the JSON response
    return jsonify({
        'question': question,
        'conversation': conversation
    })

@app.route('/send_answer', methods=['POST'])
def send_answer():
    # Retrieve the question and answer from the request payload
    question = request.json.get('question')
    answer = request.json.get('answer')

    # Check if the question and answer exist
    if question and answer:
        # Add the question and answer to the conversation history
        conversation.append({'content': question, 'type': 'question'})
        conversation.append({'content': answer, 'type': 'answer'})

        # Return a JSON response indicating success
        return jsonify({'success': True})
    else:
        # Return a JSON response indicating failure with an error message
        return jsonify({'success': False, 'error': 'Question or answer not provided'})


# # Define a list to store the conversation history
# conversation = []

# @app.route('/get_question', methods=['GET'])
# def get_question():
#     # Fetch the question from your data source
#     question = fetch_question_from_data_source()

#     # Return the question and conversation history in the JSON response
#     return jsonify({
#         'question': question,
#         'conversation': conversation
#     })

# @app.route('/send_answer', methods=['POST'])
# def send_answer():
#     # Retrieve the answer from the request payload
#     answer = request.json.get('answer')

#     # Check if the answer exists
#     if answer:
#         # Add the question and answer to the conversation history
#         conversation.append({'content': answer, 'type': 'answer'})

#         # Return a JSON response indicating success
#         return jsonify({'success': True})
#     else:
#         # Return a JSON response indicating failure with an error message
#         return jsonify({'success': False, 'error': 'Answer not provided'})

# @app.route('/send_answer', methods=['POST'])
# def send_answer():
#     # Retrieve the answer from the request payload
#     answer = request.json.get('answer')
#     answers_list=[]

#     # Check if the answer exists
#     if answer:
#         # Add the answer to the answers list
#         answers_list.append(answer)

#         # Return a JSON response indicating success
#         return jsonify({'success': True})
#     else:
#         # Return a JSON response indicating failure with an error message
#         return jsonify({'success': False, 'error': 'Answer not provided'})

@app.route("/texting")
def texting():
    return render_template("texting_new.html")

@app.route("/reading")
def reading():
    return "<h1>this is reading task</h1>"

if __name__ == "__main__":
    app.run(debug=True)