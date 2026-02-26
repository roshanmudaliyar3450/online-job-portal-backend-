from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/")
def home():
    return jsonify({"message": "Backend is running"})

@app.route("/jobs")
def jobs():
    return jsonify([
        {"id": 1, "title": "Frontend Developer"},
        {"id": 2, "title": "Python Developer"}
    ])

if __name__ == "__main__":
    app.run(debug=True)