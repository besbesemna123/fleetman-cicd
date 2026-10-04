from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello depuis le conteneur Flask — host: {}\n".format(os.uname().nodename)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
