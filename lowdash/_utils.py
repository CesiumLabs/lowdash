from typing import TypeVar

_T = TypeVar("_T")


def args_type_checker(func: _T) -> _T:
    def predicate(*args, **kwargs):
        annotations = func.__annotations__.copy()
        annotations.pop("return")

        for index, (arg, arg_type) in enumerate(annotations.items()):
            try:
                if not isinstance(args[index], arg_type):
                    raise TypeError(
                        f"[lowdash.{func.__name__}] Expected {arg_type} for parameter {arg}"
                    )
            except KeyError:
                if not isinstance(kwargs[arg], arg_type):
                    raise TypeError(
                        f"[lowdash.{func.__name__}] Expected {arg_type} for parameter {arg}"
                    )

        return func(*args, **kwargs)

    return predicate
