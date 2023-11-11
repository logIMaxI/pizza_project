from AbstractPizza import AbstractPizza
from Margherita import Margherita
from Pepperoni import Pepperoni
from Hawaiian import Hawaiian
import click


def pizza_bake_delivery(pizza: AbstractPizza, delivery: bool) -> None:
    """
    Function for combine two AbstractPizza methods: bake and delivery
    ------
    :param: pizza - position from menu
    :type pizza: AbstractPizza

    :param: delivery - pizza is delivered or not
    :type delivery: bool
    """
    pizza.bake()
    if delivery:
        pizza.deliver()


@click.group()
def cli() -> None:
    """
    Function for working with terminal; calling each time when execute command
    from terminal
    """
    pass


@cli.command()
@click.option("--delivery", default=False, is_flag=True)
@click.argument("pizza", nargs=1)
@click.argument("size", nargs=1)
@click.argument("additives", nargs=-1)
def order(pizza: str, size: str, delivery: bool, additives: str) -> None:
    """
    Function for creating order (from termiinal)
    ------
    :param: pizza - name of position from menu
    :type pizza: str

    :param: size - size of pizza
    :type size: str

    :param: delivery - bool flag representing pizza's delivering
    :type delivery: bool

    :param: additives - additional components for pizza
    :type additives: str
    """
    pizza = pizza.lower()
    if pizza not in ("margherita", "pepperoni", "hawaiian"):
        click.echo("This pizza is not represented in menu ❌")
        return
    if pizza == "margherita":
        margherita = Margherita(size, *additives)
        pizza_bake_delivery(margherita, delivery)
    elif pizza == "pepperoni":
        pepperoni = Pepperoni(size, *additives)
        pizza_bake_delivery(pepperoni, delivery)
    else:
        hawaiian = Hawaiian(size, *additives)
        pizza_bake_delivery(hawaiian, delivery)


@cli.command()
def menu() -> None:
    """
    Function for showing menu (in terminal)
    """
    click.echo("You are welcome to out virtual restaurant!💻🥰")
    click.echo("Our menu 📄:")
    a, b, c = Margherita("S"), Pepperoni("S"), Hawaiian("S")
    emojis = {
        "Margherita": ["🧀", dict(a)["ingredients"]],
        "Pepperoni": ["🍕", dict(b)["ingredients"]],
        "Hawaiian": ["🍍", dict(c)["ingredients"]],
    }
    for name, attrs in emojis.items():
        click.echo(f'- {name} {attrs[0]}: {", ".join(attrs[1])}')


if __name__ == "__main__":
    cli()
