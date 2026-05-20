# 9.5.2 The PD Controller

A common special case of the PID controller is when we turn o the integration function by setting $K _ { I } = 0 .$ . In this case the $^ { 6 6 } \mathrm { P D } ^ { \prime }$ controller becomes

$$C (s) = K _ {D} \left(s ^ {2} + \frac {K _ {P}}{K _ {D}} s + \frac {0}{K _ {D}}\right) \frac {1}{s}C (s) = K _ {D} \left(s ^ {2} + \frac {K _ {P}}{K _ {D}} s\right) \frac {1}{s} = K _ {D} \left(s + \frac {K _ {P}}{K _ {D}}\right)$$

We solve for $K _ { P }$ as above. Thus the PD controller has no pole at the origin (does not increase system type), and has only one zero to place.
