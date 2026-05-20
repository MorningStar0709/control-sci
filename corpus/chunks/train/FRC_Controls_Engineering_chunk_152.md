# 6.9.1 Continuous state-space model

Using equation (12.15), the position and velocity derivatives of the elevator can be written as

$$\dot {x} = v \tag {6.5}\dot {v} = - \frac {G ^ {2} K _ {t}}{R r ^ {2} m K _ {v}} v + \frac {G K _ {t}}{R r m} V \tag {6.6}$$

Factor out v and V into column vectors.

$$\left[ \dot {v} \right] = \left[ - \frac {G ^ {2} K _ {t}}{R r ^ {2} m K _ {v}} \right] \left[ v \right] + \left[ \frac {G K _ {t}}{R r m} \right] \left[ V \right]$$

Augment the matrix equation with the position state x, which has the model equation ${ \dot { x } } = v$ . The matrix elements corresponding to v will be 1, and the others will be 0 since they don’t appear, so $\dot { x } = 0 x + 1 v + 0 V$ . The existing rows will have zeroes inserted where x is multiplied in.

$$
{\left[ \begin{array}{l} \dot {x} \\ v \end{array} \right]} = {\left[ \begin{array}{l l} 0 & 1 \\ 0 & - \frac {G ^ {2} K _ {t}}{R r ^ {2} m K _ {v}} \end{array} \right]} {\left[ \begin{array}{l} x \\ v \end{array} \right]} + {\left[ \begin{array}{l} 0 \\ \frac {G K _ {t}}{R r m} \end{array} \right]} [ V ]
$$

Theorem 6.9.1 — Elevator state-space model.

$$
\dot {\mathbf {x}} = \mathbf {A} \mathbf {x} + \mathbf {B} \mathbf {u}\mathbf {y} = \mathbf {C x} + \mathbf {D u}
\mathbf {x} = \left[ \begin{array}{c} x \\ v \end{array} \right] = \left[ \begin{array}{c} \text { position } \\ \text { velocity } \end{array} \right] \quad \mathbf {y} = x = \text { position } \quad \mathbf {u} = V = \text { voltage }

\mathbf {A} = \left[ \begin{array}{c c} 0 & 1 \\ 0 & - \frac {G ^ {2} K _ {t}}{R r ^ {2} m K _ {v}} \end{array} \right] \tag {6.7}

\mathbf {B} = \left[ \begin{array}{c} 0 \\ \frac {G K _ {t}}{R r m} \end{array} \right] \tag {6.8}

\mathbf {C} = \left[ \begin{array}{l l} 1 & 0 \end{array} \right] \tag {6.9}
\mathbf {D} = 0 \tag {6.10}
$$
