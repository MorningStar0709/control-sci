# Moment of inertia J

Given the simplicity of this mechanism, it may be easier to compute this value theoretically using material properties in CAD. A procedure for measuring it experimentally is presented below.

First, rearrange equation (12.18) into the form $y \ = \ m x + b$ such that J is in the numerator of $m$ .

$$\dot {\omega} = - \frac {G ^ {2} K _ {t}}{K _ {v} R J} \omega + \frac {G K _ {t}}{R J} VJ \dot {\omega} = - \frac {G ^ {2} K _ {t}}{K _ {v} R} \omega + \frac {G K _ {t}}{R} V$$

Multiply by $\frac { K _ { v } R } { G ^ { 2 } K _ { t } }$ on both sides.

$$\frac {J K _ {v} R}{G ^ {2} K _ {t}} \dot {\omega} = - \omega + \frac {G K _ {t}}{R} \cdot \frac {K _ {v} R}{G ^ {2} K _ {t}} V\frac {J K _ {v} R}{G ^ {2} K _ {t}} \dot {\omega} = - \omega + \frac {K _ {v}}{G} V\omega = - \frac {J K _ {v} R}{G ^ {2} K _ {t}} \dot {\omega} + \frac {K _ {v}}{G} V \tag {12.19}$$

The test procedure is as follows.

1. Run the flywheel forward at a constant voltage. Record the angular velocity over time.   
2. Compute the angular acceleration from the angular velocity data as the difference between each sample divided by the time between them.   
3. Perform a linear regression of angular velocity versus angular acceleration. The slope of this line has the form $- \frac { \smile J K _ { v } R } { G ^ { 2 } K _ { t } }$ as per equation (12.19).   
4. Multiply the slope by $- \frac { G ^ { 2 } K _ { t } } { K _ { v } R }$ t to obtain a least squares estimate of J.
