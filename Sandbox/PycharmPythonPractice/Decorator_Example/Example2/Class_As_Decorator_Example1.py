"""

    For making the class a decorator, it needs to be callable;
    this is achieved using the dunder method __call__.
    Furthermore, the __init__ method
    needs to take a function as an argument

"""


class CountUpdates:
    def __init__(self, func):
        self.func = func
        self.version = 0

    def __call__(self, *args, **kwargs):
        self.version += 1
        print(f"Updating to version 0.3.{self.version}")
        return self.func(*args, **kwargs)


@CountUpdates
def update():
    print("Update complete", end="\n\n")


update()
update()
update()
update()
print(update.version)