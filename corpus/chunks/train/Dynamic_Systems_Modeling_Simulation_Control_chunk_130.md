The coil inductance of a solenoid actuator is a nonlinear function of the armature position. Inductance (and hence magnetic flux) decreases the farther the armature is moved out of the coil and increases the closer the armature is drawn into the center of the coil. Figure 3.22 shows the solenoid actuator–valve system from Example 2.1 (recall that we derived the mechanical model for this system in Chapter 2). Note that Fig. 3.22 shows a push-type solenoid where energizing the coil draws the armature toward the center of the coil and therefore pushing the valve to the right. One accepted method for modeling the coil inductance is to use the nonlinear expression [1, 2]

$$L (x) = \frac {c}{d - x} = \frac {L _ {0}}{1 - (x / d)} \tag {3.91}$$

where x is the armature displacement (measured positive to the right from the seated position; see Fig. 3.22). The constants c and d depend on the geometry and material properties of the solenoid coil. Note that coil inductance $L ( x )$ is minimum when x = 0 (seated armature) and increases when x > 0 and the armature moves to the right to close the air gap. The inductance when x = 0 is

$$L _ {0} = \frac {\mu A N ^ {2}}{l} \tag {3.92}$$

where N is the number of turns of the coil, A is the area of the air gap, l is the coil length, and ?? is the magnetic permeabilities of air and the iron core. The minimum coil inductance $L _ { 0 }$ is a known constant given the values for A, N, l, and ??.

Figure 3.23 shows a schematic diagram of the solenoid actuator. The armature circuit (coil) is composed of the voltage source $e _ { \mathrm { i n } } ( t )$ , armature coil inductance L(x), and armature resistance R. A single lumped mass m represents the sum of the armature (plunger) and the load (valve) masses. The energized solenoid coil produces the electromagnetic force $F _ { \mathrm { e m } }$ that pushes on mass m to the right. Displacement of the mass is x (positive to the right), and the return spring k and viscous friction b act on the armature–valve mass m.

As with the DC motor, we develop the complete mathematical model of the solenoid actuator by applying Kirchhoff’s laws to the armature circuit and Newton’s laws to the single inertia element. To begin, we apply Kirchhoff’s voltage law around the loop

$$- e _ {R} - e _ {L} + e _ {\text { in }} (t) = 0 \tag {3.93}$$

![](image/3956b3a299a6d364f63998fa9d76d1e4d56e4701b6d86f41ab02439955119ad2.jpg)  
Figure 3.23 Schematic diagram of a solenoid actuator.
