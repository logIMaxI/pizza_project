from AbstractPizza import AbstractPizza
from log_decorator import log


class Margherita(AbstractPizza):
    """
    Class for Margherita pizza realisation
    """

    def __init__(self, size: str, *args: str) -> None:
        """
        Constructor of class
        ------
        :raises: ValueError if gotten size is not available
        """
        super(AbstractPizza, self).__init__()
        if size not in ("L", "XL", "M", "S"):
            raise ValueError(
                "This size is not available; "
                "please, choose form following: S, M, L, XL"
            )
        self._size = size
        self._additive = list(args)
        self._ingredients = ["tomato sauce", "mozzarella", "tomatoes"]

    @log("Bakes by {} seconds!")
    def bake(self) -> None:
        """
        Method for modeling pizza's baking
        """
        print(f"Start of baking pizza: {self.__module__}")
        for ingredient in self._ingredients:
            print(f"Add {ingredient}")
        print("Base is done", "-----", sep="\n")

        for add_ingredient in self._additive:
            print(f"Add additive ingredient: {add_ingredient}")
        print(
            f"Additives already in pizza {self.__module__}!", "-----",
            sep="\n"
        )

        print("👨‍ Pizza is done!")

    @log("Delivers by {} seconds!")
    def deliver(self) -> None:
        """
        Method for modeling pizza's delivering
        """
        print(f"🚴 Send {self.__module__} to courier")
