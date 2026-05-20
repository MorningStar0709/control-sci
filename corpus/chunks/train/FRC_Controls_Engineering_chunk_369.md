# Angular velocity constant $K _ { v }$

Recall equation (12.1).

$$V = I R + \frac {\omega}{K _ {v}}V - I R = \frac {\omega}{K _ {v}}K _ {v} = \frac {\omega}{V - I R}$$

When the motor is spinning under no load,

$$K _ {v} = \frac {\omega_ {f r e e}}{V - I _ {f r e e} R} \tag {12.6}$$

where $\omega _ { f r e e }$ is the angular velocity of the motor under no load (also known as the free speed), and V is the voltage applied to the motor when it’s spinning at $\omega _ { f r e e }$ , and $I _ { f r e e }$ is the current drawn by the motor under no load.

![](image/17f41493f4303909e204a8e847d3cd833fae4da5ef902c1008a936e9f1e90507.jpg)

To model a mechanism with several identical motors in one gearbox, multiply the stall torque, stall current, and free current by the number of motors N. $K _ { t }$ and $K _ { v }$ will be the same because N cancels out, but R will be divided by N. This multiplies the acceleration contribution of each model term by N.
