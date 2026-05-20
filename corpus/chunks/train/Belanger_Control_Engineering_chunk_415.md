<details>
<summary>line</summary>

| Time(s) | Spring, coupler 1 | Spring, coupler 2 | Damper, coupler 1 |
| --- | --- | --- | --- |
| 0 | 8000 | 4000 | -6000 |
| 5 | 6000 | 4000 | -2000 |
| 10 | 5000 | 4000 | 0 |
| 15 | 5000 | 4000 | 0 |
| 20 | 5000 | 4000 | 0 |
| 25 | 5000 | 4000 | 0 |
| 30 | 5000 | 4000 | 0 |
</details>

Figure 7.19 LQ control of train motion, final solution: Traction force, desired and actual (dotted) velocity coupler forces

To ascertain the controllability of that mode, we use the eigenvector test,

$$
[ \mathbf {w} _ {i} ^ {T} \quad 0 ] \left[ \begin{array}{c} B \\ 0 \end{array} \right] = \mathbf {w} _ {i} ^ {T} B \neq 0
$$

because of the controllability assumption. The eigenvectors corresponding to the $m$ eigenvalues at $s = 0$ satisfy

$$
[ \mathbf {w} _ {i 1} ^ {T} \quad \mathbf {w} _ {i 2} ^ {T} ] \left[ \begin{array}{l l} A & 0 \\ C & 0 \end{array} \right] = 0
$$

or

$$
[ \mathbf {w} _ {i 1} ^ {T} \quad \mathbf {w} _ {i 2} ^ {T} ] \left[ \begin{array}{c} A \\ C \end{array} \right] = 0. \tag {7.50}
$$

Suppose a mode $s = 0$ is not controllable. Then, by the eigenvector test,

$$
[ \mathbf {w} _ {i 1} ^ {T} \quad \mathbf {w} _ {i 2} ^ {T} ] \left[ \begin{array}{l} B \\ 0 \end{array} \right] = 0. \tag {7.51}
$$

Putting together Equations 7.50 and 7.51,

$$
\left[ \mathbf {w} _ {i 1} ^ {T} \quad \mathbf {w} _ {i 2} ^ {T} \right] \left[ \begin{array}{l l} A & B \\ C & 0 \end{array} \right] = 0. \tag {7.52}
$$

This is equivalent to $\left[\begin{array}{cc}A & B\\ c & 0\end{array}\right]$ having rank deficiency, which, from Chapter 3, is equivalent to the condition for a transmission zero at $s = 0$ . Conversely, if Equation 7.52 is satisfied, so are Equations 7.50 and 7.51; this shows that the existence of a transmission zero at $s = 0$ implies the existence of an uncontrollable mode.

With this controllability result in hand, we can now assert that the system of Equation 7.49 can be stabilized by state feedback, given the assumptions of Theorem 7.7. Let

$$
\mathbf {u} = \mathbf {u} _ {f} - [ K _ {x} \quad K _ {z} ] \left[ \begin{array}{c} \mathbf {x} \\ \mathbf {z} \end{array} \right]
$$

where $u_{f}$ is a feedforward term linearly dependent on $y_{d}$ and possibly on w. We assume that the gain $[K_{x} - K_{z}]$ is stabilizing. In the dc steady state,
