import time

# Number of folds to compare
FOLDS = 100000   
# Method 1: Using the exponentiation operator
THICKNESS = 0.00008

start = time.time()
folded_thickness_exp = THICKNESS * (2 ** FOLDS)
elapsed_time_exp = time.time() - start
print("Exponentiation method time: {}[s]".format(elapsed_time_exp))

# Method 2: Using a for loop
folded_thickness_loop = THICKNESS
start = time.time()
for i in range(FOLDS):
    folded_thickness_loop *= 2
elapsed_time_loop = time.time() - start
print("For loop method time: {}[s]".format(elapsed_time_loop))

# Compare the results
print("\nFinal Thickness with Exponentiation: {:.2e} meters".format(folded_thickness_exp))
print("Final Thickness with For Loop: {:.2e} meters".format(folded_thickness_loop))

