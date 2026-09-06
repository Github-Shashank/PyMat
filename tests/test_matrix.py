import unittest
import math
from matrix import Matrix
from matrix.validators import (
    check_matrix,
    is_equal_order,
    is_valid_index,
    is_multiplicable
)


class TestMatrix(unittest.TestCase):

    def test_check_matrix_valid(self):
        m = [[1, 2], [3, 4]]

        self.assertEqual(check_matrix(m), True)

    def test_check_matrix_invalid(self):
        m = [[1, 2], [3]]

        self.assertEqual(check_matrix(m), [3])

    def test_is_equal_order_true(self):
        A = Matrix([[1, 2], [3, 4]])
        B = Matrix([[5, 6], [7, 8]])

        self.assertTrue(is_equal_order(A, B))

    def test_is_equal_order_false(self):
        A = Matrix([[1, 2], [3, 4]])
        B = Matrix([[1, 2, 3], [4, 5, 6]])

        self.assertFalse(is_equal_order(A, B))

    def test_is_valid_index_true(self):
        A = Matrix([[1, 2], [3, 4]])

        self.assertTrue(is_valid_index(A, (0, 0)))
        self.assertTrue(is_valid_index(A, (1, 1)))

    def test_is_valid_index_false(self):
        A = Matrix([[1, 2], [3, 4]])

        self.assertFalse(is_valid_index(A, (2, 0)))
        self.assertFalse(is_valid_index(A, (0, 2)))
        self.assertFalse(is_valid_index(A, (1,)))
        self.assertFalse(is_valid_index(A, (0, 1, 2)))

    def test_is_multiplicable_true(self):
        A = Matrix([[1, 2, 3], [4, 5, 6]])
        B = Matrix([[1, 2], [3, 4], [5, 6]])

        self.assertTrue(is_multiplicable(A, B))

    def test_is_multiplicable_false(self):
        A = Matrix([[1, 2], [3, 4]])
        B = Matrix([[1, 2], [3, 4], [5, 6]])

        self.assertFalse(is_multiplicable(A, B))

    def test_transpose(self):
        A = Matrix([
            [1, 2, 3],
            [4, 5, 6]
        ])

        expected = Matrix([
            [1, 4],
            [2, 5],
            [3, 6]
        ])

        self.assertEqual(A.transpose, expected)

    def test_minor(self):
        A = Matrix([
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]
        ])

        self.assertEqual(
            A.minor(0, 0),
            Matrix([
                [5, 6],
                [8, 9]
            ])
        )


    def test_cofactor(self):
        A = Matrix([
            [1, 2],
            [3, 4]
        ])

        self.assertEqual(A.cofactor(0, 0), 4)
        self.assertEqual(A.cofactor(0, 1), -3)


    def test_determinant(self):
        A = Matrix([
            [1, 2],
            [3, 4]
        ])

        self.assertEqual(A.determinant, -2)


    def test_determinant_3x3(self):
        A = Matrix([
            [1, 2, 3],
            [0, 1, 4],
            [5, 6, 0]
        ])

        self.assertEqual(A.determinant, 1)

        def test_matrix_of_minors(self):
            A = Matrix([
                [1, 2],
                [3, 4]
            ])

            result = A.matrixOfMinors

            self.assertEqual(result[0, 0], 4)
            self.assertEqual(result[0, 1], 3)
            self.assertEqual(result[1, 0], 2)
            self.assertEqual(result[1, 1], 1)   

    def test_matrix_of_cofactors(self):
        A = Matrix([
            [1, 2],
            [3, 4]
        ])

        result = A.matrixOfCofactors

        self.assertEqual(result[0, 0], 4)
        self.assertEqual(result[0, 1], -3)
        self.assertEqual(result[1, 0], -2)
        self.assertEqual(result[1, 1], 1)

    def test_adjoint(self):
        A = Matrix([
            [1, 2],
            [3, 4]
        ])

        expected = Matrix([
            [4, -2],
            [-3, 1]
        ])

        self.assertEqual(A.adjoint, expected)

    def test_inverse(self):
        A = Matrix([
            [1, 2],
            [3, 4]
        ])

        expected = Matrix([
            [-2, 1],
            [1.5, -0.5]
        ])

        self.assertEqual(A.inverse, expected)

    def test_inverse_singular(self):
        A = Matrix([
            [1, 2],
            [2, 4]
        ])

        with self.assertRaises(ValueError):
            A.inverse

    def test_one(self):
        self.assertEqual(
            Matrix.one(2, 3),
            Matrix([
                [1, 1, 1],
                [1, 1, 1]
            ])
        )

    def test_zero(self):
        self.assertEqual(
            Matrix.zero(2, 3),
            Matrix([
                [0, 0, 0],
                [0, 0, 0]
            ])
        )

    def test_identity(self):
        self.assertEqual(
            Matrix.identity(3),
            Matrix([
                [1, 0, 0],
                [0, 1, 0],
                [0, 0, 1]
            ])
        )

    def test_constant(self):
        self.assertEqual(
            Matrix.constant(2, 3, 7),
            Matrix([
                [7, 7, 7],
                [7, 7, 7]
            ])
        )

    def test_diagonal(self):
        self.assertEqual(
            Matrix.diagonal([1, 2, 3]),
            Matrix([
                [1, 0, 0],
                [0, 2, 0],
                [0, 0, 3]
            ])
        )

    def test_elementwise(self):
        result = Matrix.elementwise(
            2,
            3,
            lambda i, j: i + j
        )

        self.assertEqual(
            result,
            Matrix([
                [0, 1, 2],
                [1, 2, 3]
            ])
        )

    def test_random(self):
        result = Matrix.random(3, 4, 1, 5)

        self.assertEqual(result.order, (3, 4))

        for value in result.traverse:
            self.assertTrue(1 <= value <= 5)

    def test_from_string(self):
        result = Matrix.from_string(
            "1 2 3\n4 5 6",
            dtype=int
        )

        self.assertEqual(
            result,
            Matrix([
                [1, 2, 3],
                [4, 5, 6]
            ])
        )


    def test_divide_scalar(self):
        A = Matrix([
            [2, 4],
            [6, 8]
        ])

        self.assertEqual(
            A / 2,
            Matrix([
                [1, 2],
                [3, 4]
            ])
        )


    def test_divide_by_zero(self):
        A = Matrix([
            [1, 2],
            [3, 4]
        ])

        with self.assertRaises(ZeroDivisionError):
            A / 0

    def test_negate(self):
        A = Matrix([
            [1, -2],
            [-3, 4]
        ])

        self.assertEqual(
            -A,
            Matrix([
                [-1, 2],
                [3, -4]
            ])
        )

    def test_power(self):
        A = Matrix([
            [1, 2],
            [3, 4]
        ])

        self.assertEqual(
            A ** 2,
            Matrix([
                [7, 10],
                [15, 22]
            ])
        )

    def test_right_multiply(self):
        A = Matrix([
            [1, 2],
            [3, 4]
        ])

        self.assertEqual(
            3 * A,
            Matrix([
                [3, 6],
                [9, 12]
            ])
        )

    def test_elementwise_multiply(self):
        A = Matrix([
            [1, 2],
            [3, 4]
        ])

        B = Matrix([
            [5, 6],
            [7, 8]
        ])

        self.assertEqual(
            A.elementwise_multiply(B),
            Matrix([
                [5, 12],
                [21, 32]
            ])
        )

        with self.assertRaises(ValueError):
            A.elementwise_multiply(
                Matrix([
                    [1, 2, 3],
                    [4, 5, 6]
                ])
            )

        self.assertEqual(
            A * B,
            Matrix([
                [19, 22],
                [43, 50]
            ])
        )


    def test_apply(self):
        A = Matrix([
            [1, 2],
            [3, 4]
        ])

        result = A.apply(lambda x: x * 2)

        self.assertEqual(
            result,
            Matrix([
                [2, 4],
                [6, 8]
            ])
        )


    def test_apply_builtin(self):
        A = Matrix([
            [-1, 2],
            [-3, 4]
        ])

        result = A.apply(abs)

        self.assertEqual(
            result,
            Matrix([
                [1, 2],
                [3, 4]
            ])
        )


    def test_exp(self):
        A = Matrix([
            [0, 1],
            [2, 0]
        ])

        result = A.exp()

        self.assertEqual(result[0, 0], 1)
        self.assertEqual(result[1, 1], 1)

        self.assertAlmostEqual(result[0, 1], 2.718281828459045)
        self.assertAlmostEqual(result[1, 0], 7.38905609893065)


    def test_log(self):
        A = Matrix([
            [1, math.e],
            [math.e ** 2, 10]
        ])

        result = A.log()

        self.assertAlmostEqual(result[0, 0], 0)
        self.assertAlmostEqual(result[0, 1], 1)
        self.assertAlmostEqual(result[1, 0], 2)
        self.assertAlmostEqual(result[1, 1], math.log(10))

    def test_sqrt(self):
        A = Matrix([
            [1, 4],
            [9, 16]
        ])

        result = A.sqrt()

        self.assertEqual(result[0, 0], 1)
        self.assertEqual(result[0, 1], 2)
        self.assertEqual(result[1, 0], 3)
        self.assertEqual(result[1, 1], 4)

    def test_abs(self):
        A = Matrix([
            [-1, 2],
            [-3, -4]
        ])

        result = A.abs()

        self.assertEqual(result[0, 0], 1)
        self.assertEqual(result[0, 1], 2)
        self.assertEqual(result[1, 0], 3)
        self.assertEqual(result[1, 1], 4)

    def test_sin(self):
        A = Matrix([
            [0, math.pi / 2],
            [math.pi, 3 * math.pi / 2]
        ])

        result = A.sin()

        self.assertAlmostEqual(result[0, 0], 0)
        self.assertAlmostEqual(result[0, 1], 1)
        self.assertAlmostEqual(result[1, 0], 0)
        self.assertAlmostEqual(result[1, 1], -1)

    def test_cos(self):
        A = Matrix([
            [0, math.pi / 2],
            [math.pi, 2 * math.pi]
        ])

        result = A.cos()

        self.assertAlmostEqual(result[0, 0], 1)
        self.assertAlmostEqual(result[0, 1], 0)
        self.assertAlmostEqual(result[1, 0], -1)
        self.assertAlmostEqual(result[1, 1], 1)

    def test_tan(self):
        A = Matrix([
            [0, math.pi / 4],
            [-math.pi / 4, math.pi]
        ])

        result = A.tan()

        self.assertAlmostEqual(result[0, 0], 0)
        self.assertAlmostEqual(result[0, 1], 1)
        self.assertAlmostEqual(result[1, 0], -1)
        self.assertAlmostEqual(result[1, 1], 0)

    def test_sinh(self):
        A = Matrix([
            [0, 1],
            [-1, 2]
        ])

        result = A.sinh()

        self.assertAlmostEqual(result[0, 0], 0)
        self.assertAlmostEqual(result[0, 1], math.sinh(1))
        self.assertAlmostEqual(result[1, 0], math.sinh(-1))
        self.assertAlmostEqual(result[1, 1], math.sinh(2))

    def test_cosh(self):
        A = Matrix([
            [0, 1],
            [-1, 2]
        ])

        result = A.cosh()

        self.assertAlmostEqual(result[0, 0], 1)
        self.assertAlmostEqual(result[0, 1], math.cosh(1))
        self.assertAlmostEqual(result[1, 0], math.cosh(-1))
        self.assertAlmostEqual(result[1, 1], math.cosh(2))

    def test_tanh(self):
        A = Matrix([
            [0, 1],
            [-1, 2]
        ])

        result = A.tanh()

        self.assertAlmostEqual(result[0, 0], 0)
        self.assertAlmostEqual(result[0, 1], math.tanh(1))
        self.assertAlmostEqual(result[1, 0], math.tanh(-1))
        self.assertAlmostEqual(result[1, 1], math.tanh(2))

        self.assertAlmostEqual(result[1, 0], -result[0, 1])

    def test_sum(self):
        A = Matrix([
            [1, 2],
            [3, 4]
        ])

        self.assertEqual(A.sum(), 10)

    def test_sum_negative(self):
        A = Matrix([
            [-1, 2],
            [-3, 4]
        ])

        self.assertEqual(A.sum(), 2)

    def test_sum_single(self):
        A = Matrix([[7]])

        self.assertEqual(A.sum(), 7)

    def test_mean_negative(self):
        A = Matrix([
            [-2, 4],
            [6, -8]
        ])

        self.assertEqual(A.mean(), 0)

    def test_mean_non_square(self):
        A = Matrix([
            [1, 2, 3],
            [4, 5, 6]
        ])

        self.assertEqual(A.mean(), 3.5)

    def test_max(self):
        A = Matrix([
            [3, 7],
            [-2, 5]
        ])

        self.assertEqual(A.max(), 7)

    def test_prod(self):
        A = Matrix([
            [1, 2],
            [3, 4]
        ])

        self.assertEqual(A.prod(), 24)

    def test_prod(self):
        A = Matrix([
            [1, 2],
            [3, 4]
        ])

        self.assertEqual(A.prod(), 24)

    def test_norm(self):
        A = Matrix([
            [3, 4]
        ])

        self.assertEqual(A.norm(), 5)

    def test_norm_matrix(self):
        A = Matrix([
            [1, 2],
            [3, 4]
        ])

        self.assertAlmostEqual(
            A.norm(),
            math.sqrt(30)
        )

    def test_apply_square(self):
        A = Matrix([
            [1, 2],
            [3, 4]
        ])

        result = A.apply(lambda x: x ** 2)

        self.assertEqual(
            result,
            Matrix([
                [1, 4],
                [9, 16]
            ])
        )

    def test_apply_square(self):
        A = Matrix([
            [1, 2],
            [3, 4]
        ])

        result = A.apply(lambda x: x ** 2)

        self.assertEqual(
            result,
            Matrix([
                [1, 4],
                [9, 16]
            ])
        )

    def test_matrix_multiplication_after_sum(self):
        A = Matrix([
            [1, 2],
            [3, 4]
        ])

        B = Matrix([
            [5, 6],
            [7, 8]
        ])

        self.assertEqual(
            A * B,
            Matrix([
                [19, 22],
                [43, 50]
            ])
        )

    def test_random_uniform_square(self):
        A = Matrix.random_uniform(3)

        self.assertEqual(A.order, (3, 3))

        for i in range(3):
            for j in range(3):
                self.assertGreaterEqual(A[i, j], -1.0)
                self.assertLess(A[i, j], 1.0)

    def test_random_uniform_rectangular(self):
        A = Matrix.random_uniform(2, 4)

        self.assertEqual(A.order, (2, 4))

        for i in range(2):
            for j in range(4):
                self.assertGreaterEqual(A[i, j], -1.0)
                self.assertLess(A[i, j], 1.0)

    def test_random_uniform_range(self):
        A = Matrix.random_uniform(
            3,
            2,
            10,
            20
        )

        for i in range(3):
            for j in range(2):
                self.assertGreaterEqual(A[i, j], 10)
                self.assertLess(A[i, j], 20)

    def test_random_uniform_invalid_dimensions(self):
        with self.assertRaises(ValueError):
            Matrix.random_uniform(0, 2)

        with self.assertRaises(ValueError):
            Matrix.random_uniform(-1, 2)

    def test_random_uniform_invalid_range(self):
        with self.assertRaises(ValueError):
            Matrix.random_uniform(2, 2, 5, 5)

        with self.assertRaises(ValueError):
            Matrix.random_uniform(2, 2, 10, 5)

    def test_random_uniform_seed(self):
        Matrix.seed(42)

        A = Matrix.random_uniform(2, 3)

        Matrix.seed(42)

        B = Matrix.random_uniform(2, 3)

        self.assertEqual(A, B)

    def test_random_uniform_different_seed(self):
        Matrix.seed(42)
        A = Matrix.random_uniform(2, 2)

        Matrix.seed(100)
        B = Matrix.random_uniform(2, 2)

        self.assertNotEqual(A, B)

    def test_shape(self):
        A = Matrix([
            [1, 2, 3],
            [4, 5, 6]
        ])

        self.assertEqual(A.shape, (2, 3))
        self.assertEqual(A.shape, A.order)

    def test_flatten(self):
        A = Matrix([
            [1, 2, 3],
            [4, 5, 6]
        ])

        result = A.flatten()

        self.assertEqual(
            result,
            Matrix([
                [1, 2, 3, 4, 5, 6]
            ])
        )

    def test_flatten_order(self):
        A = Matrix([
            [1, 2],
            [3, 4],
            [5, 6]
        ])

        result = A.flatten()

        self.assertEqual(result.order, (1, 6))

    def test_flatten_does_not_modify_original(self):
        A = Matrix([
            [1, 2],
            [3, 4]
        ])

        A.flatten()

        self.assertEqual(
            A,
            Matrix([
                [1, 2],
                [3, 4]
            ])
        )

    def test_reshape(self):
        A = Matrix([
            [1, 2, 3],
            [4, 5, 6]
        ])

        result = A.reshape(3, 2)

        self.assertEqual(
            result,
            Matrix([
                [1, 2],
                [3, 4],
                [5, 6]
            ])
        )

    def test_reshape_invalid_size(self):
        A = Matrix([
            [1, 2],
            [3, 4]
        ])

        with self.assertRaises(ValueError):
            A.reshape(3, 3)

    def test_reshape_invalid_dimensions(self):
        A = Matrix([
            [1, 2],
            [3, 4]
        ])

        with self.assertRaises(ValueError):
            A.reshape(0, 4)

        with self.assertRaises(ValueError):
            A.reshape(4, 0)

        with self.assertRaises(ValueError):
            A.reshape(-1, 4)

    def test_reshape_does_not_modify_original(self):
        A = Matrix([
            [1, 2],
            [3, 4]
        ])

        A.reshape(4, 1)

        self.assertEqual(
            A,
            Matrix([
                [1, 2],
                [3, 4]
            ])
        )


    def test_swap_rows(self):
        A = Matrix([
            [1, 2],
            [3, 4],
            [5, 6]
        ])

        result = A.swapRows(0, 2)

        self.assertEqual(
            result,
            Matrix([
                [5, 6],
                [3, 4],
                [1, 2]
            ])
        )

    def test_swap_rows_not_inplace(self):
        A = Matrix([
            [1, 2],
            [3, 4]
        ])

        A.swapRows(0, 1)

        self.assertEqual(
            A,
            Matrix([
                [1, 2],
                [3, 4]
            ])
        )

    def test_swap_rows_not_inplace(self):
        A = Matrix([
            [1, 2],
            [3, 4]
        ])

        A.swapRows(0, 1)

        self.assertEqual(
            A,
            Matrix([
                [1, 2],
                [3, 4]
            ])
        )

    def test_swap_rows_invalid_index(self):
        A = Matrix([
            [1, 2],
            [3, 4]
        ])

        with self.assertRaises(IndexError):
            A.swapRows(-1, 1)

        with self.assertRaises(IndexError):
            A.swapRows(0, 2)

    def test_swap_rows_invalid_index(self):
        A = Matrix([
            [1, 2],
            [3, 4]
        ])

        with self.assertRaises(IndexError):
            A.swapRows(-1, 1)

        with self.assertRaises(IndexError):
            A.swapRows(0, 2)

    def test_swap_cols_not_inplace(self):
        A = Matrix([
            [1, 2],
            [3, 4]
        ])

        A.swapCols(0, 1)

        self.assertEqual(
            A,
            Matrix([
                [1, 2],
                [3, 4]
            ])
        )

    def test_swap_cols_inplace(self):
        A = Matrix([
            [1, 2],
            [3, 4]
        ])

        result = A.swapCols(0, 1, inplace=True)

        self.assertIs(result, A)

        self.assertEqual(
            A,
            Matrix([
                [2, 1],
                [4, 3]
            ])
        )

    def test_swap_cols_invalid_index(self):
        A = Matrix([
            [1, 2],
            [3, 4]
        ])

        with self.assertRaises(IndexError):
            A.swapCols(-1, 1)

        with self.assertRaises(IndexError):
            A.swapCols(0, 2)

    def test_is_approx_equal(self):
        A = Matrix([
            [1.0, 2.0],
            [3.0, 4.0]
        ])

        B = Matrix([
            [1.0, 2.0],
            [3.0, 4.0]
        ])

        self.assertTrue(A.isApproxEqual(B))

    def test_is_approx_equal_floating_point(self):
        A = Matrix([
            [0.1 + 0.2]
        ])

        B = Matrix([
            [0.3]
        ])

        self.assertTrue(A.isApproxEqual(B))

    def test_is_approx_equal_outside_tolerance(self):
        A = Matrix([
            [1.0]
        ])

        B = Matrix([
            [1.001]
        ])

        self.assertFalse(A.isApproxEqual(B))

    def test_is_approx_equal_custom_tolerance(self):
        A = Matrix([
            [1.0]
        ])

        B = Matrix([
            [1.001]
        ])

        self.assertTrue(
            A.isApproxEqual(B, tolerance=0.01)
        )

    def test_is_approx_equal_different_shape(self):
        A = Matrix([
            [1, 2]
        ])

        B = Matrix([
            [1],
            [2]
        ])

        self.assertFalse(A.isApproxEqual(B))

    def test_is_approx_equal_negative_tolerance(self):
        A = Matrix([[1]])
        B = Matrix([[1]])

        with self.assertRaises(ValueError):
            A.isApproxEqual(B, tolerance=-1)

    def test_exact_equality_still_exact(self):
        A = Matrix([[0.1 + 0.2]])
        B = Matrix([[0.3]])

        self.assertFalse(A == B)
        self.assertTrue(A.isApproxEqual(B))



if __name__ == "__main__":
    unittest.main()