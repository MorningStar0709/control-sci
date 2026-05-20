# 5.5 Offset-Free MPC

We are now in a position to give a more realistic solution to the problem of offset-free MPC, briefly introduced in Chapter 2 in a deterministic context. Suppose the system to be controlled is described by

$$
\begin{array}{l} x ^ {+} = A x + B _ {d} d + B u + w _ {x} \\ y = C x + C _ {d} d + v \\ r = H y \quad \tilde {r} = r - \bar {r} \\ \end{array}
$$

where $w _ { x }$ and ν are unknown bounded disturbances taking values, respectively, in the compact sets $\mathbb { W } _ { x }$ and N containing the origin in their interiors. We assume d is constant, or almost constant, but unknown, and models an additive disturbance; $\gamma = C x + C _ { d } d$ is the output of the system being controlled, r is the controlled variable and $\bar { r }$ is its setpoint. The variable $\tilde { r }$ is the tracking error that we wish to minimize. We assume, for purposes of determining a control, that d satisfies

$$d ^ {+} = d + w _ {d}$$

where $w _ { d }$ is a bounded disturbance taking values in the compact set $\mathbb { W } _ { d } ;$ in practice d is bounded although this is not implied by our model.
