
class MyError(Exception):
    def __init__(self, value, args):
        super(MyError, self).__init__(args)
        self.value = value

    def __str__(self):
        return "MyError: "+repr(self.value)+repr(self.args)


if __name__ == '__main__':
    try:
        raise MyError(2*2, "aaa")
    except MyError as e:
        print('My exception occurred, value:', e.value, e.args)
        print(e)
