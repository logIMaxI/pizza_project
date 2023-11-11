from abc import abstractmethod
from typing import Iterator


class AbstractPizza:
    """
    Class for modeling pizza object (not specific pizza)
    ------
    :attr: _ingredients - list of ingredients for pizza
    :type _ingredients: list

    :attr: _additive - additional components for pizzas
    :type _additive: list

    :attr: _size - size of pizza
    :type _size: str
    ------
    :method: __init__ - constructor

    :method: get_ingredients: returns _ingredients value

    :method: get_additive - returns _additive value

    :method: get_size - returns _size value

    :method: __iter__ - Returns list of iterators for all object attributes

    :method: __getitem__ - returns value for one of object attributes

    :method: keys - returns all attributes of class like keys for dict

    :method: __eq__ - method for compairing different pizzas

    :method: bake - abstract method for modeling pizza's baking

    :method: deliver - abstract method for modeling pizza's delivering
    """

    def __init__(self, size: str, *args: str) -> None:
        """
        Class constructor; responsible for initialize attributes
        ------
        :param: size - size of pizza
        :type size: str

        :param: args - additives for pizza
        :type args: str
        """
        self._ingredients = []
        self._additive = list(args)
        self._size = size

    def get_ingredients(self) -> list[str]:
        """
        Returns list of ingredients for pizza
        ------
        :return: list of ingredients (_ingredients)
        :rtype: list[str]
        """
        return self._ingredients

    def get_additive(self) -> list[str]:
        """
        Returns list of additives for pizza
        ------
        :return: list of additives (_additive)
        :rtype: list[str]
        """
        return self._additive

    def get_size(self) -> str:
        """
        Returns pizza's size
        ------
        :return: pizza's size (_size)
        :rtype: str
        """
        return self._size

    def __iter__(self, *args: str) -> list[Iterator]:
        """
        Returns list of iterators for all object attributes
        ------
        :param: args - name(s) of object attributes
        :type args: str
        ------
        :return: result - list of iterators
        :rtype: list
        """
        result = []
        if "ingredients" in args:
            result.append(self._ingredients.__iter__())
        if "size" in args:
            result.append(self._size)
        if "additive" in args:
            result.append(self._additive.__iter__())
        return result

    def __getitem__(self, *args: str) -> list[str] or str:
        """
        Method for getting items like in dictionary
        ------
        :param: args - name(s) of object attributes
        :type args: str
        ------
        :return: value of object attribute
        :rtype: list[str] or str
        """
        if "ingredients" in args:
            return self._ingredients
        if "size" in args:
            return self._size
        if "additive" in args:
            return self._additive

    def keys(self) -> list[str]:
        """
        Method for getting attributes of class like keys in dict
        ------
        :return: list of object attributes
        :rtype: list[str]
        """
        attributes = self.__dir__()
        return [
            attr.replace("_", "")
            for attr in attributes
            if len(attr) -
            len(attr.replace("_", "")) == 1 and attr.startswith("_")
        ]

    def __eq__(self, other) -> dict[str, int]:
        """
        Method for compiring two different pizzas
        ------
        :param: other - another pizza
        :type other: AbstractPizza
        ------
        :raises: TypeError if other not AbstractPizza object
        ------
        :return: dict with compairing result:
            -1 for different pizzas type or 1 for one type

            -1 if other pizza size > current pizza size; 0 if current pizza
            size equals other pizza size; else 1

            -1 if additives count in other pizza more than current pizza; 0 if
            count of additives matches in both pizzas; else 1
        :rtype: dict[str, int]
        """
        if not isinstance(other, AbstractPizza):
            raise TypeError("Compaired object must have a pizza's properties")

        size_to_number = {"S": 0, "M": 1, "L": 2, "XL": 3}

        return {
            "ingredients": -1 if
            self._ingredients != other.get_ingredients() else 1,
            "size": -1
            if size_to_number[self._size] < size_to_number[other.get_size()]
            else int(size_to_number[self._size] >
                     size_to_number[other.get_size()]),
            "additive": -1
            if len(self._additive) < len(other.get_additive())
            else int(len(self._additive) > len(other.get_additive())),
        }

    @abstractmethod
    def bake(self) -> None:
        """
        Abstract method for modeling baking process
        """

    @abstractmethod
    def deliver(self) -> None:
        """
        Abstract method for modeling delivering process
        """
