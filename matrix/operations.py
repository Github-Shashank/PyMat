def transpose(matrix):
    rows, cols = matrix.order

    result = [
        [matrix.m[j][i] for j in range(rows)]
        for i in range(cols)
    ]

    return type(matrix)(result)


def minor(matrix, row_index, col_index):
    return matrix.delRow(row_index).delCol(col_index)


def cofactor(matrix, row_index, col_index):
    return ((-1) ** (row_index + col_index)) * determinant(
        minor(matrix, row_index, col_index)
    )


def determinant(matrix):
    rows, cols = matrix.order

    if rows != cols:
        raise ValueError()

    if rows == 1:
        return matrix.m[0][0]

    if rows == 2:
        m = matrix.m
        return m[0][0] * m[1][1] - m[0][1] * m[1][0]

    return sum(
        matrix.m[0][i] * cofactor(matrix, 0, i)
        for i in range(cols)
    )


def matrix_of_minors(matrix):
    rows, cols = matrix.order

    result = [
        [
            determinant(minor(matrix, i, j))
            for j in range(cols)
        ]
        for i in range(rows)
    ]

    return type(matrix)(result)


def matrix_of_cofactors(matrix):
    rows, cols = matrix.order

    result = [
        [
            cofactor(matrix, i, j)
            for j in range(cols)
        ]
        for i in range(rows)
    ]

    return type(matrix)(result)


def trace(self):
    r,c = self.order
    if not r == c:
        raise ValueError()
    return sum(self.m[i][i] for i in range(r))


def adjoint(matrix):
    return matrix_of_cofactors(matrix).transpose


def inverse(matrix):
    if not matrix.isInvertible:
        raise ValueError()

    return adjoint(matrix) * (1 / determinant(matrix))

def rank(matrix):
    values = [
        [matrix.m[i][j] for j in range(matrix.order[1])]
        for i in range(matrix.order[0])
    ]

    rows, cols = matrix.order
    rank = 0
    tolerance = 1e-12

    for col in range(cols):
        pivot = None

        for row in range(rank, rows):
            if abs(values[row][col]) > tolerance:
                pivot = row
                break

        if pivot is None:
            continue

        values[rank], values[pivot] = (
            values[pivot],
            values[rank]
        )

        pivot_value = values[rank][col]

        for row in range(rank + 1, rows):
            factor = values[row][col] / pivot_value

            for j in range(col, cols):
                values[row][j] -= factor * values[rank][j]

        rank += 1

        if rank == rows:
            break

    return rank

def solve(matrix, other):
    rows, cols = matrix.order

    if rows != cols:
        raise ValueError("coefficient matrix must be square")

    if other.order[0] != rows:
        raise ValueError("incompatible dimensions")

    n = rows

    augmented = [
        [
            matrix.m[i][j]
            for j in range(cols)
        ] + [
            other.m[i][j]
            for j in range(other.order[1])
        ]
        for i in range(rows)
    ]

    rhs_cols = other.order[1]
    tolerance = 1e-12

    for col in range(n):
        pivot = max(
            range(col, n),
            key=lambda row: abs(augmented[row][col])
        )

        if abs(augmented[pivot][col]) <= tolerance:
            raise ValueError("matrix is singular")

        augmented[col], augmented[pivot] = (
            augmented[pivot],
            augmented[col]
        )

        pivot_value = augmented[col][col]

        for j in range(col, n + rhs_cols):
            augmented[col][j] /= pivot_value

        for row in range(n):
            if row == col:
                continue

            factor = augmented[row][col]

            for j in range(col, n + rhs_cols):
                augmented[row][j] -= (
                    factor * augmented[col][j]
                )

    result = [
        augmented[i][n:n + rhs_cols]
        for i in range(n)
    ]

    return type(matrix)(result)