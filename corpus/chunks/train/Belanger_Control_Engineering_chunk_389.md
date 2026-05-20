By Equation 7.26, $\dot{V} \leq 0$ , so $V(t)$ is nonincreasing. Also, since $P \geq 0$ , we have $V \geq 0$ ; $V(t)$ is bounded from below by zero. The shape of $V(t)$ must therefore be as shown in Figure 7.5. $V(t)$ cannot oscillate, because that would require $\dot{V} > 0$ part of the time, and $V$ cannot cross the real axis, because $V \geq 0$ . Thus, $V$ must tend to a constant, so $\dot{V} \to 0$ . From Equation 7.26, if $\dot{V} \to 0$ , then $S^{1/2}\mathbf{x} \to 0$ .

Consider the system

$$
\begin{array}{l} \dot {\mathbf {x}} = A \mathbf {x} \\ \mathbf {y} = S ^ {1 / 2} \mathbf {x}. \\ \end{array}
$$

If $\mathbf{y} \to 0$ as $t \to \infty$ , then either (i) all modes are stable, in which case $\mathbf{x} \to 0$ , or (ii) there are unstable modes, but they are not observable. However, the latter case is excluded by assumption, so $A$ must be stable.

![](image/69255b11dc5be6b0ce24071c258273e77f0f82751bc1b612e96ac1c851eacc89.jpg)

<details>
<summary>line</summary>

| t | V(t) |
| --- | --- |
| 0 | 1.0 |
| 1 | 0.8 |
| 2 | 0.6 |
| 3 | 0.4 |
| 4 | 0.2 |
| 5 | 0.1 |
</details>

Figure 7.5 Time plot for a Lyapunov function
