# Definitions

Stability is first defined with respect to changes in the initial conditions. Consider the discrete-time state-space equation (possibly nonlinear and time-varying)

$$x (k + 1) = f (x (k), k) \tag {3.1}$$

Let $x^{0}(k)$ and $x(k)$ be solutions of (3.1) when the initial conditions are $x^{0}(k_{0})$ and $x(k_{0})$ , respectively. Further, let $\| \cdot \|$ denote a vector norm.

DEFINITION 3.1 STABILITY The solution $x^0(k)$ of (3.1) is stable if for a given $\varepsilon > 0$ , there exists a $\delta(\varepsilon, k_0) > 0$ such that all solutions with $\|x(k_0) - x^0(k_0)\| < \delta$ are such that $\|x(k) - x_0(k)\| < \varepsilon$ for all $k \geq k_0$ .

DEFINITION 3.2 ASYMPTOTIC STABILITY The solution $x^0(k)$ (3.1) is asymptotically stable if it is stable and if $\delta$ can be chosen such that $\| x(k_0) - x^0(k_0) \| < \delta$ implies that $\| x(k) - x^0(k) \| \to 0$ when $k \to \infty$ .

From the definitions, it follows that stability in general is defined for a particular solution and not for the system. The definitions also imply that stability, in general, is a local concept. The interpretation of Definitions 3.1 and 3.2 is that the system is (asymptotically) stable if the trajectories do not change much if the initial condition is changed by a small amount.
