# A.7 Quadratic Forms

Positive definite and positive semidefinite matrices show up often in LQ problems. Here are some basic facts about them. In the following Q is real and symmetric and R is real.

The matrix Q is positive definite $( Q > 0 ) , { \mathrm { i f } }$

$$x ^ {\prime} Q x > 0, \quad \forall \text { nonzero } x \in \mathbb {R} ^ {n}$$

The matrix Q is positive semidefinite $( Q \ge 0 )$ , if

$$x ^ {\prime} Q x \geq 0, \quad \forall x \in \mathbb {R} ^ {n}$$

You should be able to prove the following facts.

1. $Q > 0$ if and only if $\lambda ( Q ) > 0 , \quad \lambda \in \mathrm { e i g } ( Q )$ .   
2. $Q \geq 0$ if and only if $\lambda ( Q ) \ge 0 , \quad \lambda \in \mathrm { e i g } ( Q )$ .   
3. $Q \geq 0 \Rightarrow R ^ { \prime } Q R \geq 0 \quad \forall R .$ .

4. Q > 0 and R nonsingular $\Rightarrow R ^ { \prime } Q R > 0 $ .

5. $Q > 0$ and R full column rank $\Rightarrow R ^ { \prime } Q R > 0$ .

6. $Q _ { 1 } > 0 , Q _ { 2 } \geq 0 \Rightarrow Q = Q _ { 1 } + Q _ { 2 } > 0 .$

7. $Q > 0 \Rightarrow z ^ { * } Q z > 0$ ∀ nonzero $z \in \mathbb { C } ^ { n }$ .

8. Given $Q \geq 0 , x ^ { \prime } Q x = 0$ if and only if $Q x = 0$ .

You may want to use the Schur decomposition (Schur, 1909) of a matrix in establishing some of these eigenvalue results. Golub and Van Loan (1996, p.313) provide the following theorem

Theorem A.1 (Schur decomposition). If $A \in \mathbb { C } ^ { n \times n }$ then there exists a unitary $Q \in \mathbb { C } ^ { n \times n }$ such that

$$Q ^ {*} A Q = T$$

in which T is upper triangular.

Note that because T is upper triangular, its diagonal elements are the eigenvalues of A. Even if A is a real matrix, T can be complex because the eigenvalues of a real matrix may come in complex conjugate pairs. Recall a matrix Q is unitary if $Q ^ { * } Q = I$ . You should also be able to prove the following facts (Horn and Johnson, 1985).

1. If $A \in \mathbb { C } ^ { n \times n }$ and BA = I for some $B \in \mathbb { C } ^ { n \times n }$ , then

(b) B is unique   
(c) $A B = I$

(a) A is nonsingular

2. The matrix Q is unitary if and only if

(a) Q is nonsingular and $Q ^ { * } = Q ^ { - 1 }$   
(b) $Q Q ^ { * } = I$   
(c) $Q ^ { * }$ is unitary   
(d) The rows of Q form an orthonormal set   
(e) The columns of Q form an orthonormal set

3. If A is real and symmetric, then T is real and diagonal and Q can be chosen real and orthogonal. It does not matter if the eigenvalues of A are repeated.
