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


if __name__ == "__main__":
    unittest.main()
