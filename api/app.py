from flask import Flask
app = Flask(__name__)

@app.route("/api/python")
def hello_world():
    return "<p>Hello, World!</p>"

# if __name__ == "__main__":
#     # if use FLASK_DEBUG=1 python api/app.py
#     app.run(host='0.0.0.0', port=5328, debug=True)