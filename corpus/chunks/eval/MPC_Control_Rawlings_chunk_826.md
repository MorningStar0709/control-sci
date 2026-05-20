For real, but not necessarily symmetric, A you can restrict yourself to real matrices, by using the real Schur decomposition (Golub and Van Loan, 1996, p.341), but the price you pay is that you can achieve only block upper triangular T , rather than strictly upper triangular T .

Theorem A.2 (Real Schur decomposition). $I f A \in \mathbb { R } ^ { n \times n }$ then there exists an orthogonal $Q \in \mathbb { R } ^ { n \times n }$ such that

$$
Q ^ {\prime} A Q = \left[ \begin{array}{c c c c} R _ {1 1} & R _ {1 2} & \dots & R _ {1 m} \\ 0 & R _ {2 2} & \dots & R _ {2 m} \\ \vdots & \vdots & \ddots & \vdots \\ 0 & 0 & \dots & R _ {m m} \end{array} \right]
$$

in which each $R _ { i i }$ is either a real scalar or a $2 \times 2$ real matrix having complex conjugate eigenvalues; the eigenvalues of $R _ { i i }$ are the eigenvalues of A.

If the eigenvalues of $R _ { i i }$ are disjoint (i.e., the eigenvalues are not repeated), then R can be taken block diagonal instead of block triangular (Golub and Van Loan, 1996, p.366).
