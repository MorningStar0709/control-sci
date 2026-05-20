# Engineering Applications

7.26 Figure P7.26 shows the thermal system (interior office room) from Example 4.7 in Chapter 4 and Problem 6.25. The thermal system parameters are

Total thermal capacitance $C = 4 . 8 3 ( 1 0 ^ { 5 } ) \mathrm { J / ^ { \circ } C }$

North wall thermal resistance $R _ { 1 } = 0 . 0 4 1 ^ { \circ } \mathrm { C - s / J }$

South wall thermal resistance $R _ { \mathrm { 7 } } = 0 . 1 5 1 ^ { \circ } \mathrm { C } \mathrm { - } \mathrm { s } / \mathrm { J }$

East wall thermal resistance $R _ { \mathrm { 3 } } = 0 . 1 0 8 ^ { \circ } \mathrm { C } \mathrm { - } \mathrm { s } / \mathrm { J }$

West wall thermal resistance $R _ { 4 } = 0 . 2 0 9 ^ { \circ } \mathrm { C - s / J }$

Ceiling thermal resistance $R _ { 5 } = 0 . 2 4 0 \mathrm { ^ { \circ } C \mathrm { - } s / J }$

Floor thermal resistance $R _ { 6 } = 0 . 1 5 9 ^ { \circ } \mathrm { C } \mathrm { - } \mathrm { s } / \mathrm { J }$

Sketch the temperature response of the room if its initial temperature is equal to the (constant) ambient temperature, i.e., $T ( 0 ) \overset { \cdot } { = } T _ { a } = 1 0 ^ { \circ } \mathrm { C } ~ ( 5 0 ^ { \circ } \mathrm { F } )$ and the baseboard heater provides a constant heat input $q _ { \mathrm { B H } } = 1 0 0 0 \mathrm { W } \left( \mathrm { 1 k W } \right)$ ). Use units of hours for the time axis. Compare your sketch to the numerical solution (using Simulink) that was determined in Problem 6.25.

![](image/26eaa8dfb86f4056c2783ebe9c6e5e38fac27f77eab61f54bda7cb155bfabc67.jpg)

<details>
<summary>text_image</summary>

North
door
window
Thermal resistance, R₁
Baseboard heater
q_BH
Temperature, T
Thermal capacitance, C
R₄
door
R₂
Top view
</details>

![](image/a29a1bab28a8fd532212ff626ecd3cb0014e47fd708b8c93a8b8fea5e8a9e8a1.jpg)

<details>
<summary>text_image</summary>

ceiling, R₅
door
East view
floor, R₆
</details>

Figure P7.26

7.27 The LC circuit shown in Fig. P7.27 (originally presented in Problem 3.25) is connected to an antenna and is the basic circuit component used in electrical oscillators and frequency tuners. The system parameters are $L = 3$ mH and $C = 2 0 \mu \mathrm { F } .$ . At time $t = 0 ^ { - }$ the capacitor is charged and its voltage is $e _ { C } ( 0 ) = 2 . 5 \ : \mathrm { V } ,$ , the switch is open, and there is no current in the circuit. At time $t = 0$ the switch is closed. Accurately sketch the capacitor voltage $e _ { C } ( t )$ and current I(t) responses. Verify both sketches with a numerical simulation using Simulink and plot voltage $e _ { C } ( t )$ and current I(t) responses from the simulation.
