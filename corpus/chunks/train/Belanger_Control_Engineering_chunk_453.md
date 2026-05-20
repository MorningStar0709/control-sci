a. Compute the eigenvectors, and identify each with heave, roll, or sway.   
b. Using pole placement, use $u_{LC}$ to shift the heave modes to $-x \pm jx$ for $x = 100, 150$ , and $200\mathrm{rad / s}$ .   
c. Use $u_{LD}$ to shift the roll modes to $-1.5x \pm j1.5x$ for $x$ as in part (b).   
d. Use $u_{GD}$ to shift the sway modes to $-0.5x \pm j0.5x$ for $x$ as in part (b).   
e. Compute the responses $\Delta z, \Delta \theta$ , and $\Delta y$ and the inputs $\Delta u_{L1}, \Delta u_{L2}, \Delta u_{G1}$ , and $\Delta u_{G2}$ for the three initial conditions $\Delta z(0) = 1$ , $\Delta \theta(0) = 1$ , $\Delta y(0) = 1$ , and all other state variables equal to zero (i.e., three separate simulations, each with one nonzero state variable). If it is required that $|\Delta u_{L1}|$ , $|\Delta u_{L2}| \leq 700$ and $|\Delta u_{G1}|$ , $|\Delta u_{G2}| \leq 170$ (because the inputs are the squares of currents, they may not be negative and cannot be less than minus the nominal value), what are the maximum allowable values of $\Delta z(0)$ , $\Delta \theta(0)$ , and $\Delta y(0)$ ?

![](image/6ef10ad3d285c2ef0e451fdbd0f76738c95ac54221240f573920452f606e94e4.jpg)

7.17 For the system of Problem 7.1, with $u = 0$ , set up and solve the matrix Lyapunov equation to compute $J = \int_0^\infty y^2 (t)dt$ , given $x(0) = x_0$ . From the solution of the Lyapunov equation, verify that the system is stable.

![](image/584675f641bd6a2e5c0b7ae8655f77cc74a35ed8b69a523274b6752e2da57b68.jpg)

7.18 A control law $u = -ky$ is used for the system of Problem 7.2.

a. Write the closed-loop state equation.   
b. Set up and solve the matrix Lyapunov equation to obtain $J = \int_0^\infty y^2 (t)dt$ as a function of $k$ .   
c. Plot $J(k)$ versus $k$ and find the minima for $x(0) = [\frac{1}{0}]$ and $[\frac{0}{1}]$ . Ascertain from the solution of the Lyapunov equation that the minimizing value of $k$ leads, in each case, to a stable closed-loop system.

7.19 For $A = \left[ \begin{array}{cc}0 & 1\\ -1 & -2 \end{array} \right]$ , solve the matrix Lyapunov equation with $Q = I$ to show that $A$ is unstable.

7.20 For the system

$$
\dot {\mathbf {x}} = \left[ \begin{array}{l l} 0 & 1 \\ - 1 & 0 \end{array} \right] \mathbf {x} + \left[ \begin{array}{l} 0 \\ 1 \end{array} \right] u

y = \left[ \begin{array}{l l} 1 & 0 \end{array} \right] \mathbf {x}
$$

Calculate (analytically) the state feedback control matrix that minimizes $J = \int_0^\infty [y^2 (t) + \rho u^2 (t)]dt, \rho > 0$ .
