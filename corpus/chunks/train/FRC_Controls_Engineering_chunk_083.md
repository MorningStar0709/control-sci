# 2.6 Manual tuning

These steps apply to position PID controllers. Velocity PID controllers typically don’t need $K _ { d }$ .

1. Set $K _ { p } , K _ { i }$ , and $K _ { d }$ to zero.   
2. Increase $K _ { p }$ until the output starts to oscillate around the setpoint.   
3. Increase $K _ { d }$ as much as possible without introducing jittering in the system response.

If the setpoint follows a trapezoid profile (see section 15.1), tuning becomes a lot easier. Plot the position setpoint, velocity setpoint, measured position, and measured velocity. The velocity setpoint can be obtained via numerical differentiation of the position setpoint (i.e., $\begin{array} { r } { { v _ { d e s i r e d , k } } \ = \ \frac { r _ { k } - r _ { k - 1 } } { \Delta t } ) } \end{array}$ . Increase $K _ { p }$ until the position tracks well, then increase $K _ { d }$ until the velocity tracks well.

If the controller settles at an output above or below the setpoint, one can increase $K _ { i }$ such that the controller reaches the setpoint in a reasonable amount of time.

![](image/f19de0f85e453ee21d0e7bc5c4d0c5ee45df0b010ab4f3b9134225a847ca44be.jpg)

If a model is available (not the case here with output-based control), prefer a feedforward (section 7.8) or an integrator in the plant (section 6.7) instead of an integrator in the controller (e.g., the I term in PID). Use integrators only to compensate for unmodelable dynamics.

Beware that if $K _ { i }$ is too large, integral windup can occur. Following a large change in setpoint, the integral term can accumulate an error larger than the maximal control input. As a result, the system overshoots and continues to increase until this accumulated error is unwound.
