# 2.9.2 Offset-Free MPC

If uncertainty is present, in the form of model error or an unknown constant disturbance, the tracking error $y - r$ may converge to a nonzero constant vector, called the $o f f s e t ,$ rather than to the origin. It is possible to ensure zero offset by augmenting the system with a model of the disturbance.

We therefore assume that the system to be controlled satisfies

$$
\begin{array}{l} x ^ {+} = f (x, u) \\ d ^ {+} = d \\ y = h (x) + d + v \\ \end{array}
$$

in which ν is measurement noise. If we assume, as we do everywhere in this chapter, that the state x is known, then a simple filter may be used to obtain an estimate $\hat { d }$ of the unknown, but constant disturbance $d .$ . The filter is described by

$$\hat {d} ^ {+} = \hat {d} + L (y - h (x) - \hat {d})$$
