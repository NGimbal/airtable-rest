from flask import Flask, request, jsonify
app = Flask(__name__)

import os
import sys
from airtable import Airtable

# http://localhost:5000/gettable/?table=Projects
@app.route('/gettable/', methods=['GET'])
def get_table():
  # Retrieve the name from url parameter
  table = request.args.get("table", None)

  # For debugging
  print(f"got name {table}")

  response = {}

  # Check if user sent a name at all
  if not table:
    response["ERROR"] = "no table found, please send a name"
  elif str(table).isdigit():
    response["ERROR"] = "table can't be numeric."
  else:
    base_key = 'appWi0DmmJUsA3mHD'
    # table_name = 'Projects'
    airtable = Airtable(base_key, table, api_key=os.environ['AIR_KEY'])
    records = airtable.get_all(view='Has Logo', maxRecords=10)
    response["MESSAGE"] = records

  return jsonify(response)

@app.route('/post/', methods=["POST"])
def post_something():
  param = request.form.get('name')
  print(param)

  if param:
    return jsonify({
      "Message": f"Welcome {name} to our awesome platform!!",
      "METHOD" : "POST"
    })
  else:
    return jsonify({
      "ERROR": "no name found, please send a name."
    })

# A welcome message to test our server
@app.route('/')
def index():
  # base_key = 'appWi0DmmJUsA3mHD'
  # table_name = 'Projects'

  # # print(os.environ.get('AIR_KEY')) 
  # # sys.stdout.flush()

  # airtable = Airtable(base_key, table_name, api_key=os.environ['AIR_KEY'])

  # records = airtable.get_all(view='Has Logo', maxRecords=10)

  # return airtable.get_all()
  return '<h1> Hi! </h1>'

if __name__ == '__main__':
  # Threaded option to enable multiple instances for multiple user access support
  app.run(threaded=True, port=5000)
