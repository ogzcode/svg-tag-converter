import xml.etree.ElementTree as ET
import os

def capitalize_tag(element):
    element.tag = element.tag.split('}')[1].capitalize()

def update_recursively(element):
    capitalize_tag(element)

    for child in element:
        update_recursively(child)


def update_svg(file_path, new_path):
    tree = ET.parse(file_path)

    root = tree.getroot()

    update_recursively(root)

    downloads_path = os.path.join(os.path.expanduser('~'), 'Downloads')

    new_file_path = os.path.join(downloads_path, f"{new_path}_new.svg")

    tree.write(new_file_path)
    print(f"Updated SVG saved as {new_file_path}")
