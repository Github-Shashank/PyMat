import copy
from .validators import (
    check_matrix,
    is_equal_order,
    is_valid_index,
    is_multiplicable,
    is_approx_equal,
)
from .operations import (
    transpose,
    minor,
    cofactor,
    determinant,
    matrix_of_minors,
    matrix_of_cofactors,
    trace,
    adjoint,
    inverse,
    rank,
    solve,    
)
from .constructors import (
    one,
    zero,
    identity,   
    constant,
    diagonal,
    random_matrix,
    elementwise,
    from_string,
    random_uniform,
    seed
)
from .bool import (
    is_square,
    is_diagonal,
    is_column,
    is_row,
    is_scalar,
    is_identity,
    is_zero,
    is_symmetric,
    is_skew_symmetric,
    is_invertible,
    is_singular,
    is_non_singular
)
from .manipulation import (
    insert_row,
    insert_col,
    delete_row,
    delete_col,
    get_row,
    get_col,
    flatten,
    reshape,
    swap_cols,
    swap_rows,
)
from .arithmetic import (
    add,
    subtract,
    multiply,
    divide,
    negate,
    power,
    elementwise_multiply,
    apply,
    exp,
    log,
    sqrt,
    abs,
    sin,
    cos,
    tan,
    sinh,
    cosh,
    tanh,
    sum,
    mean,
    min,
    max,
    prod, 
    norm_squared,
    norm
)

