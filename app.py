from flask import Flask, render_template, request
from units import convert, get_categories, get_units_by_category
import datetime

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    categories = get_categories()
    selected_category = 'Length'
    units = get_units_by_category(selected_category)

    if request.method == 'POST':
        value = float(request.form['value'])
        from_unit = request.form['from_unit']
        to_unit = request.form['to_unit']
        category = request.form['category']
        selected_category = category
        units = get_units_by_category(category)

        result = convert(value, from_unit, to_unit, category)

        with open('log.txt', 'a') as f:
            timestamp = datetime.datetime.now().isoformat()
            f.write(f"{timestamp}: {value} {from_unit} -> {result} {to_unit}\n")

    return render_template('index.html', result=result, categories=categories, units=units, selected_category=selected_category)

if __name__ == '__main__':
    app.run(debug=True)
