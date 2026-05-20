# 11.5.2 Forward kinematics

The mapping from the left and right wheel velocities $v _ { l }$ and $v _ { r }$ to v and $\omega$ is derived as follows.

$$v _ {r} = v _ {c} + \omega r _ {b}v _ {c} = v _ {r} - \omega r _ {b} \tag {11.5}$$

Substitute equation (11.5) equation for $v _ { l }$

$$v _ {l} = v _ {c} - \omega r _ {b}v _ {l} = \left(v _ {r} - \omega r _ {b}\right) - \omega r _ {b}v _ {l} = v _ {r} - 2 \omega r _ {b}2 \omega r _ {b} = v _ {r} - v _ {l}\omega = \frac {v _ {r} - v _ {l}}{2 r _ {b}}$$

Substitute this back into equation (11.5).

$$v _ {c} = v _ {r} - \omega r _ {b}v _ {c} = v _ {r} - \left(\frac {v _ {r} - v _ {l}}{2 r _ {b}}\right) r _ {b}v _ {c} = v _ {r} - \frac {v _ {r} - v _ {l}}{2}v _ {c} = v _ {r} - \frac {v _ {r}}{2} + \frac {v _ {l}}{2}v _ {c} = \frac {v _ {r} + v _ {l}}{2}$$

So the two forward kinematic equations are as follows.

$$v _ {c} = \frac {v _ {r} + v _ {l}}{2} \tag {11.6}\omega = \frac {v _ {r} - v _ {l}}{2 r _ {b}} \tag {11.7}$$
