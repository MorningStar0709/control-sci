$$
\left[ \begin{array}{c c} \mathbf {A} ^ {\prime} + \mathbf {Q A} ^ {- 1} \mathbf {E} & - \mathbf {Q A} ^ {- 1} \\ - \mathbf {A} ^ {- 1} \mathbf {E} & \mathbf {A} ^ {- 1} \end{array} \right] \left[ \begin{array}{c} g \\ - f \end{array} \right] = \mu \left[ \begin{array}{c} g \\ - f \end{array} \right].
$$

Using (5.4.21), we have

$$
\left[ \mathbf {H} ^ {- T} \right] \left[ \begin{array}{c} g \\ - f \end{array} \right] = \mu \left[ \begin{array}{c} g \\ - f \end{array} \right]. \tag {5.4.23}
$$

This shows that $\mu$ is also an eigenvalue of $H^{-T}$ , and hence of $H^{-1}$ . We know that from elementary matrix algebra that if $\alpha$ is an eigenvalue of a matrix A, then $1/\alpha$ is also an eigenvalue of matrix $A^{-1}$ . Therefore, $1/\mu$ is an eigenvalue of H, and hence the result. This means that the eigenvalues of H can be arranged as

$$
\mathbf {D} = \left[ \begin{array}{c c} \mathbf {M} & 0 \\ 0 & \mathbf {M} ^ {- 1} \end{array} \right] \tag {5.4.24}
$$

where, M is a diagonal (Jordon) matrix containing n eigenvalues outside the unit circle and $M^{-1}$ is a diagonal matrix containing n eigenvalues inside the unit circle which means that $M^{-1}$ is stable. Now, we note that D can be written in terms of a nonsingular matrix W whose columns are the eigenvectors of H as

$$\mathbf {W} ^ {- 1} \mathbf {H} \mathbf {W} = \mathbf {D}. \tag {5.4.25}$$
