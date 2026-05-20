Create the magnitude Bode diagram of this nonlinear system by executing a series of numerical simulations with Simulink. Use this basic two-step procedure: (1) obtain the dynamic response using Simulink for a sinusoidal input $x _ { \mathrm { i n } } ( t ) = 0 . 0 3$ sin ??t m where ?? is the input frequency (rad/s), and (2) from the simulation data determine the steady-state amplitude ratio $( x / x _ { \mathrm { i n } } )$ . Finally, create the Bode diagram by plotting the amplitude ratio (dB) for a sequence of discrete input frequencies $1 < \omega < 1 0 0$ rad/s (use a log-scale plot for the frequency axis). This procedure is best handled by an M-file that performs all calculations in a “looping” manner by changing input frequency ??. Describe the key features of the frequency response of this nonlinear system.

9.28 Figure P9.28 shows the 1∕4-car suspension system from Problems 2.30 and 6.23. The input is road position, $z _ { \mathrm { i n } } ( t )$ , which is measured with respect to a level road datum. All displacements are measured with respect to their static equilibrium positions. The system parameters are

$$1 / 4 \mathrm{-carmass} m _ {1} = 2 5 0 \mathrm{kg}\text { Wheel - axle mass } m _ {2} = 3 0 \mathrm{kg}\text { Suspension spring } k _ {1} = 1. 6 (1 0 ^ {4}) \mathrm{N/m}\text { Suspension damper coefficient } b = 9 8 0 \mathrm{N} \cdot \mathrm{s} / \mathrm{m}\text { Tire stiffness } k _ {2} = 1. 6 (1 0 ^ {5}) \mathrm{N/m}$$

a. Determine the vibration frequencies for an impulsive (“bump”) input caused by a sudden displacement of the road.   
b. Analyze the frequency response of the position of the 1∕4-car mass $m _ { 1 }$ using the Bode diagram. In particular, estimate the resonant frequencies and the associated transmissibility for each resonant frequency.

![](image/c4ac020fe6332f236861e78e6156bb6eef4a574716fd786cb6342c5be82f5aca.jpg)

<details>
<summary>text_image</summary>

1/4-car mass
m₁
Suspension
system
k₁
b
Wheel/axle assembly
m₂
k₂
z₁
z₂
Level road
zᵢₙ(t)
</details>

Figure P9.28

9.29 Figure P9.29 shows a 1-DOF vibration isolation system for a sensitive instrument with mass m = 1.4 kg.

![](image/e835fe5b55c1b8f42f6b5a80d4347347d73c5d1cf3a1500c2c8579dc5f6833ed.jpg)

<details>
<summary>text_image</summary>

m
k
b
x
x_b(t)
Shaker
table
Vibration
mounts
</details>

Figure P9.29
