def get_categories():
    return list(unit_categories.keys())

def get_units_by_category(category):
    return list(unit_categories[category].keys())

def convert(value, from_unit, to_unit, category):
    if category == 'Temperature':
        return convert_temperature(value, from_unit, to_unit)
    factor = unit_categories[category][from_unit]
    target_factor = unit_categories[category][to_unit]
    return value * (target_factor / factor)

def convert_temperature(value, from_unit, to_unit):
    if from_unit == to_unit:
        return value
    if from_unit == 'C':
        if to_unit == 'F':
            return value * 9/5 + 32
        elif to_unit == 'K':
            return value + 273.15
    elif from_unit == 'F':
        if to_unit == 'C':
            return (value - 32) * 5/9
        elif to_unit == 'K':
            return (value - 32) * 5/9 + 273.15
    elif from_unit == 'K':
        if to_unit == 'C':
            return value - 273.15
        elif to_unit == 'F':
            return (value - 273.15) * 9/5 + 32
    raise ValueError("Invalid temperature conversion")

unit_categories = {
    'Length': {
        'm': 1, 'km': 1000, 'mi': 1609.34, 'ft': 0.3048, 'in': 0.0254, 'yd': 0.9144, 'nm': 1852
    },
    'Weight': {
        'g': 1, 'kg': 1000, 'lb': 453.592, 'oz': 28.3495, 't': 1_000_000
    },
    'Temperature': {
        'C': 1, 'F': 1, 'K': 1
    },
    'Time': {
        's': 1, 'min': 60, 'h': 3600, 'day': 86400
    },
    'Speed': {
        'm/s': 1, 'km/h': 0.277778, 'mph': 0.44704
    },
    'Volume': {
        'ml': 1, 'l': 1000, 'gal': 3785.41, 'm3': 1_000_000
    }
}
