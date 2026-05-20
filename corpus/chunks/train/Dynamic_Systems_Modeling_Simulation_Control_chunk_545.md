# Example 10.4

Figure 10.7 shows an electrical circuit known as a buck converter, which is used to step the source voltage $e _ { \mathrm { i n } } ( t )$ “down” to a lower desired output voltage (see Problem 3.27). The buck converter uses a switch to repeatedly connect and disconnect the voltage supply $e _ { \mathrm { i n } } ( t )$ from the remainder of the circuit until the output (capacitor)

![](image/8d23d29de486b73b5949d59865af6d5121137af49d2b709d9fbe13890e4a5dcf.jpg)

<details>
<summary>text_image</summary>

e_in(t) = 28 V
+
-
1
L = 18 mH
2
C = 220 μF
+
-
e_C
R = 4 Ω
</details>

Figure 10.7 Buck converter electrical circuit (Example 10.4).

voltage $e _ { C }$ is equal to a desired reference voltage $e _ { \mathrm { r e f } } .$ . Simulate the closed-loop system if the desired reference voltage is $e _ { \mathrm { r e f } } = 1 2  { \mathrm { V } }$ and the supply voltage is constant at $e _ { \mathrm { i n } } = 2 8 \mathrm { V } _ { \mathrm { \Omega } }$ . At time $t = 0$ , the system has zero stored energy.

The mathematical model of the buck converter circuit was developed in Problem 3.27 and an SSR was obtained in Problem 5.24. When the switch is in position “1,” the voltage supply is connected to the circuit:

$$\text { Capacitor: } \quad R C \dot {e} _ {C} = R I _ {L} - e _ {C}\text { Inductor: } \quad L \dot {I} _ {L} = e _ {\text { in }} - e _ {C}$$

Consequently, the state equation is

$$
\dot {\mathbf {x}} = \left[ \begin{array}{c c} - 1 / (R C) & 1 / C \\ - 1 / L & 0 \end{array} \right] \mathbf {x} + \left[ \begin{array}{l} 0 \\ 1 / L \end{array} \right] u \tag {10.9}
$$

where the states are $x _ { 1 } = e _ { C }$ and $x _ { 2 } = I _ { L }$ and u is the input voltage to the circuit. The switching action is an on–off controller that is dictated by the simple equation

$$
u (t) = \left\{ \begin{array}{l l} e _ {\text { in }} & \text { if } e _ {\text { ref }} - e _ {C} \geq 0 \\ 0 & \text { if } e _ {\text { ref }} - e _ {C} <   0 \end{array} \right. \tag {10.10}
$$
