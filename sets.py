from sets_categories_data import (ALCOHOLS)


    def clean_ingredients(dishname, dishingredients):
    temp_set = set()
    for ingredient in dishingredients:
        temp_set.add(ingredient)
    return_tuple = (dishname, tempset)
    return return_tuple



    def check_drinks(drinkname, drinkingredients):
    for ingredient in drinkingredients:
        if ingredient in ALCOHOLS:
            return f"{drinkname} Cocktail"
    return f"{drinkname} Mocktail"


