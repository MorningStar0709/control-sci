# B.1 Matrix Functions

In connection with sampled-data systems functions like $\exp A$ and $\ln A$ , where $A$ is a matrix, are of interest. The matrix exponential and matrix logarithm are both matrix functions. This section gives some properties of matrix functions and discusses some ways to compute them.

A useful property of a square matrix is given by Theorem B.1.

THEOREM B.1 THE CAYLEY-HAMILTON THEOREM Let

$$a (\lambda) = \lambda^ {n} + a _ {1} \lambda^ {n - 1} + \dots + a _ {n} = 0$$

be the characteristic equation of the square matrix A. Then A satisfies the following equation

$$a (A) = A ^ {n} + a _ {1} A ^ {n - 1} + \dots + a _ {n} I = 0$$

That is, the matrix satisfies its own characteristic equation.

Let $A$ be an $n \times n$ square matrix and $f(\lambda)$ a scalar function of a scalar argument $\lambda$ . We now want to extend the function $f(\lambda)$ to a function with a matrix argument, that is, $f(A)$ . If $f(\lambda)$ is a polynomial

$$f (\lambda) = \alpha_ {0} \lambda^ {m} + \alpha_ {1} \lambda^ {m - 1} + \dots + \alpha_ {m}$$

then the matrix function $f(A)$ is defined as

$$f (A) = \alpha_ {0} A ^ {m} + \alpha_ {1} A ^ {m - 1} + \dots + a _ {m} I$$

The eigenvalues of $f(A)$ can be found using the following theorem.

THEOREM B.2 EIGENVALUES OF A MATRIX FUNCTION If $f(A)$ is a polynomial in A and $e_{i}$ the eigenvectors of A associated with the eigenvalues $\lambda_{i}$ , then

$$f (A) e _ {i} = f (\lambda_ {i}) e _ {i}$$

so $f(\lambda_i)$ is an eigenvalue of $f(A)$ and $e_i$ is the corresponding eigenvector.

Further, if $f(\lambda)$ can be defined by the power series

$$f (\lambda) = \sum_ {i = 0} ^ {\infty} c _ {i} \lambda^ {i}$$

which is assumed to be convergent for $|\lambda| < R$ , then the matrix function

$$f (A) = \sum_ {i = 0} ^ {\infty} c _ {i} A ^ {i}$$

is convergent if all the eigenvalues of $A$ , $\lambda_i$ satisfy $|\lambda_i| < R$ .

By using the Cayley-Hamilton theorem, it can be shown that for every function $f$ there is a polynomial $p$ of degree less than $n$ such that

$$f (A) = p (A) = \alpha_ {0} A ^ {n - 1} + \alpha_ {1} A ^ {n - 2} + \dots + \alpha_ {n - 1} I \tag {B.1}$$

From Theorem B.2 we get

$$f (\lambda_ {i}) = p (\lambda_ {i}) \quad i = 1, \dots , n \tag {B.2}$$

If the eigenvalues are distinct, then these conditions are sufficient to determine $\alpha_{i}, i = 0, \ldots, n - 1$ . If there is a multiple eigenvalue with multiplicity m, then the additional conditions

$$f ^ {(1)} (\lambda_ {i}) = p ^ {(1)} (\lambda_ {i})\vdots \tag {B.3}f ^ {(m - 1)} (\lambda_ {i}) = p ^ {(m - 1)} (\lambda_ {i})$$

hold, where $f^{(i)}$ is the $i$ th derivative with respect to $\lambda$ .

By using (B.1) and the conditions in (B.2) and (B.3), it is possible to compute matrix functions. For low-order systems, this is a very convenient method for hand calculations.
