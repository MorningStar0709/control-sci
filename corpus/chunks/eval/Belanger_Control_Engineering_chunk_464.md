b. Simulate the system for $T_0(t) = 10^5 u_0(t)$ and $\omega_1(0_-) = \omega_2(0_-) = 66.6$ rad/s, $\omega_0(0_-) = 4.67$ rad/s, $\Delta_1(0_-) = \Delta_2(0_-) = 0$ , $u_1(t) = u_2(t) = 40$ . V. Simulate the observer, using the same initial conditions as for the plant. Compare the estimator and actual state variable values.

c. Repeat parts (a) and (b) for $v_0 = 0.1$ rad/s and 0.01 rad/s; this represents improved sensor accuracy. Comment on the degree of improvement in the estimator.

M

7.48 Two-pendula problem In Problem 2.19 (Chapter 2), a linearized model was derived for a system with two pendula. In this instance, let $\ell_1 = 1\mathrm{m}$ and $\ell_2 = 0.5\mathrm{m}$ . We wish to design an observer, assuming that $\theta_{1}, \theta_{2}$ , and $x$ are available for measurement. The assumption of errors of $\pm 0.001\mathrm{m}$ on $x$ and $\pm 0.001$ rad on $\theta_{1}$ and $\theta_{2}$ suggests using

$$V = (0. 0 0 1) ^ {2} I.$$

To model plant disturbances, assume external torque impulses of magnitude $w_{0}$ acting directly on the rods. This suggests using a W that is diagonal, with elements $w_{0}^{2}$ in the positions corresponding to $\omega_{1}$ and $\omega_{2}$ .

Design optimal observers for several values of $w_{0}$ , and calculate the eigenvalues of the error system (i.e., of A-GC). Select a value of $w_{0}$ just sufficient to ensure that every eigenvalue has a real part of -2 or less (i.e., 0.5a time constant of 0.5 s or less).

7.49 For the system of Problem 7.2, design a reduced-order observer of order 1 with the error-system eigenvalue at -2.

7.50 The system of Problem 7.1 has an output that is not a single state variable; i.e., $y = x_{1} + x_{2}$ .

a. Choose the second row of $T^{-1} = \begin{bmatrix} 1 & 1 \\ x & x \end{bmatrix}$ so that $T^{-1}$ is nonsingular. Use $T$ to carry out a linear transformation to a coordinate system $\mathbf{z}$ , with $\mathbf{x} = T\mathbf{z}$ . Note that $y = z_1$ .   
b. Design a reduced-order observer of order 1 for the transformed system, with the error-system eigenvalue at -4. Use $z_1$ and $\widehat{z}_2$ to generate estimates of the components of $\mathbf{x}$ .

M

7.51 dc servo with flexible shaft For the servo with flexible shaft of Problem 2.5 (Chapter 2):

a. Design a reduced-order observer (of order 4), using $\theta_{2}$ as the output. The eigenvalues of the error system should be $-200 \pm j200$ and $-10 \pm j10$ .
