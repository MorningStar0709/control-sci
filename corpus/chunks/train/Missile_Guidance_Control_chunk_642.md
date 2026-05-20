$$\mathbf {V} _ {g} = \mathbf {V} _ {g o} + \int_ {0} ^ {t} \mathbf {V} _ {g} d t, \tag {6.225a}V _ {Z I} = V _ {Z i o} + \int_ {0} ^ {t} \left(\frac {d V _ {Z I}}{d t}\right) d t. \tag {6.225b}$$

Also modeled in the guidance phase of a simulation is a variety of possible pitch $( d \theta _ { c } / d t )$ and yaw $( d \psi _ { c } / d t )$ rate command computations. As outputs from the guidance computer, $\theta _ { c }$ and $\psi _ { c }$ are intended to represent command values of pitch and yaw attitude defined as follows (where $( X _ { M } , Y _ { M } , Z _ { M } )$ are rectangular missile fixed axes of roll $( X _ { M } )$ , pitch $( Y _ { M } )$ , and yaw $( Z _ { M } )$ aligned with the $( X , Y , Z )$ guidance axes when $\theta = \psi = 0 )$ :

θ = pitch angle; rotation of missile $X _ { M }$ (roll) axis from

the guidance X-axis about the guidance Y -axis;

$\psi$ = yaw angle; subsequent rotation of missile $X _ { M }$ (roll) axis from

the guidance XZ-plane about the pitched missile $Z _ { M } \ ( \mathrm { y a w } )$ axis.

The third Euler angle $( \phi$ , roll angle) is not of importance in this simulation and is always considered to be zero. It is assumed that the actual instrumentation of the autopilot will adequately approximate the above definitions of pitch and yaw.

The response of the missile to $\theta _ { c }$ and $\psi _ { c }$ , which closes the guidance loop, is represented on two different ways. During launch recovery, from actual first-stage ignition to the start of guidance control, the values of θ and $\psi$ are given as solutions to second-order differential equations as follows:

$$\frac {d ^ {2} \theta}{d t ^ {2}} = - 2 \zeta \omega_ {n} \left(\frac {d \theta}{d t}\right) - \omega_ {n} ^ {2} [ \theta - (9 0 ^ {\circ} - \alpha_ {X}) ], \tag {6.226a}\frac {d ^ {2} \psi}{d t ^ {2}} = - 2 \zeta \omega_ {n} \left(\frac {d \psi}{d t}\right) - \omega_ {n} ^ {2} \psi , \tag {6.226b}\left| \frac {d ^ {2} \theta}{d t ^ {2}} \right| _ {\max} = \left| \frac {d ^ {2} \psi}{d t ^ {2}} \right| _ {\max} = \kappa_ {\max}, \tag {6.226c}$$
