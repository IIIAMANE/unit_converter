from flask import Flask, render_template, request, redirect

app = Flask(__name__)

def convert_func(val: float, unit_in: str, unit_out: str):
    length_units = {
        "millimeter": 0.001, "centimeter": 0.01, "meter": 1, "kilometer": 1000,
        "inch": 0.0254, "foot": 0.3048, "yard": 0.9144
    }

    weight_units = {
        "milligram": 0.000001, "gram": 0.001, "kilogram": 1,
        "ounce": 0.0283495, "pound": 0.453592
    }

    if unit_in in length_units and unit_out in length_units:
        return val * length_units[unit_in] / length_units[unit_out]
    elif unit_in in weight_units and unit_out in weight_units:
        return val * weight_units[unit_in] / weight_units[unit_out]
    else:
        if unit_in == "Celsius":
            if unit_out == "Fahrenheit":
                return (val * (9/5)) + 32
            elif unit_out == "Kelvin":
                return val + 273.15
        elif unit_in == "Fahrenheit":
            if unit_out == "Celsius":
                return (val - 32) * 5/9
            elif unit_out == "Kelvin":
                return (val - 32) * 5/9 + 273.15
        elif unit_in == "Kelvin":
            if unit_out == "Celsius":
                return val - 273.15
            elif unit_out == "Fahrenheit":
                return (val - 273.15) * 9/5 + 32


def prikol(num):
    return num+1

@app.route('/', methods=['GET', "POST"])
def index():
    if request.method == "POST":
        unit_to_convert = request.form.get('len_to_convert')
        convert_from = request.form.get("convert_from_value")
        convert_to = request.form.get("convert_to_value")
        convert = convert_func(float(unit_to_convert), convert_from, convert_to)
        return render_template('result.html', convert=convert)
    return render_template("index.html")

if __name__ == '__main__':
    app.run(debug=True)