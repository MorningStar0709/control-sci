Definitions of Transient-Response Specifications. Frequently, the performance characteristics of a control system are specified in terms of the transient response to a unit-step input, since it is easy to generate and is sufficiently drastic. (If the response to a step input is known, it is mathematically possible to compute the response to any input.)

The transient response of a system to a unit-step input depends on the initial conditions. For convenience in comparing transient responses of various systems, it is a common practice to use the standard initial condition that the system is at rest initially with the output and all time derivatives thereof zero. Then the response characteristics of many systems can be easily compared.

The transient response of a practical control system often exhibits damped oscillations before reaching steady state. In specifying the transient-response characteristics of a control system to a unit-step input, it is common to specify the following:

1. Delay time, $t _ { d }$   
2. Rise time, $t _ { r }$

3. Peak time, $t _ { p }$   
4. Maximum overshoot, $M _ { p }$   
5. Settling time, $t _ { s }$

These specifications are defined in what follows and are shown graphically in Figure 5–8.

1. Delay time, $t _ { d } \mathrm { . }$ : The delay time is the time required for the response to reach half the final value the very first time.   
2. Rise time, $t _ { r } \colon$ The rise time is the time required for the response to rise from 10% to 90%, 5% to 95%, or 0% to 100% of its final value. For underdamped secondorder systems, the 0% to 100% rise time is normally used. For overdamped systems, the 10% to 90% rise time is commonly used.   
3. Peak time, $t _ { p } \colon$ The peak time is the time required for the response to reach the first peak of the overshoot.   
4. Maximum (percent) overshoot, $M _ { p } ;$ : The maximum overshoot is the maximum peak value of the response curve measured from unity. If the final steady-state value of the response differs from unity, then it is common to use the maximum percent overshoot. It is defined by

$$\text { Maximum percent overshoot} = \frac {c (t _ {p}) - c (\infty)}{c (\infty)} \times 100 \%$$

The amount of the maximum (percent) overshoot directly indicates the relative stability of the system.
