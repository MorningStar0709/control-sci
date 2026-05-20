# Example 7.8

Figure 7.20 shows a one degree-of-freedom (1-DOF) rotational mechanical system that possesses stiffness and friction elements. If the system is initially at rest, $\theta ( 0 ) = { \dot { \theta } } ( 0 ) = 0$ , and the input torque is a step function $T _ { \mathrm { i n } } ( t ) =$ 2.5U(t) N-m, sketch the angular response ??(t) of the mechanical system and note the important response criteria.

The system has inertia $J = 0 . 2 \mathrm { k g } – \mathrm { m } ^ { 2 }$ , viscous friction coefficient $b = 1 . 6 \mathrm { N - m - s / r a d }$ , and torsional spring constant $k = 6 5 \mathrm { N } \mathrm { - m } / \mathrm { r a d }$ . Therefore, the mathematical model is

$$0. 2 \ddot {\theta} + 1. 6 \dot {\theta} + 6 5 \theta = T _ {\mathrm{in}} (t) \tag {7.81}$$

![](image/bc4418c57674cf02f0a9960b82495f4c2e4a372779553188ae8cca449dd18622.jpg)

<details>
<summary>text_image</summary>

Tin(t) = 2.5U(t) N-m
J = 0.2 kg-m²
Flexible shaft,
k = 65 N-m/rad
θ
</details>

$\mathsf { F r i c t i o n } , b = 1 . 6 \mathrm { N } \mathrm { - m } \mathrm { - s } / \mathrm { r a d }$   
Figure 7.20 1-DOF rotational mechanical system for Example 7.8.

First, we rewrite the modeling equation (7.81) in our standard form by dividing by moment of inertia $J = 0 . 2 \mathrm { k g } – \mathrm { m } ^ { 2 }$ in order to have a unity coefficient on angular acceleration

$$\ddot {\theta} + 8 \dot {\theta} + 3 2 5 \theta = 5 T _ {\mathrm{in}} (t) \tag {7.82}$$

Comparing Eq. (7.82) to the standard form of a second-order system Eq. (7.66), we can compute the undamped natural frequency

$$\omega_ {n} = \sqrt {3 2 5} = 1 8. 0 2 7 8 \mathrm{rad/s}$$

The damping ratio is computed from the term involving angular velocity

$$2 \zeta \omega_ {n} = 8 \quad \mathrm{or} \quad \zeta = 0. 2 2 1 9$$

Because damping ratio $\zeta < 1$ , we can use the performance equations in Table 7.4, which pertain only to an underdamped second-order system (the reader should note that if damping ratio is computed to be greater than or equal to unity, then the performance equations contained in Table 7.4 do not apply and cannot be used).

Using the two parameters $\zeta$ and $\omega _ { n }$ , the important response characteristics are computed as follows:

Peak time: $t _ { p } = { \frac { \pi } { \omega _ { n } { \sqrt { 1 - \zeta ^ { 2 } } } } } = 0 . 1 7 8 7$

Maximum overshoot: $M _ { \mathrm { o s } } = e ^ { - \zeta \pi / \sqrt { 1 - \zeta ^ { 2 } } } = 0 . 4 8 9 3 ~ ( 4 8 . 9 3 \% \ \mathrm { o v e r s h o o t } )$

Settling time: tS = $t _ { S } = \frac { 4 } { \zeta \omega _ { n } } = 1 . 0 ~ \mathrm { s }$ ????
