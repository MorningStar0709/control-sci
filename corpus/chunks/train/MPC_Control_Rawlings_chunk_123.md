# Exercise 1.7: Commuting functions of a matrix

Although matrix multiplication does not commute in general

$$A B \neq B A$$

multiplication of functions of the same matrix do commute. You may have used the following fact in Exercise 1.5

$$A ^ {- 1} \exp (A t) = \exp (A t) A ^ {- 1} \tag {1.53}$$

(a) Prove that (1.53) is true assuming A has distinct eigenvalues and can therefore be represented as

$$
A = Q \Lambda Q ^ {- 1} \qquad \Lambda = \left[ \begin{array}{c c c c} \lambda_ {1} & 0 & \dots & 0 \\ 0 & \lambda_ {2} & \dots & 0 \\ \vdots & \vdots & \ddots & \vdots \\ 0 & 0 & \dots & \lambda_ {n} \end{array} \right]
$$

in which Λ is a diagonal matrix containing the eigenvalues of A, and $Q$ is the matrix of eigenvectors such that

$$A q _ {i} = \lambda_ {i} q _ {i}, \quad i = 1, \dots , n$$

in which $q _ { i }$ is the ith column of matrix $Q$ .

(b) Prove the more general relationship

$$f (A) g (A) = g (A) f (A) \tag {1.54}$$

in which f and $^ g$ are any functions definable by Taylor series.

(c) Prove that (1.54) is true without assuming the eigenvalues are distinct.

Hint: use the Taylor series defining the functions and apply the Cayley-Hamilton theorem (Horn and Johnson, 1985, pp. 86–87).
