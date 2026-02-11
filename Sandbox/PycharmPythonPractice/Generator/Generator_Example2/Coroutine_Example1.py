
def coroutine_example():
    while True:
        x = yield
        # Do something with x
        print(x)

c = coroutine_example()
c.__next__()
c.send(10)

def counter(String):
    count = 0
    try:
        while True:
            # print("Inside While Loop")
            item = yield
            if isinstance(item, str):
                if item in String:
                    count += 1
                    print(item)
                else:
                    print("No Match")
            else:
                print("Not a string")
    except GeneratorExit:
        print(count)


c = counter("Singapore")
c.__next__()
c.send("Singa")
c.send("pore")
c.close()


def coroutine_decorator(func):

    def wrap(*args, **kwargs):
        cr = func(*args, **kwargs)
        cr.__next__()
        return cr
    return wrap

@coroutine_decorator
def coroutine_example():
    while True:
        x = yield
        #do something with x
        print(x)

c = coroutine_example()
c.send("Success!")
