Figure 6.19 Simulation of the ODEs of the parameter estimates for the integrator when d = 2 and c = -0.8. (a) $\tau = 0.4$ . (b) $\tau = 0.6$ . The parameter values corresponding to the moving-average controller are indicated by dots.

Since $b$ is nonnegative, it follows that this equation has roots in the right half-plane or at $\lambda = 0$ for all $c$ in the interval $(-1,1)$ . The equilibrium is thus always unstable.

In Case 2(b) the characteristic equation of the matrix K is given by

$$\frac {(1 + c ^ {2}) (1 - b c) ^ {2} + c ^ {4} (1 - b ^ {2})}{c (c - b) (1 - b c)} \lambda^ {2} + \frac {1 + c ^ {2} - b c}{c} \lambda + 1 = 0$$

This equation has all roots in the left half-plane if b < c.

In Case 2(c), moving-average control, the characteristic equation is

$$\lambda^ {2} + 2 \lambda (b - c) + b (b - c) = 0$$

Since b is positive, it follows that this equation has its roots in the left half-plane if b > c. Notice that the moving-average controller is locally stable for b > c even if $h/2 < \tau < h$ , that is, when the controlled process is non-minimum-phase.

Summarizing, we find that if d = 1, there is only one equilibrium, which corresponds to the minimum-variance control. This equilibrium is locally stable only if $\tau < h/2$ . When d = 2, there are three equilibria, corresponding to Cases 2(a), 2(b), and 2(c). Equilibrium 2(a) is always unstable; equilibrium 2(b) is stable if b < c; and equilibrium 2(c) is stable if b > c.

The phase portraits of the ODEs associated with the algorithm are shown in Fig. 6.19 for the case in which d = 2 and c = -0.8. When $\tau = 0.4$ , there are three equilibria. They correspond to Case 2(a), which is a saddle point, Case 2(b), which is an unstable focus, and Case 2(c), which is a stable node. The stable node corresponds to the moving-average controller. The parameters are $r_{1} = 0.08$ and $s_{0} = 0.20$ . For $\tau = 0.6$ there is only one equilibrium, which corresponds to the moving-average controller with the parameters $r_{1} = 0.12$ and $s_{0} = 0.20$ . Figure 6.19 also shows that starting points exist for which the algorithm does not converge. The estimates are driven toward the stability boundary.

The examples show how it is possible to use the associated ODE both to analyze the system and to get a feel for the behavior close to the stationary points as well as far away from them.
