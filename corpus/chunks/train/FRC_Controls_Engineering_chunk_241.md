# 8.7.3 Linear time-varying model

We can control the drivetrain’s global pose $( x , y , \theta )$ by augmenting the state with x and y. The change in global pose is defined by these three equations.

$$\dot {x} = \frac {v _ {l} + v _ {r}}{2} \cos \theta = \frac {v _ {r}}{2} \cos \theta + \frac {v _ {l}}{2} \cos \theta\dot {y} = \frac {v _ {l} + v _ {r}}{2} \sin \theta = \frac {v _ {r}}{2} \sin \theta + \frac {v _ {l}}{2} \sin \theta\dot {\theta} = \frac {v _ {r} - v _ {l}}{2 r _ {b}} = \frac {v _ {r}}{2 r _ {b}} - \frac {v _ {l}}{2 r _ {b}}$$

This augmented model is a nonlinear vector function where $\mathbf { x } = \left[ x \quad y \quad \theta \quad v _ { l } \quad v _ { r } \right] ^ { \mathsf { T } }$ and $\mathbf { u } = \left[ V _ { l } \quad V _ { r } \right] ^ { \mathsf { T } }$ .

$$
f (\mathbf {x}, \mathbf {u}) =
\left[ \begin{array}{c} \frac {v _ {r}}{2} \cos \theta + \frac {v _ {l}}{2} \cos \theta \\ \frac {v _ {r}}{2} \sin \theta + \frac {v _ {l}}{2} \sin \theta \\ \frac {v _ {r}}{2 r _ {b}} - \frac {v _ {l}}{2 r _ {b}} \\ \left(\frac {1}{m} + \frac {r _ {b} ^ {2}}{J}\right) C _ {1} v _ {l} + \left(\frac {1}{m} - \frac {r _ {b} ^ {2}}{J}\right) C _ {3} v _ {r} + \left(\frac {1}{m} + \frac {r _ {b} ^ {2}}{J}\right) C _ {2} V _ {l} + \left(\frac {1}{m} - \frac {r _ {b} ^ {2}}{J}\right) C _ {4} V _ {r} \\ \left(\frac {1}{m} - \frac {r _ {b} ^ {2}}{J}\right) C _ {1} v _ {l} + \left(\frac {1}{m} + \frac {r _ {b} ^ {2}}{J}\right) C _ {3} v _ {r} + \left(\frac {1}{m} - \frac {r _ {b} ^ {2}}{J}\right) C _ {2} V _ {l} + \left(\frac {1}{m} + \frac {r _ {b} ^ {2}}{J}\right) C _ {4} V _ {r} \end{array} \right] \tag {8.12}
$$

As mentioned in chapter 8, one can approximate a nonlinear system via linearizations around points of interest in the state-space and design controllers for those linearized subspaces. If we sample linearization points progressively closer together, we converge on a control policy for the original nonlinear system. Since the linear plant being controlled varies with time, its controller is called a linear time-varying (LTV) controller.

If we use LQRs for the linearized subspaces, the nonlinear control policy will also be locally optimal. We’ll be taking this approach with a differential drive. To create an LQR, we need to linearize equation (8.12).
