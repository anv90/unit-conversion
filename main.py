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

from flask import Flask, jsonify, request

app = Flask(__name__)

def calculate_time_conversion(num, unit):
    factors = {"sec": 1, "min": 60, "hr": 3600, "day": 86400}
    num_in_sec = num * factors[unit]
    conversions = {"sec": num_in_sec, 
                    "min": num_in_sec/factors["min"],  
                    "hr": num_in_sec/factors["hr"], 
                    "day": num_in_sec/factors["day"]}
    return conversions


# Helper function to convert a given unit to grams
def gram_conversion(num, unit): 
    match unit: 
        # Imperial
        case "oz": 
            return (num * 28.3495)
        case "lb":
            return (num * 453.592)
        case "tn_short": 
            return (num * 907185)
        # Metric 
        case "mg":
            return (num / 1000)
        case "g":
            return (num)
        case "kg":
            return (num * 1000)
        case "tn_metric":
            return (num * 1000000)
    return -1

def calculate_weight_conversion(num, unit):
    conversions = {}
    grams_unit = gram_conversion(num, unit) 
    conversions['oz'] = (grams_unit / 28.3495)
    conversions['lb'] = (grams_unit / 453.592)
    conversions['tn_short'] = (grams_unit / 907185)
    conversions['mg'] = (grams_unit * 1000)
    conversions['g'] = (grams_unit)
    conversions['kg'] = (grams_unit * 0.001)
    conversions['tn_metric'] = (grams_unit * 0.000001)
    return conversions


def calculate_conversion(num, unit):
    conversions = {}
    match unit:
        case "hr" | "min" | "sec" | "day":
            conversions = calculate_time_conversion(num, unit)
        case "oz" | "lb" | "tn_imperial" | "mg" | "g" | "kg" | "tn_metric":
            conversions = calculate_weight_conversion(num, unit)
    return conversions

@app.get('/unit-conversion')
def unit_conversion():
    num = float(request.args.get('num'))
    unit = request.args.get('unit')
    if num and unit:
        conversions =  calculate_conversion(num, unit)
        if conversions: #list is not empty
            return jsonify(conversions), 200
        else:
            return jsonify({"error": "unsupported conversion"}, 400)
    else:
        return jsonify({"error": "Missing 'num' or 'unit' parameter"}), 400


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=6001, debug=True)
