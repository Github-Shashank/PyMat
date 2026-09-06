# PyMat API Reference

Complete API reference for **PyMat 1.0.0**.

---

## Table of Contents

1. [Import](#import)
2. [Matrix Construction](#matrix-construction)
3. [Class Methods](#class-methods)
4. [Operators](#operators)
5. [Indexing and Iteration](#indexing-and-iteration)
6. [Shape and Matrix Access](#shape-and-matrix-access)
7. [Matrix Manipulation](#matrix-manipulation)
8. [Arithmetic Methods](#arithmetic-methods)
9. [Mathematical Functions](#mathematical-functions)
10. [Reduction Methods](#reduction-methods)
11. [Matrix Operations](#matrix-operations)
12. [Linear Algebra](#linear-algebra)
13. [Validation](#validation)
14. [Matrix Properties](#matrix-properties)
15. [Copying](#copying)

---

# Import

```python
from matrix import Matrix
```

---

# Matrix Construction

A matrix can be created by passing a two-dimensional list to `Matrix`.

```python
A = Matrix([
    [1, 2, 3],
    [4, 5, 6]
])
```

This creates a `2 × 3` matrix.

---

# Class Methods

PyMat provides several class methods for constructing matrices.

## `Matrix.one()`

Creates a matrix containing only `1`.

```python
Matrix.one(rows, cols)
```

Example:

```python
A = Matrix.one(2, 3)
```

Result:

```text
[1 1 1]
[1 1 1]
```

---

## `Matrix.zero()`

Creates a matrix containing only `0`.

```python
Matrix.zero(rows, cols)
```

Example:

```python
A = Matrix.zero(2, 3)
```

Result:

```text
[0 0 0]
[0 0 0]
```

---

## `Matrix.identity()`

Creates an identity matrix.

```python
Matrix.identity(n)
```

Example:

```python
I = Matrix.identity(3)
```

Result:

```text
[1 0 0]
[0 1 0]
[0 0 1]
```

---

## `Matrix.constant()`

Creates a matrix whose elements all have the same value.

```python
Matrix.constant(rows, cols, value)
```

Example:

```python
A = Matrix.constant(2, 3, 7)
```

Result:

```text
[7 7 7]
[7 7 7]
```

---

## `Matrix.diagonal()`

Creates a diagonal matrix from a sequence of values.

```python
Matrix.diagonal(values)
```

Example:

```python
A = Matrix.diagonal([1, 2, 3])
```

Result:

```text
[1 0 0]
[0 2 0]
[0 0 3]
```

---

## `Matrix.random()`

Creates a random matrix using PyMat's random matrix constructor.

```python
Matrix.random(...)
```

The existing `random()` API is retained for backward compatibility.

---

## `Matrix.random_uniform()`

Creates a matrix with values sampled uniformly from a specified interval.

```python
Matrix.random_uniform(
    rows,
    cols=None,
    low=-1.0,
    high=1.0
)
```

If `cols` is omitted, a square matrix is created.

Example:

```python
A = Matrix.random_uniform(3)
```

creates a `3 × 3` matrix.

A range can also be specified:

```python
A = Matrix.random_uniform(
    2,
    3,
    low=0,
    high=10
)
```

---

## `Matrix.seed()`

Sets the random seed used by PyMat's random-uniform generator.

```python
Matrix.seed(value=None)
```

Example:

```python
Matrix.seed(42)

A = Matrix.random_uniform(2, 2)
B = Matrix.random_uniform(2, 2)
```

Using the same seed allows reproducible random values.

---

## `Matrix.elementwise()`

Creates a matrix from element-wise generation.

```python
Matrix.elementwise(...)
```

This constructor is intended for creating matrices according to an element-generation operation.

---

## `Matrix.from_string()`

Creates a matrix from a string representation.

```python
Matrix.from_string(...)
```

This is useful when matrix data is available as text.

---

# Operators

## Addition — `A + B`

Adds two matrices element by element.

```python
C = A + B
```

The matrices must have the same order.

---

## Subtraction — `A - B`

Subtracts two matrices element by element.

```python
C = A - B
```

The matrices must have the same order.

---

## Matrix Multiplication — `A * B`

Performs matrix multiplication.

```python
C = A * B
```

For:

```text
A = m × n
B = n × p
```

the result is:

```text
C = m × p
```

---

## Scalar Multiplication — `A * scalar`

Every element is multiplied by the scalar.

```python
C = A * 5
```

---

## Right Scalar Multiplication — `scalar * A`

Scalar multiplication also works with the scalar on the left.

```python
C = 5 * A
```

---

## Scalar Division — `A / scalar`

Divides every element by the scalar.

```python
C = A / 2
```

Division by zero raises `ZeroDivisionError`.

---

## Negation — `-A`

Negates every element.

```python
C = -A
```

---

## Power — `A ** n`

Raises a square matrix to a positive integer power.

```python
C = A ** 2
```

which is equivalent to:

```text
A × A
```

---

## Equality — `A == B`

Checks exact matrix equality.

```python
A == B
```

This compares corresponding elements directly.

For floating-point comparisons, use [`isApproxEqual()`](#isapproxequal).

---

# Indexing and Iteration

## `A[row, column]`

Accesses an individual matrix element.

```python
value = A[0, 1]
```

---

## Assignment

Elements can be modified using the same indexing syntax.

```python
A[0, 1] = 10
```

---

## `__iter__()`

Matrices can be iterated over.

```python
for row in A:
    print(row)
```

---

# Shape and Matrix Access

## `order`

Returns the dimensions of the matrix.

```python
A.order
```

Example:

```python
A = Matrix([
    [1, 2],
    [3, 4],
    [5, 6]
])

print(A.order)
```

Result:

```text
(3, 2)
```

---

## `shape`

Alias for `order`.

```python
A.shape
```

Result:

```text
(rows, columns)
```

---

## `transpose`

Returns the transpose of the matrix.

```python
B = A.transpose
```

---

## `traverse`

Provides matrix traversal access.

```python
A.traverse
```

---

# Matrix Manipulation

## `insertRow()`

Inserts a row into the matrix.

```python
A.insertRow(...)
```

---

## `insertCol()`

Inserts a column into the matrix.

```python
A.insertCol(...)
```

---

## `delRow()`

Deletes a row.

```python
A.delRow(...)
```

---

## `delCol()`

Deletes a column.

```python
A.delCol(...)
```

---

## `getRow()`

Retrieves a row.

```python
row = A.getRow(...)
```

---

## `getCol()`

Retrieves a column.

```python
column = A.getCol(...)
```

---

## `swapRows()`

Swaps two rows.

```python
B = A.swapRows(row1, row2)
```

By default, the operation returns a new matrix.

For example:

```python
A = Matrix([
    [1, 2],
    [3, 4]
])

B = A.swapRows(0, 1)
```

`A` remains unchanged.

### In-place operation

```python
A.swapRows(0, 1, inplace=True)
```

---

## `swapCols()`

Swaps two columns.

```python
B = A.swapCols(col1, col2)
```

In-place operation:

```python
A.swapCols(0, 1, inplace=True)
```

---

## `flatten()`

Converts a matrix into a single-row matrix.

```python
B = A.flatten()
```

Example:

```text
[1 2]
[3 4]
```

becomes:

```text
[1 2 3 4]
```

---

## `reshape()`

Changes the dimensions of a matrix while preserving the number of elements.

```python
B = A.reshape(rows, cols)
```

For example:

```python
A = Matrix([
    [1, 2],
    [3, 4]
])

B = A.reshape(4, 1)
```

Result:

```text
[1]
[2]
[3]
[4]
```

The new dimensions must contain the same number of elements as the original matrix.

---

# Arithmetic Methods

## `elementwise_multiply()`

Performs element-wise multiplication.

```python
C = A.elementwise_multiply(B)
```

Both matrices must have the same order.

---

## `apply()`

Applies a function to every element.

```python
B = A.apply(function)
```

Example:

```python
B = A.apply(lambda x: x * 2)
```

---

# Mathematical Functions

The following methods apply their mathematical function independently to every element.

## `exp()`

```python
B = A.exp()
```

Calculates:

```text
eˣ
```

for every element `x`.

---

## `log()`

```python
B = A.log()
```

Calculates the natural logarithm of every element.

---

## `sqrt()`

```python
B = A.sqrt()
```

Calculates the square root of every element.

---

## `abs()`

```python
B = A.abs()
```

Calculates the absolute value of every element.

---

## `sin()`

```python
B = A.sin()
```

Calculates the sine of every element.

---

## `cos()`

```python
B = A.cos()
```

Calculates the cosine of every element.

---

## `tan()`

```python
B = A.tan()
```

Calculates the tangent of every element.

---

## `sinh()`

```python
B = A.sinh()
```

Calculates the hyperbolic sine.

---

## `cosh()`

```python
B = A.cosh()
```

Calculates the hyperbolic cosine.

---

## `tanh()`

```python
B = A.tanh()
```

Calculates the hyperbolic tangent.

---

# Reduction Methods

These methods reduce all matrix elements to a single value.

## `sum()`

Returns the sum of all elements.

```python
total = A.sum()
```

---

## `mean()`

Returns the arithmetic mean of all elements.

```python
value = A.mean()
```

---

## `min()`

Returns the smallest element.

```python
value = A.min()
```

---

## `max()`

Returns the largest element.

```python
value = A.max()
```

---

## `prod()`

Returns the product of all elements.

```python
value = A.prod()
```

---

## `norm_squared()`

Returns the squared Frobenius norm.

```python
value = A.norm_squared()
```

For:

```text
[a b]
[c d]
```

the result is:

```text
a² + b² + c² + d²
```

---

## `norm()`

Returns the Frobenius norm.

```python
value = A.norm()
```

It is calculated as:

```text
√(sum of squared elements)
```

---

# Matrix Operations

## `minor()`

Returns the minor associated with a matrix element.

```python
value = A.minor(row, column)
```

---

## `cofactor()`

Returns the cofactor associated with a matrix element.

```python
value = A.cofactor(row, column)
```

---

## `matrixOfMinors`

Returns the matrix containing the minors of the corresponding elements.

```python
M = A.matrixOfMinors
```

---

## `matrixOfCofactors`

Returns the matrix containing the cofactors.

```python
C = A.matrixOfCofactors
```

---

## `determinant`

Returns the determinant of a square matrix.

```python
value = A.determinant
```

---

## `trace`

Returns the sum of the main diagonal.

```python
value = A.trace
```

The trace is defined for square matrices.

---

## `adjoint`

Returns the adjoint of the matrix.

```python
B = A.adjoint
```

---

## `inverse`

Returns the inverse of an invertible matrix.

```python
B = A.inverse
```

A matrix must be square and non-singular to have an inverse.

---

# Linear Algebra

## `rank()`

Returns the rank of the matrix.

```python
value = A.rank()
```

Example:

```python
A = Matrix([
    [1, 2],
    [2, 4]
])

print(A.rank())
```

Result:

```text
1
```

The implementation uses numerical elimination with a tolerance for determining pivots.

---

## `solve()`

Solves a square linear system:

```text
AX = B
```

using:

```python
X = A.solve(B)
```

Example:

```python
A = Matrix([
    [2, 1],
    [1, 3]
])

B = Matrix([
    [5],
    [6]
])

X = A.solve(B)
```

The coefficient matrix must be square.

The right-hand side must have a compatible number of rows.

Multiple right-hand sides are supported:

```python
B = Matrix([
    [5, 1],
    [6, 2]
])

X = A.solve(B)
```

A singular coefficient matrix raises `ValueError`.

---

# Validation

## `isValidIndex()`

Checks whether a matrix index is valid.

```python
A.isValidIndex(...)
```

---

## `isEqualOrder()`

Checks whether two matrices have the same dimensions.

```python
A.isEqualOrder(B)
```

Returns:

```text
True
```

when the orders match.

---

## `isMultiplicable()`

Checks whether two matrices can be multiplied.

```python
A.isMultiplicable(B)
```

For:

```text
A = m × n
B = n × p
```

the matrices are multiplicable.

---

## `isApproxEqual()`

Checks whether two matrices are equal within a numerical tolerance.

```python
A.isApproxEqual(B)
```

Default tolerance:

```text
1e-9
```

A custom tolerance can be provided:

```python
A.isApproxEqual(B, tolerance=1e-6)
```

A negative tolerance is invalid.

Unlike `==`, this method is intended for floating-point results where small numerical differences are expected.

---

# Matrix Properties

## `isSqrMatrix`

Checks whether the matrix is square.

```python
A.isSqrMatrix
```

---

## `isDiagMatrix`

Checks whether the matrix is diagonal.

```python
A.isDiagMatrix
```

---

## `isRowMatrix`

Checks whether the matrix has one row.

```python
A.isRowMatrix
```

---

## `isColMatrix`

Checks whether the matrix has one column.

```python
A.isColMatrix
```

---

## `isSclrMatrix`

Checks whether the matrix is a scalar matrix.

```python
A.isSclrMatrix
```

---

## `isIdntMatrix`

Checks whether the matrix is an identity matrix.

```python
A.isIdntMatrix
```

---

## `isZeroMatrix`

Checks whether every element is zero.

```python
A.isZeroMatrix
```

---

## `isSymtMatrix`

Checks whether the matrix is symmetric.

```python
A.isSymtMatrix
```

---

## `isSkewSymtMatrix`

Checks whether the matrix is skew-symmetric.

```python
A.isSkewSymtMatrix
```

---

## `isInvertible`

Checks whether the matrix is invertible.

```python
A.isInvertible
```

---

## `isSingularMatrix`

Checks whether the matrix is singular.

```python
A.isSingularMatrix
```

---

## `isNonSingularMatrix`

Checks whether the matrix is non-singular.

```python
A.isNonSingularMatrix
```

---

# Copying

## `copy()`

Creates an independent copy of a matrix.

```python
B = A.copy()
```

Example:

```python
A = Matrix([
    [1, 2],
    [3, 4]
])

B = A.copy()

B[0, 0] = 100
```

`A` remains unchanged.

The copy uses independent matrix data rather than sharing the original matrix's internal storage.

---

# Complete Public API

The PyMat 1.0 `Matrix` class exposes the following public functionality.

## Construction

```text
Matrix(...)
Matrix.one(...)
Matrix.zero(...)
Matrix.identity(...)
Matrix.constant(...)
Matrix.diagonal(...)
Matrix.random(...)
Matrix.random_uniform(...)
Matrix.seed(...)
Matrix.elementwise(...)
Matrix.from_string(...)
```

## Operators

```text
+
-
*
/
-
**
==
```

## Access

```text
A[row, column]
A[row, column] = value
iter(A)
```

## Shape and access properties

```text
order
shape
transpose
traverse
```

## Manipulation

```text
insertRow()
insertCol()
delRow()
delCol()
getRow()
getCol()
swapRows()
swapCols()
flatten()
reshape()
copy()
```

## Arithmetic and numerical methods

```text
elementwise_multiply()
apply()

exp()
log()
sqrt()
abs()

sin()
cos()
tan()

sinh()
cosh()
tanh()

sum()
mean()
min()
max()
prod()

norm_squared()
norm()
```

## Matrix operations

```text
minor()
cofactor()

matrixOfMinors
matrixOfCofactors

determinant
trace
adjoint
inverse
```

## Linear algebra

```text
rank()
solve()
```

## Validation

```text
isValidIndex()
isEqualOrder()
isMultiplicable()
isApproxEqual()
```

## Properties

```text
isSqrMatrix
isDiagMatrix
isRowMatrix
isColMatrix
isSclrMatrix
isIdntMatrix
isZeroMatrix
isSymtMatrix
isSkewSymtMatrix

isInvertible
isSingularMatrix
isNonSingularMatrix
```

---

# PyMat 1.0 API Summary

PyMat 1.0 provides a complete base API for:

```text
Matrix Creation
       ↓
Matrix Manipulation
       ↓
Arithmetic
       ↓
Element-wise Mathematics
       ↓
Reductions and Norms
       ↓
Matrix Operations
       ↓
Linear Algebra
       ↓
Validation and Properties
```

This reference describes the public API of the PyMat 1.0 release.
