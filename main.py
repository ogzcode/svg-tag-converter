import sys
from src.svg_updater import update_svg

def main():
    if len(sys.argv) < 3:
        print("Please provide a file path and new file name.")
        sys.exit(1)

    if not sys.argv[1].endswith(".svg"):
        print("Please provide a valid SVG file.")
        sys.exit(1)

    file_path = sys.argv[1]
    new_name = sys.argv[2]
    update_svg(file_path, new_name)

if __name__ == "__main__":
    main()