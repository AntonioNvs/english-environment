import json, os

# Specify the path to your JSON file

def return_the_word_day(day):
    filepath = os.path.join(os.getcwd(), "data", "database.json")

    # Read the JSON file
    with open(filepath, 'r') as file:
        data = json.load(file)

    return data[day] if day in data else "No word for today."


def set_the_word_day(day, word):
    filepath = os.path.join(os.getcwd(), "data", "database.json")

    # Read the JSON file
    with open(filepath, 'r') as file:
        data = json.load(file)

    data[day] = word

    # Write the JSON file
    with open(filepath, 'w') as file:
        json.dump(data, file, indent=4)


def return_all_words():
    filepath = os.path.join(os.getcwd(), "data", "database.json")

    # Read the JSON file
    with open(filepath, 'r') as file:
        data = json.load(file)

    return data.values()
        