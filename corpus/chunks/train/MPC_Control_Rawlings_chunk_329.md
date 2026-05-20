# Exercise 2.21: Unreachable setpoints in constrained versus unconstrained linear systems

Consider the linear system with input constraint

$$x ^ {+} = A x + B u \quad u \in \mathbb {U}$$

We examine here both unconstrained systems in which $\mathbb { U } = \mathbb { R } ^ { m }$ and constrained systems in which U $\subset \mathbb { R } ^ { m }$ is a convex polyhedron. Consider the stage cost defined in terms of setpoints for state and input $x _ { \mathrm { s p } }$ , usp

$$\ell (x, u) = (1 / 2) \big (| x - x _ {\mathrm{sp}} | _ {Q} ^ {2} + | u - u _ {\mathrm{sp}} | _ {R} ^ {2} \big)$$

in which we assume for simplicity that $Q , R > 0$ . For the setpoint to be unreachable in an unconstrained problem, the setpoint must be inconsistent, i.e., not a steady state of the system, or

$$x _ {\mathrm{sp}} \neq A x _ {\mathrm{sp}} + B u _ {\mathrm{sp}}$$

Consider also using the stage cost centered at the optimal steady state $( x _ { s } , u _ { s } )$

$$\ell_ {s} (x, u) = (1 / 2) \left(| x - x _ {s} | _ {Q} ^ {2} + | u - u _ {s} | _ {R} ^ {2}\right)$$

The optimal steady state satisfies

$$(x _ {s}, u _ {s}) = \arg \min _ {x, u} \ell (x, u)$$

subject to

$$
\left[ \begin{array}{c c} I - A & - B \end{array} \right] \left[ \begin{array}{c} x \\ u \end{array} \right] = 0 \quad u \in \mathbb {U}
$$

Figure 2.10 depicts an inconsistent setpoint, and the optimal steady state for unconstrained and constrained systems.

(a) For unconstrained systems, show that optimizing the cost function with terminal constraint

$$V (x, \mathbf {u}) := \sum_ {k = 0} ^ {N - 1} \ell (x (k), u (k))$$

![](image/dad55755c4b548ec45fe3b4760d4f8a0c5f35178d16ce8dd476dddfa91993900.jpg)

<details>
<summary>line</summary>

| x | ℓ(x, u⁰(x)) |
| --- | --- |
| k | ℓ = ℓ(x) |
| k+1 | ℓ = ℓ(x) |
| k+2 | ℓ < V⁰(x) |
| k+3 | ℓ < V⁰(x) |
| k+4 | ℓ < V⁰(x) |
| k+5 | ℓ < V⁰(x) |
| k+6 | ℓ < V⁰(x) |
| k+7 | ℓ < V⁰(x) |
</details>

Figure 2.11: Stage cost versus time for the case of unreachable setpoint. The cost $V ^ { 0 } ( x ( k ) )$ is the area under the curve to the right of time k.

subject to

$$x ^ {+} = A x + B u \quad x (0) = x \quad x (N) = x _ {s}$$

gives the same solution as optimizing the cost function

$$V _ {s} (x, \mathbf {u}) := \sum_ {k = 0} ^ {N - 1} \ell_ {s} (x (k), u (k))$$

subject to the same model constraint, initial condition, and terminal constraint.
