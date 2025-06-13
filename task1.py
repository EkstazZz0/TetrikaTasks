from typing import Callable, Any

def strict(func: Callable[..., Any]) -> Callable[..., Any]:
    def wrapper(*args, **kwargs):
        print(func.__annotations__, args, kwargs)
        for arg, (key, annotation_type) in zip(args, func.__annotations__.items()):
            if type(arg) != annotation_type:
                raise TypeError(f'Unsupported type {type(arg)} for argument {key}. It requires {annotation_type}')
        
        for kwarg_key, kwarg_value in kwargs.items():
            if func.__annotations__.get(kwarg_key) != type(kwarg_value):
                raise TypeError(f'Unsupported type {type(kwarg_value)} for argument {kwarg_key}. It requires {func.__annotations__.get(kwarg_key)}')
        
        return func(*args, **kwargs)
    
    return wrapper


@strict
def sum_two(a: int, b: int) -> int:
    return a + b


@strict
def some_func(a: str, b: int) -> str:
    return a + ' ' +  str(b)


@strict
def some_another(some_arg: bool, some_another: str, some_float: float) -> str:
    if some_arg:
        return some_another + str(some_float)
    
    return str(some_float) + some_another
