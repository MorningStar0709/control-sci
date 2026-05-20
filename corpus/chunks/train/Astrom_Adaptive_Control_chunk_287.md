# DEFINITION 5.1 Lyapunov stability

The solution $x(t) = 0$ to the differential equation (5.17) is called stable if for given $\varepsilon > 0$ there exists a number $\delta(\varepsilon) > 0$ such that all solutions with initial conditions

$$\left| \left| x (0) \right| \right| < \delta$$

have the property

$$\| x (t) \| < \varepsilon \quad \text { for } \quad 0 \leq t < \infty \tag {5.18}$$

The solution is unstable if it is not stable. The solution is asymptotically stable if it is stable and $\delta$ can be found such that all solutions with $\|x(0)\| < \delta$ have the property that $\|x(t)\| \to 0$ as $t \to \infty$ .

Remark 1. If the solution is asymptotically stable for any initial value, then it is said to be globally asymptotically stable.

Remark 2. Notice that Lyapunov stability refers to stability of a particular solution and not to the differential equation. □

Lyapunov developed a method for investigating stability that is based on the idea of finding a function with special properties. To describe these, we first introduce the notion of positive definite functions.
