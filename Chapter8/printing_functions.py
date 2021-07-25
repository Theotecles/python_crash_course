def print_models(unprinted_designs, completed_models):
    """
    SIMULATE PRINTING EACH DESIGN, UNTIL NONE ARE LEFT.
    MOVE EACH DESIGN TO COMPLETED_MODELS AFTER PRINTING
    """
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print(f"Printing model: {current_design}")
        completed_models.append(current_design)

def show_completed_models(completed_models):
    """SHOW ALL MODELS THAT WERE PRINTED"""
    print("\nThe following models have been printed:")
    for completed_model in completed_models:
        print(completed_model)