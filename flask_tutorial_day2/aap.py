from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

# Create the Flask application
app = Flask(__name__)

# Configure the SQLite database
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///todo.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

# Database Model
class Todo(db.Model):
    slno = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    desc = db.Column(db.String(500), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f"{self.slno} - {self.title}"

# Route: Home Page
@app.route("/")
def rendering_template():
    return render_template("index.html")

# Route: Production
@app.route("/production")
def products():
    return "<p>This is for production</p>"

# Entry Point
if __name__ == "__main__":
    app.run(debug=True, port=8000)
