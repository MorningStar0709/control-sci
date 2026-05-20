# Example 3.5

Figure 3.11 shows a dual-loop electrical system driven by a voltage source. Derive the mathematical model of the electrical system.

We begin the model development as we did in Examples 3.2 and 3.3: this network contains two energystorage elements, inductor L and capacitor C. Therefore, the model consists of two first-order ODEs in terms of capacitor voltage $e _ { C }$ and inductor current $I _ { L }$

$$\text { Capacitor voltage: } \quad C \dot {e} _ {C} = I _ {C} \tag {3.52}\text { Inductor current: } \quad L \dot {I} _ {L} = e _ {L} \tag {3.53}$$

![](image/4469626655a6b6632eb3cb641ed648b203959b60b5e764a1c977a6277d05a9c0.jpg)

<details>
<summary>text_image</summary>

R₁
I₁
A
L
Iₗ
C
I꜀
R₂
eᵢₙ(t)
+
</details>

Figure 3.11 Electrical system for Example 3.5.

We must express capacitor current $I _ { C }$ and inductor voltage $e _ { L }$ in terms of dynamic variables $I _ { L }$ and $e _ { C }$ and input voltage $e _ { \mathrm { i n } } ( t )$ . To begin, apply Kirchhoff’s current law to node $\ " { \bf A } ^ { , , , }$ in Fig. 3.11

$$I _ {1} - I _ {C} - I _ {L} = 0 \tag {3.54}$$

Therefore, the capacitor current required in Eq. (3.52) is $I _ { C } = I _ { 1 } - I _ { L }$ . Current through resistor $R _ { 1 }$ can be computed from Ohm’s law, $I _ { 1 } = e _ { R _ { 1 } } / R _ { 1 }$ , if we can determine the voltage drop across the resistor. Voltage drop across $R _ { 1 }$ is 1determined from Kirchhoff’s voltage law around the left-hand side loop (moving clockwise):

$$- e _ {R _ {1}} - e _ {C} + e _ {\text { in }} (t) = 0 \tag {3.55}$$

Therefore, the voltage drop for $R _ { 1 }$ is

$$e _ {R _ {1}} = e _ {\text { in }} (t) - e _ {C} \tag {3.56}$$

and the current through resistor $R _ { 1 }$ is

$$I _ {1} = \frac {e _ {\text { in }} (t) - e _ {C}}{R _ {1}} \tag {3.57}$$

Finally, substituting Eq. (3.57) for resistor $R _ { 1 }$ current and using Eq. (3.54) for capacitor current in Eq. (3.52), the modeling equation for capacitor voltage is

$$C \dot {e} _ {C} = \frac {e _ {\text { in }} (t) - e _ {C}}{R _ {1}} - I _ {L} \tag {3.58}$$

Equation (3.58) is complete because it is in terms of $e _ { C } , I _ { L }$ , and $e _ { \mathrm { i n } } ( t )$ .

Next, we must determine an expression for the inductor voltage $e _ { L }$ in the dynamic equation for the inductor, Eq. (3.53). Applying Kirchhoff’s voltage law to the right-hand side loop in Fig. 3.11 (moving clockwise) yields

$$- e _ {L} - e _ {R _ {2}} + e _ {C} = 0 \tag {3.59}$$
