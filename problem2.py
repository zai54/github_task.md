#[Problem 2] Unit Conversion
THICKNESS = 0.00008
folded_thickness = THICKNESS * (2 ** 43)

print("Thickness: {: .2f} kilometers".format(folded_thickness / 1000))
output
Thickness: 703687441.78 kilometers
