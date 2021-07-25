# CREATE A FUNCTION THAT STORES INFORMATION ABOUT CARS
def make_car(manufacturer, model, **kwargs):
    """STORE INFROMATION ABOUT THE CARE PROVIDED"""
    kwargs['manufacturer'] = manufacturer
    kwargs['model'] = model
    return kwargs

car = make_car('hyundai', 'accent', year=2015, color='silver')
print(car)