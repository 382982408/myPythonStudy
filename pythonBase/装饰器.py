import logging as LOG

def use_logging(func):
    def wrapper(*args, **kwargs):
        LOG.warn("%s is running" % func.__name__)
        func()
        # return func(*args, **kwargs)

    return wrapper


@use_logging
def func():
    print("i am func")


@use_logging
def func2():
    print("i am func2")


func()

func2()