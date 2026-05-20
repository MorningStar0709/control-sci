# Example 8.11

Figure 8.5 shows the series RL circuit with voltage source $e _ { \mathrm { i n } } ( t )$ from Example 7.6. Obtain the current response I(t) for an impulse voltage input, $e _ { \mathrm { i n } } ( t ) = 0 . 0 8 \delta ( t )$ V. The system has zero energy at time $t = 0 , \mathrm { o r } I ( 0 ) = 0$ , and the inductance and resistance values are $L = 0 . 0 2$ H and $R = 1 . 2 \Omega$ , respectively.

The mathematical model of the RL circuit was derived in Chapter 3 and used in Example 7.6

$$L \dot {I} + R I = e _ {\text { in }} (t) \tag {8.43}$$

![](image/edbc9bbec01b7164752a98e8119cc70037fcc1ae90dd81abc8d70b4e8d4cd68e.jpg)

<details>
<summary>text_image</summary>

e_in(t) = 0.08δ(t) V
+ -
R
I
L
</details>

Figure 8.5 Electrical system with impulse input (Example 8.11).

Taking the Laplace transform (with zero initial conditions) yields

$$(L s + R) I (s) = E _ {\mathrm{in}} (s)$$

Forming the output/input ratio gives us the system transfer function

$$G (s) = \frac {I (s)}{E _ {\mathrm{in}} (s)} = \frac {1}{L s + R} = \frac {1}{0 . 0 2 s + 1 . 2} \tag {8.44}$$

Equation (8.44) is valid for any input. The Laplace transform of the current is

$$I (s) = G (s) E _ {\text { in }} (s) = \frac {1}{0 . 0 2 s + 1 . 2} E _ {\text { in }} (s) \tag {8.45}$$

Equation (8.45) is also valid for any voltage input. For this problem the voltage input is an impulse, or $e _ { \mathrm { i n } } ( t ) =$ 0.08??(t) V. Consulting entry 1 in Table 8.1 we see that $\mathcal { L } \{ \bar { 0 . 0 8 } \delta ( t ) \} = 0 . 0 8 = E _ { \mathrm { i n } } ( \bar { s } )$ . Hence, using the Laplace transform of the voltage impulse and Eq. (8.45) the Laplace transform of the current is

$$I (s) = \frac {0 . 0 8}{0 . 0 2 s + 1 . 2} \tag {8.46}$$

or, dividing all terms by 0.02 we obtain

$$I (s) = \frac {4}{s + 6 0} \tag {8.47}$$

Clearly, the inverse Laplace transform of the current Eq. (8.47) is an exponential function (see number 6 in Table 8.1). Therefore, the dynamic response to the impulsive voltage input is

$$I (t) = 4 e ^ {- 6 0 t} \mathrm{A} \tag {8.48}$$

Consequently, the current response shows an instantaneous jump from 0 to 4 A at time t = 0+ when the impulsive voltage input is applied to the electrical system. The time constant of this system is $\tau = L / R = 0 . 0 2 / 1 . 2 =$ 0.0167 s and, therefore, the current decays to zero at the settling time $t _ { S } = 4 \tau = 0 . 0 6 6 7 ~ \mathrm { s }$ . This solution is identical to the current response obtained in Example 7.6 (note that in Example 7.6 the impulse is applied at time t = 0.1 s instead of time t = 0 as in this case).
