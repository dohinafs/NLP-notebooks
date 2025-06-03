from flask import Flask
from flask import request
from flask import jsonify

app=Flask(__name__)

# if __name__ == '__main__':
    
    
data=[
    {'name':'John Doe', 'ClaimID': '1234556', 'Loss':'Water-damage', 'Insurer': 'State-Farms', 'Date':'April 20,2025'},
    {'name':'Paige Turner', 'ClaimID':'9876544','Loss':'Auto-damage','Insurer':'xyz-farms', 'Date':'May 2, 2025'}
]

@app.route('/data', methods=['POST'])
def add_data():
    new_data=request.get_json()
    data.append(new_data)
    return jsonify(new_data), 201

@app.route('/data', methods=['GET'])
def get_data():
    return jsonify(data)


app.run(debug=True, port=8089)
