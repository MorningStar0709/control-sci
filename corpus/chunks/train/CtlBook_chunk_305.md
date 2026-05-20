# Rise time, Tr

Rise Time, Tr is dened as the time taken by the step response to reach 90% of the amplitude, A. There is no analytical expression for Rise time based on the pole locations. However, for a range of damping ratios, ζ, we can determine the rise-time, expressed as a constant multiplied by the reciprocal of the systems natural frequency $\omega _ { n } \mathrm { : }$

$$T _ {r} = \frac {1}{\omega_ {n}} F (\zeta) \tag {9.4}$$

where $F ( )$ is an empirical function measured by numerical simulations (Table 9.2). Two curves t to this function are

$$T _ {r} \approx \frac {1}{\omega_ {n}} (1. 7 6 \zeta + 0. 8 2 4) \quad 0. 1 < \zeta < 0. 8 \tag {9.5}$$

and

$$T _ {r} \approx \frac {1}{\omega_ {n}} (2. 2 3 \zeta^ {2} - 0. 7 8 \zeta + 1. 1 2) \tag {9.6}$$

We can use the non-linear equation (eqn 9.6) if more accuracy is required. In practice however, settling time, $T _ { s }$ is a more practical specication for use in design and $T _ { r }$ is less often used.
