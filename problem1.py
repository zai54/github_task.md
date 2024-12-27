# Code to calculate the thickness when the paper is folded 43 times

THICKNESS = 0.00008

folded_thickness = THICKNESS * (2 ** 43)

print("Thickness after 43 folds: {} meters".format(folded_thickness))
