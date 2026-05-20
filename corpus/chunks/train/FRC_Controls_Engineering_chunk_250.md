# Encoder position augmentation

Estimation of the global pose can be significantly improved if encoder position measurements are used instead of velocity measurements. By augmenting the plant with the line integral of each wheel’s velocity over time, we can provide a mapping from model states to position measurements. We can augment the linear subspace of the model as follows.

Augment the matrix equation with position states $x _ { l }$ and $x _ { r }$ , which have the model equations ${ \dot { x } } _ { l } = v _ { l }$ and ${ \dot { x } } _ { r } = v _ { r }$ . The matrix elements corresponding to $v _ { l }$ in the first equation and $v _ { r }$ in the second equation will be 1, and the others will be 0 since they don’t appear, so ${ \dot { x } } _ { l } = 1 v _ { l } + 0 v _ { r } + 0 x _ { l } + 0 x _ { r } + 0 V _ { l } + 0 V _ { r }$ and $\dot { x } _ { r } = 0 v _ { l } + 1 v _ { r } +$ $0 x _ { l } + 0 x _ { r } + 0 V _ { l } + 0 V _ { r }$ . The existing rows will have zeroes inserted where $x _ { l }$ and $x _ { r }$ are multiplied in.

$$
\left[ \begin{array}{c} \dot {x _ {l}} \\ x _ {r} \end{array} \right] = \left[ \begin{array}{c c} 1 & 0 \\ 0 & 1 \end{array} \right] \left[ \begin{array}{c} v _ {l} \\ v _ {r} \end{array} \right] + \left[ \begin{array}{c c} 0 & 0 \\ 0 & 0 \end{array} \right] \left[ \begin{array}{c} V _ {l} \\ V _ {r} \end{array} \right]
$$

This produces the following linear subspace over $\mathbf { x } = \left[ v _ { l } \quad v _ { r } \quad x _ { l } \quad x _ { r } \right] ^ { \mathsf { T } }$ .

$$
\mathbf {A} = \left[ \begin{array}{c c c c} \left(\frac {1}{m} + \frac {r _ {b} ^ {2}}{J}\right) C _ {1} & \left(\frac {1}{m} - \frac {r _ {b} ^ {2}}{J}\right) C _ {3} & 0 & 0 \\ \left(\frac {1}{m} - \frac {r _ {b} ^ {2}}{J}\right) C _ {1} & \left(\frac {1}{m} + \frac {r _ {b} ^ {2}}{J}\right) C _ {3} & 0 & 0 \\ 1 & 0 & 0 & 0 \\ 0 & 1 & 0 & 0 \end{array} \right] \tag {8.18}

\mathbf {B} = \left[ \begin{array}{c c} \left(\frac {1}{m} + \frac {r _ {b} ^ {2}}{J}\right) C _ {2} & \left(\frac {1}{m} - \frac {r _ {b} ^ {2}}{J}\right) C _ {4} \\ \left(\frac {1}{m} - \frac {r _ {b} ^ {2}}{J}\right) C _ {2} & \left(\frac {1}{m} + \frac {r _ {b} ^ {2}}{J}\right) C _ {4} \\ 0 & 0 \\ 0 & 0 \end{array} \right] \tag {8.19}
$$

The measurement model for the complete nonlinear model is now $\mathbf { y } = \left[ \theta \quad x _ { l } \quad x _ { r } \right] ^ { \mathsf { T } }$ instead of $\mathbf { y } = \left[ \theta \quad v _ { l } \quad v _ { r } \right] ^ { \mathsf { T } }$ .
