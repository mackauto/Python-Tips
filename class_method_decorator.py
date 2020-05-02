def catch_exception(func):
    def wrapper(self, *args, **kwargs):
        try:
            res = func(self, *args, **kwargs)
            return res
        except ZeroDivisionError:
            return self.revive()

    return wrapper


class Dummy(object):
    def __init__(self, name):
        self.name = name

    def revive(self):
        print(f'{self.name} revive')
        return 0

    @catch_exception
    def read(self):
        if self.name == 'error':
            a = 1 / 0
        else:
            a = 1 / len(self.name)
        print(f'{self.name} read {a}')
        return a


if __name__ == '__main__':
    d1 = Dummy(name='me')
    d1_res = d1.read()
    print(d1_res)

    d2 = Dummy(name='error')
    d2_res = d2.read()
    print(d2_res)
