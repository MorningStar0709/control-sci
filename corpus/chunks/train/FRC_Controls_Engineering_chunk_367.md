# 12.1.2 Calculating constants

A typical motor’s datasheet should include graphs of the motor’s measured torque and current for different angular velocities for a given voltage applied to the motor. Figure 12.2 is an example. An FRC motor’s datasheet can be found on its vendor’s website.

Torque constant $K _ { t }$

$$\tau = K _ {t} IK _ {t} = \frac {\tau}{I}K _ {t} = \frac {\tau_ {s t a l l}}{I _ {s t a l l}} \tag {12.4}$$

where $\tau _ { s t a l l }$ is the stall torque and $I _ { s t a l l }$ is the stall current of the motor from its datasheet.
