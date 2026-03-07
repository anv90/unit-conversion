"""
app.get
    param:
        num to convert
        units of num
    case (unit)
        time (hrs, days, min) :
            do conversions for all based on input unit
        weight (lb, kgs, g):
            do conversions for all based on input unit
    returns the array of conversions




"""

from flask import Flask, jsonify

app = Flask(__name__)

def calculate_time_conversion(num, unit):
    return
def calculate_weight_conversion(num, unit):
    return
def calculate_conversion(num, unit):
    conversions = []
    match unit:
        case "hr" | "min" | "sec" | "day":
            conversions = calculate_time_conversion(num, unit)
        case "lb": #add more here depending on use case
            conversions = calculate_weight_conversion(num, unit)
    return conversions

@app.get('/unit_conversion')
def unit_conversion():
    num = request.args.get('num')
    unit = request.args.get('unit')
    if num and unit:
        conversions =  calculate_conversion(num, unit)
        if conversions: #list is not empty
            return jsonify(result), 200
        else:
            return jsonify({"error": "unsupported conversion"}, 400)
    else:
        return jsonify({"error": "Missing 'num' or 'unit' parameter"}), 400


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=6001, debug=True)
