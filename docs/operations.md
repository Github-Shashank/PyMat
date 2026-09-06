# PyMat Matrix Operations

Matrix operations and linear-algebra functionality available in **PyMat 1.0.0**.

---

## Table of Contents

1. [Overview](#overview)
2. [Transpose](#transpose)
3. [Minor](#minor)
4. [Cofactor](#cofactor)
5. [Matrix of Minors](#matrix-of-minors)
6. [Matrix of Cofactors](#matrix-of-cofactors)
7. [Determinant](#determinant)
8. [Trace](#trace)
9. [Adjoint](#adjoint)
10. [Inverse](#inverse)
11. [Rank](#rank)
12. [Solving Linear Systems](#solving-linear-systems)
13. [Operation Relationships](#operation-relationships)
14. [Examples](#examples)

---

# Overview

PyMat provides several operations for working with matrices and solving linear-algebra problems.

The main operations include:

* Transpose
* Minors
* Cofactors
* Matrix of minors
* Matrix of cofactors
* Determinant
* Trace
* Adjoint
* Inverse
* Rank
* Linear-system solving

Example:

```python id="a7m3q9"
from matrix import Matrix

A = Matrix([
    [1, 2],
    [3, 4]
])
```

---

# Transpose

## `A.transpose`

The transpose of a matrix is obtained by exchanging its rows and columns.

```python id="q4v8n2"
B = A.transpose
```

For:

```text id="x6k1p5"
A = [1 2 3]
    [4 5 6]
```

the transpose is:

```text id="m9c3w7"
Aᵀ = [1 4]
     [2 5]
     [3 6]
```

Therefore:

```text id="p2r8v4"
A : m × n
Aᵀ: n × m
```

---

# Minor

## `A.minor(row, column)`

The minor associated with an element is obtained by removing the element's row and column and calculating the determinant of the remaining matrix.

```python id="n5x2c8"
value = A.minor(row, column)
```

### Example

Consider:

```text id="j7q4m1"
A = [1 2 3]
    [4 5 6]
    [7 8 9]
```

The minor corresponding to element `A[0, 0]` is calculated from:

```text id="v3k9p6"
[5 6]
[8 9]
```

Its determinant is:

```text id="w8m2x5"
5×9 - 6×8 = -3
```

Therefore:

```python id="c1r7n4"
A.minor(0, 0)
```

returns:

```text id="s6q3v9"
-3
```

---

# Cofactor

## `A.cofactor(row, column)`

The cofactor of an element is:

```text id="x4m8p2"
Cᵢⱼ = (-1)ⁱ⁺ʲ Mᵢⱼ
```

where `Mᵢⱼ` is the corresponding minor.

In zero-based programming indices, PyMat uses the corresponding row and column indices.

```python id="k9v5c1"
value = A.cofactor(row, column)
```

For example:

```python id="m3q7x8"
A.cofactor(0, 0)
```

calculates the cofactor associated with the first element.

---

# Matrix of Minors

## `A.matrixOfMinors`

Returns a matrix containing the minor associated with every element.

```python id="r8n2v6"
M = A.matrixOfMinors
```

For:

```text id="t4c9m1"
A = [a b]
    [c d]
```

the matrix of minors has the corresponding minor value at each position.

For a `2 × 2` matrix:

```text id="y7p3x5"
[a b]  →  [d c]
[c d]     [b a]
```

---

# Matrix of Cofactors

## `A.matrixOfCofactors`

Returns the matrix containing the cofactors of all elements.

```python id="v2m8q4"
C = A.matrixOfCofactors
```

For:

```text id="f6n1k9"
A = [a b]
    [c d]
```

the cofactor matrix is:

```text id="q3x7m5"
[d  -c]
[-b  a]
```

---

# Determinant

## `A.determinant`

Returns the determinant of a square matrix.

```python id="j8c4v2"
det = A.determinant
```

---

## `2 × 2` Determinant

For:

```text id="m5q9x1"
A = [a b]
    [c d]
```

the determinant is:

```text id="r7v3n6"
det(A) = ad - bc
```

Example:

```python id="x2k8p4"
A = Matrix([
    [1, 2],
    [3, 4]
])

print(A.determinant)
```

Result:

```text id="w6m1c9"
-2
```

---

## Determinant and Invertibility

For a square matrix:

```text id="p9q4v7"
det(A) ≠ 0
```

indicates that the matrix is non-singular and has an inverse.

If:

```text id="c3x8m2"
det(A) = 0
```

the matrix is singular and does not have an inverse.

---

# Trace

## `A.trace`

Returns the sum of the main diagonal elements.

```python id="n7m2q5"
value = A.trace
```

For:

```text id="x4v8c1"
A = [1 2 3]
    [4 5 6]
    [7 8 9]
```

the trace is:

```text id="j6p3n9"
1 + 5 + 9 = 15
```

Therefore:

```python id="s8k2m4"
A.trace
```

returns:

```text id="z5q7v1"
15
```

The trace is defined for square matrices.

---

# Adjoint

## `A.adjoint`

Returns the adjoint of a matrix.

```python id="m9c4x6"
B = A.adjoint
```

For a matrix, the adjoint is obtained from the transpose of its cofactor matrix:

```text id="q2v8n5"
adj(A) = Cᵀ
```

where `C` is the matrix of cofactors.

Conceptually:

```text id="r6m1x9"
A
 ↓
Matrix of Cofactors
 ↓
Transpose
 ↓
Adjoint
```

---

# Inverse

## `A.inverse`

Returns the inverse of an invertible matrix.

```python id="w3p7k2"
B = A.inverse
```

The inverse satisfies:

```text id="n8q4v6"
A × A⁻¹ = I
```

where `I` is the identity matrix.

---

## Example

```python id="a5m9x3"
A = Matrix([
    [1, 2],
    [3, 4]
])

B = A.inverse
```

The inverse is:

```text id="j7c2v8"
[-2    1]
[3/2 -1/2]
```

up to the numerical representation used by PyMat.

---

## Conditions for an Inverse

A matrix must be:

1. Square
2. Non-singular

Therefore:

```text id="q4n8m1"
det(A) ≠ 0
```

must hold.

Attempting to invert a singular matrix results in an error.

---

# Rank

## `A.rank()`

Returns the rank of the matrix.

```python id="x6v3p9"
rank = A.rank()
```

Rank represents the number of linearly independent rows or columns.

---

## Example

```python id="m8q2c5"
A = Matrix([
    [1, 2],
    [2, 4]
])

print(A.rank())
```

The second row is twice the first row, so there is only one linearly independent row.

Result:

```text id="r4n7k1"
1
```

---

## Full-Rank Matrix

```python id="v5m9x2"
A = Matrix([
    [1, 0],
    [0, 1]
])

print(A.rank())
```

Result:

```text id="p8c3q6"
2
```

A `2 × 2` matrix with rank `2` has full rank.

---

## Rectangular Matrices

Rank is also defined for non-square matrices.

For example:

```python id="j1x7m4"
A = Matrix([
    [1, 2, 3],
    [4, 5, 6]
])

print(A.rank())
```

The maximum possible rank is:

```text id="w6q2v9"
min(rows, columns)
```

---

# Solving Linear Systems

## `A.solve(B)`

PyMat can solve systems represented by:

```text id="c8m4x1"
AX = B
```

using:

```python id="v3q9n7"
X = A.solve(B)
```

The method uses numerical elimination with pivoting.

---

## Basic Example

Consider:

```text id="m5k8p2"
2x + y = 5
x + 3y = 6
```

Represent the system as:

```python id="q7v2c9"
A = Matrix([
    [2, 1],
    [1, 3]
])

B = Matrix([
    [5],
    [6]
])
```

Solve:

```python id="n4x8m1"
X = A.solve(B)
```

The resulting matrix contains the values of `x` and `y`.

---

## Multiple Right-Hand Sides

PyMat also supports multiple right-hand sides.

For:

```text id="p6m3q8"
AX = B
```

where `B` contains multiple columns:

```python id="x9v4k2"
B = Matrix([
    [5, 1],
    [6, 2]
])

X = A.solve(B)
```

each column of `B` represents a separate right-hand side.

---

## Requirements

For `A.solve(B)`:

### Coefficient matrix

`A` must be square.

```text id="q2n7c5"
rows(A) = columns(A)
```

### Right-hand side

`B` must have the same number of rows as `A`.

```text id="m8v1x4"
rows(B) = rows(A)
```

---

## Singular Matrix

A singular coefficient matrix cannot be solved using the implemented direct solver.

For example:

```python id="c5q9m2"
A = Matrix([
    [1, 2],
    [2, 4]
])
```

has dependent rows and is singular.

Calling:

```python id="v7x3n8"
A.solve(B)
```

raises:

```text id="j4m6p1"
ValueError
```

---

## Incompatible Dimensions

If `B` does not have the correct number of rows:

```python id="r8k2q5"
A.solve(B)
```

raises:

```text id="x6n9v3"
ValueError
```

---

# Operation Relationships

Several PyMat operations are mathematically connected.

## Determinant → Inverse

For a square matrix:

```text id="m3q8v1"
det(A) ≠ 0
        ↓
A is non-singular
        ↓
A has an inverse
```

---

## Cofactors → Adjoint → Inverse

The inverse can be expressed as:

```text id="c7x2n9"
A⁻¹ = adj(A) / det(A)
```

where:

```text id="p4m8q6"
adj(A) = transpose(matrix of cofactors)
```

Conceptually:

```text id="v9n3k5"
A
│
├── minor()
│
├── cofactor()
│
└── matrixOfCofactors
          │
          ↓
       transpose
          │
          ↓
       adjoint
          │
          ↓
      determinant
          │
          ↓
       inverse
```

---

## Rank → Singularity

For an `n × n` matrix:

```text id="q6m2x8"
rank(A) < n
```

indicates that the matrix is rank-deficient and therefore singular.

A full-rank square matrix has:

```text id="w4v9c1"
rank(A) = n
```

---

# Examples

## Complete Matrix Analysis

```python id="k8p3m5"
from matrix import Matrix

A = Matrix([
    [1, 2],
    [3, 4]
])

print("Transpose:")
print(A.transpose)

print("Determinant:")
print(A.determinant)

print("Trace:")
print(A.trace)

print("Rank:")
print(A.rank())

print("Matrix of Cofactors:")
print(A.matrixOfCofactors)

print("Adjoint:")
print(A.adjoint)

print("Inverse:")
print(A.inverse)
```

---

## Solving a System

```python id="x5n8q2"
from matrix import Matrix

A = Matrix([
    [2, 1],
    [1, 3]
])

B = Matrix([
    [5],
    [6]
])

X = A.solve(B)

print(X)
```

---

# Operations Summary

| Operation           | API                   | Return  |
| ------------------- | --------------------- | ------- |
| Transpose           | `A.transpose`         | Matrix  |
| Minor               | `A.minor(i, j)`       | Scalar  |
| Cofactor            | `A.cofactor(i, j)`    | Scalar  |
| Matrix of minors    | `A.matrixOfMinors`    | Matrix  |
| Matrix of cofactors | `A.matrixOfCofactors` | Matrix  |
| Determinant         | `A.determinant`       | Scalar  |
| Trace               | `A.trace`             | Scalar  |
| Adjoint             | `A.adjoint`           | Matrix  |
| Inverse             | `A.inverse`           | Matrix  |
| Rank                | `A.rank()`            | Integer |
| Solve               | `A.solve(B)`          | Matrix  |

---

# Summary

PyMat's matrix operations provide the core linear-algebra functionality required for manipulating and analyzing matrices.

The API progresses naturally from basic operations:

```text id="n2v7c4"
Transpose
```

to determinant-related operations:

```text id="m8q3x9"
Minor
  ↓
Cofactor
  ↓
Matrix of Cofactors
  ↓
Adjoint
  ↓
Inverse
```

and numerical linear algebra:

```text id="q5k1p8"
Rank
  ↓
Solve
```

Together, these operations form the linear-algebra foundation of PyMat 1.0.
