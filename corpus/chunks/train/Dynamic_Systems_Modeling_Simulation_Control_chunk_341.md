6.24 Figure P6.24 shows a pneumatic servomechanism [4]. The total length of the cylinder is 10 cm and the piston position x is measured relative to the mid-point of the cylinder (hence, when x = 0 the piston is at the middle of the cylinder). This highly nonlinear system has been linearized about a nominal pressure, volume, and piston position $( x = 0 )$ and the resulting system transfer function is

$$G (s) = \frac {7 . 0 0 3 (1 0 ^ {6})}{s (s ^ {2} + 2 8 . 3 s + 1 5 , 8 9 0)} = \frac {X (s)}{U (s)}$$

where x(t) is the piston/load mass position (in m) and u(t) is the spool-valve position (in m). See Reference 4 for details in developing the linear model.

a. Use Simulink to obtain the dynamic response of the piston/load mass x(t) for a pulse input for valve position: $u ( t ) = 0 . 0 0 1$ m (or 1 mm) for $0 < t \leq 0 . 0 5 \mathrm { s } .$ , and $u ( t ) = 0$ for $0 . 0 5 < t \leq 0 . 5 \mathrm { ~ s ~ }$ . At time $t = 0$ the piston is initially at rest at the mid-point position. Plot the time response of the piston/load mass position (in cm) for the 1-mm pulse input.   
b. Use your simulation to determine the maximum pulse duration of a 1-mm valve displacement (i.e., a feasible piston position response). Plot the piston response x(t) for this maximum pulse input.

![](image/174f6692dbff097d6d373413daa85d064064b9ac754551cdd2319132db7777e8.jpg)

<details>
<summary>text_image</summary>

Cylinder
Piston/load
mass position, x
Load mass
m
Piston
P1
P2
4-way
spool valve
Valve
position, u
Supply
tank, Ps
</details>

Figure P6.24

6.25 Figure P6.25 shows the thermal system (interior office room with baseboard heater) from Example 4.7 in Chapter 4. The system parameters are [5]

Total thermal capacitance $C = 4 . 8 3 ( 1 0 ^ { 5 } ) \mathrm { J / ^ { \circ } C }$

North wall thermal resistance $R _ { 1 } = 0 . 0 4 1 ^ { \circ } \mathrm { C } \mathrm { - } \mathrm { s } / \mathrm { J }$

South wall thermal resistance $R _ { 2 } = 0 . 1 5 1 ^ { \circ } \mathrm { C - s / J }$

East wall thermal resistance $R _ { 3 } = 0 . 1 0 8 ^ { \circ } \mathrm { C } \mathrm { - } \mathrm { s } / \mathrm { J }$

West wall thermal resistance $R _ { 4 } = 0 . 2 0 9 ^ { \circ } \mathrm { C } \mathrm { - } \mathrm { s } / \mathrm { J }$

Ceiling thermal resistance $R _ { 5 } = 0 . 2 4 0 \mathrm { ^ { \circ } C \mathrm { - } s / J }$

Floor thermal resistance $R _ { 6 } = 0 . 1 5 9 ^ { \circ } \mathrm { C - s / J }$

![](image/a268bae2a1362645112391b4b51b945a2fad608ca946bbc8406930dc2d3ab7cd.jpg)

<details>
<summary>text_image</summary>
