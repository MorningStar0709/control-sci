# 11.5 HYDRAULIC SERVOMECHANISM CONTROL

Our fourth case study involves a feedback control system design for a hydraulic actuator. Hydraulic actuators have many applications ranging from robotics, earth-moving machinery, construction equipment, and aerospace [6, 7]. Figure 11.32 shows a schematic diagram of an electrohydraulic actuator (EHA) that consists of an electromechanical actuator (solenoid), spool valve, and hydraulic cylinder with piston. An input voltage signal is applied to the solenoid actuator (not shown in Fig. 11.32), which in turn moves the spool valve left or right in order to meter flow in and out of the hydraulic cylinder. If the spool-valve displacement y is positive (to the right) as shown in Fig. 11.32, fluid flows from the supply pressure $P _ { S }$ through the valve orifice and into the right-hand side of the cylinder. Consequently, if right-side cylinder pressure $P _ { 1 }$ is higher than pressure $P _ { 2 }$ , the piston moves to the left resulting in a positive displacement x for the piston. When $y > 0$ , fluid flows from the left-side cylinder (pressure $P _ { 2 } )$ to the reservoir (drain) pressure $P _ { r }$ . Volumetric flow into and out of the right-side cylinder is $Q _ { 1 }$ , while $Q _ { 2 }$ is the volumetric flow out of and into the left-side cylinder.

![](image/40d98f33ab06fb1039eef032b717776283d54eb43a940f0fa1bb4dd3caf9b7b3.jpg)

<details>
<summary>text_image</summary>

Pr
(drain for y > 0)
PS
(supply)
Pr
(drain for y < 0)
y
Spool
valve
Port A
Port B
Valve
area, Av
b
Q2
Q1
P2
P1
Cylinder
Piston mass, m
x
</details>

Figure 11.32 Schematic diagram of an electrohydraulic actuator.

Our objective is to develop a feedback control system for the EHA that will automatically adjust the input voltage so that the piston stroke x reaches a desired target position. We want a fast piston response with good damping characteristics and very little overshoot. As an example, this case study might represent a hydraulic actuator for positioning an aerodynamic surface such as an airplane’s elevator, aileron, or rudder. This type of actuator is called a servomechanism.
