# 6.11.1 Continuous state-space model

Using equation (12.23), the angle and angular rate derivatives of the arm can be written as

$$\dot {\theta} _ {a r m} = \omega_ {a r m} \tag {6.29}$$

![](image/061fd3bd946be8dae923fa8d0f8b7aea79a443d9f8c77a2079890846976531b9.jpg)

<details>
<summary>text_image</summary>

R
I
V
Vemf
ωm
G
ωarm
m
l
circuit
mechanics
</details>

Figure 6.8: Single-jointed arm system diagram

$$\dot {\omega} _ {a r m} = - \frac {G ^ {2} K _ {t}}{K _ {v} R J} \omega_ {a r m} + \frac {G K _ {t}}{R J} V \tag {6.30}$$

Factor out $\omega _ { a r m }$ and V into column vectors.

$$\left[ \dot {\omega_ {a r m}} \right] = \left[ - \frac {G ^ {2} K _ {t}}{K _ {v} R J} \right] \left[ \omega_ {a r m} \right] + \left[ \frac {G K _ {t}}{R J} \right] \left[ V \right]$$

Augment the matrix equation with the angle state $\theta _ { a r m }$ , which has the model equation $\dot { \theta } _ { a r m } = \omega _ { a r m }$ . The matrix elements corresponding to $\omega _ { a r m }$ will be 1, and the others will be 0 since they don’t appear, so $\dot { \theta } _ { a r m } = 0 \theta _ { a r m } + 1 \omega _ { a r m } + 0 V$ . The existing rows will have zeroes inserted where $\theta _ { a r m }$ is multiplied in.

$$
\left[ \begin{array}{c} \dot {\theta_ {a r m}} \\ \omega_ {a r m} \end{array} \right] = \left[ \begin{array}{c c} 0 & 1 \\ 0 & - \frac {G ^ {2} K _ {t}}{K _ {v} R J} \end{array} \right] \left[ \begin{array}{c} \theta_ {a r m} \\ \omega_ {a r m} \end{array} \right] + \left[ \begin{array}{c} 0 \\ \frac {G K _ {t}}{R J} \end{array} \right] [ V ]
$$

Theorem 6.11.1 — Single-jointed arm state-space model.

$$
\dot {\mathbf {x}} = \mathbf {A} \mathbf {x} + \mathbf {B} \mathbf {u}\mathbf {y} = \mathbf {C x} + \mathbf {D u}
\mathbf {x} = \left[ \begin{array}{c} \theta_ {a r m} \\ \omega_ {a r m} \end{array} \right] = \left[ \begin{array}{c} \text {angle} \\ \text {angular velocity} \end{array} \right] \quad \mathbf {y} = \theta_ {a r m} = \text {angle} \quad \mathbf {u} = V = \text {voltage}

\mathbf {A} = \left[ \begin{array}{c c} 0 & 1 \\ 0 & - \frac {G ^ {2} K _ {t}}{K _ {v} R J} \end{array} \right] \tag {6.31}

\mathbf {B} = \left[ \begin{array}{c} 0 \\ \frac {G K _ {t}}{R J} \end{array} \right] \tag {6.32}

\mathbf {C} = \left[ \begin{array}{l l} 1 & 0 \end{array} \right] \tag {6.33}
\mathbf {D} = 0 \tag {6.34}
$$
