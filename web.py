from flask import Flask,render_template
app = Flask(__name__)

@app.route("/")
def welcome():
    return render_template('starter-page.html')

@app.route("/index")
def index():
    return render_template('index.html')

@app.route("/service-details")
def service():
    return render_template('service-details.html')

app.run(debug=True)