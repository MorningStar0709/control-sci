# Example 2.4

Consider again the solenoid actuator–valve system shown in Fig. 2.8 and discussed in Example 2.1. Let us assume that Coulomb or dry friction acts on the armature–valve mass along with linear viscous friction. Derive the mathematical model of the mechanical system with this nonlinear friction effect.

Figure 2.14 shows the solenoid actuator with the return spring k, viscous friction coefficient b (due to motion of the spool valve in the hydraulic fluid), and dry friction force (due to sliding motion of the armature in the electric coil). The electromagnetic force $F _ { \mathrm { e m } }$ is the same as in Example 2.1.

Coulomb or dry friction is the kinetic friction force that exists when a mass is sliding relative to an unlubricated flat surface. From basic mechanics, we know that the magnitude of the dry friction force is $F _ { \mathrm { d r y } } = \mu _ { k } N _ { \mathrm { } }$ , where $\mu _ { k }$ is the coefficient of kinetic friction and N is the normal force. Because the dry friction force always opposes the direction of motion, it is usually modeled as $F _ { \mathrm { d r y } } \mathrm { s g n } ( \dot { x } )$ , where the operator “sgn” is the signum function, which returns the sign of its input value. In this case, the input to the signum function is velocity ẋ . Consequently sgn(ẋ ) = 1 when ẋ > 0, sgn(ẋ ) = −1 when ẋ < 0, and sgn(ẋ ) = 0 when ẋ = 0. Figure 2.15 shows the discontinuous nature of the dry friction force, which is clearly a nonlinear function of velocity ẋ .

![](image/9fa70f77fdc0d96e2552b68ef003d1252237f041337d8eb7be6a39de90f5789e.jpg)

<details>
<summary>text_image</summary>

Seated
position
(wall)
x
Electromagnetic
force, Fem
m
k
b
Dry friction
Armature + spool valve
</details>

Figure 2.14 Solenoid actuator with dry friction (Example 2.4).

Figure 2.16 shows the FBD of the mechanical system with the spring, linear damper, dry friction, and electromagnetic forces. The reader should note that the dry friction force $F _ { \mathrm { d r y } } \mathrm { s g n } ( \dot { x } )$ in Fig. 2.16 will always oppose the motion of mass m regardless of the sign of velocity ẋ . Summing all external forces on mass m with the sign convention as positive to the right yields

$$+ \rightarrow \sum F = F _ {\mathrm{em}} - k x - b \dot {x} - F _ {\mathrm{dry}} \mathrm{sgn} (\dot {x}) = m \ddot {x}$$

![](image/812577ddecbca403e69b234de8e26a2c2844d189b14278d7ed547d3c9d1df133.jpg)

<details>
<summary>line</summary>
