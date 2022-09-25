import sys

from image_helper import generate


def main():
    text = sys.argv[1]
    print(text)
    generate(text)

main()
