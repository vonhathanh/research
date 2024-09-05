import unittest

import libnum
from libnum import has_sqrtmod_prime_power, has_sqrtmod_prime_power


def double(x, y, a, p):
    lambd = (((3 * x**2) % p) * pow(2 * y, -1, p)) % p
    newx = (lambd**2 - 2 * x) % p
    newy = (-lambd * newx + lambd * x - y) % p
    return (newx, newy)


def add_points(xq, yq, xp, yp, p, a=0):
    if xq == yq == None:
        return xp, yp
    if xp == yp == None:
        return xq, yq

    assert (xq**3 + 3) % p == (yq**2) % p, "q not on curve"
    assert (xp**3 + 3) % p == (yp**2) % p, "p not on curve"

    if xq == xp and yq == yp:
        return double(xq, yq, a, p)
    elif xq == xp:
        return None, None

    lambd = ((yq - yp) * pow((xq - xp), -1, p)) % p
    xr = (lambd**2 - xp - xq) % p
    yr = (lambd * (xp - xr) - yp) % p
    return xr, yr


class TestLibnum(unittest.TestCase):
    def test_sqrt(self):
        # the functions take arguments# has_sqrtmod_prime_power(n, field_mod, k), where n**k,
        # but we aren't interested in powers in modular fields, so we set k = 1
        # check if sqrt(8) mod 11 exists
        print(has_sqrtmod_prime_power(8, 11, 1))
        # False

        # check if sqrt(5) mod 11 exists
        print(has_sqrtmod_prime_power(5, 11, 1))
        # True

        # compute sqrt(5) mod 11
        print(list(libnum.sqrtmod_prime_power(5, 11, 1)))
        # [4, 7]

        assert (4**2) % 11 == 5
        assert (7**2) % 11 == 5

        # we expect 4 and 7 to be inverses of each other, because in "regular" math, the two solutions to a square
        # root are sqrt and -sqrt
        assert (4 + 7) % 11 == 0

    def test_add(self):
        x1, y1 = (0, 5)
        x2, y2 = (4, 10)
        result = add_points(x1, y1, x2, y2, 11)
        print(result)
