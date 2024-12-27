# Green dashed line with increased line width
plt.title("Thickness of Folded Paper", fontsize=16)  
plt.xlabel("Number of Folds", fontsize=12) 
plt.ylabel("Thickness [m]", fontsize=12)  
plt.plot(process_values, color='green', linestyle='--', linewidth=2)  
plt.grid(True)  
plt.show()
