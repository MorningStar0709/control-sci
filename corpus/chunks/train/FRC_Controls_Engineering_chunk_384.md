# Moment of inertia J

Given the simplicity of this mechanism, it may be easier to compute this value theoretically using material properties in CAD. J can also be approximated as the moment of inertia of a thin rod rotating around one end. Therefore

$$J = \frac {1}{3} m l ^ {2} \tag {12.24}$$

where m is the mass of the arm and l is the length of the arm. Otherwise, a procedure for measuring it experimentally is presented below.

First, rearrange equation (12.23) into the form $y \ = \ m x + b$ such that J is in the numerator of m.

$$\dot {\omega} = - \frac {G ^ {2} K _ {t}}{K _ {v} R J} \omega + \frac {G K _ {t}}{R J} VJ \dot {\omega} = - \frac {G ^ {2} K _ {t}}{K _ {v} R} \omega + \frac {G K _ {t}}{R} V$$

Multiply by $\frac { K _ { v } R } { G ^ { 2 } K _ { t } }$ on both sides.

$$\frac {J K _ {v} R}{G ^ {2} K _ {t}} \dot {\omega} = - \omega + \frac {G K _ {t}}{R} \cdot \frac {K _ {v} R}{G ^ {2} K _ {t}} V\frac {J K _ {v} R}{G ^ {2} K _ {t}} \dot {\omega} = - \omega + \frac {K _ {v}}{G} V\omega = - \frac {J K _ {v} R}{G ^ {2} K _ {t}} \dot {\omega} + \frac {K _ {v}}{G} V \tag {12.25}$$

The test procedure is as follows.

1. Orient the arm such that its axis of rotation is aligned with gravity (i.e., the arm is on its side). This avoids gravity affecting the measurements.

2. Run the arm forward at a constant voltage. Record the angular velocity over time.   
3. Compute the angular acceleration from the angular velocity data as the difference between each sample divided by the time between them.   
4. Perform a linear regression of angular velocity versus angular acceleration. The slope of this line has the form $- \frac { \smile J K _ { v } R } { G ^ { 2 } K _ { t } }$ as per equation (12.25).   
5. Multiply the slope by $- \frac { G ^ { 2 } K _ { t } } { K _ { v } R }$ t to obtain a least squares estimate of J.
