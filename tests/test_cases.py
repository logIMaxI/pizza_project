import pytest
from Margherita import Margherita
from Pepperoni import Pepperoni
from Hawaiian import Hawaiian
from AbstractPizza import AbstractPizza


def pizza_by_name(info: list) -> AbstractPizza:
    """
    Function for returning pizza by name and it's parameters
    ------
    :param: info - information about name of pizza and it's params
    :type info: list
    ------
    :return: pizza - resulting pizza
    :rtype: AbstractPizza
    """
    if info[0] == "margherita":
        pizza = Margherita(info[1], *info[2])
    elif info[0] == "pepperoni":
        pizza = Pepperoni(info[1], *info[2])
    else:
        pizza = Hawaiian(info[1], *info[2])

    return pizza


@pytest.mark.parametrize(
    "name, got, expected",
    [
        (
            "margherita",
            {"size": "XL", "additive": ["onion", "mushroom"]},
            {"size": "XL"},
        ),
        (
            "pepperoni",
            {"size": "M", "additive": []},
            {"ingredients": ["tomato sauce", "mozzarella", "pepperoni"]},
        ),
        (
            "hawaiian",
            {"size": "S", "additive": ["onion", "mushroom",
                                       "apple", "chili_pepper"]},
            {"additive": ["onion", "mushroom", "apple", "chili_pepper"]},
        ),
        (
            "pepperoni",
            {"size": "XL", "additive": ["onion", "garlic", "pineapples"]},
            {
                "ingredients": ["tomato sauce", "mozzarella", "pepperoni"],
                "size": "XL",
                "additive": ["onion", "garlic", "pineapples"],
            },
        ),
    ],
)
def test_positive(
    name: str, got: dict[str, str or list], expected: dict[str, str or list]
) -> None:
    """
    Function for positive tests
    ------
    :param: name - name of pizza
    :type name: str

    :param: got - info about pizza's attributes
    :type got: dict[str, str or list]

    :param: expected - expected result
    :type param: dict[str, str or list]
    ------
    :raises: AssertionError if expected result does not equal fact result
    """
    if name == "margherita":
        pizza = Margherita(got["size"], *got["additive"])
    elif name == "pepperoni":
        pizza = Pepperoni(got["size"], *got["additive"])
    else:
        pizza = Hawaiian(got["size"], *got["additive"])

    if len(expected) == 1:
        if "size" in expected.keys():
            assert pizza.get_size() == expected["size"]
        elif "additive" in expected.keys():
            assert pizza.get_additive() == expected["additive"]
        else:
            assert pizza.get_ingredients() == expected["ingredients"]
    else:
        assert dict(pizza) == expected


@pytest.mark.parametrize(
    "name, got, expected",
    [
        ("margherita", "N", ValueError),
        ("margherita", ["XL", 5], TypeError),
        ("pepperoni", ["M", "string"], TypeError),
        ("hawaiian", ["S", []], TypeError),
    ],
)
def test_negative(
    name: str, got: list or str, expected: TypeError or ValueError
) -> None:
    """
    Function for negative tests
    ------
    :param: name - pizza's name
    :type name: str

    :param: got - info about pizza (if type(got) == str) and compaired value
    (if type(got) == list)
    :type got: list or str

    :param: expected - expected result
    :type expected: TypeError or ValueError
    """
    if name == "pepperoni":
        pizza = Pepperoni(got[0])
        with pytest.raises(TypeError):
            print(pizza == got[1])
    elif name == "hawaiian":
        pizza = Hawaiian(got[0])
        with pytest.raises(TypeError):
            print(pizza == got[1])
    else:
        if isinstance(got, list):
            pizza = Margherita(got[0])
            with pytest.raises(TypeError):
                print(pizza == got[1])
        else:
            with pytest.raises(ValueError):
                pizza = Margherita(got)


@pytest.mark.parametrize(
    "first_pizza, second_pizza, expected",
    [
        (
            ["margherita", "M", ["apple"]],
            ["margherita", "M", ["onion"]],
            {"ingredients": 1, "size": 0, "additive": 0},
        ),
        (
            ["pepperoni", "S", ["onion", "mushroom"]],
            ["hawaiian", "XL", ["apple"]],
            {"ingredients": -1, "size": -1, "additive": 1},
        ),
    ],
)
def test_equal(
    first_pizza: list[str, str, list[str]],
    second_pizza: list[str, str, list[str]],
    expected: dict[str, int],
) -> None:
    """
    Function for test __eq__ method
    ------
    :param: first_pizza - info about first pizza
    :type first_pizza: list[str, str, list[str]]

    :param: second_pizza - info about second pizza
    :type second_pizza: list[str, str, list[str]]

    :param: expected - expected result
    :type expected: dict[str, int]
    ------
    :raises: AssertionError if expected result does not equal fact result
    """
    pizza_first = pizza_by_name(first_pizza)
    pizza_second = pizza_by_name(second_pizza)

    result = pizza_first == pizza_second
    assert result == expected
