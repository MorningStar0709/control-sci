The Euclidean 2-norm has some very nice properties:

Lemma 2.2 Let $x \in \mathbb { F } ^ { n }$ and $y \in \mathbb { F } ^ { m }$ .

1. Suppose $n \geq m$ . Then $\| x \| = \| y \|$ iff there is a matrix $U \in \mathbb { F } ^ { n \times m }$ such that $x = U y$ and $U ^ { * } U = I$ .   
2. Suppose $n = m$ . Then $| x ^ { * } y | \leq \| x \| \| y \|$ . Moreover, the equality holds $i f f \ x = \alpha y$ for some $\alpha \in \mathbb { F } \ o r \ y = 0$ .   
3. $\| x \| \leq \| y \|$ iff there is a matrix $\Delta \in \mathbb { F } ^ { n \times m }$ with $\| \Delta \| \leq 1$ such that $x = \Delta y$ Furthermore, $\| x \| < \| y \| \ i f f \| \Delta \| < 1$ .   
4. $\| U x \| = \| x \|$ for any appropriately dimensioned unitary matrices U.

Another often used matrix norm is the so called Frobenius norm. It is defined as

$$\| A \| _ {F} := \sqrt {\operatorname{trace} (A ^ {*} A)} = \sqrt {\sum_ {i = 1} ^ {m} \sum_ {j = 1} ^ {n} | a _ {i j} | ^ {2}}.$$

However, the Frobenius norm is not an induced norm.

The following properties of matrix norms are easy to show:

Lemma 2.3 Let A and B be any matrices with appropriate dimensions. Then

1. $\rho ( A ) \leq \| A \|$ (this is also true for the F -norm and any induced matrix norm).   
2. $\| A B \| \leq \| A \| \| B \|$ . In particular, this gives $\left\| A ^ { - 1 } \right\| \ge \left\| A \right\| ^ { - 1 }$ if A is invertible. (This is also true for any induced matrix norm.)   
3. $\| U A V \| = \| A \|$ , and $\| U A V \| _ { F } = \| A \| _ { F }$ , for any appropriately dimensioned unitary matrices U and V .   
4. $\left\| A B \right\| _ { F } \leq \left\| A \right\| \left\| B \right\| _ { F }$ and $\| A B \| _ { F } \leq \| B \| \| A \| _ { F }$ .

Note that although premultiplication or postmultiplication of a unitary matrix on a matrix does not change its induced 2-norm and F -norm, it does change its eigenvalues. For example, let

$$
A = \left[ \begin{array}{c c} 1 & 0 \\ 1 & 0 \end{array} \right].
$$

Then $\lambda _ { 1 } ( A ) = 1 , \lambda _ { 2 } ( A ) = 0$ . Now let

$$
U = \left[ \begin{array}{c c} {\frac {1}{\sqrt {2}}} & {\frac {1}{\sqrt {2}}} \\ {- \frac {1}{\sqrt {2}}} & {\frac {1}{\sqrt {2}}} \end{array} \right];
$$

then U is a unitary matrix and

$$
U A = \left[ \begin{array}{c c} {\sqrt {2}} & 0 \\ {0} & 0 \end{array} \right]
$$

with $\lambda _ { 1 } ( U A ) = \sqrt { 2 } , \lambda _ { 2 } ( U A ) = 0$ . This property is useful in some matrix perturbation problems, particularly in the computation of bounds for structured singular values, which will be studied in Chapter 9.

Related MATLAB Commands: norm, normest
