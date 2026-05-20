# 6.3.5 Lead-Lag and Proportional-Integral-Derivative Control

Lead-lag compensation is simply a combination of both types of compensation. First a lead compensator is designed to push the bandwidth to some desired value. Then a lag compensator is added to the design to shape the low-frequency portion of the loop gain. The result is a compensator of the form

$$G _ {c} (s) = k \frac {\alpha T _ {1} s + 1}{T _ {1} s + 1} \frac {\beta T _ {2} s + 1}{T _ {2} s + 1} \tag {6.43}$$

where $\alpha < 1$ and $\beta > 1$ .
