# PyMat

A modular Python library for creating, manipulating, and performing mathematical operations on matrices.

**Version:** `1.0.0`
**Status:** Stable

---

## Features

PyMat provides a collection of tools for working with matrices:

* Matrix creation and constructors
* Matrix indexing and iteration
* Matrix addition and subtraction
* Matrix multiplication
* Scalar multiplication and division
* Element-wise multiplication
* Matrix powers
* Mathematical functions
* Aggregation and reduction operations
* Matrix norms
* Row and column manipulation
* Matrix reshaping and flattening
* Transpose
* Minors and cofactors
* Determinant
* Adjoint and inverse
* Matrix rank
* Linear-system solving
* Matrix property checks
* Approximate equality
* Random matrix generation
* Deep copying
* Input validation

---

## Installation

Clone the repository:

```bash
git clone https://github.com/Github-Shashank/PyMat.git
cd PyMat
```

Create and activate a virtual environment if desired:

```bash
python -m venv .venv
```

On Windows:

```bash
.venv\Scripts\activate
```

On Linux/macOS:

```bash
source .venv/bin/activate
```

Install PyMat:

```bash
pip install -e .
```

---

## Quick Start

```python
from matrix import Matrix

A = Matrix([
    [1, 2],
    [3, 4]
])

B = Matrix([
    [5, 6],
    [7, 8]
])

print(A)
print(B)
```

### Matrix arithmetic

```python
print(A + B)
print(A - B)
print(A * B)
```

`*` performs matrix multiplication when both operands are matrices.

Scalar multiplication is also supported:

```python
print(A * 2)
print(2 * A)
```

Scalar division:

```python
print(A / 2)
```

Negation:

```python
print(-A)
```

---

## Indexing

Matrix elements are accessed using:

```python
A[row, column]
```

For example:

```python
print(A[0, 1])
```

Assigning an element:

```python
A[0, 1] = 10
```

---

## Matrix Properties

```python
print(A.order)
print(A.shape)
```

Both return:

```text
(rows, columns)
```

Matrix classification properties include:

```python
A.isSqrMatrix
A.isDiagMatrix
A.isRowMatrix
A.isColMatrix
A.isSclrMatrix
A.isIdntMatrix
A.isZeroMatrix
A.isSymtMatrix
A.isSkewSymtMatrix
```

Invertibility-related properties:

```python
A.isInvertible
A.isSingularMatrix
A.isNonSingularMatrix
```

---

## Constructors

PyMat provides several class methods for creating matrices.

### Ones

```python
Matrix.one(3, 3)
```

Creates a matrix filled with `1`.

### Zeros

```python
Matrix.zero(3, 3)
```

Creates a matrix filled with `0`.

### Identity

```python
Matrix.identity(3)
```

Creates a `3 × 3` identity matrix.

### Constant

```python
Matrix.constant(2, 3, 5)
```

Creates a `2 × 3` matrix filled with `5`.

### Diagonal

```python
Matrix.diagonal([1, 2, 3])
```

Creates a diagonal matrix.

### Random

```python
Matrix.random(3, 3)
```

Creates a random matrix using PyMat's existing random constructor.

### Uniform random

```python
Matrix.random_uniform(3, 3, low=-1, high=1)
```

Creates a matrix whose elements are uniformly distributed between `low` and `high`.

### Seed

```python
Matrix.seed(42)
```

Sets the random generator seed used by PyMat's uniform random constructor.

---

## Matrix Transformation

### Transpose

```python
A.transpose
```

Returns the transpose of `A`.

### Flatten

```python
A.flatten()
```

Converts the matrix into a single-row matrix.

For example:

```text
[1 2]
[3 4]
```

becomes:

```text
[1 2 3 4]
```

### Reshape

```python
A.reshape(4, 1)
```

Changes the matrix dimensions while preserving the element count.

The number of elements must remain unchanged.

---

## Row and Column Manipulation

Rows and columns can be inserted, deleted, retrieved, or swapped.

