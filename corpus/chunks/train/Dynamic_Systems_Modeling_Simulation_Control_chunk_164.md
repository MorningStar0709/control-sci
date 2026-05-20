# Modeling Hydromechanical Systems

Hydromechanical systems are created by combining hydraulic and mechanical components, and they are used to convert the energy stored in the pressurized fluid to mechanical energy (motion and displacement). For example, a hydraulic actuator (or servomechanism) uses a pressurized liquid to move a piston in a cylinder that is connected to a mechanical load. As previously indicated, hydraulic servomechanisms are used extensively in industry to provide large forces for heavy machinery such as harvesters, excavators, and forging presses. Hydraulic accumulators store energy in a pressurized reservoir and often use a spring-mass mechanical subsystem to do so.

Figure 4.9 shows a simple hydraulic actuator that consists of a piston and cylinder with circular crosssectional area A. In this elementary example, hydraulic oil is flowing into the left chamber of the cylinder $( Q _ { \mathrm { i n } } )$ , and, therefore, we establish a CV on the left side of the cylinder (most hydraulic servomechanisms involve pressurized fluid on both sides of the cylinder so that the piston can move left or right). Conservation of mass (4.19) is applied to the CV

$$w _ {\mathrm{CV}} = w _ {\text { in }} - w _ {\text { out }} \tag {4.35}$$

The left-hand side of Eq. (4.35) is the time derivative of total mass in the CV

$$w _ {\mathrm{CV}} = \dot {m} _ {\mathrm{CV}} = \dot {\rho} V + \rho \dot {V} \tag {4.36}$$

![](image/d1c8a73015f53b2d1459111df34879fa727c143fa54d0a72b044bda74c4adbf0.jpg)

<details>
<summary>text_image</summary>

Volumetric-flow rate, Qin
Control volume (CV)
Piston with area A
Cylinder
Position, x
</details>

Figure 4.9 Hydraulic piston and cylinder.

We consider the high-pressure hydraulic fluid to be compressible, and therefore ${ \dot { \rho } } \neq 0$ (the reader should note that most hydraulic oils will experience a density change less than 2% despite a pressure increase on the order of 20 MPa). By expressing the input mass-flow rate as $w _ { \mathrm { i n } } = \rho Q _ { \mathrm { i n } }$ and noting that the output mass-flow rate $w _ { \mathrm { o u t } }$ is zero Eq. (4.35) becomes

$$\dot {\rho} V + \rho \dot {V} = \rho Q _ {\text { in }} \tag {4.37}$$

The time derivative of density can be expressed by using the chain rule

$$\dot {\rho} = \frac {d \rho}{d P} \frac {d P}{d t} \tag {4.38}$$
