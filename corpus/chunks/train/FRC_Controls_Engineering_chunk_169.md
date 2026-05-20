# 6.11.3 Gravity feedforward

Input voltage is proportional to torque and gravity is a constant force, but the torque applied against the motor varies according to the arm’s angle. We’ll use sum of torques to find a compensating torque.

We’ll model gravity as an acceleration disturbance $- g .$ . To compensate for it, we want to find a torque that is equal and opposite to the torque applied to the arm by gravity. The bottom row of the continuous elevator model contains the angular acceleration terms, so $B u _ { f f }$ is angular acceleration caused by the motor; $J B u _ { f f }$ is the torque.

$$
\begin{array}{l} J B u _ {f f} = - (\mathbf {r} \times \mathbf {F}) \\ J B u _ {f f} = - (r F \cos \theta) \\ \end{array}
$$

Torque is usually written as $r F$ sin θ where θ is the angle between the r and F vectors, but θ in this case is being measured from the horizontal axis rather than the vertical one, so the force vector is $\frac { \pi } { 4 }$ radians out of phase. Thus, an angle of 0 results in the maximum torque from gravity being applied rather than the minimum.

The force of gravity mg is applied at the center of the arm’s mass. For a uniform beam, this is halfway down its length, or $\begin{array} { l } { { \frac { L } { 2 } } } \end{array}$ where L is the length of the arm.

$$
J B u _ {f f} = - \left(\left(\frac {L}{2}\right) (- m g) \cos \theta\right)J B u _ {f f} = m g \frac {L}{2} \cos \thetaB = \frac {G K _ {t}}{R J}, \mathrm{so}
\begin{array}{l} J \frac {G K _ {t}}{R J} u _ {f f} = m g \frac {L}{2} \cos \theta \\ u _ {f f} = \frac {R J}{J G K _ {t}} m g \frac {L}{2} \cos \theta \\ u _ {f f} = \frac {L}{2} \frac {R m g}{G K _ {t}} \cos \theta \\ \end{array}
$$

$\begin{array} { l } { { \frac { L } { 2 } } } \end{array}$ can be adjusted according to the location of the $\mathrm { a r m } ^ { \prime } \mathrm { s }$ center of mass.
