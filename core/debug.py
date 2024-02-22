def debug(func):
    from core.settings import debug 
    def wrapper(*args, **kwargs):
        if debug == True:
            print(f"Function/method [ {func.__name__} ] is calling")
        return func(*args, **kwargs)
    return wrapper