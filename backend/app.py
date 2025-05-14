from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Sample word dictionary for autocompletion
word_list = [
    "apple", "application", "apply", "appoint", "appreciate", "banana",
    "basket", "bat", "battle", "cat", "catch", "cater", "dog", "door",
    "cat","carrom","cash","castle"
]

@app.route('/autocomplete', methods=['POST'])
def autocomplete():
    data = request.get_json()
    prefix = data.get("prefix", "").lower()

    suggestions = [word for word in word_list if word.startswith(prefix)]
    return jsonify({"suggestions": suggestions})

if __name__ == '__main__':
    app.run(debug=True)
