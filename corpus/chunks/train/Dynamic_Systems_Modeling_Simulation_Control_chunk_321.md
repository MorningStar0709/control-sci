# Example 6.9

Figure 6.22 shows the solenoid actuator–valve system described in Chapters 2, 3, and 5. Construct an integrated model using Simulink and determine the response of the solenoid coil current I(t) and valve position x(t) for a 10-V constant voltage input $e _ { \mathrm { i n } } ( t )$ applied at time $t = 0 . 0 5 \mathrm { s }$ . The system has zero stored energy at time t = 0.

![](image/ad0dc5cae432ad02eb007b68f4559bb14c72c47b5b19eb3ade02ef5fdd3c22af.jpg)

<details>
<summary>text_image</summary>

Seated position
Coil
Air gap
Supply pressure
Spool valve
Drain
Return spring
Electrical input
Armature (plunger)
Push rod
Fluid flow
</details>

Figure 6.22 Solenoid actuator–valve system for Example 6.9.

Recall that the electromechanical system consists of a solenoid coil circuit and a valve mass constrained by a return spring. For this example, let us assume that the inductance L of the solenoid coil is constant and that the “back-emf” and force coefficient $K ( = d L / d x )$ ) is also constant. Let us also assume that the return spring does not include a preload force and that the armature–valve mass m experiences viscous and dry friction effects. The complete mathematical model of the electromechanical system is

$$L \dot {I} + R I = e _ {\text { in }} (t) - K I \dot {x} \tag {6.29}m \ddot {x} + b \dot {x} + F _ {\text { dry }} \operatorname{sgn} (\dot {x}) + k x = F _ {\mathrm{em}} \tag {6.30}$$

The electromagnetic force $F _ { \mathrm { e m } }$ is a nonlinear function of current, I

$$F _ {\mathrm{em}} = 0. 5 K I ^ {2} \tag {6.31}$$
