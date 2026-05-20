# 2.5.2.2 Neutrally Stable Systems

The system to be controlled is, again, $x ^ { + } = A x + B u$ , but A is now neutrally $\mathrm { s t a b l e ^ { 5 } }$ and the control u is subject to the constraint $u \in \mathbb { U }$ where U is compact, contains the origin in its interior, and has the form

$$\mathbb {U} = \left\{\boldsymbol {u} \in \mathbb {R} ^ {m} \mid \boldsymbol {u} _ {i} \in \left[ a _ {i}, b _ {i} \right], i \in \mathbb {I} _ {1: m} \right\}$$

where $a _ { i } < 0 < b _ { i }$ . The linear system $x ^ { + } = A x$ is therefore Lyapunov stable but not asymptotically stable. We assume that the pair $( A , B )$ is controllable. This problem is much more challenging than the problem considered immediately above since control has to be applied to make the system asymptotically stable, and this control can transgress the control constraints. Any linear control law $u \ = \ K x$ , no matter how small K, transgresses the control constraints for large enough x. Recent research, however, has demonstrated the existence of a global CLF for $x ^ { + } = A x + B u$ where A is neutrally stable; the Lyapunov function is, unusually, based on a nonlinear control law of the form $u = \mathsf { s a t } ( K x )$ where sat(·) is the vector saturation function defined by

$$
\operatorname{sat} (u) := \left[ \begin{array}{c c c c} \operatorname{sat} (u _ {1}) & \operatorname{sat} (u _ {2}) & \dots & \operatorname{sat} (u _ {m}) \end{array} \right] ^ {\prime}
$$

in which $u _ { i }$ is the ith component of the vector u, and

$$
\operatorname{sat} (u _ {i}) := \left\{ \begin{array}{l l} b _ {i} & u _ {i} \geq b _ {i} \\ u _ {i} & u _ {i} \in [ a _ {i}, b _ {i} ] \\ a _ {i} & u _ {i} \leq a _ {i} \end{array} \right.
$$

If A is neutrally stable, there exists a $P > 0$ such that

$$A ^ {\prime} P A \leq P$$

Note that this is weaker than the corresponding result in the previous section. If κ satisfies

$$\kappa B ^ {\prime} P B < I$$

however, then the linear control law $u = K x$ in which

$$K := - \kappa B ^ {\prime} P A$$

globally stabilizes the unconstrained system, i.e., the matrix $A _ { K } : = A +$ BK is stable. Hence, for all $Q ^ { * } > 0$ , there exists a positive definite matrix $P ^ { * }$ satisfying

$$A _ {K} ^ {\prime} P ^ {*} A _ {K} + Q ^ {*} = P ^ {*}$$

Let $\kappa _ { f } ( \cdot )$ denote the nonlinear control law defined by

$$\kappa_ {f} (x) := \operatorname{sat} (K x)$$

Then, as shown in Kim, Yoon, Jadbabaie, and Persis (2004), there exists a $\lambda > 0$ such that $V _ { f } ( \cdot )$ defined by
