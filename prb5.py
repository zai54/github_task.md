THICKNESS = 0.00008  # Initial thickness of the paper in meters
folded_thickness = THICKNESS  # Start with the initial thickness
process_values []
process_values.append(folded_thickness)
for i in range(43):
    folded_thickness *= 2  # Double the thickness each time
    process_values.append(folded_thickness)  


print("Number of values stored:", len(process_values)) 

print("First value (initial thickness): {:.8f} meters".format(process_values[0]))
print("Last value (thickness after 43 folds): {:.8f} meters".format(process_values[-1]))
