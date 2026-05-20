a. Verify that the pantograph is in static equilibrium at time t = 0 if the piston force is $f _ { a } ( 0 ) = 9 0 \mathrm { N } , z _ { 1 } ( 0 ) =$ $0 , z _ { 2 } ( 0 ) = 0 . 0 1 2 8 5 7 1 \mathrm { m }$ , and $z _ { w } ( 0 ) = - 0 . 0 0 1 0 9 7 6 \mathrm { m }$ . Compute the contact force at time $t = 0$ .   
b. Use Simulink to numerically simulate the pantograph response using the static equilibrium initial condition in part (a), a constant piston force $f _ { a } ( t ) = 9 0 \mathrm { N } .$ , and the sinusoidal wire displacement. Let the simulation time be 4 s. Plot the two measured output variables: $y _ { 1 } = { \mathrm { s h o e } }$ contact force and $y _ { 2 } = z _ { 1 } - z _ { 2 }$ . Does the pantograph head remain in contact with the overhead wire? Explain your answer.

6.21 Figure P6.21 shows the dual-disk mechanical system from Example 2.9 in Chapter 2 and Problem 5.29. The system parameters are [2]

Piston moment of inertia $J _ { 1 } = 0 . 3 \mathrm { k g } – \mathrm { m } ^ { 2 }$

Cylinder moment of inertia $J _ { 2 } = 0 . 3 \mathrm { k g } \mathrm { - m } ^ { 2 }$

Torsional spring constant $k = 6 0 0 0 \mathrm { N } \mathrm { - m } / \mathrm { r a d }$

Piston/cylinder friction coefficient b = 2 N-m-s/rad

The system is initially at rest. The input torque is a periodic pulse with a magnitude of 5500 N-m and pulse width that is 10% of the period. Simulate two pulse frequencies: (a) period = 0.02 s (50 Hz) and (b) period = 0.0314 s (31.85 Hz). Obtain the dynamic response using Simulink. Plot the relative angular displacement $\Delta \theta = \theta _ { 2 } - \theta _ { 1 }$ vs. time for a simulation time of 0.5 s and comment on the effect of the pulse period [Hint: use the Pulse Generator (Sources library) to create the periodic torque input].

![](image/718473fdd7f00c100434caf010da3a21af131ea87212f51539b23e2d9552b723.jpg)

<details>
<summary>text_image</summary>

Piston
inertia, J₁
Tᵢₙ(t)
Torsional
spring, k
Cylinder
inertia, J₂
θ₁
θ₂
Tᵢₙ(t)
Friction, b
Friction, b
</details>

Figure P6.21

6.22 The railroad-car system discussed in Problems 2.29 and 5.31 is shown in Fig. P6.22. The system parameters are [3]

Locomotive mass $m _ { 1 } = 1 2 , 0 0 0 \mathrm { k g }$

Car mass $m _ { 2 } = m _ { 3 } = 9 0 0 0 \mathrm { k g }$

Coupler stiffness $k = 5 . 2 ( 1 0 ^ { 6 } ) \mathrm { N / m }$

Coupler friction $b = 2 . 6 ( 1 0 ^ { 4 } ) \mathrm { N { - } s / m }$

Rolling friction $b _ { r } = 3 ( 1 0 ^ { 4 } ) \mathrm { N { - s / m } }$
