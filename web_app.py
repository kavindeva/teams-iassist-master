"""
Deploy Flask App in IIS Server
"""
from flask import Flask

app = Flask(__name__)


@app.route("/msteams")
def home():
    return "Hello, Welcome to iAssist MSTeams"


if __name__ == "__main__":
    app.run()
