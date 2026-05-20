# 2.7 Semidefinite Matrices

A square Hermitian matrix $A = A ^ { * }$ is said to be positive definite $( s e m i d e f i n i t e )$ , denoted by $A > 0 ~ ( \geq 0 )$ , if $x ^ { * }$ Ax $> 0 \ ( \geq 0 )$ for all $x \neq 0$ . Suppose $A \in \mathbb { F } ^ { n \times n }$ and $A = A ^ { * } \geq 0 ;$ then there exists a $B \in \mathbb { F } ^ { n \times r }$ with $r \geq \mathrm { r a n k } ( A )$ such that $A = B B ^ { * }$ .

Lemma 2.7 Let $B \in \mathbb { F } ^ { m \times n }$ and $C \in \mathbb { F } ^ { k \times n }$ . Suppose m $\geq k$ and $B ^ { * } B = C ^ { * } C$ . Then there exists a matrix $U \in \mathbb { F } ^ { m \times k }$ such that $U ^ { * } U = I$ and $B = U C$ .

Proof. Let $V _ { 1 }$ and $V _ { 2 }$ be unitary matrices such that

$$
B = V _ {1} \left[ \begin{array}{c} B _ {1} \\ 0 \end{array} \right], C = V _ {2} \left[ \begin{array}{c} C _ {1} \\ 0 \end{array} \right],
$$

where $B _ { 1 }$ and $C _ { 1 }$ are full-row rank. Then $B _ { 1 }$ and $C _ { 1 }$ have the same number of rows and $V _ { 3 } : = B _ { 1 } C _ { 1 } ^ { * } ( C _ { 1 } C _ { 1 } ^ { * } ) ^ { - 1 }$ satisfies $V _ { 3 } ^ { * } V _ { 3 } = I$ since $B ^ { * } B = C ^ { * } C$ . Hence $V _ { 3 }$ is a unitary matrix and $V _ { 3 } ^ { * } B _ { 1 } = C _ { 1 }$ . Finally, let

$$
U = V _ {1} \left[ \begin{array}{c c} V _ {3} & 0 \\ 0 & V _ {4} \end{array} \right] V _ {2} ^ {*}
$$

for any suitably dimensioned $V _ { 4 }$ such that $V _ { 4 } ^ { * } V _ { 4 } = I$ .

We can define square root for a positive semidefinite matrix A, $A ^ { 1 / 2 } = ( A ^ { 1 / 2 } ) ^ { * } \geq 0$ by

$$A = A ^ {1 / 2} A ^ {1 / 2}.$$

Clearly, $A ^ { 1 / 2 }$ can be computed by using spectral decomposition or SVD: Let $A = U \Lambda U ^ { * }$ ; then

$$A ^ {1 / 2} = U \Lambda^ {1 / 2} U ^ {*},$$

where

$$\Lambda = \operatorname{diag} \left\{\lambda_ {1}, \dots , \lambda_ {n} \right\}, \quad \Lambda^ {1 / 2} = \operatorname{diag} \left\{\sqrt {\lambda_ {1}}, \dots , \sqrt {\lambda_ {n}} \right\}.$$

Lemma 2.8 Suppose $A = A ^ { * } > 0$ and $B = B ^ { * } \geq 0$ . Then $A > B \ i f f ( B A ^ { - 1 } ) < 1$

Proof. Since $A > 0$ , we have $A > B$ iff

$$0 < I - A ^ {- 1 / 2} B A ^ {- 1 / 2}$$

i.e., iff $\rho ( A ^ { - 1 / 2 } B A ^ { - 1 / 2 } ) < 1$ . However, $A ^ { - 1 / 2 } B A ^ { - 1 / 2 }$ and $B A ^ { - 1 }$ are similar, hence $\rho ( B A ^ { - 1 } ) \stackrel { } { = } \rho ( A ^ { - 1 / 2 } B A ^ { - 1 / 2 } )$ and the claim follows. ✷
