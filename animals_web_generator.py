"""..."""
import json

def load_data(file_path):
    """ Loads a JSON file """
    with open(file_path, "r", encoding="utf-8") as handle:
        return json.load(handle)


def get_information_from_animals(infos):
    """Printed the Information Name, Diet, first location and typ from every animal.
    If no location is found, it will print nothing
    """
    for animal in infos:
        is_characteristics = animal.get('characteristics')
        animal_type = is_characteristics.get("type")
        if animal_type is None:
            print(f"Name: {animal['name']}\nDiet: {animal['characteristics']['diet']}\nLocation: "
                  f"{animal['locations'][0]}\n")
        else:
            print (f"Name: {animal['name']}\nDiet: {animal['characteristics']['diet']}\nLocation: "
            f"{animal['locations'][0]}\nType: {animal_type}\n")

def main():
    """start of the Programm"""
    animals_data = load_data('animals_data.json')
    get_information_from_animals(animals_data)

if __name__ == "__main__":
    main()
