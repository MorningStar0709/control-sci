6.17 Use the MATLAB command lsim to obtain the voltage response for the washout filter in Problem 6.16. Plot output and input voltages $e _ { O } ( t )$ and $e _ { \mathrm { i n } } ( t )$ on the same plot.   
6.18 Professor Jones buys a cup of coffee at a local coffeehouse near campus. The coffee is initially $8 0 ~ ^ { \circ } \mathrm { C }$ $( 1 7 6 ^ { \circ } \mathrm { F } )$ when she receives it, and it is in a capped to-go cup with a total thermal resistance $R = 0 . 2 5 ^ { \circ } \mathrm { C } \mathrm { - }$ - s/J. The 10-oz coffee has a total thermal capacitance of $\mathrm { \bar { \it C } } = \mathrm { \bar { 1 } } 2 3 7 \mathrm { \ : J / \mathrm { \mathrm { \bar { \circ } } C } }$ . The outside temperature is constant at $T _ { a } = - 1 0 ^ { \circ } \mathrm { C } \left( 1 4 ^ { \circ } \mathrm { F } \right)$ . Figure P6.18 shows the simple thermal model.

![](image/a10d05d727bf3f174c5d09f5fd47075d31479aa8a823130d7c5eb857c50237c7.jpg)

<details>
<summary>text_image</summary>

Ambient
temperature, Ta
Insulation, R
Coffee
temperature, T
Thermal capacitance, C
</details>

Figure P6.18

a. It takes Prof. Jones 6 min to walk from the coffeehouse to her office. Use Simulink to determine the temperature of the coffee when she enters the building.   
b. Repeat part (a) for the case where Prof. Jones puts the hot coffee in an insulated thermos (thermal resistance $R = 5 . 5 ^ { \circ } \mathrm { C - s / J ) }$ before leaving the coffeehouse.

6.19 Figure P6.19 shows the wind turbine generator system from Example 2.8 in Chapter 2. The system inputs are aerodynamic torque $T _ { \mathrm { a e r o } }$ (from the wind) and generator (or electrical) torque $T _ { \mathrm { g e n } }$ . The system parameters for a 3000 kW wind turbine generator are

Turbine moment of inertia $J _ { 1 } = 1 . 2 6 ( 1 0 ^ { 7 } ) \mathrm { k g } \mathrm { - m } ^ { 2 }$

Turbine radius (blade tip to hub) $R = 4 5 . 6  { \mathrm { m } }$

Turbine friction coefficient $b _ { 1 } = 1 1 0 0 \mathrm { N \mathrm { - m { - s / r a d } } }$

Generator moment of inertia $J _ { 2 } = 2 4 0 \mathrm { k g } { \cdot } \mathrm { m } ^ { 2 }$

Generator friction coefficient $b _ { 2 } = 0 . 1 \mathrm { N - m - s / r a d }$

Gear ratio $N = r _ { 2 } / r _ { 1 } = 1 / 9 3$

The aerodynamic torque is a function of air density $\rho ( \mathrm { i n } \mathrm { k g } / \mathrm { m } ^ { 3 } )$ , turbine radius R (in m), wind speed $V _ { w }$ (in m/s), and torque coefficient $C _ { q }$

$$T _ {\mathrm{aero}} = \frac {1}{2} \rho \pi R ^ {3} V _ {w} ^ {2} C _ {q}$$
