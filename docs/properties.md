# PyMat Matrix Properties

Matrix properties and validation-related checks available in **PyMat 1.0.0**.

---

## Table of Contents

1. [Overview](#overview)
2. [Order](#order)
3. [Shape](#shape)
4. [Square Matrix](#square-matrix)
5. [Diagonal Matrix](#diagonal-matrix)
6. [Row Matrix](#row-matrix)
7. [Column Matrix](#column-matrix)
8. [Scalar Matrix](#scalar-matrix)
9. [Identity Matrix](#identity-matrix)
10. [Zero Matrix](#zero-matrix)
11. [Symmetric Matrix](#symmetric-matrix)
12. [Skew-Symmetric Matrix](#skew-symmetric-matrix)
13. [Invertibility](#invertibility)
14. [Singular Matrix](#singular-matrix)
15. [Non-Singular Matrix](#non-singular-matrix)
16. [Approximate Equality](#approximate-equality)
17. [Validation Helpers](#validation-helpers)
18. [Property Summary](#property-summary)

---

# Overview

PyMat provides properties and methods for determining the mathematical structure and characteristics of a matrix.

These include:

* Matrix dimensions
* Square matrices
* Diagonal matrices
* Row matrices
* Column matrices
* Scalar matrices
* Identity matrices
* Zero matrices
* Symmetric matrices
* Skew-symmetric matrices
* Invertibility
* Singularity
* Non-singularity
* Approximate equality
* Index and dimension validation

Example:

```python id="x7m2q9"
from matrix import Matrix

A = Matrix([
    [1, 2],
    [3, 4]
])
```

---

# Order

## `A.order`

Returns the dimensions of the matrix as:

```text id="p4v8n1"
(rows, columns)
```

Example:

```python id="c6q3m9"
A = Matrix([
    [1, 2, 3],
    [4, 5, 6]
])

print(A.order)
```

Result:

```text id="k8x2v5"
(2, 3)
```

---

# Shape

## `A.shape`

`shape` is an alias for `order`.

```python id="m5n9q2"
print(A.shape)
```

For a `2 × 3` matrix:

```text id="r7c4x1"
(2, 3)
```

Therefore:

```python id="v3k8p6"
A.shape == A.order
```

returns:

```text id="j2m5q9"
True
```

---

# Square Matrix

## `A.isSqrMatrix`

Checks whether the matrix is square.

A matrix is square when:

```text id="q6x3m8"
rows = columns
```

Example:

```python id="n4v7p1"
A = Matrix([
    [1, 2],
    [3, 4]
])

print(A.isSqrMatrix)
```

Result:

```text id="c8m2q5"
True
```

A `2 × 3` matrix is not square.

---

# Diagonal Matrix

## `A.isDiagMatrix`

Checks whether a matrix is diagonal.

A diagonal matrix is a square matrix in which every element outside the main diagonal is zero.

Example:

```python id="x5k9v2"
A = Matrix([
    [1, 0, 0],
    [0, 2, 0],
    [0, 0, 3]
])

print(A.isDiagMatrix)
```

Result:

```text id="m7q3c8"
True
```

---

# Row Matrix

## `A.isRowMatrix`

Checks whether the matrix contains exactly one row.

Example:

```python id="p4n8x1"
A = Matrix([
    [1, 2, 3]
])

print(A.isRowMatrix)
```

Result:

```text id="w6m2q9"
True
```

A row matrix has the form:

```text id="r3v7k5"
[a b c ...]
```

---

# Column Matrix

## `A.isColMatrix`

Checks whether the matrix contains exactly one column.

Example:

```python id="c9x4m7"
A = Matrix([
    [1],
    [2],
    [3]
])

print(A.isColMatrix)
```

Result:

```text id="n5q8v2"
True
```

A column matrix has the form:

```text id="j1m6p9"
[a]
[b]
[c]
```

---

# Scalar Matrix

## `A.isSclrMatrix`

Checks whether a matrix is a scalar matrix.

A scalar matrix is a diagonal matrix whose diagonal elements are equal.

For example:

```text id="v8k3q1"
[5 0]
[0 5]
```

is a scalar matrix.

Example:

```python id="m4x7c2"
A = Matrix([
    [5, 0],
    [0, 5]
])

print(A.isSclrMatrix)
```

Result:

```text id="q9n2p6"
True
```

---

# Identity Matrix

## `A.isIdntMatrix`

Checks whether a matrix is an identity matrix.

An identity matrix has:

```text id="x6m3v8"
1
```

on the main diagonal and:

```text id="k4q7n1"
0
```

everywhere else.

Example:

```python id="p2c9m5"
A = Matrix([
    [1, 0],
    [0, 1]
])

print(A.isIdntMatrix)
```

Result:

```text id="w8v4x2"
True
```

---

# Zero Matrix

## `A.isZeroMatrix`

Checks whether every element of the matrix is zero.

Example:

```python id="n7m3q9"
A = Matrix([
    [0, 0],
    [0, 0]
])

print(A.isZeroMatrix)
```

Result:

```text id="c5x8v1"
True
```

---

# Symmetric Matrix

## `A.isSymtMatrix`

Checks whether the matrix is symmetric.

A matrix is symmetric when:

```text id="j4q9m2"
A = Aᵀ
```

For individual elements:

```text id="v6n3x8"
A[i, j] = A[j, i]
```

Example:

```python id="m8p2c5"
A = Matrix([
    [1, 2, 3],
    [2, 4, 5],
    [3, 5, 6]
])

print(A.isSymtMatrix)
```

Result:

```text id="r1k7q4"
True
```

A symmetric matrix must be square.

---

# Skew-Symmetric Matrix

## `A.isSkewSymtMatrix`

Checks whether the matrix is skew-symmetric.

A matrix is skew-symmetric when:

```text id="x9m4v2"
Aᵀ = -A
```

Therefore:

```text id="p6q1n8"
A[i, j] = -A[j, i]
```

For a skew-symmetric matrix, every diagonal element must be zero.

Example:

```python id="k3c8m5"
A = Matrix([
    [ 0,  2],
    [-2,  0]
])

print(A.isSkewSymtMatrix)
```

Result:

```text id="w7v2q9"
True
```

---

# Invertibility

## `A.isInvertible`

Checks whether the matrix is invertible.

A matrix must be square and non-singular to have an inverse.

For a square matrix:

```text id="n5x3k8"
det(A) ≠ 0
```

indicates invertibility.

Example:

```python id="q8m1v6"
A = Matrix([
    [1, 2],
    [3, 4]
])

print(A.isInvertible)
```

Result:

```text id="c4p7x2"
True
```

---

# Singular Matrix

## `A.isSingularMatrix`

Checks whether a matrix is singular.

A square matrix is singular when:

```text id="m9v3q5"
det(A) = 0
```

A singular matrix does not have an inverse.

Example:

```python id="x2k6n8"
A = Matrix([
    [1, 2],
    [2, 4]
])

print(A.isSingularMatrix)
```

Result:

```text id="p5c9m1"
True
```

The rows are linearly dependent.

---

# Non-Singular Matrix

## `A.isNonSingularMatrix`

Checks whether a matrix is non-singular.

For a square matrix:

```text id="v7q2m4"
det(A) ≠ 0
```

indicates that the matrix is non-singular.

Example:

```python id="n8x3c6"
A = Matrix([
    [1, 2],
    [3, 4]
])

print(A.isNonSingularMatrix)
```

Result:

```text id="j4m9p2"
True
```

A non-singular square matrix is invertible.

---

# Relationship Between Singularity and Invertibility

For a square matrix, these properties are directly related.

```text id="r6k1v8"
Singular
    ↓
det(A) = 0
    ↓
Not invertible
```

and:

```text id="x3m7q5"
Non-singular
    ↓
det(A) ≠ 0
    ↓
Invertible
```

Therefore, for a square matrix:

```python id="c8v2n9"
A.isInvertible
```

and:

```python id="m5q7x1"
A.isNonSingularMatrix
```

represent closely related mathematical conditions.

---

# Approximate Equality

## `A.isApproxEqual(B)`

Checks whether two matrices are approximately equal within a specified tolerance.

```python id="p9n4v6"
A.isApproxEqual(B)
```

The default tolerance is:

```text id="k2x8m3"
1e-9
```

This is especially useful for floating-point calculations.

---

## Example

Consider:

```python id="w7q3c1"
A = Matrix([
    [1.0, 2.0],
    [3.0, 4.0]
])

B = Matrix([
    [1.0 + 1e-10, 2.0],
    [3.0, 4.0]
])
```

The matrices are not exactly equal:

```python id="v4m8n2"
A == B
```

may return:

```text id="j6q1x9"
False
```

But they are approximately equal:

```python id="c3p7k5"
A.isApproxEqual(B)
```

returns:

```text id="r8m2v6"
True
```

---

## Custom Tolerance

A different tolerance can be supplied:

```python id="n1x5q8"
A.isApproxEqual(
    B,
    tolerance=1e-6
)
```

A larger tolerance allows a larger numerical difference.

---

## Negative Tolerance

Tolerance must not be negative.

For example:

```python id="m7v3c9"
A.isApproxEqual(
    B,
    tolerance=-1
)
```

raises:

```text id="q4n8x2"
ValueError
```

---

## Shape Mismatch

Matrices with different dimensions are not approximately equal.

For example:

```text id="p6m2v7"
2 × 2
```

and:

```text id="x9c4k1"
2 × 3
```

cannot be approximately equal.

In this case:

```python id="w5q8n3"
A.isApproxEqual(B)
```

returns:

```text id="j2v6m9"
False
```

---

# Exact vs Approximate Equality

PyMat provides two different equality concepts.

### Exact equality

```python id="c7x3m5"
A == B
```

Requires corresponding elements to be exactly equal.

### Approximate equality

```python id="n8q4v1"
A.isApproxEqual(B)
```

Allows small numerical differences within the specified tolerance.

Use approximate equality when working with floating-point calculations.

---

# Validation Helpers

In addition to mathematical properties, PyMat provides methods for validating matrix operations.

---

## `isValidIndex()`

Checks whether an index refers to a valid matrix element.

```python id="r3m7x9"
A.isValidIndex(...)
```

This can be used before accessing or modifying an element.

---

## `isEqualOrder()`

Checks whether two matrices have the same dimensions.

```python id="v6q2k8"
A.isEqualOrder(B)
```

Example:

```text id="m4x9c1"
A = 2 × 3
B = 2 × 3
```

returns:

```text id="p7n3v5"
True
```

while matrices with different orders return:

```text id="q1k8m6"
False
```

---

## `isMultiplicable()`

Checks whether two matrices satisfy the dimension requirements for matrix multiplication.

For:

```text id="x5v2n9"
A = m × n
B = n × p
```

the matrices are multiplicable.

Example:

```python id="c8m4q7"
A.isMultiplicable(B)
```

---

# Property Summary

| Property              | Meaning                          |
| --------------------- | -------------------------------- |
| `order`               | Matrix dimensions                |
| `shape`               | Alias for `order`                |
| `isSqrMatrix`         | Matrix is square                 |
| `isDiagMatrix`        | Matrix is diagonal               |
| `isRowMatrix`         | Matrix has one row               |
| `isColMatrix`         | Matrix has one column            |
| `isSclrMatrix`        | Matrix is scalar                 |
| `isIdntMatrix`        | Matrix is identity               |
| `isZeroMatrix`        | Matrix contains only zero values |
| `isSymtMatrix`        | Matrix is symmetric              |
| `isSkewSymtMatrix`    | Matrix is skew-symmetric         |
| `isInvertible`        | Matrix is invertible             |
| `isSingularMatrix`    | Matrix is singular               |
| `isNonSingularMatrix` | Matrix is non-singular           |

---

# Validation Summary

| Method              | Purpose                             |
| ------------------- | ----------------------------------- |
| `isValidIndex()`    | Validate an element index           |
| `isEqualOrder()`    | Compare matrix dimensions           |
| `isMultiplicable()` | Check multiplication compatibility  |
| `isApproxEqual()`   | Compare matrices within a tolerance |

---

# Example

The following example demonstrates several properties together:

```python id="t6q2m8"
from matrix import Matrix

A = Matrix([
    [1, 2],
    [2, 1]
])

print("Order:", A.order)
print("Shape:", A.shape)

print("Square:", A.isSqrMatrix)
print("Diagonal:", A.isDiagMatrix)
print("Symmetric:", A.isSymtMatrix)
print("Skew-symmetric:", A.isSkewSymtMatrix)

print("Invertible:", A.isInvertible)
print("Singular:", A.isSingularMatrix)
print("Non-singular:", A.isNonSingularMatrix)
```

---

# Property Relationships

Some properties naturally imply others.

For example:

```text id="m3v8q1"
Identity Matrix
      ↓
Scalar Matrix
      ↓
Diagonal Matrix
      ↓
Square Matrix
```

Similarly:

```text id="x7n2c5"
Invertible
    ↕
Non-Singular
```

for square matrices.

And:

```text id="q4m9v6"
Singular
   ↓
Not Invertible
```

These relationships are useful when reasoning about matrix structure.

---

# Summary

PyMat's property API provides quick checks for common matrix classifications and mathematical characteristics.

The properties can be broadly grouped into:

```text id="v8k3m1"
Shape
 ├── order
 └── shape

Structure
 ├── isSqrMatrix
 ├── isDiagMatrix
 ├── isRowMatrix
 ├── isColMatrix
 ├── isSclrMatrix
 ├── isIdntMatrix
 └── isZeroMatrix

Symmetry
 ├── isSymtMatrix
 └── isSkewSymtMatrix

Invertibility
 ├── isInvertible
 ├── isSingularMatrix
 └── isNonSingularMatrix

Validation
 ├── isValidIndex()
 ├── isEqualOrder()
 ├── isMultiplicable()
 └── isApproxEqual()
```

These properties and validation methods form the structural and numerical checking layer of PyMat 1.0.
