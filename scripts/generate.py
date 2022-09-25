import sys
from .utils.image_helper import generate


def main():
    text = sys.argv[1]
    generate(text)

main()
