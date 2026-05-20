# EXAMPLE 6.11 Step commands

With the transfer function of Eq. (6.63) used in Example 6.10, the closed-loop characteristic equation is given by

$$(s + 1) (s ^ {2} + 3 0 s + 2 2 9) + 4 5 8 \theta_ {2} = 0$$

or

$$s ^ {3} + 3 1 s ^ {2} + 2 5 9 s + 2 2 9 + 4 5 8 \theta_ {2} = 0$$

This equation has all roots in the left half-plane if

$$- 0. 5 < \hat {\theta} _ {2} < 1 7. 0 3 = \theta_ {2} ^ {s t a h}$$

The averaged equations for the parameter estimates are obtained by setting $\omega = 0$ in Eqs. (6.60). If it is assumed that $G_{m}(0) = 1$ , the equations become

$$\frac {d \bar {\theta} _ {1}}{d t} = - \frac {\gamma u _ {0} ^ {2}}{2} \left(\frac {\bar {\theta} _ {1} G (0)}{1 + \bar {\theta} _ {2} G (0)} - 1\right) \tag {6.65}\frac {d \bar {\theta} _ {2}}{d t} = \frac {\gamma u _ {0} ^ {2}}{2} \frac {\bar {\theta} _ {1} G (0)}{1 + \bar {\theta} _ {2} G (0)} \left(\frac {\bar {\theta} _ {1} G (0)}{1 + \bar {\theta} _ {2} G (0)} - 1\right)$$

These differential equations have the equilibrium set of Eq. (6.64).

Close to the equilibrium set, the equations are described by the following linearized equation:

$$
\frac {d x}{d t} = \frac {\gamma u _ {0} ^ {2}}{2 \theta_ {1} ^ {0}} \left( \begin{array}{c c} - 1 & 1 \\ 1 & - 1 \end{array} \right) x \tag {6.66}
$$

where $x_{1} = \bar{\theta}_{1} - \theta_{1}^{0}$ and $x_{2} = \bar{\theta}_{2} - \theta_{2}^{0}$ . Consider a point away from the equilibrium line, that is, $x_{2} = x_{1} + \delta$ or $\bar{\theta}_{2} = \bar{\theta}_{1} - 1 / G(0) + \delta$ . The velocity of the state vector at that point is $\dot{x}_{1} = \gamma u_{0}^{2}\delta/\theta_{1}^{0}$ , $\dot{x}_{2} = -\gamma u_{0}^{2}\delta/\theta_{1}^{0}$ . The vector field of the linearized equation is thus as shown in Fig. 6.15. The vector field thus pushes the parameter toward the equilibrium for $\bar{\theta}_{1} > 0$ and away from the equilibrium for $\bar{\theta}_{1} < 0$ . Notice that the system is not structurally stable because one eigenvalue of the linearized equation is zero. This means that we can expect drastically different properties when the system is perturbed.

![](image/33f47cd7f8971927de5c13f2d65943789f9509747e76213405fa1982fbac5ea5.jpg)

<details>
<summary>text_image</summary>

Stability boundary
θ̄₂
θ̄₁
</details>

Figure 6.15 Equilibrium set and local behavior of the averaged equations.

![](image/4e802eaa20cb414bce78dfa1d3a0699013ae97831a8df6f353ff84e2ff1ceab1.jpg)

<details>
<summary>contour</summary>
