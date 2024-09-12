def get_names(spicy_foods):
    """Returns a list of names of spicy foods."""
    return [food["name"] for food in spicy_foods]

def get_spiciest_foods(spicy_foods):
    """Returns a list of foods with a heat level greater than 5."""
    return [food for food in spicy_foods if food["heat_level"] > 5]

def print_spicy_foods(spicy_foods):
    """Prints each food with its name, cuisine, and heat level formatted with 🌶 emojis."""
    for food in spicy_foods:
        heat_level = '🌶' * food["heat_level"]
        print(f"{food['name']} ({food['cuisine']}) | Heat Level: {heat_level}")

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    """Returns the food that matches the specified cuisine."""
    for food in spicy_foods:
        if food["cuisine"] == cuisine:
            return food
    return None

def print_spiciest_foods(spicy_foods):
    """Prints foods with heat level over 5 formatted with 🌶 emojis."""
    spicy_foods_over_5 = get_spiciest_foods(spicy_foods)
    print_spicy_foods(spicy_foods_over_5)

def get_average_heat_level(spicy_foods):
    """Returns the average heat level of all spicy foods."""
    if not spicy_foods:
        return 0
    total_heat_level = sum(food["heat_level"] for food in spicy_foods)
    return total_heat_level // len(spicy_foods)

def create_spicy_food(spicy_foods, new_food):
    """Adds a new spicy food to the list and returns the updated list."""
    return spicy_foods + [new_food]