# 5.1 Variational Calculus for Discrete-Time Systems

Substituting (5.1.8) in (5.1.6) and noting that the first variation should be zero, we have

$$
\begin{array}{l} \sum_ {k = k _ {0}} ^ {k _ {f} - 1} \left[ \frac {\partial V (x ^ {*} (k) , x ^ {*} (k + 1) , k)}{\partial x ^ {*} (k)} + \frac {\partial V (x ^ {*} (k - 1) , x ^ {*} (k) , k - 1)}{\partial x ^ {*} (k)} \right] \delta x (k) \\ + \left. \left[ \frac {\partial V (x ^ {*} (k - 1) , x ^ {*} (k) , k - 1)}{\partial x ^ {*} (k)} \delta x (k) \right] \right| _ {k = k _ {0}} ^ {k = k _ {f}} = 0. \tag {5.1.9} \\ \end{array}
$$

\- Step 4: Euler-Lagrange Equation: For (5.1.9) to be satisfied for arbitrary variations $\delta x(k)$ , we have the condition that the coefficient of $\delta x(k)$ in the first term in (5.1.9) be zero. That is

$$\boxed {\frac {\partial V \left(x ^ {*} (k) , x ^ {*} (k + 1) , k\right)}{\partial x ^ {*} (k)} + \frac {\partial V \left(x ^ {*} (k - 1) , x ^ {*} (k) , k - 1\right)}{\partial x ^ {*} (k)} = 0.} \tag {5.1.10}$$

This may very well be called the discrete-time version of the Euler-Lagrange (EL) equation.

\- Step 5: Boundary Conditions: The boundary or transversality condition is obtained by setting the second term in (5.1.9) equal to zero. That is

$$\boxed {\left[ \frac {\partial V (x ^ {*} (k - 1) , x ^ {*} (k) , k - 1)}{\partial x ^ {*} (k)} \delta x (k) \right] \Bigg | _ {k = k _ {0}} ^ {k = k _ {f}} = 0.} \tag {5.1.11}$$

Now, we discuss two important cases:

1. For a fixed-end point system, we have the boundary conditions $x(k_{0})$ and $x(k_{f})$ fixed and hence $\delta x(k_{0}) = \delta x(k_{f}) = 0$ . The additional (or derived) boundary condition (5.1.11) does not exist.   
2. For a free-final point system, we are given the initial condition $x(k_{0})$ and hence $\delta x(k_{0}) = 0$ in (5.1.11). Next, at the final point, $k_{f}$ is specified, and $x(k_{f})$ is not specified or is free,

and hence $\delta x(k_f)$ is arbitrary. Thus, the coefficient of $\delta x(k)$ at $k = k_{f}$ is zero in the condition (5.1.11) which reduces to

$$\left. \left[ \frac {\partial V \left(x ^ {*} (k - 1) , x ^ {*} (k) , k - 1\right)}{\partial x ^ {*} (k)} \right] \right| _ {k = k _ {f}} = 0. \tag {5.1.12}$$

Let us note that the necessary condition (5.1.10) and the associated boundary or transversality condition (5.1.12) are derived for the scalar function $x(k)$ only.
