# Example 4.2

Figure 4.10 shows a simple hydraulic actuator with an input flow rate $Q _ { \mathrm { i n } }$ to the cylinder and a piston connected to the load mass. Derive the mathematical model of the hydromechanical system.

![](image/8a6e38b6ecdd00c4a51a49be1e19590a9d4d7e92f5e84c49cf2910c446687e63.jpg)

<details>
<summary>text_image</summary>

Volumetric-flow rate, Qin
Cylinder
Piston with area, A
P, V
Patm
x
Load mass
m
Spring,
k
Load force, FL
Viscous friction, b
</details>

Figure 4.10 Hydraulic actuator for Example 4.2.

We begin with Eq. (4.40), which models the pressure change in the left-hand side of the cylinder

$$\dot {P} = \frac {\beta}{V} (Q _ {\text { in }} - \dot {V}) \tag {4.41}$$

where P and V are the pressure and volume of the left-side cylinder, respectively. The instantaneous volume is

$$V = V _ {0} + A x \tag {4.42}$$

where piston position x is measured from the static equilibrium position (no spring deflection) and $V _ { 0 }$ is the leftside chamber volume when x = 0. If we use Eq. (4.42), the time-rate of chamber volume is ${ \dot { V } } = A { \dot { x } }$ and hence Eq. (4.41) becomes

$$\dot {P} = \frac {\beta}{V _ {0} + A x} (Q _ {\text { in }} - A \dot {x}) \tag {4.43}$$

Next, we derive the mechanical model that governs the position and velocity of the piston and load mass. Figure 4.11 shows a free-body diagram of the mechanical system where m is the total mass of the piston, connecting rod, and load mass. The hydraulic-pressure force PA acts on the left side of the piston, while the atmospheric pressure force $P _ { \mathrm { a t m } } A$ acts on the right side of the piston (note that although the area of the right side of the piston is less than A due to the connecting rod area $A _ { \mathrm { r o d } } .$ , the atmospheric pressure distribution on the load mass results in an incremental force $P _ { \mathrm { a t m } } A _ { \mathrm { r o d } }$ acting to the left and hence the net atmospheric pressure force on the piston/load mass is $P _ { \mathrm { a t m } } A )$ . The spring, friction, and load forces act on the load mass as shown in Fig. 4.11. Next, apply Newton’s second law and sum all external forces on piston/load mass m with the sign convention as positive to the right:

$$+ \rightarrow \sum F = P A - P _ {\mathrm{atm}} A - k x - b \dot {x} - F _ {L} = m \ddot {x} \tag {4.44}$$

Rearranging Eq. (4.44) yields

$$m \ddot {x} + b \dot {x} + k x = (P - P _ {\mathrm{atm}}) A - F _ {L} \tag {4.45}$$
