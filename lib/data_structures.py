spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]

def get_names(spicy_foods):
    # food_names = []
    # for food in spicy_foods:
    #     food_name = food.get("name")
    #     food_names.append(food_name)
    # return food_names
    food_names = [food.get("name") for food in spicy_foods]
    return food_names

def get_spiciest_foods(spicy_foods):
    spiciest_foods = [food for food in spicy_foods if food["heat_level"]> 9]
    return spiciest_foods

def print_spicy_foods(spicy_foods):
    for food in spicy_foods:
        food["heat_level"] = "🌶" * food["heat_level"]
    [print(f"{food['name']} ({food['cuisine']}) | Heat Level: {food['heat_level']}") for food in spicy_foods]
    for food in spicy_foods:
        food["heat_level"] = len(food["heat_level"])

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    for food in spicy_foods:
        if food["cuisine"] == cuisine:
            return food
        else:
            pass
def print_spiciest_foods(spicy_foods):
    spiciest_foods = []
    for food in spicy_foods:
        if food["heat_level"] > 5:
            spiciest_foods.append(food)
        else:
            pass
        food["heat_level"] = "🌶" * food["heat_level"]
    [print(f"{food['name']} ({food['cuisine']}) | Heat Level: {food['heat_level']}") for food in spiciest_foods]
    for food in spicy_foods:
        food["heat_level"] = len(food["heat_level"])

def get_average_heat_level(spicy_foods):
    heat_total = 0
    for food in spicy_foods:
        heat_total = heat_total + food["heat_level"]
        pass
    return heat_total / len(spicy_foods)

def create_spicy_food(spicy_foods, spicy_food):
    spicy_foods.append(spicy_food)
    return spicy_foods
