# PyMat Matrix Manipulation

Matrix indexing, iteration, row/column operations, and structural transformations available in **PyMat 1.0.0**.

---

## Table of Contents

1. [Overview](#overview)
2. [Indexing](#indexing)
3. [Modifying Elements](#modifying-elements)
4. [Iteration](#iteration)
5. [Rows](#rows)
6. [Columns](#columns)
7. [Swapping Rows](#swapping-rows)
8. [Swapping Columns](#swapping-columns)
9. [Flattening](#flattening)
10. [Reshaping](#reshaping)
11. [Copying](#copying)
12. [Manipulation Summary](#manipulation-summary)

---

# Overview

PyMat provides several operations for accessing and modifying matrix data.

These operations include:

* Element indexing
* Element assignment
* Matrix iteration
* Row insertion
* Column insertion
* Row deletion
* Column deletion
* Row retrieval
* Column retrieval
* Row swapping
* Column swapping
* Flattening
* Reshaping
* Copying

Example matrix:

```python id="h7q3m1"
from matrix import Matrix

A = Matrix([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])
```

---

# Indexing

Matrix elements are accessed using:

```python id="p4n8v2"
A[row, column]
```

Both row and column indices are zero-based.

For:

```text id="c6x1m9"
[1 2 3]
[4 5 6]
[7 8 9]
```

the element:

```python id="k2r7w5"
A[0, 0]
```

is:

```text id="m8q3v1"
1
```

and:

```python id="z5n4c8"
A[1, 2]
```

is:

```text id="u3p9x6"
6
```

---

# Modifying Elements

An individual element can be changed using the same indexing syntax.

```python id="r6v2k9"
A[0, 1] = 20
```

Before:

```text id="q4m8x1"
[1 2 3]
[4 5 6]
[7 8 9]
```

After:

```text id="w7c3p5"
[1 20 3]
[4  5 6]
[7  8 9]
```

---

# Iteration

A `Matrix` can be iterated over.

```python id="n2v6k8"
for row in A:
    print(row)
```

This provides access to the matrix rows during iteration.

Example:

```python id="f8m4q1"
for row in A:
    print(row)
```

---

# Traverse

PyMat also exposes the matrix traversal through:

```python id="x3p7v9"
A.traverse
```

This provides access to the matrix's traversal representation.

---

# Rows

PyMat provides operations for inserting, deleting, and retrieving rows.

---

## `insertRow()`

Inserts a row into a matrix.

```python id="j6q2m8"
A.insertRow(...)
```

The supplied row must be compatible with the matrix's column count and the method's expected insertion format.

---

## `getRow()`

Retrieves a row from the matrix.

```python id="c9v4x7"
row = A.getRow(...)
```

This is useful when a specific row needs to be accessed independently.

---

## `delRow()`

Deletes a row.

```python id="m5k8p2"
A.delRow(...)
```

The matrix order changes after a row is removed.

For example, removing one row from a:

```text id="t7n3c6"
3 × 3
```

matrix produces a:

```text id="r2x9v4"
2 × 3
```

matrix.

---

# Columns

PyMat provides equivalent operations for columns.

---

## `insertCol()`

Inserts a column into a matrix.

```python id="b8q1m5"
A.insertCol(...)
```

The supplied column must be compatible with the matrix's row count and the method's expected insertion format.

---

## `getCol()`

Retrieves a column.

```python id="x4c7n2"
column = A.getCol(...)
```

---

## `delCol()`

Deletes a column.

```python id="p9v3k6"
A.delCol(...)
```

Removing one column from a:

```text id="j2m8q5"
3 × 3
```

matrix produces a:

```text id="w6x1c9"
3 × 2
```

matrix.

---

# Swapping Rows

## `swapRows()`

Swaps two rows.

```python id="r8k4m2"
B = A.swapRows(row1, row2)
```

Example:

```python id="v5q9x3"
A = Matrix([
    [1, 2],
    [3, 4]
])

B = A.swapRows(0, 1)
```

Result:

```text id="c7m1n8"
[3 4]
[1 2]
```

The original `A` is unchanged.

---

## In-place Row Swapping

To modify the original matrix directly:

```python id="n4x8p6"
A.swapRows(0, 1, inplace=True)
```

After this operation, `A` itself contains the swapped rows.

### Default behavior

```python id="y3q7k1"
B = A.swapRows(0, 1)
```

returns a new matrix.

### In-place behavior

```python id="f6m2v9"
A.swapRows(0, 1, inplace=True)
```

modifies `A`.

---

## Invalid Row Indices

The row indices must refer to existing rows.

An invalid index raises:

```text id="q8c4x5"
IndexError
```

---

# Swapping Columns

## `swapCols()`

Swaps two columns.

```python id="k7m3v1"
B = A.swapCols(col1, col2)
```

Example:

```python id="z2q8c6"
A = Matrix([
    [1, 2],
    [3, 4]
])

B = A.swapCols(0, 1)
```

Result:

```text id="p5x9n4"
[2 1]
[4 3]
```

The original matrix remains unchanged.

---

## In-place Column Swapping

To modify the original matrix:

```python id="c1v6m8"
A.swapCols(0, 1, inplace=True)
```

---

## Invalid Column Indices

An invalid column index raises:

```text id="w4q7k2"
IndexError
```

---

# Flattening

## `flatten()`

Converts the matrix into a single-row matrix.

```python id="m9x3c7"
B = A.flatten()
```

Example:

```text id="v2n8q5"
A = [1 2]
    [3 4]
    [5 6]
```

After:

```python id="s6k1p4"
B = A.flatten()
```

the result is:

```text id="x8m5c2"
[1 2 3 4 5 6]
```

---

## Flattening Order

Elements are collected row by row.

For:

```text id="q4v7n1"
[1 2 3]
[4 5 6]
```

the flattened result is:

```text id="k8p2x6"
[1 2 3 4 5 6]
```

---

# Reshaping

## `reshape()`

Changes the dimensions of a matrix while preserving all elements.

```python id="n5c9q3"
B = A.reshape(rows, cols)
```

The total number of elements must remain unchanged.

The required condition is:

```text id="y7m2v8"
new_rows × new_cols
=
old_rows × old_cols
```

---

## Example

Start with:

```python id="r3x8k1"
A = Matrix([
    [1, 2],
    [3, 4]
])
```

`A` has:

```text id="p6q4n9"
2 × 2 = 4 elements
```

Reshape it into:

```python id="c8v2m5"
B = A.reshape(4, 1)
```

Result:

```text id="f1k7x3"
[1]
[2]
[3]
[4]
```

---

## Another Example

```python id="m4q9c2"
B = A.reshape(1, 4)
```

Result:

```text id="v8n3p6"
[1 2 3 4]
```

---

## Invalid Reshape

The number of elements must remain the same.

For a `2 × 2` matrix:

```python id="x6k1q8"
A.reshape(3, 2)
```

is invalid because:

```text id="n9c4m7"
2 × 2 ≠ 3 × 2
```

and raises:

```text id="p2v5x1"
ValueError
```

Matrix dimensions must also be positive.

---

# Copying

## `copy()`

Creates an independent copy of a matrix.

```python id="q7m3c9"
B = A.copy()
```

Example:

```python id="w5x8n2"
A = Matrix([
    [1, 2],
    [3, 4]
])

B = A.copy()

B[0, 0] = 100
```

`B` becomes:

```text id="j4p1v7"
[100 2]
[  3 4]
```

while `A` remains:

```text id="s8k2m6"
[1 2]
[3 4]
```

This means the copy does not share the original matrix's internal nested-list storage.

---

# Non-Mutating vs In-Place Operations

PyMat distinguishes between operations that return a new matrix and operations that explicitly modify the existing matrix.

### Non-mutating example

```python id="c5n9x2"
B = A.swapRows(0, 1)
```

`A` remains unchanged.

### In-place example

```python id="m7q3v8"
A.swapRows(0, 1, inplace=True)
```

`A` is modified.

This explicit `inplace=True` design helps prevent accidental modification of matrices.

---

# Manipulation Summary

| Operation     | Syntax             | Purpose                   |
| ------------- | ------------------ | ------------------------- |
| Index         | `A[i, j]`          | Access an element         |
| Assignment    | `A[i, j] = x`      | Modify an element         |
| Iteration     | `for row in A`     | Iterate through rows      |
| Traverse      | `A.traverse`       | Matrix traversal          |
| Insert row    | `A.insertRow(...)` | Add a row                 |
| Insert column | `A.insertCol(...)` | Add a column              |
| Get row       | `A.getRow(...)`    | Retrieve a row            |
| Get column    | `A.getCol(...)`    | Retrieve a column         |
| Delete row    | `A.delRow(...)`    | Remove a row              |
| Delete column | `A.delCol(...)`    | Remove a column           |
| Swap rows     | `A.swapRows(...)`  | Exchange rows             |
| Swap columns  | `A.swapCols(...)`  | Exchange columns          |
| Flatten       | `A.flatten()`      | Convert to one row        |
| Reshape       | `A.reshape(r, c)`  | Change dimensions         |
| Copy          | `A.copy()`         | Create independent matrix |

---

# Example Workflow

The following example combines several manipulation operations:

```python id="u2m8q5"
from matrix import Matrix

A = Matrix([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

# Access an element
print(A[1, 2])

# Modify an element
A[1, 2] = 10

# Swap rows without modifying A
B = A.swapRows(0, 2)

# Swap columns in-place
A.swapCols(0, 1, inplace=True)

# Flatten
C = A.flatten()

# Reshape
D = A.reshape(1, 9)

# Create an independent copy
E = A.copy()
```

These operations provide the basic tools required to rearrange and transform matrix data in PyMat.
