# 3.3.3 Dynamic Modes

We may write

$$(s I - A) ^ {- 1} = \frac {A d j (s I - A)}{\det (s I - A)}. \tag {3.12}$$

The determinant is an $n$ th-order polynomial. As for the adjoint, the cofactors of $sI - A$ are also polynomials, of degree $n - 1$ at most. Therefore, any particular element of $(sI - A)^{-1}$ can be expanded by partial fractions into an expression of the form

$$\cdot \frac {A _ {1 1}}{s - s _ {1}} + \frac {A _ {1 2}}{(s - s _ {1}) ^ {2}} + \dots + \frac {A _ {2 1}}{s - s _ {2}} + \frac {A _ {2 2}}{(s - s _ {2}) ^ {2}} + \dots$$

where $s_1, s_2, \ldots$ are the roots of the determinant, some of which may be multiple roots. Upon inverse transforming, there results an expression of the form

$$A _ {1 1} e ^ {s _ {1} t} + A _ {1 2} t e ^ {s _ {1} t} + \dots + A _ {2 1} e ^ {s _ {2} t} + A _ {2 2} t e ^ {s _ {2} t} + \dots .$$

Clearly, the elements of $e^{At}$ are sums of exponentials or time-weighted exponentials, whose exponents are the roots of the determinant. These roots satisfy the equation

$$\det (s I - A) = 0.$$

But that is precisely the equation satisfied by the eigenvalues of the matrix $A$ , so the roots $s_1, s_2, \ldots$ are also the eigenvalues of $A$ . In other words, the elements of the matrix exponential are composed of exponentials whose exponents are the eigenvalues of $A$ , with time-weighted exponentials corresponding to repeated eigenvalues. In linear systems theory, we speak of these eigenvalues as the modes.

The eigenvectors of $A$ also have special significance. Recall that an eigenvector $\mathbf{v}_i$ , corresponding to an eigenvalue $s_i$ , satisfies

$$A \mathbf {v} _ {i} = s _ {i} \mathbf {v} _ {i}.$$

We now show that $\mathbf{v}_i$ is also an eigenvector of $e^{At}$ . Using Equation 3.8,

$$e ^ {A t} \mathbf {v} _ {i} = \mathbf {v} _ {i} + A \mathbf {v} _ {i} t + \frac {1}{2 !} A ^ {2} \mathbf {v} _ {i} t ^ {2} + \dots + \frac {1}{k !} A ^ {k} \mathbf {v} _ {i} t ^ {k} + \dots .$$

But

$$
\begin{array}{l} A ^ {2} \mathbf {v} _ {i} = A A \mathbf {v} _ {i} = A s _ {i} \mathbf {v} _ {i} = s _ {i} A \mathbf {v} _ {i} = s _ {i} ^ {2} \mathbf {v} _ {i} \\ A ^ {3} \mathbf {v} _ {i} = A A ^ {2} \mathbf {v} _ {i} = A s _ {i} ^ {2} \mathbf {v} _ {i} = s _ {i} ^ {3} \mathbf {v} _ {i} \\ A ^ {k} \mathbf {v} _ {i} = s _ {i} ^ {k} \mathbf {v} _ {i}. \\ \end{array}
$$

•
•
•

Therefore,
