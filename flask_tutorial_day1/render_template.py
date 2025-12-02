from flask import Flask, render_template

# Create the Flask application
app = Flask(__name__)


@app.route("/")
def hello_world():
    
    return render_template('index2.html')

# Run the application
# "__main__" ensures this file runs only when executed directly
if __name__ == "__main__":
    
    app.run(debug=True, port=8000) 
