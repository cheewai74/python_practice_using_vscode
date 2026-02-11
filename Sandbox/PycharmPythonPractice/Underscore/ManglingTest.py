class ManglingTest:

    def __init__(self):
        self.__mangled = 'hello'

    def get_mangled(self):
        return self.__mangled


print(ManglingTest().get_mangled())
print(ManglingTest().__mangled)