class Test_Underscore:

    def __init__(self):
        self.foo = 11
        self._bar = 23
        self.__baz = 23


t = Test_Underscore()
print(dir(t))


class Test_Extended(Test_Underscore):
    def __init__(self):
        super().__init__()
        self.foo = 'overriden'
        self._bar = 'overriden'
        self.__baz = 'overriden'


class ManglingTest:

    def __init__(self):
        self.__mangled = 'Hello'

    def get_mangled(self):
        return self.__mangled


t2 = Test_Extended()
print(t2._Test_Underscore__baz)
print(t2.foo)
print(t2._bar)
print(t2.__baz)
# print(t2._Test_Underscore__baz)