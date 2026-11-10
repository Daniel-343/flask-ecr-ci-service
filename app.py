from flask import Flask

app = Flask(__name__)


def greeting():
    return "Hello, CSK!, change #1 by daniel"


@app.route("/")
def index():
    return greeting() + "\n"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
