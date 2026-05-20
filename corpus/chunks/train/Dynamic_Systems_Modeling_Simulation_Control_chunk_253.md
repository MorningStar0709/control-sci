# Example 5.16

Figure 5.12 shows a simple series RL circuit that has voltage source $e _ { \mathrm { i n } } ( t )$ as the input. The desired output, perhaps measured by a voltmeter, is the voltage across the resistor R. We wish to draw the block diagrams for this system using (1) a transfer function block and (2) an integrator block.

As with all problems, we start with the mathematical model. Applying Kirchhoff’s voltage law around the loop yields

$$- e _ {L} - e _ {R} + e _ {\mathrm{in}} (t) = 0$$

![](image/0c5d523b2ccf946981e59056d5e16b8d5eaaee2be380b85d22008e30fb6e3720.jpg)

<details>
<summary>text_image</summary>

L
+
e_in(t)
-
I
R
e_O
</details>

Figure 5.12 Series RL circuit for Example 5.16.

where the voltage across the inductor is $e _ { L } = L \dot { I }$ and the voltage across the resistor is $e _ { R } = R I$ . By placing all terms involving the dynamic variable (current, I) on the left-hand side, we obtain the mathematical model

$$L \dot {I} + R I = e _ {\text { in }} (t) \tag {5.113}$$

We can derive the transfer function by applying the D operator to Eq. (5.113) and forming the ratio of current to source voltage to obtain

$$\frac {I (t)}{e _ {\text { in }} (t)} = \frac {1}{L D + R} \tag {5.114}$$

Next, we substitute $s = D$ to obtain the transfer function $G ( s )$

$$\frac {1}{L s + R} = \frac {I (s)}{E _ {\mathrm{in}} (s)} \tag {5.115}$$

This transfer function has source voltage $e _ { \mathrm { i n } } ( t )$ as the input and current I as the output; however, we want resistor voltage $e _ { O } = R I$ as the output variable. Therefore, we can multiply the transfer function output (current) by resistance R to obtain the desired system output $e _ { O }$ . Figure 5.13a shows this configuration in a block diagram with two blocks in series: the current signal from the transfer function block is sent to a gain block with magnitude R in order to produce the desired system output $e _ { O }$ . Figure 5.13b shows an equivalent block diagram for the RL circuit where the gain block R is simply factored into the RL circuit transfer function.
