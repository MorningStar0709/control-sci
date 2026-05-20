# 3.6 Multivariable System Poles and Zeros

A matrix is called a polynomial matrix of a variable if every element of the matrix is a polynomial of the variable.

Definition 3.10 Let $Q ( s )$ be a $( p \times m )$ polynomial matrix (or a transfer matrix) of s. Then the normal rank of $Q ( s )$ , denoted normalrank $\left( Q ( s ) \right)$ ), is the maximally possible rank of $Q ( s )$ for at least one $s \in \mathbb { C }$ .

To show the difference between the normal rank of a polynomial matrix and the rank of the polynomial matrix evaluated at a certain point, consider

$$
Q (s) = \left[ \begin{array}{c c} s & 1 \\ s ^ {2} & 1 \\ s & 1 \end{array} \right].
$$

Then $Q ( s )$ has normal rank 2 since rank $Q ( 3 ) = 2$ . However, $Q ( 0 )$ has rank 1.

The poles and zeros of a transfer matrix can be characterized in terms of its statespace realizations. Let

$$
\left[ \begin{array}{c c} A & B \\ \hline C & D \end{array} \right]
$$

be a state-space realization of $G ( s )$ .

Definition 3.11 The eigenvalues of A are called the poles of the realization of $G ( s )$ .

To define zeros, let us consider the following system matrix:

$$
Q (s) = \left[ \begin{array}{c c} A - s I & B \\ C & D \end{array} \right].
$$

Definition 3.12 A complex number $z _ { 0 } \in \mathbb { C }$ is called an invariant zero of the system realization if it satisfies

$$
\operatorname{rank} \left[ \begin{array}{c c} A - z _ {0} I & B \\ C & D \end{array} \right] <   \text {normalrank} \left[ \begin{array}{c c} A - s I & B \\ C & D \end{array} \right].
$$

The invariant zeros are not changed by constant state feedback since

$$
\begin{array}{l} \operatorname{rank} \left[ \begin{array}{c c} A + B F - z _ {0} I & B \\ C + D F & D \end{array} \right] = \operatorname{rank} \left[ \begin{array}{c c} A - z _ {0} I & B \\ C & D \end{array} \right] \left[ \begin{array}{c c} I & 0 \\ F & I \end{array} \right] \\ = \operatorname{rank} \left[ \begin{array}{c c} A - z _ {0} I & B \\ C & D \end{array} \right]. \\ \end{array}
$$

It is also clear that invariant zeros are not changed under similarity transformation.

The following lemma is obvious.

Lemma 3.7 Suppose $\left\lceil \begin{array} { c c } { { A - s I } } & { { B } } \\ { { C } } & { { D } } \end{array} \right\rceil$ has full-column normal rank. Then $z _ { 0 } \in \mathbb { C }$ is an invariant zero of a realization $( A , B , { \overline { { C } } } , D )$ if and only if there exist $0 \neq x \in \mathbb { C } ^ { n }$ and $u \in \mathbb { C } ^ { m }$ such that
