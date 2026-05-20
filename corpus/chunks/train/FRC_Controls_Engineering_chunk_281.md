# 9.3.14 Covariance matrix

The covariance matrix for a random vector $\mathbf { x } \in \mathbb { R } ^ { n }$ is

$$
\boldsymbol {\Sigma} = \operatorname{cov} (\mathbf {x}, \mathbf {x}) = E [ (\mathbf {x} - \overline {{\mathbf {x}}}) (\mathbf {x} - \overline {{\mathbf {x}}}) ^ {\mathsf {T}} ]
\boldsymbol {\Sigma} = \left[ \begin{array}{c c c} \operatorname{cov} (x _ {1}, x _ {1}) & \ldots & \operatorname{cov} (x _ {1}, x _ {n}) \\ \vdots & \ddots & \vdots \\ \operatorname{cov} (x _ {n}, x _ {1}) & \ldots & \operatorname{cov} (x _ {n}, x _ {n}) \end{array} \right]
$$

This $n \times n$ matrix is symmetric and positive semidefinite. A positive semidefinite matrix satisfies the relation that for any $\mathbf { v } \in \mathbb { R } ^ { n }$ for which $\mathbf { v } \neq 0 , \mathbf { v } ^ { \mathsf { T } } \pm \mathbf { v } \geq 0$ . In other words, the eigenvalues of Σ are all greater than or equal to zero.
