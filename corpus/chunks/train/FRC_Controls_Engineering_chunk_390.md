# 12.6.1 Equations of motion

We want to derive equations for the accelerations of the left and right sides of the robot $\dot { v } _ { l }$ and $\dot { v } _ { r }$ given left and right input voltages $V _ { l }$ and $V _ { r }$ .

From equation (12.16) of the flywheel model derivations

$$\tau = \frac {G K _ {t}}{R} V - \frac {G ^ {2} K _ {t}}{K _ {v} R} \omega \tag {12.28}$$

where $\tau$ is the torque applied by one wheel of the differential drive, G is the gear ratio of the differential drive, $K _ { t }$ is the torque constant of the motor, R is the resistance of the motor, and $K _ { v }$ is the angular velocity constant. Since $\tau = r F$ and $\begin{array} { r } { \omega = \frac { v } { r } } \end{array}$ where v is the velocity of a given drive side along the ground and r is the drive wheel radius

$$(r F) = \frac {G K _ {t}}{R} V - \frac {G ^ {2} K _ {t}}{K _ {v} R} \left(\frac {v}{r}\right)r F = \frac {G K _ {t}}{R} V - \frac {G ^ {2} K _ {t}}{K _ {v} R r} vF = \frac {G K _ {t}}{R r} V - \frac {G ^ {2} K _ {t}}{K _ {v} R r ^ {2}} vF = - \frac {G ^ {2} K _ {t}}{K _ {v} R r ^ {2}} v + \frac {G K _ {t}}{R r} V$$

Therefore, for each side of the robot,

$$F _ {l} = - \frac {G _ {l} ^ {2} K _ {t}}{K _ {v} R r ^ {2}} v _ {l} + \frac {G _ {l} K _ {t}}{R r} V _ {l}F _ {r} = - \frac {G _ {r} ^ {2} K _ {t}}{K _ {v} R r ^ {2}} v _ {r} + \frac {G _ {r} K _ {t}}{R r} V _ {r}$$

where the l and r subscripts denote the side of the robot to which each variable corresponds.

$\begin{array} { r } { \mathrm { L e t } C _ { 1 } = - \frac { G _ { l } ^ { 2 } K _ { t } } { K _ { v } R r ^ { 2 } } , C _ { 2 } = \frac { G _ { l } K _ { t } } { R r } , C _ { 3 } = - \frac { G _ { r } ^ { 2 } K _ { t } } { K _ { v } R r ^ { 2 } } , \mathrm { a n d } C _ { 4 } = \frac { G _ { r } K _ { t } } { R r } . } \end{array}$ G2rKt2 , and C4 = GrKt .

$$F _ {l} = C _ {1} v _ {l} + C _ {2} V _ {l} \tag {12.29}F _ {r} = C _ {3} v _ {r} + C _ {4} V _ {r} \tag {12.30}$$

First, find the sum of forces.

$$\sum F = m aF _ {l} + F _ {r} = m \dot {v}F _ {l} + F _ {r} = m \frac {\dot {v} _ {l} + \dot {v} _ {r}}{2}\frac {2}{m} (F _ {l} + F _ {r}) = \dot {v} _ {l} + \dot {v} _ {r}\dot {v} _ {l} = \frac {2}{m} (F _ {l} + F _ {r}) - \dot {v} _ {r} \tag {12.31}$$

Next, find the sum of torques.

$$\sum \tau = J \dot {\omega}\tau_ {l} + \tau_ {r} = J \left(\frac {\dot {v} _ {r} - \dot {v} _ {l}}{2 r _ {b}}\right)$$

where $r _ { b }$ is the radius of the differential drive.
