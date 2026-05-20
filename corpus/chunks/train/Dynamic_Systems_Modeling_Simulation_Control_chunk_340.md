Obtain the dynamic response using Simulink. The system is initially at rest (equilibrium). The locomotive force is modeled by a 200-kN step function applied at time t = 0 s plus a quadratic term:

$$
F _ {a} (t) = \left\{ \begin{array}{c c} 2 (1 0 ^ {5}) + 5 0 0 0 t ^ {2} & \text { for } 0 <   t <   2 0 \\ 2. 2 (1 0 ^ {6}) & \text { for } t \geq 2 0 \end{array} \right. \quad (\text { in   N })
$$

The locomotive force increases at a quadratic rate until t = 20 s and then remains constant at $2 . 2 ( 1 0 ^ { 6 } ) \mathrm { N }$ . Plot the velocity of the locomotive vs. time and the relative displacement of the first coupler $( z _ { 1 } - z _ { 2 } )$ ) vs. time for a simulation time of 25 s. What is the final speed of the locomotive in mph? [Hint: use the Saturation block from the Discontinuities library to limit the locomotive force so it never exceeds 2.2 (106) N].

![](image/eb2b98ca3b6ac848c6daf0ca4ebf656b6985bcb817abd38732f668da61339c91.jpg)

<details>
<summary>text_image</summary>

F_a(t)
m_1
Locomotive
k
b
m_2
Car 1
k
b
m_3
Car 2
z_1
z_2
z_3
Rolling friction = b_r \dot{z}_i
</details>

Figure P6.22

6.23 Figure P6.23 shows the 1/4-car suspension system from Problem 2.30 in Chapter 2. The input is road position, $z _ { \mathrm { i n } } ( t )$ , which is measured with respect to a level road datum. All displacements are measured with respect to their static equilibrium positions. The system parameters are

1/4-car mass $m _ { \mathrm { 1 } } = 2 5 0 \mathrm { k g }$

Wheel–axle mass $m _ { 2 } = 3 0 \mathrm { k g }$

Suspension spring $k _ { 1 } = 1 . 6 ( 1 0 ^ { 4 } ) \mathrm { N / m }$

Suspension damper coefficient $b = 9 8 0 \mathrm { N - s / m }$

Tire stiffness $k _ { 2 } = 1 . 6 ( 1 0 ^ { 5 } ) \mathrm { N } / \mathrm { m }$

Obtain the dynamic response using Simulink. The system is initially at rest (zero initial conditions), which represents cruise at 60 mph (26.82 m/s) on level road. The car hits a bump, modeled as a rectangular pulse $z _ { \mathrm { i n } } ( t )$ with an amplitude of 0.1 m (with respect to the level road) and width of 0.4 m. Plot the time responses of suspension travel $z _ { 1 } - z _ { 2 }$ and relative velocity $\dot { z } _ { 1 } - \dot { z } _ { 2 }$ .

![](image/1a6e5a2e252af49bf23fe546ad6a763780f0a7acd669b4a604828832dfdf8026.jpg)

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

Figure P6.23
