####### python3 helloflask.py

from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/test")
def hellotest():
    return "Hello World test !"

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=8080)
