def generate_diet(profile):
    veg = profile["diet"]

    if veg == "Vegetarian":
        return """
        Breakfast: Poha / Oats + Fruits  
        Lunch: Rice + Dal + Vegetables  
        Snack: Roasted chana / sprouts  
        Dinner: Roti + Sabzi + Curd
        """

    return """
    Breakfast: Eggs + Toast  
    Lunch: Rice + Chicken curry  
    Snack: Fruits  
    Dinner: Roti + Dal / Paneer
    """
