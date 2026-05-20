# Definiteness

Let $\mathbf{P}$ be a real and symmetric matrix and $\mathbf{x}$ be a nonzero real vector, then

1. P is positive definite if the scalar quantity $x^{\prime}Px > 0$ or is positive.   
2. $\mathbf{P}$ is positive semidefinite if the scalar quantity $\mathbf{x}'\mathbf{P}\mathbf{x} \geq 0$ or is nonnegative.   
3. $\mathbf{P}$ is negative definite if the scalar quantity $\mathbf{x}'\mathbf{P}\mathbf{x} < 0$ or is negative.   
4. $\mathbf{P}$ is negative semidefinite if the scalar quantity $\mathbf{x}'\mathbf{P}\mathbf{x} \leq 0$ or nonpositive.

A test for real symmetric matrix P to be positive definite is that all its principal or leading minors must be positive, that is,

$$
p _ {1 1} > 0, \quad \left| \begin{array}{l l} p _ {1 1} & p _ {1 2} \\ p _ {1 2} & p _ {2 2} \end{array} \right| > 0, \quad \left| \begin{array}{l l} p _ {1 1} & p _ {1 2} p _ {1 3} \\ p _ {1 2} & p _ {2 2} p _ {2 3} \\ p _ {1 3} & p _ {2 3} p _ {3 3} \end{array} \right| > 0 \tag {A.3.2}
$$

for a 3x3 matrix P. The > sign is changed accordingly for positive semidefinite ( $\geq$ ), negative definite (<), and negative semidefinite ( $\leq$ 0) cases. Another simple test for definiteness is using eigenvalues (all eigenvalues positive for positive definiteness, etc.).

Also, note that

$$\left[ \mathbf {x} ^ {\prime} \mathbf {P x} \right] ^ {\prime} = \mathbf {x} ^ {\prime} \mathbf {P} ^ {\prime} \mathbf {x} = \mathbf {x} ^ {\prime} \mathbf {P x}\mathbf {P} = \sqrt {\mathbf {P}} \sqrt {\mathbf {P} ^ {\prime}} = \sqrt {\mathbf {P} ^ {\prime}} \sqrt {\mathbf {P}}. \tag {A.3.3}$$
