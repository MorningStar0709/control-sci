# Example 9.12

Compute the control eort for step input for the system consisting of controller, $C ( s )$ and plant, $P ( s )$ :

$$C (s) = \frac {k (s + 2)}{s (s + 2 0)} \quad P (s) = \frac {0 . 5}{(s + 0 . 5)} \quad H (s) = 1$$

for three gains:

$$k = [ 0. 5, 5, 1 0 0 ]$$

Using scilab we will plot the closed loop system step response for the input X(s) = 1/s (the unit step):

$$Y (s) = X (s) \frac {C (s) P (s)}{1 + C (s) P (s)}$$

and control eort:

$$U (s) = X (s) \frac {C (s)}{1 + C (s) P (s)}$$

![](image/5c0d5c983db0f7c828b85948262d25d67e1ab3747c2cac1b3cf1e1a8c03b9a84.jpg)

<table><tr><td rowspan="2">The responses are colored as follows:</td><td>k</td><td>0.5</td><td>5</td><td>100</td></tr><tr><td>color</td><td>blue</td><td>green</td><td>red</td></tr></table>

The highest gain (red) has a much faster response than the lowest gain (blue) but note how much higher is the control eort. If for example, our maximum actuator capability is 1.5 units, we would have to limit our gain to something like $k = 5$ (noting that the green line stays below that level), and expect correspondingly slower step response.
