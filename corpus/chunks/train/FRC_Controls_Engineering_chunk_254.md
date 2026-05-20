$$
\mathbf {x} = \left[ \begin{array}{c} x \\ y \\ \theta \end{array} \right] = \left[ \begin{array}{c} \mathrm{xposition} \\ \mathrm{yposition} \\ \text {heading} \end{array} \right] \quad \mathbf {u} = \left[ \begin{array}{c} v \\ \omega \end{array} \right] = \left[ \begin{array}{c} \text {linear velocity} \\ \text {angular velocity} \end{array} \right]

\mathbf {A} = \left. \frac {\partial f (\mathbf {x} , \mathbf {u})}{\partial \mathbf {x}} \right| _ {\theta = 0} = \left[ \begin{array}{c c c} 0 & 0 & 0 \\ 0 & 0 & v \\ 0 & 0 & 0 \end{array} \right]

\mathbf {B} = \left. \frac {\partial f (\mathbf {x} , \mathbf {u})}{\partial \mathbf {u}} \right| _ {\theta = 0} = \left[ \begin{array}{c c} 1 & 0 \\ 0 & 0 \\ 0 & 1 \end{array} \right]
$$

The linear time-varying unicycle controller is

$$
\mathbf {u} = \mathbf {K} \left[ \begin{array}{c c c} \cos \theta & \sin \theta & 0 \\ - \sin \theta & \cos \theta & 0 \\ 0 & 0 & 1 \end{array} \right] (\mathbf {r} - \mathbf {x}) \tag {8.25}
$$

At each timestep, the LQR controller gain K is computed for the (A, B) pair evaluated at the current input.

With the model in theorem 8.8.1, y is uncontrollable at $v = 0$ because nonholonomic drivetrains are unable to move sideways. Some DARE solvers throw errors in this case, but one can avoid it by linearizing the model around a slightly nonzero velocity instead.

The controller in theorem 8.8.1 results in figures 8.10 and 8.11.

![](image/1e7e6d6f458ec3442afdf9507a039baca0d50a95484696ee69a4a88930e0fb7e.jpg)

<details>
<summary>line</summary>

| x (m) | Reference | State |
| --- | --- | --- |
| 1 | 13.0 | 13.5 |
| 2 | 13.5 | 14.0 |
| 4 | 14.5 | 14.8 |
| 6 | 15.5 | 16.0 |
| 8 | 16.5 | 17.0 |
| 10 | 17.5 | 18.0 |
</details>

Figure 8.10: Linear time-varying unicycle controller x-y plot

![](image/5a93b864f7f7fab37a02f200a00430cd267b27129bc9b2ce93822e468dbfc091.jpg)

<details>
<summary>line</summary>
