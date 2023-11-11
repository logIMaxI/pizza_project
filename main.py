from Margherita import Margherita
from Pepperoni import Pepperoni
from Hawaiian import Hawaiian


def main() -> None:
    """
    Here you can test any functional in interpreter
    """
    pepperoni = Pepperoni("S", "onion", "mushroom")
    hawaiian = Hawaiian("XL", "apple")
    print(pepperoni == hawaiian)


if __name__ == "__main__":
    main()
