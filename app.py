from flask import Flask, render_template, request, redirect, url_for
import pymongo

app = Flask(__name__)

# Database connection
client = pymongo.MongoClient("mongodb+srv://carnage:0123456789@cluster0.yuqtmuo.mongodb.net/")
db = client["vdb"]
collection = db["vdb-tables"]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    your_name = request.form['yourName']
    their_name = request.form['theirName']
    their_number = request.form['theirNumber']
    message = request.form['message']

    # Insert data into MongoDB
    document = {"yourName": your_name, "theirName": their_name, "theirNumber": their_number, "message": message}
    collection.insert_one(document)
    print("message saved successfully")
    # Redirect to thank_you.html
    return redirect(url_for('thank_you'))

@app.route('/thank_you')
def thank_you():
    return render_template('thank_you.html')

