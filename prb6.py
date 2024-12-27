import matplotlib.pyplot as plt

THICKNESS = 0.00008  
folded_thickness = THICKNESS  
process_values = []  
process_values.append(folded_thickness)

for i in range(43):
    folded_thickness *= 2  
    process_values.append(folded_thickness)  
print("Number of values stored:", len(process_values))

plt.title("Thickness of Folded Paper")
plt.xlabel("Number of Folds")
plt.ylabel("Thickness [m]")
plt.plot(process_values)  
plt.show()

