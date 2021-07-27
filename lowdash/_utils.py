from typing import TypeVar

_T = TypeVar('_T')

def args_type_checker(func: _T) -> _T:
    def predicate(*args, **kwargs):
        annotations = func.__annotations__.copy()
        annotations.pop('return')
        
        for index, (arg, parameter) in enumerate(annotations.items()):
            try:
                if not isinstance(args[index], parameter):
                    raise TypeError(f"[lowdash.{func.__name__}] Expected {parameter} for parameter {arg}")
            except KeyError:
                if not isinstance(kwargs[arg], parameter):
                    raise TypeError(f"[lowdash.{func.__name__}] Expected {parameter} for parameter {arg}")

        return func(*args, **kwargs)

    return predicate