a. Using Simulink, determine the piston-load mass response x(t) to a sinusoidal valve position input u(t) = 0.001 sin 50t m (the input frequency is ∼8 Hz). Plot piston and valve position vs. time on the same figure. Describe how the simulated frequency response of the piston-load mass differs from the “standard” analytical frequency-response equation (9.17). Explain why the simulated frequency response does not match the form of Eq. (9.17).   
[Hint: Reread the section on the derivation of the frequency response and the associated assumptions.]   
b. Use Simulink to determine the piston-load mass response x(t) to a sinusoidal valve input $u ( t ) = 0 . 0 0 1$ sin 126t m (the input frequency is ∼20 Hz). Plot piston and valve positions vs. time on the same figure to show that they are $1 8 0 ^ { \circ }$ out of phase. Verify this phase difference using the Bode diagram of G(s).   
c. Develop the transfer function with velocity of the piston-load mass (i.e., ẋ ) as the output and valve position u as the input. Use Simulink to determine the velocity response to the valve input $u ( t ) =$ 0.001 sin 50t m and plot ẋ (t). Plot the Bode diagram for the velocity-output transfer function and show

that it can be used to estimate the frequency response for piston velocity by verifying the simulated velocity response to the ∼8-Hz input signal.

9.27 A simplified 1-DOF model of a car suspension system is shown in Fig. P9.27 (see Problem 6.14 in Chapter 6). The mass m is one-quarter of the vehicle’s mass, and the stiffness and damper elements represent the suspension system. The displacement $x _ { \mathrm { i n } } ( t )$ is the position of the wheel–axle assembly, and it is considered to be the known input to the system. Displacement x is measured from its static equilibrium position. The system parameters are m = 1100 kg, k = 65,000 N/m, and the damper force of the shock absorber is modeled by the nonlinear equation

$$F _ {d} = \frac {4 5 0 0 \dot {z}}{\sqrt {\dot {z} ^ {2} + v ^ {2}}} \quad (\mathrm{inN})$$

where $\dot { z } = \dot { x } - \dot { x } _ { \mathrm { i n } } ( t )$ is the relative velocity across the shock absorber (m/s), and $\nu = 0 . 2 \mathrm { m / s }$ . The system is initially at rest.

![](image/c8e05cfffae2913c5b2e028fe9a649f9260947d6dd39929f9c4e06646cc9d75d.jpg)

<details>
<summary>text_image</summary>

½ vehicle mass
m
Suspension system
k
Shock absorber
x
Wheel/axle position
x_in(t)
</details>

Figure P9.27
