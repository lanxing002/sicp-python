import sys
sys.set_int_max_str_digits(10000000)


def tail_opt(g):
    class TailRecurseException(BaseException):
        def __init__(self, args, kwargs):
            self.args = args
            self.kwargs = kwargs

    def func(*args, **kwargs):
        f = sys._getframe()
        if f.f_back and f.f_back.f_back and f.f_back.f_back.f_code == f.f_code:
            raise TailRecurseException(args, kwargs)
        else:
            while 1:
                try:
                    return g(*args, **kwargs)
                except TailRecurseException as e:
                    args = e.args
                    kwargs = e.kwargs

    func.__doc__ = g.__doc__
    return func


@tail_opt
def factorial_i1(n, acc=1):
    "calculate a factorial"
    if n == 0:
        return acc
    return factorial_i1(n-1, n*acc) * factorial_i1(n-1)

print(factorial_i1(10009))