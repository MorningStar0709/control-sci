# Solenoid–Actuator Design

Our objective is to select the strength of the electromagnet and stiffness of the mechanical spring in order to achieve the fastest possible response of the solenoid. For this solenoid design, we require a constant 2-mm displacement of the armature–valve mass when we supply the coil with a 12-V step input voltage. This scenario defines our expected nominal operation of the solenoid.

As previously stated, the number of coil turns N and spring constant k are the free design variables. We begin our analysis by observing the steady-state conditions of the solenoid actuator after the valve has reached x = 2 mm. Equation (11.10) shows that when the armature–valve mass reaches static equilibrium $( \ddot { x } = \dot { x } = 0 )$ , the total spring force must balance the electromagnetic force, or

$$k \bar {x} + F _ {\mathrm{PL}} = \overline {{F}} _ {\mathrm{em}} \tag {11.17}$$

where x is the required steady-state stroke of the armature $( { \overline { { x } } } = 2 \operatorname { m m } )$ and $\overline { { F } } _ { \mathrm { e m } }$ is the steady-state electromagnetic force. The reader should note that the wall-contact force $F _ { C }$ is zero because the armature has been pulled off its seat. Equation (11.15) shows that the steady-state electromagnetic force depends on the steady-state coil current $\bar { I } { : }$

$$\overline {{F}} _ {\mathrm{em}} = \frac {1}{2} K \bar {I} ^ {2} \tag {11.18}$$

Steady-state current can be determined from the mathematical model of the coil. Equation (11.9) shows that when the actuator reaches static equilibrium $( \dot { I } = \dot { x } = 0 )$ , the mathematical model of the solenoid coil is reduced to Ohm’s law:

$$R \bar {I} = e _ {\text { in }} (t) \tag {11.19}$$

Because the step input voltage is $e _ { \mathrm { i n } } ( t ) = 1 2  { \mathrm { V } }$ and $R = 3 \Omega$ , the steady-state current is $\overline { { I } } = 4 \mathrm { A }$ . Finally, the steady-state electromagnetic force equation (11.18) can be expanded by substituting Eq. (11.14) for

$K = d L / d x$ and Eq. (11.12) for $L _ { 0 }$ . The result is

$$\overline {{F}} _ {\mathrm{em}} = \frac {\mu A N ^ {2} \overline {{I}} ^ {2}}{2 d l (1 - x _ {\mathrm{nom}} / d) ^ {2}} \tag {11.20}$$

where $x _ { \mathrm { { n o m } } } = 1$ mm is the nominal displacement required for the computation of the constant $K = d L / d x$ Every parameter in Eq. (11.20) is fixed (see Table 11.2) except the number of turns N.