```python
A.insertRow(...)
A.insertCol(...)
A.delRow(...)
A.delCol(...)
A.getRow(...)
A.getCol(...)
```

Rows:

```python
A.swapRows(0, 1)
```

Columns:

```python
A.swapCols(0, 1)
```

By default, swapping returns a new matrix.

In-place swapping is also supported:

```python
A.swapRows(0, 1, inplace=True)
A.swapCols(0, 1, inplace=True)
```

---

## Element-wise Operations

Matrix multiplication and element-wise multiplication are different operations.

Element-wise multiplication:

```python
A.elementwise_multiply(B)
```

Each corresponding pair of elements is multiplied:

```text
[a b]    [x y]       [a*x b*y]
[c d] ×  [z w]   =   [c*z d*w]
```

The matrices must have the same dimensions.

---

## Applying Functions

PyMat provides a general `apply()` operation:

```python
A.apply(function)
```

Example:

```python
A.apply(lambda x: x * x)
```

This applies the function independently to every matrix element.

---

## Mathematical Functions

PyMat provides element-wise mathematical functions:

```python
A.exp()
A.log()
A.sqrt()

A.abs()

A.sin()
A.cos()
A.tan()

A.sinh()
A.cosh()
A.tanh()
```

For example:

```python
A.sqrt()
```

returns a matrix containing the square root of every element.

---

## Reductions

PyMat provides operations that reduce the entire matrix to a single value.

### Sum

```python
A.sum()
```

### Mean

```python
A.mean()
```

### Minimum

```python
A.min()
```

### Maximum

```python
A.max()
```

### Product

```python
A.prod()
```

---

## Norm

The Frobenius norm of a matrix can be calculated using:

```python
A.norm()
```

The squared norm is available through:

```python
A.norm_squared()
```

For a matrix

```text
[a b]
[c d]
```

the squared Frobenius norm is:

```text
a² + b² + c² + d²
```

and the norm is:

```text
√(a² + b² + c² + d²)
```

---

## Matrix Operations

### Minor

```python
A.minor(row, column)
```

Returns the minor associated with an element.

### Cofactor

```python
A.cofactor(row, column)
```

Returns the corresponding cofactor.

### Matrix of Minors

```python
A.matrixOfMinors
```

### Matrix of Cofactors

```python
A.matrixOfCofactors
```

### Determinant

```python
A.determinant
```

### Trace

```python
A.trace
```

### Adjoint

```python
A.adjoint
```

### Inverse

```python
A.inverse
```

The inverse exists only for an invertible square matrix.

---

## Rank

The rank of a matrix can be calculated using:

```python
A.rank()
```

Example:

```python
A = Matrix([
    [1, 2],
    [2, 4]
])

print(A.rank())
```

The rank is:

```text
1
```

---

## Solving Linear Systems

PyMat can solve a system of linear equations represented as:

```text
AX = B
```

using:

```python
A.solve(B)
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

print(X)
```

The coefficient matrix must be square and the right-hand side must have compatible dimensions.

---

## Approximate Equality

Exact equality:

```python
A == B
```

checks whether corresponding elements are exactly equal.

For floating-point calculations, approximate equality is available:

```python
A.isApproxEqual(B)
```

A custom tolerance can be supplied:

```python
A.isApproxEqual(B, tolerance=1e-6)
```

This is useful when numerical calculations produce small floating-point differences.

---

## Copying

To create an independent copy of a matrix:

```python
B = A.copy()
```

The copy is independent of the original matrix.

Changing `B` does not modify `A`.

---

## Iteration

A matrix can be iterated over:

```python
for row in A:
    print(row)
```

The matrix's traversal functionality is also available through:

```python
A.traverse
```

---

## Matrix Power

Positive integer powers are supported:

```python
A ** 2
```

which performs:

```text
A × A
```

For example:

```python
A ** 3
```

calculates:

```text
A × A × A
```

---

## API Overview

### Operators

