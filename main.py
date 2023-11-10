import xml.etree.ElementTree as ET
import sys
import os


def update_svg(file_path):
    tree = ET.parse(file_path)

    root = tree.getroot()

    root_tag = root.tag.split('}')[1]
    root.tag = root_tag.capitalize()

    for child in root:
        child.tag = child.tag.split('}')[1]
        child.tag = child.tag.capitalize()

    downloads_path = os.path.join(os.path.expanduser('~'), 'Downloads')
    new_file_path = os.path.join(downloads_path, f"{file_path.split('.')[0]}_new.svg")

    tree.write(new_file_path)
    print(f"Updated SVG saved as {new_file_path}")


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Please provide a file path")
    else:
        file_path = sys.argv[1]
        update_svg(file_path)
    
