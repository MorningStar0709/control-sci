# Mathematical Model

We developed the mathematical modeling equations of the solenoid actuator–valve system in Chapters 2, 3, and 5. The complete modeling equations are

$$L (x) \dot {I} + R I = e _ {\text { in }} (t) - L _ {x} I \dot {x} \tag {11.9}m \ddot {x} + b \dot {x} + F _ {\text { dry }} \operatorname{sgn} (\dot {x}) + k x = F _ {\mathrm{em}} - F _ {\mathrm{PL}} + F _ {C} \tag {11.10}$$

Recall that the coil current is I, resistance is R, $e _ { \mathrm { i n } } ( t )$ is the input voltage, and coil inductance is L. The mechanical system is composed of armature–valve mass m, x is the position of m, b is the viscous friction coefficient, k is the return spring constant, $F _ { \mathrm { e m } }$ is the electromagnetic force from the solenoid coil, $F _ { \mathrm { P L } }$ is the preload force in the spring, and $F _ { C }$ is the wall-contact force when the mass is seated. If the mathematical model of the solenoid is unclear, the reader may want to review Example 2.5, Section 3.5, and Example 5.3.

Note that we have assumed that the coil inductance L(x) is a function of armature position x. Inductance L increases as the armature moves toward the center of the coil, which is evident in the accepted modeling equation for solenoid inductance [3, 4]

$$L (x) = \frac {c}{d - x} = \frac {L _ {0}}{1 - x / d} \tag {11.11}$$

Because armature displacement x is measured positive to the right from the seated position (see Fig. 11.13), inductance is minimum when $x = 0 .$ . The constants c and d depend on geometry and material properties of the solenoid coil, such as the number of coil turns N, area of the air gap A, coil length l, and magnetic permeabilities of air and the iron core $\mu .$ . The inductance when x = 0 is

$$L _ {0} = \frac {\mu A N ^ {2}}{l} \tag {11.12}$$

Recall that in Chapter 3 we derived the “back-emf ” voltage $e _ { b }$ due to motion of the armature mass relative to the coil by taking the time derivative of the magnetic flux, $\lambda = L ( x ) I$ , which resulted in

$$e _ {b} = L _ {x} I \dot {x} = \frac {d L}{d x} I \dot {x} \tag {11.13}$$

Table 11.2 Parameters for the Solenoid Actuator
