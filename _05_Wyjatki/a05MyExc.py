# przyklad z tutoriala


class MyError(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return "MyError: "+repr(self.value)

try:
    raise MyError(2*2)
except MyError, e:
    print 'My exception occurred, value:', e.value, e.message, e.args
    print e
