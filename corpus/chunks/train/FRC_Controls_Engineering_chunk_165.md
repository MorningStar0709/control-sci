There’s one stable open-loop pole at − KtJRK . $- \frac { K _ { t } } { J R K _ { v } }$ Let’s try a simple P controller.

$$\mathbf {u} = \mathbf {K} (\mathbf {r} - \mathbf {x})V = K _ {p} (\omega_ {g o a l} - \omega)$$

Closed-loop models have the form ${ \dot { \mathbf { x } } } = ( \mathbf { A } - \mathbf { B K } ) \mathbf { x } + \mathbf { B K r }$ . Therefore, the closedloop poles are the eigenvalues of A − BK.

$$
\begin{array}{l} \dot {\mathbf {x}} = (\mathbf {A} - \mathbf {B K}) \mathbf {x} + \mathbf {B K r} \\ \dot {\omega} = \left(\left(- \frac {K _ {t}}{J R K _ {v}}\right) - \left(\frac {K _ {t}}{J R}\right) (K _ {p})\right) \omega + \left(\frac {K _ {t}}{J R}\right) (K _ {p}) (\omega_ {g o a l}) \\ \dot {\omega} = - \left(\frac {K _ {t}}{J R K _ {v}} + \frac {K _ {t} K _ {p}}{J R}\right) \omega + \frac {K _ {t} K _ {p}}{J R} \omega_ {g o a l} \\ \end{array}
$$

This closed-loop flywheel model has one pole at $\begin{array} { r } { - \left( \frac { K _ { t } } { J R K _ { v } } + \frac { K _ { t } K _ { p } } { J R } \right) } \end{array}$ It therefore only needs one P controller to place that pole anywhere on the real axis. A derivative term is unnecessary on an ideal flywheel. It may compensate for unmodeled dynamics such as accelerating projectiles slowing the flywheel down, but that effect may also increase recovery time; $K _ { d }$ drives the acceleration to zero in the undesired case of negative acceleration as well as well as the actually desired case of positive acceleration.

This analysis assumes that the motor is well coupled to the mass and that the time constant of the inductor is small enough that it doesn’t factor into the motor equations. The latter is a pretty good assumption for a CIM motor with the following constants: $J =$ $3 . 2 2 8 4 \times 1 0 ^ { - 6 } \ k g { \cdot } m ^ { 2 } , b = 3 . 5 0 7 7 \times 1 0 ^ { - 6 } \ N { \cdot } m { \cdot } s , K _ { e } = K _ { t } = 0 . 0 1 8 1 V / r a d / s$ , $R = 0 . 0 9 0 2 \Omega$ , and $L = 2 3 0 ~ \mu \mathrm { H }$ . Notice the slight wiggle in figure 6.6 compared to figure 6.7. If more mass is added to the motor armature, the response timescales increase and the inductance matters even less.

![](image/ae15546ac4dc1e92f6d8284dbf39f6e8c5472be8ef0548933d7c81f4bc4362ea.jpg)

<details>
<summary>line</summary>

| Time (s) | Reference | Step response |
| --- | --- | --- |
| 0.00 | 1.0 | 0.0 |
| 0.05 | 1.0 | 0.9 |
| 0.10 | 1.0 | 1.0 |
| 0.15 | 1.0 | 1.0 |
| 0.20 | 1.0 | 1.0 |
| 0.25 | 1.0 | 1.0 |
</details>

Figure 6.6: Step response of second-order DC motor plant augmented with position $( L = 2 3 0 \mu \mathrm { H } )$

![](image/bd37b34da7409b802240ac8189c8c4f626f1060c2745cdbe0e44dddad47473d3.jpg)

<details>
<summary>line</summary>

| Time (s) | Reference | Step response |
| --- | --- | --- |
| 0.00 | 1.0 | 0.0 |
| 0.05 | 1.0 | 0.9 |
| 0.10 | 1.0 | 1.0 |
| 0.15 | 1.0 | 1.0 |
| 0.20 | 1.0 | 1.0 |
| 0.25 | 1.0 | 1.0 |
</details>

Figure 6.7: Step response of first-order DC motor plant augmented with position $( L =$ 0 μH)

Subsection 6.7.2 covers a superior compensation method that avoids zeroes in the controller, doesn’t act against the desired control action, and facilitates better tracking.
