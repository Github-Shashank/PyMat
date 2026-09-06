# PyMat Constructors

Matrix construction methods available in **PyMat 1.0.0**.

---

## Table of Contents

1. [Overview](#overview)
2. [Matrix Constructor](#matrix-constructor)
3. [Ones Matrix](#ones-matrix)
4. [Zero Matrix](#zero-matrix)
5. [Identity Matrix](#identity-matrix)
6. [Constant Matrix](#constant-matrix)
7. [Diagonal Matrix](#diagonal-matrix)
8. [Random Matrix](#random-matrix)
9. [Uniform Random Matrix](#uniform-random-matrix)
10. [Random Seed](#random-seed)
11. [Element-wise Constructor](#element-wise-constructor)
12. [String Constructor](#string-constructor)
13. [Constructor Summary](#constructor-summary)

---

# Overview

PyMat provides multiple ways to create matrices.

The most direct approach is to pass a two-dimensional list to `Matrix`.

```python id="y0gq4n"
from matrix import Matrix

A = Matrix([
    [1, 2],
    [3, 4]
])
```

For commonly used matrices such as zero, identity, diagonal, and random matrices, PyMat provides dedicated class methods.

---

# Matrix Constructor

## `Matrix()`

Creates a matrix from a two-dimensional collection of values.

```python id="q8n3w6"
Matrix(values)
```

Example:

```python id="m5r1c7"
A = Matrix([
    [1, 2, 3],
    [4, 5, 6]
])
```

This creates:

```text id="j6t2p9"
[1 2 3]
[4 5 6]
```

with order:

```text id="c4v8x2"
(2, 3)
```

---

## Matrix Values

Matrix elements can be integers, floating-point values, complex numbers, or other compatible Python numeric values.

Example:

```python id="w2k7p4"
A = Matrix([
    [1, 2.5],
    [3.14, 4]
])
```

---

# Ones Matrix

## `Matrix.one()`

Creates a matrix in which every element is `1`.

```python id="a7m3q8"
Matrix.one(rows, cols)
```

### Example

```python id="p4x9v1"
A = Matrix.one(2, 3)
```

Result:

```text id="f8n2k5"
[1 1 1]
[1 1 1]
```

### Parameters

| Parameter | Description       |
| --------- | ----------------- |
| `rows`    | Number of rows    |
| `cols`    | Number of columns |

---

# Zero Matrix

## `Matrix.zero()`

Creates a matrix in which every element is `0`.

```python id="n5c8r2"
Matrix.zero(rows, cols)
```

### Example

```python id="v7j1m4"
A = Matrix.zero(2, 3)
```

Result:

```text id="b3q9x6"
[0 0 0]
[0 0 0]
```

### Parameters

| Parameter | Description       |
| --------- | ----------------- |
| `rows`    | Number of rows    |
| `cols`    | Number of columns |

---

# Identity Matrix

## `Matrix.identity()`

Creates an identity matrix.

```python id="x4p8k2"
Matrix.identity(n)
```

### Example

```python id="m7v3q9"
I = Matrix.identity(3)
```

Result:

```text id="r2c6w8"
[1 0 0]
[0 1 0]
[0 0 1]
```

The matrix is always square.

For an identity matrix:

```text id="j5n8t3"
I[i, i] = 1
```

and every non-diagonal element is `0`.

---

# Constant Matrix

## `Matrix.constant()`

Creates a matrix in which every element has the specified value.

```python id="k3w7p1"
Matrix.constant(rows, cols, value)
```

### Example

```python id="z8m4q6"
A = Matrix.constant(2, 3, 5)
```

Result:

```text id="t1v9c4"
[5 5 5]
[5 5 5]
```

### Parameters

| Parameter | Description                     |
| --------- | ------------------------------- |
| `rows`    | Number of rows                  |
| `cols`    | Number of columns               |
| `value`   | Value assigned to every element |

---

# Diagonal Matrix

## `Matrix.diagonal()`

Creates a square matrix with the supplied values on its main diagonal.

```python id="f6q2m8"
Matrix.diagonal(values)
```

### Example

```python id="p9x4v7"
A = Matrix.diagonal([1, 2, 3])
```

Result:

```text id="c5n8k1"
[1 0 0]
[0 2 0]
[0 0 3]
```

Elements outside the main diagonal are zero.

---

# Random Matrix

## `Matrix.random()`

Creates a random matrix using PyMat's existing random matrix constructor.

```python id="u7r3m9"
Matrix.random(...)
```

The original `random()` API is retained in PyMat 1.0 for compatibility with earlier versions.

Use `random_uniform()` when you need explicit control over the generated value range.

---

# Uniform Random Matrix

## `Matrix.random_uniform()`

Creates a matrix whose elements are generated from a uniform distribution.

```python id="q2v8n5"
Matrix.random_uniform(
    rows,
    cols=None,
    low=-1.0,
    high=1.0
)
```

### Parameters

| Parameter | Description       | Default  |
| --------- | ----------------- | -------- |
| `rows`    | Number of rows    | Required |
| `cols`    | Number of columns | `rows`   |
| `low`     | Lower bound       | `-1.0`   |
| `high`    | Upper bound       | `1.0`    |

---

## Square Matrix

If `cols` is omitted, PyMat creates a square matrix.

```python id="h4m7x2"
A = Matrix.random_uniform(3)
```

This creates a:

```text id="s8c1p6"
3 × 3
```

matrix.

---

## Rectangular Matrix

Specify both dimensions for a rectangular matrix:

```python id="n6q3v9"
A = Matrix.random_uniform(2, 4)
```

This creates:

```text id="z1w5k8"
2 × 4
```

---

## Custom Range

A custom interval can be supplied:

```python id="r4p9m2"
A = Matrix.random_uniform(
    3,
    3,
    low=0,
    high=10
)
```

The generated values are uniformly distributed over the requested range.

---

## Invalid Dimensions

Matrix dimensions must be positive.

For example, invalid dimensions such as:

```python id="x8v2c5"
Matrix.random_uniform(0, 3)
```

raise:

```text id="g6n1q9"
ValueError
```

---

## Invalid Range

The lower bound must be smaller than the upper bound.

```python id="m3k7w4"
Matrix.random_uniform(
    2,
    2,
    low=10,
    high=5
)
```

raises:

```text id="p8r2v6"
ValueError
```

---

# Random Seed

## `Matrix.seed()`

Sets the seed for PyMat's random-number generator.

```python id="c7x4n1"
Matrix.seed(value=None)
```

A fixed seed makes random generation reproducible.

### Example

```python id="j9m5q2"
Matrix.seed(42)

A = Matrix.random_uniform(2, 2)
```

Running the same sequence again with the same seed produces the same generated values.

This is particularly useful for:

* Testing
* Debugging
* Reproducible experiments
* Examples and demonstrations

---

## Resetting the Seed

The seed can be reset by calling:

```python id="v2k8p5"
Matrix.seed()
```

with no explicit value.

---

# Element-wise Constructor

## `Matrix.elementwise()`

Creates a matrix using an element-wise generation mechanism.

```python id="q6n3x9"
Matrix.elementwise(...)
```

This constructor is useful when matrix elements need to be generated according to an element-level operation rather than supplied as a static two-dimensional list.

---

# String Constructor

## `Matrix.from_string()`

Creates a matrix from a string representation.

```python id="w4m8c2"
Matrix.from_string(...)
```

This is useful when matrix data is provided as text.

For example, matrix data obtained from:

* User input
* Configuration files
* Text-based data
* Serialized matrix representations

can be converted into a `Matrix`.

---

# Constructor Selection Guide

Use the constructor that best matches the data you have.

| Requirement                   | Constructor               |
| ----------------------------- | ------------------------- |
| Existing matrix values        | `Matrix(...)`             |
| All ones                      | `Matrix.one()`            |
| All zeros                     | `Matrix.zero()`           |
| Identity matrix               | `Matrix.identity()`       |
| Same constant everywhere      | `Matrix.constant()`       |
| Diagonal matrix               | `Matrix.diagonal()`       |
| Existing random behavior      | `Matrix.random()`         |
| Controlled uniform randomness | `Matrix.random_uniform()` |
| Reproducible random values    | `Matrix.seed()`           |
| Element-based generation      | `Matrix.elementwise()`    |
| Matrix represented as text    | `Matrix.from_string()`    |

---

# Examples

## Creating Several Matrix Types

```python id="e7q2m5"
from matrix import Matrix

A = Matrix([
    [1, 2],
    [3, 4]
])

B = Matrix.zero(2, 2)

C = Matrix.one(2, 2)

D = Matrix.identity(2)

E = Matrix.constant(2, 2, 7)

F = Matrix.diagonal([1, 2])

G = Matrix.random_uniform(2, 2)
```

---

## Reproducible Random Matrices

```python id="n8v4c1"
from matrix import Matrix

Matrix.seed(42)

A = Matrix.random_uniform(2, 2)

Matrix.seed(42)

B = Matrix.random_uniform(2, 2)
```

`A` and `B` are generated from the same random sequence.

---

# Constructor Summary

PyMat 1.0 provides the following matrix construction APIs:

```text id="r5k9x3"
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

These constructors provide the foundation for creating matrices used throughout the rest of the PyMat API.
