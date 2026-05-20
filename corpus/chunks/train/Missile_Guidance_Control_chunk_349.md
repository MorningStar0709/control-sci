where $u _ { 1 } ( t )$ is the control along the x-axis and $u _ { 2 } ( t )$ along the y-axis. Here we note that the assumption $b = 0$ implies that we have a missile that can exert unlimited control, as evidenced from (4.166). If we assume that the LOS angle is small, then the control $u _ { 1 } ( t )$ is 0, implying that this component is along the thrust. After some algebra, the final guidance law reduces to

$$\mathbf {u} (t) = u _ {2} (t) = 3 \left(\frac {d R}{d t}\right) \left(\frac {d \lambda}{d t}\right), \tag {4.167}$$

where d $R / d t$ is the missile closing velocity $( \mathrm { i } . \mathrm { e } . , v _ { c } )$ . This is the desired result, and it will be recognized as the proportional navigation guidance law with the effective navigation ratio $N ^ { \prime } { = } 3$ . In practice, navigation ratios of 4 and 5 are commonly used, based on classical control theory analysis.

In general, the missile commanded acceleration normal to the reference LOS is constrained by the inequality

$$\left| u _ {c} \right| \leq u _ {\max}. \tag {4.168}$$

The above discussion can be extended for the case in which one wishes to compute the minimum time in intercepting the target. This leads to a nonlinear, two-point boundary value problem (TPBVP) in the calculus of variations and Pontryagin’s minimum time principle. For more details the reader is referred to [27].

The most important nonlinear characteristic associated with the airframe is acceleration saturation, which occurs when the missile attempts to pull a large angle of attack. As discussed in Chapter 3, it is desirable to avoid a large angle of attack, since the associated drag results in a rapid loss of missile velocity. Moreover, there is also the airframe structural limit, which must not be exceeded. Consequently, it is a common practice by missile designers to limit the commanded lateral acceleration, in order to prevent both angle-of-attack saturation and structural failure. Autopilot command limiting is assumed to be the dominant nonlinear effect, while all other nonlinear characteristics such as actuator angle and angle rate limiting, and aerodynamic nonlinearities are assumed to be secondary. Therefore, the resulting model is simple and generally applicable to a wide range of missile systems, and captures what is known to be a dominant nonlinear system characteristic and an important factor in miss distance performance, that is, lateral acceleration saturation.
