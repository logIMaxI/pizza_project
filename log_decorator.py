from random import randint
from typing import Callable


def log(template: str) -> Callable:
    """
    Function-decorator for showing time of execution actions
    ------
    :param: template - gotten template of showing time
    :type template: str
    ------
    :return: decorator_func - func for decorating
    :rtype: Callable
    """

    def decorator_func(func_to_wrap: Callable) -> Callable:
        """
        Function realises decorating mechanism
        ------
        :param: func_to_wrap - func to decorate
        :type func_to_wrap: - Callable
        ------
        :return: wrapper_func - decorated func
        :rtype: Callable
        """

        def wrapper_func(*args, **kwargs):
            """
            Decorated func
            ------
            :param args: positional args for decorated func

            :param kwargs: non-positional arguments for decorated func
            ------
            :return: result - work's result of decorated func
            """
            result = func_to_wrap(*args, **kwargs)
            print(template.format(randint(1, 10)))
            return result

        return wrapper_func

    return decorator_func