| Operator     | Operation             |
| ------------ | --------------------- |
| `A + B`      | Matrix addition       |
| `A - B`      | Matrix subtraction    |
| `A * B`      | Matrix multiplication |
| `A * scalar` | Scalar multiplication |
| `scalar * A` | Scalar multiplication |
| `A / scalar` | Scalar division       |
| `-A`         | Matrix negation       |
| `A ** n`     | Matrix power          |
| `A == B`     | Exact equality        |

### Core Properties

| Property      | Purpose            |
| ------------- | ------------------ |
| `order`       | Matrix dimensions  |
| `shape`       | Alias for `order`  |
| `transpose`   | Transposed matrix  |
| `traverse`    | Matrix traversal   |
| `determinant` | Matrix determinant |
| `trace`       | Matrix trace       |
| `adjoint`     | Matrix adjoint     |
| `inverse`     | Matrix inverse     |

### Numerical Methods

| Method                   | Purpose                           |
| ------------------------ | --------------------------------- |
| `elementwise_multiply()` | Element-wise multiplication       |
| `apply()`                | Apply a function to every element |
| `exp()`                  | Element-wise exponential          |
| `log()`                  | Element-wise logarithm            |
| `sqrt()`                 | Element-wise square root          |
| `abs()`                  | Element-wise absolute value       |
| `sin()`                  | Element-wise sine                 |
| `cos()`                  | Element-wise cosine               |
| `tan()`                  | Element-wise tangent              |
| `sinh()`                 | Element-wise hyperbolic sine      |
| `cosh()`                 | Element-wise hyperbolic cosine    |
| `tanh()`                 | Element-wise hyperbolic tangent   |
| `sum()`                  | Sum of all elements               |
| `mean()`                 | Mean of all elements              |
| `min()`                  | Minimum element                   |
| `max()`                  | Maximum element                   |
| `prod()`                 | Product of all elements           |
| `norm_squared()`         | Squared Frobenius norm            |
| `norm()`                 | Frobenius norm                    |
| `rank()`                 | Matrix rank                       |
| `solve()`                | Solve a linear system             |

---

## Validation

PyMat provides validation helpers:

```python
A.isValidIndex(...)
A.isEqualOrder(B)
A.isMultiplicable(B)
A.isApproxEqual(B)
```

These can be used to validate matrix dimensions, indices, and numerical equality.

---

## Testing

PyMat includes a test suite covering the library's functionality.

Run the tests with:

```bash
python -m unittest discover
```

The current v1 implementation has:

```text
100 tests
100 passed
0 failed
```

---

## Project Structure

```text
PyMat/
├── matrix/
│   ├── __init__.py
│   ├── arithmetic.py
│   ├── bool.py
│   ├── constructors.py
│   ├── exceptions.py
│   ├── manipulation.py
│   ├── matrix.py
│   ├── operations.py
│   └── validators.py
│
├── tests/
│   └── test_matrix.py
│
├── docs/
│   ├── api_reference.md
│   ├── arithmetic.md
│   ├── constructors.md
│   ├── manipulation.md
│   ├── operations.md
│   └── properties.md
│
├── README.md
├── LICENSE
├── .gitignore
└── pyproject.toml
```

---

## Design

PyMat is organized into separate modules so that different areas of matrix functionality remain independent.

```text
matrix.py
   │
   ├── arithmetic.py
   ├── constructors.py
   ├── manipulation.py
   ├── operations.py
   ├── validators.py
   └── bool.py
```

The `Matrix` class provides the public interface while the individual modules contain the underlying functionality.

This structure makes PyMat easier to maintain, test, and extend.

---

## Documentation

Detailed documentation is available in the `docs/` directory:

* [API Reference](docs/api_reference.md)
* [Arithmetic](docs/arithmetic.md)
* [Constructors](docs/constructors.md)
* [Manipulation](docs/manipulation.md)
* [Operations](docs/operations.md)
* [Properties](docs/properties.md)

---

## Version

Current release:

```text
PyMat 1.0.0
```

PyMat 1.0 represents the first stable version of the library's public API.

---

## License

PyMat is distributed under the license included in the `LICENSE` file.
