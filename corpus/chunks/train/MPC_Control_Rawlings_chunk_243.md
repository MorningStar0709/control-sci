# 2.4.8 Time-Varying Systems

Most of the control problems discussed in this book are time invariant. Time-varying problems do arise in practice, however, even if the system being controlled is time invariant. One example occurs when an observer or filter is used to estimate the state of the system being controlled since bounds on the state estimation error are often time varying. In the deterministic case, for example, state estimation error decays exponentially to zero. In this section, which may be omitted in the first reading, we show how MPC may be employed for time-varying systems.

The problem. The time-varying nonlinear system is described by

$$x ^ {+} = f (x, u, i)$$

where x is the current state at time i, u the current control, and $x ^ { + }$ the successor state at time i + 1. For each integer i, the function $f ( \cdot , i )$ is assumed to be continuous. The solution of this system at time k given that the initial state is x at time i is denoted by $\phi ( k ; x , i , { \mathbf { u } } )$ ; the solution now depends on both the initial time i and current time k rather than merely on the difference $k - i$ as in the time-invariant case. The cost
