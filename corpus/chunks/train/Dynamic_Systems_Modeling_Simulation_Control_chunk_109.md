# Example 3.1

Figure 3.7 shows a series RL circuit with a voltage source. Derive the mathematical model of the electrical system.

This circuit contains a single energy-storage element (inductor L) and a single loop. Consequently, the model will consist of one first-order ODE, which is the dynamic equation for current through the inductor, Eq. (3.10)

$$L \dot {I} _ {L} = e _ {L} \tag {3.16}$$

Next, we must express inductor voltage $e _ { L }$ in terms of the dynamic variable $I _ { L }$ and/or the source voltage $e _ { \mathrm { i n } } ( t )$ . To do so, we apply Kirchhoff’s voltage law around the loop in a clockwise direction

$$- e _ {L} - e _ {R} + e _ {\text { in }} (t) = 0 \tag {3.17}$$

Substituting Ohm’s law for the voltage across the resistor $( e _ { R } = R I _ { L } )$ in Eq. (3.17), the inductor voltage is

$$e _ {L} = e _ {\text { in }} (t) - R I _ {L} \tag {3.18}$$

Substituting Eq. (3.18) into the first-order ODE (3.16) yields

$$L \dot {I} _ {L} = e _ {\mathrm{in}} (t) - R I _ {L}$$

Finally, we move all terms involving the dynamic variable $I _ { L }$ to the left-hand side

$$L \dot {I} _ {L} + R I _ {L} = e _ {\text { in }} (t) \tag {3.19}$$

Equation (3.19) is the mathematical model of this simple series RL circuit. It is a linear, time-invariant first-order ODE.

For this simple example, we could have started with Kirchhoff’s voltage law, Eq. (3.17), repeated below

$$- e _ {L} - e _ {R} + e _ {\mathrm{in}} (t) = 0$$

Next, we simply substitute the appropriate element laws for voltage across an inductor $( e _ { L } = L \dot { I } _ { L } )$ ) and voltage across a resistor $( e _ { R } = R I _ { L } )$ to yield the mathematical model (3.19). For simple single-loop circuits, it may be easier to derive the mathematical model by starting with the loop equation from Kirchhoff’s voltage law.

![](image/7e08a030b75328a592972b4c006d050e55a314ab6da626bd884f0340d54f7930.jpg)

<details>
<summary>text_image</summary>

L
+
e_in(t)
-
I_L
R
</details>

Figure 3.7 Series RL circuit for Example 3.1.
