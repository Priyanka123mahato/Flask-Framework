from flask import Flask, render_template

# Create the Flask application
app = Flask(__name__)

# Define the home route (URL: "/")--# Running on http://127.0.0.1:8000
"""
@app.route("/") 
def hello_world():
    # This text will be shown in the browser when visiting the home page
    return "<p>Hello, World!</p>"
    
"""

# Define the route (URL: "/production")--# Visit: http://127.0.0.1:8000/production
@app.route("/production")
def products():
    # This text will appear in the browser when visiting /production
    return "<p>This is for production</p>"   


@app.route("/")
def rendering_template():
    
    return render_template('index.html')



# Entry point of the program
# "__main__" is executed only when you run this file directly
if __name__ == "__main__":
    # Run the Flask app in debug mode so errors appear in the browser
    # Default port is 5000, but you can set any port (here: 8000)
    app.run(debug=True, port=8000) 
