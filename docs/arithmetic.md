# PyMat Arithmetic

Arithmetic and numerical operations available in **PyMat 1.0.0**.

---

## Table of Contents

1. [Overview](#overview)
2. [Matrix Addition](#matrix-addition)
3. [Matrix Subtraction](#matrix-subtraction)
4. [Matrix Multiplication](#matrix-multiplication)
5. [Scalar Multiplication](#scalar-multiplication)
6. [Scalar Division](#scalar-division)
7. [Negation](#negation)
8. [Matrix Power](#matrix-power)
9. [Element-wise Multiplication](#element-wise-multiplication)
10. [Applying Functions](#applying-functions)
11. [Mathematical Functions](#mathematical-functions)
12. [Reductions](#reductions)
13. [Norms](#norms)

---

# Overview

PyMat supports both traditional matrix arithmetic and element-wise numerical operations.

For example:

```python id="g0yqf2"
from matrix import Matrix

A = Matrix([
    [1, 2],
    [3, 4]
])

B = Matrix([
    [5, 6],
    [7, 8]
])
```

The operation:

```python id="o8s7tj"
A * B
```

performs **matrix multiplication**.

It does **not** multiply corresponding elements.

For element-wise multiplication, use:

```python id="6y6r4m"
A.elementwise_multiply(B)
```

---

# Matrix Addition

## `A + B`

Adds corresponding elements of two matrices.

```python id="5m7b4d"
C = A + B
```

For:

```text id="7r4qgf"
A = [1 2]      B = [5 6]
    [3 4]          [7 8]
```

the result is:

```text id="my4y3h"
C = [6  8]
    [10 12]
```

The matrices must have the same order.

For example:

```text id="k8f0jd"
2 × 3 + 2 × 3    valid
2 × 3 + 3 × 2    invalid
```

---

# Matrix Subtraction

## `A - B`

Subtracts corresponding elements.

```python id="9jtxd7"
C = A - B
```

Example:

```text id="4z9z3w"
A = [1 2]      B = [5 6]
    [3 4]          [7 8]
```

Result:

```text id="k2q1wq"
C = [-4 -4]
    [-4 -4]
```

The matrices must have the same order.

---

# Matrix Multiplication

## `A * B`

When both operands are matrices, `*` performs matrix multiplication.

```python id="q14p0q"
C = A * B
```

Matrix multiplication is possible when:

```text id="5n7b8h"
columns(A) = rows(B)
```

If:

```text id="f0jqoa"
A = m × n
B = n × p
```

then:

```text id="f7y3v6"
A × B = m × p
```

### Example

```python id="sp9vck"
A = Matrix([
    [1, 2],
    [3, 4]
])

B = Matrix([
    [5, 6],
    [7, 8]
])

C = A * B
```

Calculation:

```text id="1t7y7a"
C[0,0] = 1×5 + 2×7 = 19
C[0,1] = 1×6 + 2×8 = 22

C[1,0] = 3×5 + 4×7 = 43
C[1,1] = 3×6 + 4×8 = 50
```

Result:

```text id="t4d1qi"
[19 22]
[43 50]
```

---

# Scalar Multiplication

## `A * scalar`

When the right-hand operand is a scalar, every matrix element is multiplied by that scalar.

```python id="wqytw5"
B = A * 2
```

Example:

```text id="3e2uj9"
A = [1 2]
    [3 4]
```

Then:

```text id="j08b3s"
2A = [2 4]
     [6 8]
```

---

# Right Scalar Multiplication

## `scalar * A`

Scalar multiplication also supports the scalar on the left.

```python id="u7g8ts"
B = 2 * A
```

This produces the same result as:

```python id="xw79hh"
B = A * 2
```

---

# Scalar Division

## `A / scalar`

Divides every matrix element by the scalar.

```python id="f0s5z2"
B = A / 2
```

Example:

```text id="qf4k90"
A = [2 4]
    [6 8]
```

Result:

```text id="ydt8ww"
[1 2]
[3 4]
```

Division by zero raises:

```python id="9l4cr9"
ZeroDivisionError
```

---

# Negation

## `-A`

Negates every element.

```python id="7fy1z4"
B = -A
```

Example:

```text id="x8qylh"
A = [ 1 -2]
    [-3  4]
```

Result:

```text id="t5n1zv"
[-1  2]
[ 3 -4]
```

---

# Matrix Power

## `A ** n`

Raises a square matrix to a positive integer power.

```python id="s0m1iy"
B = A ** 2
```

For `n = 2`:

```text id="h3p2d9"
A ** 2 = A × A
```

For `n = 3`:

```text id="c8z2fa"
A ** 3 = A × A × A
```

The operation uses matrix multiplication.

### Example

```python id="2b1k7s"
A = Matrix([
    [1, 1],
    [0, 1]
])

print(A ** 2)
```

Result:

```text id="uwxw8m"
[1 2]
[0 1]
```

---

# Element-wise Multiplication

## `A.elementwise_multiply(B)`

Element-wise multiplication multiplies corresponding elements.

```python id="x5l0a7"
C = A.elementwise_multiply(B)
```

For:

```text id="u3g6aq"
A = [a b]      B = [x y]
    [c d]          [z w]
```

the result is:

```text id="xgq7p8"
[a×x  b×y]
[c×z  d×w]
```

### Example

```python id="c6stc8"
A = Matrix([
    [1, 2],
    [3, 4]
])

B = Matrix([
    [5, 6],
    [7, 8]
])

C = A.elementwise_multiply(B)
```

Result:

```text id="xj3bq6"
[ 5 12]
[21 32]
```

### Matrix multiplication vs element-wise multiplication

| Operation                   | Syntax                      | Requirement           |
| --------------------------- | --------------------------- | --------------------- |
| Matrix multiplication       | `A * B`                     | `A.columns == B.rows` |
| Element-wise multiplication | `A.elementwise_multiply(B)` | Same order            |

This distinction is important when working with matrices.

---

# Applying Functions

## `A.apply(function)`

`apply()` applies a Python callable independently to every element.

```python id="m6g1ks"
B = A.apply(function)
```

Example:

```python id="q8qk7z"
A = Matrix([
    [1, 2],
    [3, 4]
])

B = A.apply(lambda x: x * 2)
```

Result:

```text id="y0qz4k"
[2 4]
[6 8]
```

Another example:

```python id="z6w1f4"
B = A.apply(lambda x: x ** 2)
```

Result:

```text id="z6x2n7"
[1  4]
[9 16]
```

`apply()` is the general mechanism behind many of PyMat's element-wise mathematical functions.

---

# Mathematical Functions

PyMat provides several element-wise mathematical functions.

Each function operates independently on every element and returns a new matrix.

---

## `exp()`

Calculates the exponential of every element.

```python id="7f6q3x"
B = A.exp()
```

For an element `x`:

```text id="5v1t8k"
exp(x) = eˣ
```

---

## `log()`

Calculates the natural logarithm of every element.

```python id="q8h2u0"
B = A.log()
```

For an element `x`:

```text id="q2h8t4"
log(x)
```

The input must satisfy the domain requirements of `math.log`.

---

## `sqrt()`

Calculates the square root of every element.

```python id="b4r7t9"
B = A.sqrt()
```

For an element `x`:

```text id="j4p2f6"
sqrt(x)
```

---

## `abs()`

Calculates the absolute value of every element.

```python id="z5n3w8"
B = A.abs()
```

Example:

```text id="3x7m9c"
[-1  2]
[-3  4]
```

becomes:

```text id="h4q8v2"
[1 2]
[3 4]
```

---

# Trigonometric Functions

## `sin()`

Calculates the sine of every element.

```python id="6d3p1r"
B = A.sin()
```

---

## `cos()`

Calculates the cosine of every element.

```python id="m7t4q2"
B = A.cos()
```

---

## `tan()`

Calculates the tangent of every element.

```python id="a2c9v5"
B = A.tan()
```

These functions use the angle values expected by Python's `math` functions.

---

# Hyperbolic Functions

## `sinh()`

Calculates the hyperbolic sine element-wise.

```python id="f6p3k8"
B = A.sinh()
```

---

## `cosh()`

Calculates the hyperbolic cosine element-wise.

```python id="w4j7n1"
B = A.cosh()
```

---

## `tanh()`

Calculates the hyperbolic tangent element-wise.

```python id="r8c2m6"
B = A.tanh()
```

---

# Reductions

Reduction methods operate over the entire matrix and return a single value.

---

## `sum()`

Returns the sum of all matrix elements.

```python id="j5x8q2"
result = A.sum()
```

For:

```text id="p6m3v9"
[1 2]
[3 4]
```

the result is:

```text id="8r4w2k"
10
```

---

## `mean()`

Returns the arithmetic mean of all elements.

```python id="v7k1p5"
result = A.mean()
```

For:

```text id="z8d3f2"
[1 2]
[3 4]
```

the result is:

```text id="w1m6q9"
2.5
```

---

## `min()`

Returns the smallest element.

```python id="k4p9s1"
result = A.min()
```

---

## `max()`

Returns the largest element.

```python id="n3v7c5"
result = A.max()
```

---

## `prod()`

Returns the product of all elements.

```python id="q5j8m2"
result = A.prod()
```

For:

```text id="t2x6h9"
[1 2]
[3 4]
```

the result is:

```text id="c7w4p1"
24
```

---

# Norms

PyMat provides the Frobenius norm and its squared value.

---

## `norm_squared()`

Returns the sum of the squares of all matrix elements.

```python id="u6n2r8"
result = A.norm_squared()
```

For:

```text id="m4q7v1"
[1 2]
[3 4]
```

the calculation is:

```text id="x8p3d5"
1² + 2² + 3² + 4²
```

giving:

```text id="j2k6w9"
30
```

---

## `norm()`

Returns the Frobenius norm.

```python id="c4v8n2"
result = A.norm()
```

The Frobenius norm is:

```text id="r7m1q5"
√(sum of squared elements)
```

For:

```text id="g3x9p2"
[1 2]
[3 4]
```

the result is:

```text id="h6w4k8"
√30
```

---

# Returning New Matrices

Most arithmetic and element-wise operations do not modify the original matrix.

For example:

```python id="s9v2k6"
A = Matrix([
    [1, 2],
    [3, 4]
])

B = A * 2
```

`A` remains:

```text id="d4f7q1"
[1 2]
[3 4]
```

while `B` contains the result:

```text id="m8x3c5"
[2 4]
[6 8]
```

This makes it possible to chain operations without unintentionally changing the source matrix.

---

# Operation Summary

| Operation                    | Syntax                      | Result |
| ---------------------------- | --------------------------- | ------ |
| Addition                     | `A + B`                     | Matrix |
| Subtraction                  | `A - B`                     | Matrix |
| Matrix multiplication        | `A * B`                     | Matrix |
| Scalar multiplication        | `A * x`                     | Matrix |
| Right scalar multiplication  | `x * A`                     | Matrix |
| Scalar division              | `A / x`                     | Matrix |
| Negation                     | `-A`                        | Matrix |
| Matrix power                 | `A ** n`                    | Matrix |
| Element-wise multiplication  | `A.elementwise_multiply(B)` | Matrix |
| Custom element-wise function | `A.apply(f)`                | Matrix |
| Exponential                  | `A.exp()`                   | Matrix |
| Logarithm                    | `A.log()`                   | Matrix |
| Square root                  | `A.sqrt()`                  | Matrix |
| Absolute value               | `A.abs()`                   | Matrix |
| Sine                         | `A.sin()`                   | Matrix |
| Cosine                       | `A.cos()`                   | Matrix |
| Tangent                      | `A.tan()`                   | Matrix |
| Hyperbolic sine              | `A.sinh()`                  | Matrix |
| Hyperbolic cosine            | `A.cosh()`                  | Matrix |
| Hyperbolic tangent           | `A.tanh()`                  | Matrix |
| Sum                          | `A.sum()`                   | Scalar |
| Mean                         | `A.mean()`                  | Scalar |
| Minimum                      | `A.min()`                   | Scalar |
| Maximum                      | `A.max()`                   | Scalar |
| Product                      | `A.prod()`                  | Scalar |
| Squared norm                 | `A.norm_squared()`          | Scalar |
| Frobenius norm               | `A.norm()`                  | Scalar |

---

# Important Distinction

The two most important multiplication operations are:

```python id="m8c2q7"
A * B
```

and:

```python id="p4v9x1"
A.elementwise_multiply(B)
```

They have different mathematical meanings.

### Matrix multiplication

```text id="j6w3n8"
A * B
```

uses row-by-column multiplication and requires compatible dimensions.

### Element-wise multiplication

```text id="z2r7k5"
A.elementwise_multiply(B)
```

multiplies corresponding elements and requires identical dimensions.

Understanding this distinction is essential when using PyMat for numerical and linear-algebra calculations.
