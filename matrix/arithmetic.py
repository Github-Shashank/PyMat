from math import (
    exp     as mathexp,
    log     as mathlog,
    sqrt    as mathsqrt,
    sin     as mathsin,
    cos     as mathcos,
    tan     as mathtan,
    sinh    as mathsinh,
    cosh    as mathcosh,
    tanh    as mathtanh

    )
import builtins

def add(matrix, other):
    if not matrix.isEqualOrder(other):
        raise ValueError()

    rows, cols = matrix.order

    result = [
        [
            matrix.m[i][j] + other.m[i][j]
            for j in range(cols)
        ]
        for i in range(rows)
    ]

    return type(matrix)(result)


def subtract(matrix, other):
    if not matrix.isEqualOrder(other):
        raise ValueError()

    rows, cols = matrix.order

    result = [
        [
            matrix.m[i][j] - other.m[i][j]
            for j in range(cols)
        ]
        for i in range(rows)
    ]

    return type(matrix)(result)


def multiply(matrix, other):
    # Scalar multiplication
    if isinstance(other, (int, float, complex)):
        return type(matrix)(
            [
                [matrix.m[i][j] * other for j in range(matrix.order[1])]
                for i in range(matrix.order[0])
            ]
        )

    if not matrix.isMultiplicable(other):
        raise ValueError()

    rows = matrix.order[0]
    cols = other.order[1]

    result = [
        [
            builtins.sum(
                matrix.m[i][k] * other.m[k][j]
                for k in range(matrix.order[1])
            )
            for j in range(cols)
        ]
        for i in range(rows)
    ]

    return type(matrix)(result)


def elementwise_multiply(matrix, other):
    if not matrix.isEqualOrder(other):
        raise ValueError()

    rows, cols = matrix.order

    result = [
        [
            matrix.m[i][j] * other.m[i][j]
            for j in range(cols)
        ]
        for i in range(rows)
    ]

    return type(matrix)(result)


def divide(matrix, other):
    if other == 0:
        raise ZeroDivisionError("division by zero")

    return type(matrix)(
        [
            [matrix.m[i][j] / other for j in range(matrix.order[1])]
            for i in range(matrix.order[0])
        ]
    )


def negate(matrix):
    return type(matrix)(
        [
            [-matrix.m[i][j] for j in range(matrix.order[1])]
            for i in range(matrix.order[0])
        ]
    )


def power(matrix, raised_to):
    if isinstance(raised_to, int) and raised_to > 0:
        I = type(matrix).identity(matrix.order[0])

        for _ in range(raised_to):
            I = I * matrix

        return I


def apply(matrix, function):
    rows, cols = matrix.order

    result = [
        [
            function(matrix.m[i][j])
            for j in range(cols)
        ]
        for i in range(rows)
    ]

    return type(matrix)(result)


def exp(matrix):
    return apply(matrix, mathexp)

def log(matrix):
    return apply(matrix, mathlog)

def sqrt(matrix):
    return apply(matrix, mathsqrt)

def abs(matrix):
    return apply(matrix, builtins.abs)

def sin(matrix):
    return apply(matrix, mathsin)

def cos(matrix):
    return apply(matrix, mathcos)

def tan(matrix):
    return apply(matrix, mathtan)

def sinh(matrix):
    return apply(matrix, mathsinh)

def cosh(matrix):
    return apply(matrix, mathcosh)

def tanh(matrix):
    return apply(matrix, mathtanh)

def sum(matrix):
    return builtins.sum(
        matrix.m[i][j]
        for i in range(matrix.order[0])
        for j in range(matrix.order[1])
    )

def mean(matrix):
    rows, cols = matrix.order
    return matrix.sum() / (rows * cols)

def min(matrix):
    return builtins.min(
        matrix.m[i][j]
        for i in range(matrix.order[0])
        for j in range(matrix.order[1])
    )


def max(matrix):
    return builtins.max(
        matrix.m[i][j]
        for i in range(matrix.order[0])
        for j in range(matrix.order[1])
    )


def prod(matrix):
    result = 1

    for i in range(matrix.order[0]):
        for j in range(matrix.order[1]):
            result *= matrix.m[i][j]

    return result


def norm_squared(matrix):
    return builtins.sum(
        matrix.m[i][j] ** 2
        for i in range(matrix.order[0])
        for j in range(matrix.order[1])
    )

def norm(matrix):
    return mathsqrt(norm_squared(matrix))