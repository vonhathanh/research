import random
import unittest
import numpy as np


class TestLibnum(unittest.TestCase):
    def test_example_1(self):
        # define the matrices
        C = np.array([[0, 1, 0, 0]])
        A = np.array([[0, 0, 1, 0]])
        B = np.array([[0, 0, 0, 1]])

        # witness vector
        witness = [1, 4223, 41, 103]

        # Multiplication is element-wise, not matrix multiplication. # Result contains a bool indicating an
        # element-wise indicator that the equality is true for that element.
        result = C.dot(witness) == A.dot(witness) * B.dot(witness)

        # check that every element-wise equality is true
        assert result.all(), "result contains an inequality"

    def test_example_2(self):
        A = np.zeros((3, 8))
        B = np.zeros((3, 8))
        C = np.zeros((3, 8))

        A[0, 2] = 1
        A[1, 4] = 1
        A[2, 6] = 1

        B[0, 3] = 1
        B[1, 5] = 1
        B[2, 7] = 1

        C[0, 6] = 1
        C[1, 7] = 1
        C[2, 1] = 1

        x = random.randint(1, 1000)
        y = random.randint(1, 1000)
        z = random.randint(1, 1000)
        u = random.randint(1, 1000)

        # compute the algebraic circuit
        out = x * y * z * u
        v1 = x * y
        v2 = z * u

        # create the witness vector
        w = np.array([1, out, x, y, z, u, v1, v2])

        # element-wise multiplication, not matrix multiplication
        result = C.dot(w) == np.multiply(A.dot(w), B.dot(w))

        assert result.all(), "system contains an inequality"