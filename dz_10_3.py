class MyError(Exception):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
        if a < 5 or b < 4 or c < 7:
            print('Значения должны быть не меньше указанного')

            raise MyError('We have a problem')
    def a(self):
        return self.__a
    def b(self):
        return self.__b
    def c(self):
        return self.__c

v = MyError(a= 2, b=1, c=1)



