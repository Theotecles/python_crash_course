# START WITH SOME DESIGNS THAT NEED TO BE PRINTED
unprinted_designs = [
    'phone case',
    'robot pendant',
    'dodecahedron'
]
completed_models = []

# SIMULATE PRINTING EACH DESIGN, UNTIL NONE ARE LEFT
# MOVE EACH DESIGN TO COMPLETED_MODELS AFTER PRINTING
while unprinted_designs:
    current_design = unprinted_designs.pop()
    print(f"Printing model: {current_design}")
    completed_models.append(current_design)

# DISPLAY ALL COMPLETED MODELS
print("\nThe following models have been printed:")
for completed_model in completed_models:
    print(completed_model)

# IMPORT PRINTING_FUNCTIONS MODULE
import printing_functions as printing

# SHOW HOW WE GET THE SAME RESULTS
unprinted_designs = [
    'phone case',
    'robot pendant',
    'dodecahedron'
]
completed_models = []

printing.print_models(unprinted_designs[:], completed_models)
printing.show_completed_models(completed_models)

print(unprinted_designs)
