from flask import Flask, jsonify, request
from flask_cors import CORS
from game import get_today_word, check_guess, valid_word

app = Flask(__name__)
CORS(app)

@app.route("/check", methods=["POST"])
def wordle():
    data = request.json
    guess = data["guess"]

    if not valid_word(guess):
        return jsonify({"error": "invalid guess"})

    answer = get_today_word()
    result = check_guess(guess, answer)

    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True)