class Matrix:
    def __init__(self,m):
        val = check_matrix(m)
        if val == True:
            pass
        else:
            raise ValueError(f"Invalid Format! len({val}) is not matched with first one.")
        self.m = m

    def __repr__(self):
        return '{}'.format(self.m)
    
    def __str__(self):
        return "{}".format(self.m)
    
    def __eq__(self, other):
        if not self.isEqualOrder(other):
            return False

        r,l = self.order
        for i in range(r):
            for j in range(l):
                if not self[i,j] == other[i,j]:
                    return False
        else:
            return True

    def __add__(self, other):
        return add(self, other)

    def __sub__(self, other):
        return subtract(self, other)

    def __mul__(self, other):
        return multiply(self, other)

    def elementwise_multiply(self, other):
        return elementwise_multiply(self, other)

    def apply(self, function):
        return apply(self, function)

    def exp(self):
        return exp(self)

    def log(self):
        return log(self)

    def sqrt(self):
        return sqrt(self)

    def abs(self):
        return abs(self)

    def sin(self):
        return sin(self)

    def cos(self):
        return cos(self)

    def tan(self):
        return tan(self)

    def sinh(self):
        return sinh(self)

    def cosh(self):
        return cosh(self)

    def tanh(self):
        return tanh(self)

    def sum(self):
        return sum(self)

    def mean(self):
        return mean(self)

    def min(self):
        return min(self)


    def max(self):
        return max(self)


    def prod(self):
        return prod(self)

    def norm_squared(matrix):
        return norm_squared(matrix)

    def norm(self):
        return norm(self)

    def copy(self):
        return type(self)(copy.deepcopy(self.m))
    
    def __truediv__(self, other):
        return divide(self, other)

    def __neg__(self):
        return negate(self)
    
    def __rmul__(self, other):
        return self.__mul__(other)

    def __pow__(self, raisedTo):
        return power(self, raisedTo)

    def __getitem__(self, index):
        if self.isValidIndex(index):
            row, col = index
            return self.m[row][col]

    def __setitem__(self, key, value):
        r,c = key
        self.m[r][c] = value

    def __iter__(self):
        for row in self.m:
            yield row

    @property
    def order(self):
        return (len(self.m),len(self.m[0])) 

    @property
    def shape(self):
        return self.order

    @property
    def transpose(self):
        return transpose(self)

    @property
    def traverse(self):
        l = (x for lists in self.m for x in lists)
        return l

    def insertRow(self, rowMat):
        return insert_row(self, rowMat)

    def insertCol(self, colMat):
        return insert_col(self, colMat)
    
    def delRow(self, rowIndex, inplace=False):
        return delete_row(self, rowIndex, inplace)
    
    def delCol(self, colIndex, inplace=False):
        return delete_col(self, colIndex, inplace)

    def getRow(self, rowIndex):
        return get_row(self, rowIndex)

    def getCol(self, colIndex):
        return get_col(self, colIndex)

    def flatten(self):
        return flatten(self)

    def reshape(self, rows, cols):
        return reshape(self, rows, cols)

    def swapCols(self, col1, col2, inplace=False):
        return swap_cols(self, col1, col2, inplace)

    def swapRows(self, row1, row2, inplace=False):
        return swap_rows(self, row1, row2, inplace)
    
    @property
    def isSqrMatrix(self):
        return is_square(self)

    @property
    def isDiagMatrix(self):
        return is_diagonal(self)

    @property
    def isColMatrix(self):
        return is_column(self)

    @property
    def isRowMatrix(self):
        return is_row(self)

    @property
    def isSclrMatrix(self):
        return is_scalar(self)

    @property
    def isIdntMatrix(self):
        return is_identity(self)

    @property
    def isZeroMatrix(self):
        return is_zero(self)

    @property
    def isSymtMatrix(self):
        return is_symmetric(self)

    @property
    def isSkewSymtMatrix(self):
        return is_skew_symmetric(self)

    @property
    def isInvertible(self):
        return is_invertible(self)

    @property
    def isSingularMatrix(self):
        return is_singular(self)

    @property
    def isNonSingularMatrix(self):
        return is_non_singular(self)

    def isValidIndex(self, index):
        return is_valid_index(self, index)

    def isEqualOrder(self, other):
        return is_equal_order(self, other)

    def isMultiplicable(self, other):
        return is_multiplicable(self, other)

    def isApproxEqual(self, other, tolerance=1e-9):
        return is_approx_equal(self, other, tolerance)
    
    def minor(self,rowIndex, colIndex):
        return minor(self, rowIndex, colIndex)

    def cofactor(self,rowIndex, colIndex):
        return cofactor(self,rowIndex, colIndex)

    @property
    def matrixOfMinors(self):
        return matrix_of_minors(self)

    @property
    def matrixOfCofactors(self):
        return matrix_of_cofactors(self)

    @property
    def determinant(self):
        return determinant(self)

    @property
    def trace(self):
        return trace(self)
    
    @property
    def adjoint(self):
        return adjoint(self)
    
    @property
    def inverse(self):
        return inverse(self)

    def rank(self):
        return rank(self)

    def solve(self, other):
        return solve(self, other)

    @classmethod
    def one(cls, rows, cols=None):
        return one(cls, rows, cols)

    @classmethod
    def zero(cls, rows, cols=None):
        return zero(cls, rows, cols)
    
    @classmethod
    def identity(cls, n):
        return identity(cls, n)
    
    @classmethod
    def constant(cls, rows, cols=None, value=0):
        return constant(cls, rows, cols, value)
    
    @classmethod
    def diagonal(cls, diag_list):
        return diagonal(cls, diag_list)
    
    @classmethod
    def random(cls, rows, cols=None, low=0, high=10):
        return random_matrix(cls, rows, cols, low, high)
    
    @classmethod
    def elementwise(cls, rows, cols=None, func=lambda i, j: 0):
        return elementwise(cls, rows, cols, func)

    @classmethod
    def from_string(cls, my_string, dtype=float,row_sep='\n'):
        return from_string(cls, my_string, dtype,row_sep)

    @classmethod
    def random_uniform(cls, rows, cols=None, low=-1.0, high=1.0):
        return random_uniform(cls, rows, cols, low, high)

    @classmethod
    def random_uniform(cls, rows, cols=None, low=-1.0, high=1.0):
        return random_uniform(cls, rows, cols, low, high)

    @classmethod
    def seed(cls, value=None):
        seed(value)