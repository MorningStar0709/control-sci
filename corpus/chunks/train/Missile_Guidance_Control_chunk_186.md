The yaw stabilization loop senses yaw rates, which are amplified and applied to a phase-sensitive comparator. The comparator output is then amplified within the damping circuit, which has been set to the proper altitude band gain. The damping circuit also contains suitable structural filtering, which provides suitable frequencyresponse shaping.

The transfer function $G _ { 1 }$ for lateral acceleration of the $c g$ has the same poles as those of $G _ { 3 }$ , plus high-frequency zeros that depend on the tail forces.
(Note that the transfer functions $G _ { 1 }$ and $G _ { 3 }$ correspond to the transfer functions $G _ { l a }$ and $G _ { p r }$ of Section 3.2.1, respectively, and $K _ { 1 }$ corresponds to $K _ { l a }$ of the same section.) Furthermore, $K _ { 1 }$ diminishes with increasing altitude.
At intercept, the missile needs an acceleration capability of at least 4 $g ^ { \prime } \mathbf { s }$ .
Hence, another requirement is that at the maximum altitude and minimum velocity, the available acceleration must be at least 4 $g ^ { \prime } \mathbf { s }$ at an angle of attack (α) of, say, $2 5 ^ { \circ }$ or $3 0 ^ { \circ }$ .
Generally, the largest value of the time constant $\tau ( \tau = \alpha / \dot { \gamma } ;$ ;
see also Section 3.2.1) may be related to this condition.
The transfer function $G _ { 2 }$ for acceleration at the accelerometer is quite similar to $G _ { 1 }$ .
Referring to Figure 3.36, we note that there are three feedback loops, the four actuator servos being represented by a single closed-loop transfer function $G _ { 1 2 }$ .
Since control of acceleration is required, the outermost loop is closed by an accelerometer.
Commonly, the accelerometer is placed well forward of the $c g .$ , probably about half to two-thirds of the distance from the $c g$ to the nose of the missile.
Its sensitive axis is in the direction of pitch axis (i.e., out the right wing).
If the accelerometer is placed at a distance d ahead of the $c g$ , the total acceleration it sees is equal to the acceleration of the $c g$ plus the angular acceleration $( \mathrm { i } .
\mathrm { e } .
, d R / d t$ , where R is the yaw rate) times this distance d.
Therefore, it is clear that if d is positive (that is, the accelerometer is ahead of the $c g )$ , we have from the two instruments (rate gyro and accelerometer) some feedback.
The outer accelerometer loop has the lowest bandwidth of the three loops.
The innermost rate-damping loop is required to damp the response of the bare airframe, which has an underdamped resonance in the stable case (i.e., positive static margin).
In addition, the innermost rate-damping loop has a wide bandwidth for damping the poles of the airframe.
