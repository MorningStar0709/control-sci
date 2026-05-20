If we place the zero and pole of the lag compensator very close to each other, then at $s = s _ { 1 }$ where , $s _ { 1 }$ is one of the dominant closed-loop poles, the magnitudes $s _ { 1 } + ( 1 / T )$ and $s _ { 1 } + \left[ 1 / ( \beta T ) \right]$ are almost equal, or

$$\left| G _ {c} \left(s _ {1}\right) \right| = \left| \hat {K} _ {c} \frac {s _ {1} + \frac {1}{T}}{s _ {1} + \frac {1}{\beta T}} \right| \div \hat {K} _ {c}$$

To make the angle contribution of the lag portion of the compensator small, we require

$$- 5 ^ {\circ} < \left\lfloor \frac {s _ {1} + \frac {1}{T}}{s _ {1} + \frac {1}{\beta T}} < 0 ^ {\circ} \right.$$

This implies that if gain $\hat { K } _ { c }$ of the lag compensator is set equal to 1, the alteration in the transient-response characteristics will be very small, despite the fact that the overall gain of the open-loop transfer function is increased by a factor of $\beta ,$ , where $\beta > 1$ . If the pole and zero are placed very close to the origin, then the value of $\beta$ can be made large. (A large value of $\beta$ may be used, provided physical realization of the lag compensator is possible.) It is noted that the value of $T$ must be large, but its exact value is not critical. However, it should not be too large in order to avoid difficulties in realizing the phase-lag compensator by physical components.

An increase in the gain means an increase in the static error constants. If the openloop transfer function of the uncompensated system is $G ( s )$ , then the static velocity error constant $K _ { v }$ of the uncompensated system is

$$K _ {v} = \lim _ {s \rightarrow 0} s G (s)$$

If the compensator is chosen as given by Equation (6–19), then for the compensated system with the open-loop transfer function $G _ { c } ( s ) G ( s )$ the static velocity error constant $\hat { K } _ { v }$ becomes

$$\hat {K} _ {v} = \lim _ {s \rightarrow 0} s G _ {c} (s) G (s) = \lim _ {s \rightarrow 0} G _ {c} (s) K _ {v} = \hat {K} _ {c} \beta K _ {v}$$

where $K _ { v }$ is the static velocity error constant of the uncompensated system.

Thus if the compensator is given by Equation (6–19), then the static velocity error constant is increased by a factor of $\hat { K } _ { c } \mathbf { \Psi } \cdot \mathbf { \vec { \rho } } _ { \beta }$ where, $\hat { K } _ { c }$ is approximately unity.
