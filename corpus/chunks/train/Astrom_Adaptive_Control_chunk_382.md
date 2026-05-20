# Analysis

Let us briefly summarize how a nonlinear system such as Eqs. (6.1) and (6.2) or Eqs. (6.3) can be analyzed. It is a comparatively simple task to find the equilibrium solutions by solving the algebraic equations

$$
\begin{array}{l} \frac {d \xi}{d t} = 0 \\ \frac {d \hat {\theta}}{d t} = 0 \\ \end{array}
$$

for continuous-time systems. For discrete-time systems the equivalent equations become

$$
\begin{array}{l} \xi (t + 1) = \xi (t) \\ \hat {\theta} (t + 1) = \hat {\theta} (t) \\ \end{array}
$$

It may happen that proper equilibria do not exist. In such cases there may be integral manifolds where the parameters $\hat{\theta}$ are constant although the state $\xi$ varies with time. We are then led to averaging analysis, which is discussed in depth in Section 6.6. Equilibria having been found, it is natural to determine the local behavior by linearizing the equations around the equilibria and applying standard linear theory. A complication is that critical cases in which the eigenvalues are zero frequently occur. Having determined possible equilibria, we can proceed to investigate how the nature of the equilibria changes with important parameters of the system. It is of particular interest to investigate changes in which the nature of the local equilibria changes (bifurcation analysis). When the local properties are investigated, it is natural to proceed to find the global properties. There are no general tools for this, and we have to resort to simulations and approximations. Phase plane analysis is useful for two-dimensional systems.
