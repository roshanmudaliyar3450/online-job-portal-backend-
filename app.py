from flask import Flask, jsonify
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
CORS(app)

# Database configuration
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

# Job Model
class Job(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))

# Create tables
with app.app_context():
    db.create_all()

@app.route("/")
def home():
    return jsonify({"message": "Backend is running with Database"})

@app.route("/jobs")
def jobs():
    job_list = Job.query.all()
    return jsonify([
        {"id": job.id, "title": job.title}
        for job in job_list
    ])

@app.route("/add-job")
def add_job():
    new_job = Job(title="Backend Developer")
    db.session.add(new_job)
    db.session.commit()
    return jsonify({"message": "Job added successfully"})

if __name__ == "__main__":
    app.run(debug=True)