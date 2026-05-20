# Example 2.8: Discontinuous MPC control law

Consider the nonlinear system defined by

$$
\begin{array}{l} x _ {1} ^ {+} = x _ {1} + u \\ x _ {2} ^ {+} = x _ {2} + u ^ {3} \\ \end{array}
$$

The control horizon is N = 3 and the cost function $V _ { 3 } ( \cdot )$ is defined by

$$V _ {3} (x, \mathbf {u}) := \sum_ {k = 0} ^ {2} \ell (x (k), u (k))$$

and the stage cost \`(·) is defined by

$$\ell (x, u) := | x | ^ {2} + u ^ {2}$$

The constraint sets are $\mathbb { X } = \mathbb { R } ^ { 2 } , \mathbb { U } = \mathbb { R }$ , and $\mathbb { X } _ { f } : = \{ 0 \} , \mathrm { i . e . }$ , there are no state and control constraints, and the terminal state must satisfy the constraint $x ( 3 ) = 0$ . Hence, although there are three control actions, u(0), u(1), and u(2), two must be employed to satisfy the terminal constraint, leaving only one degree of freedom. Choosing u(0) to be the free decision variable automatically constrains u(1) and u(2) to be functions of the initial state x and the first control action u(0). Solving

![](image/4ab8dfb9db04876c97d786b0f4417d4499bbfb82b2f7641464a267074377338a.jpg)

<details>
<summary>line</summary>

| θ/π | u₀ (solid line) | u₀ (dotted line with circles) |
| --- | --- | --- |
| -1.0 | 1.0 | 1.3 |
| -0.8 | 0.5 | 1.2 |
| -0.6 | 0.0 | 1.1 |
| -0.4 | -0.5 | 1.0 |
| -0.2 | -1.0 | 0.9 |
| 0.0 | -1.5 | 0.8 |
| 0.2 | -1.0 | 0.7 |
| 0.4 | -0.5 | 0.6 |
| 0.6 | 0.0 | 0.5 |
| 0.8 | 0.5 | 0.4 |
| 1.0 | 1.0 | 0.3 |
</details>

Figure 2.3: First element of control constraint set $\mathcal { U } _ { 3 } ( x )$ (shaded) and control law $\kappa _ { 3 } ( x )$ (circle) versus x = (cos(θ), sin(θ)), $\theta ~ \in ~ \left[ - \pi , \pi \right]$ on the unit circle for a nonlinear system with terminal constraint.

the equation

$$x _ {1} (3) = x _ {1} + u (0) + u (1) + u (2) \quad = 0x _ {2} (3) = x _ {2} + u (0) ^ {3} + u (1) ^ {3} + u (2) ^ {3} = 0$$

for u(1) and u(2) yields

$$u (1) = - x _ {1} / 2 - u (0) / 2 \pm \sqrt {b}u (2) = - x _ {1} / 2 - u (0) / 2 \mp \sqrt {b}$$

in which

$$b = \frac {3 u (0) ^ {3} - 3 u (0) ^ {2} x _ {1} - 3 u (0) x _ {1} ^ {2} - x _ {1} ^ {3} + 4 x _ {2}}{1 2 (u (0) + x _ {1})}$$

Clearly a real solution exists only if b is positive, i.e., if both the numerator and denominator in the expression for b have the same sign. The optimal control problem $\mathbb { P } _ { 3 } ( x )$ is defined by

![](image/cae33a2e3421878448c1aaa0572409176bc254cf2e13989f0f5b7f51743a127c.jpg)

<details>
<summary>scatter</summary>
