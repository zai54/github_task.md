# Code to calculate the thickness when the paper is folded 43 times using a for statement
THICKNESS = 0.00008  # Initial thickness of the paper in meters
folded_thickness = THICKNESS  # Start with the initial thickness

for i in range(43):
    folded_thickness *= 2  

print("Thickness: {: .2f} kilometers".format(folded_thickness / 1000))
