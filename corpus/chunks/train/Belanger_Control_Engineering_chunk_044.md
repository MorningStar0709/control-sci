$$
\begin{array}{l} \dot {x} = v \\ \dot {\theta} = \omega \\ \dot {v} = \frac {F + \omega^ {2} \sin \theta - 9 . 8 \sin \theta \cos \theta}{2 - \cos^ {2} \theta} \\ \dot {\omega} = \frac {- F \cos \theta - \omega^ {2} \sin \theta \cos \theta + 1 9 . 6 \sin \theta}{2 - \cos^ {2} \theta}. \tag {2.40} \\ \end{array}
$$

The simulation conditions are as follows: $x(0) = v(0) = \omega(0) = 0$ , $\theta(0) = 0.1$ rad, $F(t) = 0$ , $0 \leq t \leq 1$ s. Figure 2.14 shows the results (MATLAB command ode23). This system is seen to be unstable. The pendulum falls to the right ( $\theta > 0$ ) while the cart goes to the left.

![](image/5eafb244bc8dfec9769d550644ed300b26d64f14a502e5b0c2485d9ab922b47c.jpg)

<details>
<summary>line</summary>

| Time(s) | θ (rad) | x (m) |
| --- | --- | --- |
| 0.0 | 0.0 | 0.0 |
| 0.1 | 0.1 | -0.1 |
| 0.2 | 0.2 | -0.2 |
| 0.3 | 0.3 | -0.3 |
| 0.4 | 0.4 | -0.4 |
| 0.5 | 0.5 | -0.5 |
| 0.6 | 0.6 | -0.6 |
| 0.7 | 0.7 | -0.7 |
| 0.8 | 0.8 | -0.8 |
| 0.9 | 0.9 | -0.9 |
| 1.0 | 1.0 | -1.0 |
</details>

Figure 2.14 Pendulum angle and cart distance from a nonzero initial state
