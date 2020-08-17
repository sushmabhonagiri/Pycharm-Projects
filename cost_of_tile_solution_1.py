"""
Title: Find Cost of Tile to Cover W x L Floor
Description:
Ask the user to enter in a width, length and the cost per 1 unit of flooring.
Have the program calculate how much it would cost to cover the area specified with the flooring.
Tips:
This is a relatively simple program. Be sure to first find out how much area the floor is
and then multiply that by the cost per unit of flooring. Start with some simple numbers that you
can quickly calculate in your head. Try a 100 x 100 cm room with each unit of flooring costing £1.00.
Added Difficulty:
How many packs of tiles would be needed? Also figure
out how much labor costs would be given that the average flooring team can only put in 5000 square cm
of flooring per hour at a cost of £50.00/hr.
"""
# Imports
from math import ceil #import the ceil function, this is a round up function
# Variables
hourly_rate = 50.0
hourly_area = 5000
# Main
tile = {
    'width': float(input("Tile Width (cm): ")),
    'height': float(input("Tile Height (cm): ")),
    'pack': float(input("Tile Pack Size (#): ")),
    'cost': float(input("Tile Pack Cost (£): ")),
}
floor = {
    'width': float(input("Floor Width (cm): ")),
    'length': float(input("Floor Length (cm): "))
}
tile['area'] = (tile['width'] * tile['height'])
floor['area'] = (floor['width'] * floor['length'])
quote = {}
quote['needed'] =  ceil((floor['area'] / tile['area']))
quote['packs'] = ceil(quote['needed'] / tile['pack'])
quote['price'] = quote['needed'] * tile['cost']
quote['labour'] = ceil(floor['area'] / hourly_area) * hourly_rate
quote['total'] = quote['price'] + quote['labour']
quote['surplus'] = (quote['packs']*tile['pack'])- quote['needed']
print("\n\n")
print("=" * 45)
print("   ____              _    \n  / __ \            | |      \n | |  | |_   _  ___ | |_ ___ \n | |  | | | | |/ _ \| __/ _ \\\n | |__| | |_| | (_) | ||  __/\n  \___\_\\\__,_|\___/ \__\___|")
print("=" * 45)
print(f"Tile(s): H: {tile['height']}, W: {tile['width']}")
print(f"Pack: {tile['pack']}, 'Cost (each):' {tile['cost']}")
print(f"Room: L: {floor['length']}, W: {floor['width']}")
print("-" * 45)
print(f"Tiles Needed: {quote['needed']}, Price For Tiles: {quote['price']}")
print(f"Packs: {quote['packs']}, Surplus Tiles: {quote['surplus']}")
print(f"Labour @ £{hourly_rate} per {hourly_area}cm: {quote['labour']}")
print("=" * 45)
print(f"TOTAL inc Labour: {quote['total']}")
print("=" * 45)
print("\n\n")


