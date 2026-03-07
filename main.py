"""
app.get
    param:
        num to convert
        units to convert to
    case (unit)
    hrs -> divide by 60
    days -> hrs, then divide by 24
    returns the converted num




"""

from flask import Flask, jsonify

app = Flask(__name__)

def calculate_conversion(num, unit):
    case (unit)
    #fill out different cases

@app.get('/unit_conversion')
def unit_conversion():
    num = request.args.get('num')
    unit = request.args.get('unit')
    if num and unit:
        #check for valid unit??
        result =  calculate_conversion(num, unit)
        return jsonify(result), 200
    else:
        return jsonify({"error": "Missing 'num' or 'unit' parameter"}), 400


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=6001, debug=True)
