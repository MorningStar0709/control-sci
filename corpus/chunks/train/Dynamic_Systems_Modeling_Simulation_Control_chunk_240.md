# Example 5.12

Figure 5.6 shows an electrical system comprising a series RLC circuit and input voltage source $e _ { \mathrm { i n } } ( t )$ . Derive the I/O equation with output $y = I$ (loop current) and $u = e _ { \mathrm { i n } } ( t )$ .

The mathematical model of the RLC circuit can be derived by applying Kirchhoff’s voltage law around the single loop, which yields

$$- e _ {L} - e _ {R} - e _ {C} + e _ {\text { in }} (t) = 0 \tag {5.86}$$

Substituting for the voltages across each element, we obtain

$$L \dot {I} + R I + \frac {1}{C} \int I d t = e _ {\text { in }} (t) \tag {5.87}$$

Taking a time derivative of Eq. (5.87) in order to eliminate the integral term yields

$$L \ddot {I} + R \dot {I} + \frac {1}{C} I = \dot {e} _ {\text { in }} (t) \tag {5.88}$$

Let current I be the output variable y, and source voltage $e _ { \mathrm { i n } } ( t )$ be the input variable u. Therefore, the I/O equation is obtained directly from Eq. (5.88)

$$\ddot {y} + \frac {R}{L} \dot {y} + \frac {1}{L C} y = \frac {1}{L} \dot {u} \tag {5.89}$$

which matches the basic form of the I/O equation (5.85). Here, the leading coefficient $a _ { 2 }$ becomes unity by dividing the entire equation by inductance L.

![](image/130546a302bad525a923f138d534721efcc6dfc82d0f5c47ff98886e22ab3466.jpg)

<details>
<summary>text_image</summary>

R
L
C
+
e_in(t)
-
I
</details>

Figure 5.6 Series RLC circuit for Example 5.12.
