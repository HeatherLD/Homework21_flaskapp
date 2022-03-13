#!/usr/bin/env python
#pip install flask
from flask import Flask, json, render_template, request
import os

#create instance of Flask app
app = Flask(__name__)

#decorator
@app.route("/")
def echo_hello():
    return """Nobel Prize Recipients Data Access:
            (1) Add "all" to the end of the URL above to see all recipients
            (2) Add "all/year" to see a list of recipients from that year -- example: all/2008 """

@app.route("/all")
def prize_data():
    json_url = os.path.join(app.static_folder,"","nobel.json")
    data_json = json.load(open(json_url))

    return render_template('index.html',data=data_json)

@app.route("/all/<year>", methods=['GET'])
def prize_year(year):
    json_url = os.path.join(app.static_folder,"","nobel.json")
    data_json = json.load(open(json_url))

    data = data_json['year']
    #print(data)
    year = request.view_args['year']

    output_data = [x for x in data if x['year']==year]
    return render_template('index.html',data=output_data)

@app.route("/all/<category>", methods=['POST'])
def prize_subject(category):
    return 'Category: %s' % category



if __name__ == "__main__":
    app.run(debug=True)
