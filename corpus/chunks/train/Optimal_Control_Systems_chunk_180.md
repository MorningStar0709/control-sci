$$
\begin{array}{l} \left[ \begin{array}{c c} \dot {p} _ {1 1} (t) & \dot {p} _ {1 2} (t) \\ \dot {p} _ {1 2} (t) & \dot {p} _ {2 2} (t) \end{array} \right] = - \left[ \begin{array}{c c} p _ {1 1} (t) & p _ {1 2} (t) \\ p _ {1 2} (t) & p _ {2 2} (t) \end{array} \right] \left[ \begin{array}{c c} 0 & 1 \\ - 2 & 1 \end{array} \right] \\ - \left[ \begin{array}{c c} 0 & - 2 \\ 1 & 1 \end{array} \right] \left[ \begin{array}{c c} p _ {1 1} (t) & p _ {1 2} (t) \\ p _ {1 2} (t) & p _ {2 2} (t) \end{array} \right] \\ + \left[ \begin{array}{c c} p _ {1 1} (t) & p _ {1 2} (t) \\ p _ {1 2} (t) & p _ {2 2} (t) \end{array} \right] \left[ \begin{array}{c} 0 \\ 1 \end{array} \right] 4 \left[ \begin{array}{c c} 0 & 1 \end{array} \right] \left[ \begin{array}{c c} p _ {1 1} (t) & p _ {1 2} (t) \\ p _ {1 2} (t) & p _ {2 2} (t) \end{array} \right] \\ - \left[ \begin{array}{l l} 2 & 3 \\ 3 & 5 \end{array} \right] \tag {3.3.28} \\ \end{array}
$$

satisfying the final condition (3.2.35)

$$
\left[ \begin{array}{l l} p _ {1 1} (5) & p _ {1 2} (5) \\ p _ {1 2} (5) & p _ {2 2} (5) \end{array} \right] = \left[ \begin{array}{l l} 1 & 0. 5 \\ 0. 5 & 2 \end{array} \right]. \tag {3.3.29}
$$

Simplifying the matrix DRE (3.3.28), we get

$$
\begin{array}{l} \dot {p} _ {1 1} (t) = 4 p _ {1 2} ^ {2} (t) + 4 p _ {1 2} (t) - 2, \\ p _ {1 1} (5) = 1, \\ \dot {p} _ {1 2} (t) = - p _ {1 1} (t) - p _ {1 2} (t) + 2 p _ {2 2} (t) + 4 p _ {1 2} (t) p _ {2 2} (t) - 3, \\ p _ {1 2} (5) = 0. 5 \\ \dot {p} _ {2 2} (t) = - 2 p _ {1 2} (t) - 2 p _ {2 2} (t) + 4 p _ {2 2} ^ {2} (t) - 5, \\ p _ {2 2} (5) = 2. \tag {3.3.30} \\ \end{array}
$$

Solving the previous set of nonlinear, differential equations backward in time with the given final conditions, one can obtain the numerical solutions for the Riccati coefficient matrix $\mathbf{P}(t)$ . However, here the solutions are obtained using the analytical solution as given earlier in this section. The solutions for the Riccati coefficients are plotted in Figure 3.3. Using these Riccati coefficients, the closed-loop optimal control system is shown in Figure 3.4. Using the optimal control $u^{*}(t)$ given by (3.3.27), the plant equations (3.3.24) are solved forward in time to obtain the optimal states $x_{1}^{*}(t)$ and $x_{2}^{*}(t)$ as shown in Figure 3.5 for the initial conditions $[2 - 3]$ . Finally, the optimal control $u^{*}(t)$ is shown in Figure 3.6. The previous results are obtained using Control System Toolbox of the MATLAB $^{©}$ , Version 6 as shown below.
