"""..."""
import json
from bs4 import BeautifulSoup

def load_data(file_path):
    """ Loads a JSON file """
    with open(file_path, "r", encoding="utf-8") as handle:
        return json.load(handle)

def read_html():
    """read html file"""
    with open("animals_template.html", "r", encoding="utf-8") as file:
        html_content = file.read()
        return html_content


def get_information_from_animals(infos):
    """Printed the Information Name, Diet, first location and typ from every animal.
    If no location is found, it will print nothing
    """
    output = ""
    for animal in infos:
        is_characteristics = animal.get('characteristics')
        animal_type = is_characteristics.get("type")
        if animal_type is None:
            output += '<li class="cards__item">\n'
            output += f"        Name: {animal['name']}<br/>\n" \
                      f"        Diet: {animal['characteristics']['diet']}<br/>\n" \
                      f"        Location: {animal['locations'][0]}<br/>\n"
            output += "</li>\n"
        else:
            output += '<li class="cards__item">\n'
            output += f"        Name: {animal['name']}<br/>\n" \
                      f"        Diet: {animal['characteristics']['diet']}<br/>\n" \
                      f"        Location: {animal['locations'][0]}<br/>\n" \
                      f"        Type: {animal['characteristics']['type']}<br/>\n"
            output += "</li>\n"

    new_content = read_html().replace("__REPLACE_ANIMALS_INFO__", output)
    with open("animals.html", "w", encoding="utf-8") as file:
        file.write(new_content)


def main():
    """start of the Programm"""
    animals_data = load_data('animals_data.json')
    get_information_from_animals(animals_data)
    read_html()



if __name__ == "__main__":
    main()
