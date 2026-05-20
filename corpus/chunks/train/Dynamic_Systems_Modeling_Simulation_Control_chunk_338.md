Assume that air density is $\rho = 1 . 2 2 5 \mathrm { k g } / \mathrm { m } ^ { 3 }$ and the torque coefficient is $C _ { q } = 0 . 0 7 5$ . At time $t = 0$ , the wind speed is $V _ { \mathrm { { w } } } = 1 3 \mathrm { { m } / \mathrm { { s } } }$ . The generator torque is a function of generator shaft speed: $T _ { \mathrm { g e n } } = 1 5 8 . 7 \dot { \theta } _ { 2 } \ : ( \mathrm { N - m } )$ ).

![](image/9c4f7df9d42eb9e225d9b23753de1e57a043a847e1781fb25d220db579148159.jpg)

<details>
<summary>text_image</summary>

Wind
Tₐero
Bearing friction,
b₁
Gear train
Gear 1, r₁
Generator rotor,
J₂
θ₁
θ₂
T_gen
Gears 2, r₂
Viscous friction, b₂
Turbine, J₁
</details>

Figure P6.19

a. Compute the constant angular velocities of the turbine and generator shafts at time $t = 0$ .   
b. Obtain the dynamic response using Simulink. At time $t = 2 \mathrm { s } ,$ , the wind speed ramps up from 13 to 15 m/s at a constant acceleration of $0 . 2 5 \mathrm { m } / \mathrm { s } ^ { 2 }$ . Use the initial conditions computed in part (a) and set the simulation time to 90 s. Plot the angular velocities of the turbine and generator shafts vs. time.

6.20 Figures P6.20a and P6.20b show the pantograph system described in Problems 2.27 (Chapter 2) and 5.33 (Chapter 5). The pantograph system parameters [1] are

Head mass $m _ { 1 } = 9 \mathrm { k g }$

Frame mass $m _ { 2 } = 1 7$ kg

Contact shoe stiffness $k _ { 1 } = 8 . 2 ( 1 0 ) ^ { 4 } \mathrm { N / m }$

Head suspension stiffness $k _ { 2 } = 7 0 0 0$ N/m

Head suspension friction coefficient $b _ { 1 } = 1 3 0 \mathrm { N \mathrm { - s / m } }$

Frame suspension friction coefficient $b _ { 2 } = 3 0 \mathrm { N - s / m }$

![](image/6f2a1f9bf64dde3e112c835ac69a045a228058e27266c756eb9cf8d19a36db0a.jpg)

<details>
<summary>text_image</summary>

Pan-head
Upper arm
of frame
Lower arm
of frame
Base
</details>

Figure P6.20a

![](image/3acd12984b2aab6d7b5a978f8ef4ed9871b31bb2868426fa17a0a0e8c1696515.jpg)

<details>
<summary>text_image</summary>

Overhead wire
k₁
Contact shoe
Head
m₁
z₁
Head suspension
k₂
b₁
Frame
m₂
z₂
Frame suspension
fₐ(t)
b₂
Base
</details>

Figure P6.20b

The displacement of the overhead wire depends on the speed of the train and the spacing between towers that support the catenary wire. The wire displacement is modeled by the following sinusoidal function

$$z _ {w} (t) = z _ {w 0} + 0. 0 2 \sin 3 t \mathrm{m}$$

where $z _ { w 0 } = - 0 . 0 0 1 0 9 7 6$ m is the initial displacement of the wire.
