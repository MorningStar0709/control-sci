# Signal Normalization

Various modifications of the adaptive algorithm are discussed in more detail in Chapter 11. Therefore only a few sketchy remarks are given here. Notice that Theorem 6.8 gives stability conditions for adaptive control applied to the model (6.86), when v is a bounded disturbance. Unmodeled dynamics can, of course, be modeled by Eq. (6.86), but v will no longer be bounded, since it depends on the inputs and outputs. By introducing the signal defined by

$$C r (t) = \max \left(| u (t) |, | y (t) |\right)$$

where $C$ is a stable filter, and introducing the normalized signals

$$\tilde {y} = \frac {y}{r}, \quad \tilde {u} = \frac {u}{r}, \quad \tilde {v} = \frac {v}{r}$$

the model of Eq. (6.86) can be replaced by

$$A \tilde {y} = B \tilde {u} + \tilde {v}$$

where $\bar{v}$ is now bounded. By invoking Theorem 6.8, it can be established that adaptive control with a dead zone or projection gives a system with bounded signals. The detailed justification is complicated.
