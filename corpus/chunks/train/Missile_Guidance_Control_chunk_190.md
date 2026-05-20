# For stable Airframe:

5. From the gain margin, find the maximum $\omega _ { c r }$ and the “integral break frequency ωi ” $\omega _ { i } \mathbf { \overrightarrow { \Gamma } }$

$$(\omega_ {i} = K _ {9} K _ {1 1} / K _ {8} T _ {1 1}).$$

6. Discard the lags of the gyroscope, actuator, etc. Use a cubic autopilot model of the form

$$\frac {A _ {L}}{A _ {l c}} = \frac {K _ {a} (1 + a _ {1 1} s + a _ {1 2} s ^ {2})}{1 + b _ {1} s + b _ {2} s ^ {2} + b _ {3} s ^ {3}} = \frac {K _ {a} (1 + a _ {1 1} s + a _ {1 2} s ^ {2})}{\left[ 1 + \frac {s}{\omega_ {1}} \right] \left[ 1 + 2 \zeta_ {2} \left(\frac {s}{\omega_ {2}}\right) + \left(\frac {s}{\omega_ {2}}\right) ^ {2} \right]}.$$

7. Fix the parameters of the rate-damping and synthetic stability loops.

8. Calculate the accelerometer loop, which meets the specifications on the dominant frequency $\omega _ { 1 }$ .

9. Check by calculating the coefficients $b _ { 1 } , b _ { 2 }$ , and $b _ { 3 }$ and factoring into poles. A digital-computer program can perform Steps 5–9.

10. Check the structural stability on a digital frequency-response program.
