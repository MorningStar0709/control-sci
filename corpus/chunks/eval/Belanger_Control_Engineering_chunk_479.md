# 8.3 SINGULAR VALUES

The $\ell_2$ norm of a complex vector $\mathbf{w}$ is defined as

$$\| \mathbf {x} \| _ {2} = \left(\sum_ {i} | w _ {i} | ^ {2}\right) ^ {1 / 2} \tag {8.7}= \left(\mathbf {w} ^ {*} \mathbf {w}\right) ^ {1 / 2} \tag {8.8}$$

where the superscript “\*” refers to the conjugate transpose. This norm is the so-called $\ell_{2}$ norm; it is the Euclidean length of the complex vector w.

Next, the norm of an output signal spectrum must be related in some manner to that of the input. To fix ideas, consider w = Sd, the part of the output y that is due to the disturbance. We write

$$\| \mathbf {w} \| ^ {2} = (S \mathbf {d}) ^ {*} (S \mathbf {d})= \mathbf {d} ^ {*} S ^ {*} S \mathbf {d}. \tag {8.9}$$

Suppose $\|\mathbf{d}(j\omega)\|$ is given. Geometrically, we may then think of d as a vector of given length, whose direction is unknown. For given $\|d\|$ , the right-hand side (RHS) of Equation 8.9 will change as the direction of d varies. It is known, however, that $\|w\|$ has maximum and minimum values, given by

$$\max \| \mathbf {w} \| = \sqrt {\lambda_ {\max} (S ^ {*} S)} \| \mathbf {d} \| \tag {8.10}\min \| \mathbf {w} \| = \sqrt {\lambda_ {\min} (S ^ {*} S)} \| \mathbf {d} \|. \tag {8.11}$$

The matrix $S^{*}S$ is Hermitian (i.e., is its own conjugate transpose), and the eigenvalues of such a matrix are real and positive. The quantities $\lambda_{\max}$ and $\lambda_{\min}$ are the largest and smallest eigenvalues of $S^{*}S$ .

The singular values of $S$ are the square roots of the eigenvalues of $S^{*}S$ . It can be shown [1] that any $n \times n$ matrix $S$ can be written as

$$S = U \Sigma V ^ {*} \tag {8.12}$$

where U is an $n \times n$ unitary matrix, V is an $n \times n$ unitary matrix, and $\Sigma$ is an $n \times n$ diagonal matrix whose elements are the singular values of S. The number of nonzero singular values is equal to the rank of S. (Recall that a unitary matrix has the property that $UU^{*} = I$ .) The largest and smallest singular values of $S$ are denoted by $\overline{\sigma}(S)$ and $\underline{\sigma}(S)$ , respectively. Thus,

$$\overline {{{\sigma}}} (S) = \sqrt {\lambda_ {\max} (S ^ {*} S)} \tag {8.13}\underline {{\sigma}} (S) = \sqrt {\lambda_ {\min} (S ^ {*} S)} \tag {8.14}$$

and, from Equations 8.10 and 8.11,

$$\underline {{\sigma}} (S) \| \mathbf {d} \| _ {2} \leq \| \mathbf {w} \| _ {2} \leq \overline {{\sigma}} (S) \| \mathbf {d} \| _ {2}. \tag {8.15}$$

We shall need a few properties of singular values.
