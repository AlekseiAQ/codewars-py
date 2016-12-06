import sys
from utils.utils import create_files, get_kata_data

def main(slug):
    create_files(slug)
    print(get_kata_data(slug))


if __name__ == "__main__":
    main(sys.argv[1])