and the span $\{ v _ { j } , j = i , \ldots , i + k - 1 \}$ is an invariant subspace of H. The sum of all invariant subspaces corresponding to stable eigenvalues is the stable invariant subspace $\ X _ { - } ( H )$ . ✸

Example 12.1 Let

$$
A = \left[ \begin{array}{l l} - 3 & 2 \\ - 2 & 1 \end{array} \right] R = \left[ \begin{array}{l l} 0 & 0 \\ 0 & - 1 \end{array} \right], Q = \left[ \begin{array}{l l} 0 & 0 \\ 0 & 0 \end{array} \right].
$$

The eigenvalues of H are $1 , 1 , - 1 , - 1$ , and the corresponding eigenvectors and generalized eigenvectors are

$$
v _ {1} = \left[ \begin{array}{c} 1 \\ 2 \\ 2 \\ - 2 \end{array} \right], v _ {2} = \left[ \begin{array}{c} - 1 \\ - 3 / 2 \\ 1 \\ 0 \end{array} \right] v _ {3} = \left[ \begin{array}{c} 1 \\ 1 \\ 0 \\ 0 \end{array} \right], v _ {4} = \left[ \begin{array}{c} 1 \\ 3 / 2 \\ 0 \\ 0 \end{array} \right].
$$

It is easy to check that $\{ v _ { 3 } , v _ { 4 } \}$ form a basis for the stable invariant subspace $\mathcal { X } _ { - } ( H )$ , $\{ v _ { 1 } , v _ { 2 } \}$ form a basis for the antistable invariant subspace, and $\{ v _ { 1 } , v _ { 3 } \}$ form a basis for another invariant subspace corresponding to eigenvalues {1, −1} so

$$
\overline {{X}} = 0, \quad \tilde {X} = \left[ \begin{array}{c c} - 1 0 & 6 \\ 6 & - 4 \end{array} \right], \quad \hat {X} = \left[ \begin{array}{c c} - 2 & 2 \\ 2 & - 2 \end{array} \right]
$$

are all solutions of the ARE with the property

$$\lambda (A + R \overline {{X}}) = \{- 1, - 1 \}, \quad \lambda (A + R \tilde {X}) = \{1, 1 \}, \quad \lambda (A + R \hat {X}) = \{1, - 1 \}.$$

Thus only $\overline { { X } }$ is the stabilizing solution. The stabilizing solution can be found using the following Matlab command:

$$\gg [ \mathrm{X} _ {1}, \mathrm{X} _ {2} ] = \operatorname {r i c \_ s c h r} (\mathrm{H}), \mathrm{X} = \mathrm{X} _ {2} / \mathrm{X} _ {1}$$

The following well-known results give some properties of X as well as verifiable conditions under which H belongs to dom(Ric).

Theorem 12.1 Suppose $H \in \operatorname { d o m } ( \operatorname { R i c } )$ and $X = \operatorname { R i c } ( H )$ . Then

(i) X is real symmetric;   
(ii) X satisfies the algebraic Riccati equation

$$A ^ {*} X + X A + X R X + Q = 0;$$

(iii) $A + R X$ is stable.

Proof. (i) Let $X _ { 1 } , X _ { 2 }$ be as before. It is claimed that

$$X _ {1} ^ {*} X _ {2} \text { is Hermitian. } \tag {12.4}$$

To prove this, note that there exists a stable matrix $H _ { - } \mathrm { ~ i n ~ } \mathbb { R } ^ { n \times n }$ such that
