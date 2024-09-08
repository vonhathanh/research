import unittest

import galois


class TestGaloisFeild(unittest.IsolatedAsyncioTestCase):
    async def test_gf(self):
        GF = galois.GF(11)

        one_third = GF(1) / GF(3)
        one_half = GF(1) / GF(2)
        one_sixth = GF(1) / GF(6)

        assert one_third * one_half == one_sixth

    async def test_gf_2(self):
        GF = galois.GF(17)

        three_fourth = GF(3) / GF(4)
        one_half = GF(1) / GF(2)
        three_eight = GF(3) / GF(8)

        assert three_fourth * one_half == three_eight

    async def test_slope(self):
        GF11 = galois.GF(11)

        negative_1 = -GF11(1)
        negative_7 = -GF11(7)

        slope1 = GF11(negative_1) / GF11(2)
        slope2 = GF11(negative_7) / GF11(3)

        assert slope1 == slope2

    async def test_polynomial(self):
        GF103 = galois.GF(103)  # p = 103

        # we define a polynomial x^2 + 2x + 102 mod 103
        p1 = galois.Poly([1, 2, 102], GF103)

        print(p1)

        # we define a polynomial x^2 + x + 1 mod 103
        p2 = galois.Poly([1, 1, 1], GF103)

        print(p1 + p2)

        # We can input "-1" as a coefficient, and that will
        # automatically be calculated as `p - 1`
        # -1 becomes 102 in a field p = 103
        p3 = galois.Poly([-1, 1], GF103)
        p4 = galois.Poly([-1, 2], GF103)

        print(p3)
        print(p4)

    async def test_exercise_1(self):
        # replace 21888242871839275222246405745257275088548364400416034343698204186575808495617 = 103
        # for faster inference
        GF103 = galois.GF(103)

        x = GF103(0)
        y = GF103(101)
        z = GF103(2)

        assert x * y * z == 0
        assert x + y + z == 0

    async def test_exercise_2(self):
        GF11 = galois.GF(11)

        p = galois.Poly([1, 2, 3], GF11)

        assert p(7) == 0


if __name__ == "__main__":
    unittest.main()
