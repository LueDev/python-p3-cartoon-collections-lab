# roll_call_dwarves()
# summon_captain_planet()
# long_planeteer_calls()
# find_the_cheese()

def roll_call_dwarves(arr: list) -> str:
    [print(f"{index+1}. {name}") for index, name in enumerate(arr)]

def summon_captain_planet(planeteer_calls: list):
    return [f"{element}!".capitalize() for element in planeteer_calls]

def long_planeteer_calls(arr: list) -> bool:
    return any([len(x) > 4 for x in arr])

# using a generator expression (x for x in array) notice the use of parenthesis returns a generator object if true
# use the next(<generator object>) to iterate through the generator efficiently. 
# Since it looks at all values one by one rather than a contiguous set, it will return the first occurrence.
def find_the_cheese(ingredients: list) -> str:
    return next((ingredient for ingredient in ingredients if ingredient in ['cheddar', 'gouda', 'camembert']), None)

if __name__ == "__main__":
    names = ["Doc", "Broh", "Mercury", "cheddar", "gouda"]
    
    # roll_call_dwarves(names)
    # print(summon_captain_planet(names))
    # print(long_planeteer_calls(names))
    print(find_the_cheese(names))