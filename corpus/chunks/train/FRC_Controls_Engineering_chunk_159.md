# 6.10.2 Model augmentation

As per subsection 6.7.2, we will now augment the model so a $u _ { e r r o r } $ state is added to the control input.

The plant and observer augmentations should be performed before the model is discretized. After the controller gain is computed with the unaugmented discrete model, the controller may be augmented. Therefore, the plant and observer augmentations assume a continuous model and the controller augmentation assumes a discrete con-

![](image/c001aad59814dc1fc589d416a82c16bda41f06ec6f4b22e125378292aa391065.jpg)

<details>
<summary>line</summary>

| Time (s) | Angular velocity (rad/s) - Reference | Angular velocity (rad/s) - State | Voltage (V) - Input |
| --- | --- | --- | --- |
| 0 | 900 | 0 | 12 |
| 1 | 900 | 900 | 4 |
| 5 | 900 | 900 | 4 |
| 6 | 0 | 0 | -12 |
| 10 | 0 | 0 | 0 |
</details>

Figure 6.5: Flywheel response

troller.

$$
\mathbf {x} = \left[ \begin{array}{c} \omega \\ u _ {e r r o r} \end{array} \right] \quad \mathbf {y} = \omega \quad \mathbf {u} = V

\mathbf {A} _ {a u g} = \left[ \begin{array}{l l} \mathbf {A} & \mathbf {B} \\ 0 & 0 \end{array} \right] \quad \mathbf {B} _ {a u g} = \left[ \begin{array}{l} \mathbf {B} \\ 0 \end{array} \right] \quad \mathbf {C} _ {a u g} = \left[ \begin{array}{l l} \mathbf {C} & 0 \end{array} \right] \quad \mathbf {D} _ {a u g} = \mathbf {D} \tag {6.17}

\mathbf {K} _ {a u g} = \left[ \begin{array}{l l} \mathbf {K} & 1 \end{array} \right] \quad \mathbf {r} _ {a u g} = \left[ \begin{array}{l} \mathbf {r} \\ 0 \end{array} \right] \tag {6.18}
$$

This will compensate for unmodeled dynamics such as projectiles slowing down the flywheel.
