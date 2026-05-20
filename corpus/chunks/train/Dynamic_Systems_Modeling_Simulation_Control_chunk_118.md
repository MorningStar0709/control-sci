# Example 3.6

Figure 3.13 shows an op-amp circuit with input (source) voltage $e _ { \mathrm { i n } } ( t )$ ) and output voltage $e _ { O }$ . Derive the relationship between input and output voltages.

This circuit contains resistor $R _ { 1 }$ between the input voltage and the negative input terminal of the op amp and a second resistor $R _ { 2 }$ between the output voltage and the negative input terminal of the op amp (negative feedback). The positive input terminal of the op amp is directly connected to the ground and hence voltage $e _ { B } = 0$ . Because the input voltage difference is zero for an ideal op amp with negative feedback (i.e., $e _ { B } - e _ { A } = 0 )$ and $e _ { B } = 0$ , the input voltage $e _ { A }$ to the inverting terminal is also zero.

Kirchhoff’s current law is applied at the top node between the two resistors in Fig. 3.13:

$$I _ {1} - I _ {A} - I _ {2} = 0 \tag {3.64}$$

However, an ideal op amp draws negligible current $( I _ { A } = 0 )$ and, therefore, $I _ { 1 } = I _ { 2 }$ and the currents through the two resistors are equal. We can write expressions for $I _ { 1 }$ and $I _ { 2 }$ by using Ohm’s law and dividing the respective

![](image/a5d95526230242bb5703e12ca35a7aa9450cb5d65183b468ea637daa8f7dfdbd.jpg)

<details>
<summary>text_image</summary>

R1
I1
IA
eA
-
eB
+
-
K
R2
I2
eO
e_in(t)
+
</details>

Figure 3.13 Op-amp circuit for Example 3.6.

voltage drop by the resistance

$$\frac {e _ {\text { in }} (t) - e _ {A}}{R _ {1}} = \frac {e _ {A} - e _ {O}}{R _ {2}} \tag {3.65}$$

The left-side term in Eq. (3.65) is current $I _ { 1 }$ and the right-side term is current $I _ { 2 }$ . We can rewrite Eq. (3.65) as

$$R _ {2} (e _ {\mathrm{in}} (t) - e _ {A}) = R _ {1} (e _ {A} - e _ {O}) \tag {3.66}$$

Rearranging Eq. (3.66) with the op-amp input voltage $e _ { A }$ on the right-hand side, we obtain

$$R _ {2} e _ {\text { in }} (t) + R _ {1} e _ {O} = \left(R _ {1} + R _ {2}\right) e _ {A} \tag {3.67}$$

or, solving for $e _ { A }$

$$e _ {A} = \frac {R _ {2}}{R _ {1} + R _ {2}} e _ {\text { in }} (t) + \frac {R _ {1}}{R _ {1} + R _ {2}} e _ {O} \tag {3.68}$$

Next, substitute Eq. (3.68) into the amplifier gain equation (3.63)

$$e _ {O} = K (e _ {B} - e _ {A}) = - \frac {K R _ {2}}{R _ {1} + R _ {2}} e _ {\text { in }} (t) - \frac {K R _ {1}}{R _ {1} + R _ {2}} e _ {O} \tag {3.69}$$

Note that $e _ { B } = 0$ as the positive op-amp input terminal in Fig. 3.13 is directly connected to the ground. Equation (3.69) is rearranged with all output voltage terms on the left-hand side to yield
