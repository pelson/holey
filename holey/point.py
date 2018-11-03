import numba

spec = [
    ('x', numba.float64),
    ('y', numba.float64)
]

@numba.jitclass(spec)
class Point(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

