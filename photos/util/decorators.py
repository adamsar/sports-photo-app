def generative(fnc):
    """Generative is a decorator that if used
    by a class will return the class after executing the function.
    This allows chaing functions.
    """
    def wrapped(*args, **kwargs):
        result = fnc(*args, **kwargs)
        try:
            return args[0]
        except IndexError:
            return result
    return wrapped
