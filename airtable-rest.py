from flask import Flask, request, jsonify
app = Flask(__name__)

import os
import sys
from airtable import Airtable

@app.route('/getmsg/', methods=['GET'])
def respond():
  # Retrieve the name from url parameter
  name = request.args.get("name", None)

  # For debugging
  print(f"got name {name}")

  response = {}

  # Check if user sent a name at all
  if not name:
    response["ERROR"] = "no name found, please send a name"
  elif str(name).isdigit():
    response["ERROR"] = "name can't be numeric."
  else:
    response["MESSAGE"] = f"Welcome {name} to our awesome platform!!"

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
  base_key = 'appWi0DmmJUsA3mHD'
  table_name = 'Projects'

  # print(os.environ.get('AIR_KEY')) 
  # sys.stdout.flush()

  airtable = Airtable(base_key, table_name, api_key=os.environ['AIR_KEY'])

  records = airtable.get_all(view='Has Logo', maxRecords=10)

  # return airtable.get_all()
  return jsonify(records)

if __name__ == '__main__':
  # Threaded option to enable multiple instances for multiple user access support
  app.run(threaded=True, port=5000)
