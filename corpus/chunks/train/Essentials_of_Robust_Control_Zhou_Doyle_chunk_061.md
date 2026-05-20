# 2.6 Singular Value Decomposition

A very useful tool in matrix analysis is singular value decomposition (SVD). It will be seen that singular values of a matrix are good measures of the “size” of the matrix and that the corresponding singular vectors are good indications of strong/weak input or output directions.

Theorem 2.4 Let $A \in \mathbb { F } ^ { m \times n }$ . There exist unitary matrices

$$U = \left[ u _ {1}, u _ {2}, \dots , u _ {m} \right] \in \mathbb {F} ^ {m \times m}V = [ v _ {1}, v _ {2}, \dots , v _ {n} ] \in \mathbb {F} ^ {n \times n}$$

such that

$$
A = U \Sigma V ^ {*}, \quad \Sigma = \left[ \begin{array}{c c} \Sigma_ {1} & 0 \\ 0 & 0 \end{array} \right],
$$

where

$$
\Sigma_ {1} = \left[ \begin{array}{c c c c} \sigma_ {1} & 0 & \dots & 0 \\ 0 & \sigma_ {2} & \dots & 0 \\ \vdots & \vdots & \ddots & \vdots \\ 0 & 0 & \dots & \sigma_ {p} \end{array} \right]
$$

and

$$\sigma_ {1} \geq \sigma_ {2} \geq \dots \geq \sigma_ {p} \geq 0, p = \min \{m, n \}.$$

Proof. Let $\sigma = \| A \|$ and without loss of generality assume $m \geq n$ . Then, from the definition of $\| A \|$ , there exists $\mathrm { ~ a ~ } z \in \mathbb { F } ^ { n }$ such that

$$\| A z \| = \sigma \| z \|.$$

By Lemma 2.2, there is a matrix $\tilde { U } \in F ^ { m \times n }$ such that $\tilde { U } ^ { * } \tilde { U } = I$ and

$$A z = \sigma \tilde {U} z.$$

Now let

$$x = \frac {z}{\| z \|} \in \mathbb {F} ^ {n}, \quad y = \frac {\tilde {U} z}{\left\| \tilde {U} z \right\|} \in \mathbb {F} ^ {m}.$$

We have $A x = \sigma y$ . Let

$$
V = \left[ \begin{array}{c c} x & V _ {1} \end{array} \right] \in \mathbb {F} ^ {n \times n}
$$

and

$$
U = \left[ \begin{array}{c c} y & U _ {1} \end{array} \right] \in \mathbb {F} ^ {m \times m}
$$

be unitary.2 Consequently, U ∗AV has the following structure:

$$
A _ {1} := U ^ {*} A V = \left[ \begin{array}{c c} y ^ {*} A x & y ^ {*} A V _ {1} \\ U _ {1} ^ {*} A x & U _ {1} ^ {*} A V _ {1} \end{array} \right] = \left[ \begin{array}{c c} \sigma y ^ {*} y & y ^ {*} A V _ {1} \\ \sigma U _ {1} ^ {*} y & U _ {1} ^ {*} A V _ {1} \end{array} \right] = \left[ \begin{array}{c c} \sigma & w ^ {*} \\ 0 & B \end{array} \right],
$$

where $w : = V _ { 1 } ^ { \ast } A ^ { \ast } y \in \mathbb { F } ^ { n - 1 }$ and $B : = U _ { 1 } ^ { * } A V _ { 1 } \in \mathbb { F } ^ { ( m - 1 ) \times ( n - 1 ) }$ .

Since

$$
\left\| A _ {1} ^ {*} \left[ \begin{array}{c} 1 \\ 0 \\ \vdots \\ 0 \end{array} \right] \right\| _ {2} ^ {2} = (\sigma^ {2} + w ^ {*} w),
$$

it follows that $\left\| A _ { 1 } \right\| ^ { 2 } \ge \sigma ^ { 2 } + w ^ { * } w$ . But since $\sigma = \| A \| = \left\| A _ { 1 } \right\|$ , we must have $w = 0$ . An obvious induction argument gives
