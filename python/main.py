from flask import Flask, request

app = Flask(__name__)


@app.route("/validate")
def validate_word():
    return "TODO: validate word results"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3004, debug=True)
