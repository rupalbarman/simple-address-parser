import sys

from address_parser.parser import parse


def main():
    args = sys.argv[1:]

    if not len(args) or len(args) > 1:
        print('Incorrect input, please enter a raw address string in quotes')
        sys.exit(1)

    print(parse(args[0]))


if __name__ == '__main__':
    main()
