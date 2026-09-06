import copy

def insert_row(matrix, row_mat):
    cols = matrix.order[1]

    if len(row_mat) == cols:
        matrix.m.append(row_mat)
    else:
        raise ValueError(
            "Length Error! length of rowMat is not suitable for this Matrix."
        )


def insert_col(matrix, col_mat):
    rows = matrix.order[0]

    if len(col_mat) == rows:
        for i in range(rows):
            matrix.m[i].append(col_mat[i])
    else:
        raise ValueError(
            "Length Error! length of colMat is not suitable for this Matrix."
        )


def delete_row(matrix, row_index, inplace=False):
    rows = matrix.order[0]
    result = copy.deepcopy(matrix.m)

    if 0 <= row_index < rows:
        result.pop(row_index)

        if inplace:
            matrix.m = result
        else:
            return type(matrix)(result)
    else:
        raise ValueError(
            f"Index Error! index out of range {row_index} for 0 to {rows}"
        )


def delete_col(matrix, col_index, inplace=False):
    rows, cols = matrix.order
    result = copy.deepcopy(matrix.m)

    if 0 <= col_index < cols:
        for row in range(rows):
            result[row].pop(col_index)

        if inplace:
            matrix.m = result
        else:
            return type(matrix)(result)
    else:
        raise ValueError(
            f"Index Error! index out of range {col_index} for 0 to {cols}"
        )


def get_row(matrix, row_index):
    rows = matrix.order[0]

    if 0 <= row_index < rows:
        return matrix.m[row_index]
    else:
        raise ValueError()


def get_col(matrix, col_index):
    rows, cols = matrix.order

    if 0 <= col_index < cols:
        return [matrix.m[i][col_index] for i in range(rows)]
    else:
        raise ValueError()
    
def flatten(matrix):
    result = [
        value
        for row in matrix.m
        for value in row
    ]

    return type(matrix)([result])

def reshape(matrix, rows, cols):
    if rows <= 0 or cols <= 0:
        raise ValueError("matrix dimensions must be positive")

    if rows * cols != matrix.order[0] * matrix.order[1]:
        raise ValueError(
            "cannot reshape matrix: element count must remain unchanged"
        )

    values = [
        value
        for row in matrix.m
        for value in row
    ]

    result = [
        values[i * cols:(i + 1) * cols]
        for i in range(rows)
    ]

    return type(matrix)(result)

def swap_rows(matrix, row1, row2, inplace=False):
    rows, cols = matrix.order

    if not 0 <= row1 < rows:
        raise IndexError("invalid row index")

    if not 0 <= row2 < rows:
        raise IndexError("invalid row index")

    target = matrix if inplace else type(matrix)(copy.deepcopy(matrix.m))

    target.m[row1], target.m[row2] = (
        target.m[row2],
        target.m[row1]
    )

    return target

def swap_cols(matrix, col1, col2, inplace=False):
    rows, cols = matrix.order

    if not 0 <= col1 < cols:
        raise IndexError("invalid column index")

    if not 0 <= col2 < cols:
        raise IndexError("invalid column index")

    target = matrix if inplace else type(matrix)(copy.deepcopy(matrix.m))

    for i in range(rows):
        target.m[i][col1], target.m[i][col2] = (
            target.m[i][col2],
            target.m[i][col1]
        )

    return target

