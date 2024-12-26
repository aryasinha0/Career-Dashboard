from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [
    {'id':1, 'title':'Data Analyst', 'Location':'Bangaluru, India', 'Salary': 'Rs. 1,00,000'},
    {'id':2, 'title':'Data Scientist', 'Location':'Delhi, India', 'Salary': 'Rs. 15,00,000'},
    {'id':3, 'title':'Python Developer', 'Location':'Hyderabad, India', 'Salary': 'Rs. 8,00,000'},
    {'id':4, 'title':'Backend Engineer', 'Location':'Remote, India', 'Salary': 'Rs. 10,00,000'}


]

@app.route("/")
def home():
    return render_template('home.html',jobs = JOBS)

@app.route("/api/jobs")
def list_jobs():
    return jsonify(JOBS)


if __name__ == "__main__":
    app.run(debug=True)