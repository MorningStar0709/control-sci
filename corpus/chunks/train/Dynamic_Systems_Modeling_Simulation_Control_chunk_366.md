# Example 7.6

Figure 7.11 shows a series RL circuit with voltage source $e _ { \mathrm { i n } } ( t )$ . Sketch the current I(t) for an impulse voltage input, $e _ { \mathrm { i n } } ( t ) = 0 . 0 8 \delta ( t - t _ { 1 } ) \ : \mathrm { V }$ . The system has zero energy at time $t = 0 ,$ , or $I ( 0 ) = 0$ , and the impulse is applied at time $t _ { 1 } = 0 . 1 \mathrm { ~ s ~ }$ . The inductance is $L = 0 . 0 2$ H, and the resistance is $R = 1 . 2 \Omega$ .

We begin with the mathematical model of the RL circuit, which we determined in Chapter 3:

$$L \dot {I} + R I = e _ {\text { in }} (t) \tag {7.47}$$

Because the circuit has only one energy-storage element (inductor L), we have a first-order system. We substitute the numerical values for R and L and divide by resistance R to write the first-order system in our standard form

$$0. 0 1 6 7 \dot {I} + I = 0. 8 3 3 3 e _ {\mathrm{in}} (t) \tag {7.48}$$

Therefore, the time constant is identified as $\tau = 0 . 0 1 6 7 ~ \mathrm { s }$ . The impulse response is found using Eq. (7.46), where A is the strength of the impulse (0.08 V-s) and b is the input coefficient $( 1 / R = 0 . 8 3 3 3 \Omega ^ { - 1 } )$ ). The initial magnitude of the impulse response is $A b / \tau = ( 0 . 0 8 ) ( 0 . 8 3 3 3 ) / 0 . 0 1 6 7 = 4 \mathrm { ~ A ~ }$ . Note that the units are correct, as $A / \tau$ has units of $( \mathrm { V } { - } \mathrm { s } ) / \mathrm { s } = \mathrm { V }$ , and b has units $\Omega ^ { - 1 }$ , which results in volts/ohms = amperes. Hence, the impulse response for current shows a discontinuous step to 4 A at the instant the impulse is applied at $t _ { 1 } = 0 . 1 ~ \mathrm { s }$ . Total energy of the electrical system is $L I ^ { 2 } / 2$ , and therefore the system exhibits an instantaneous jump in energy at $t = 0 . 1$ s because of the impulse input. The impulse response exponentially decays to zero in about four time constants after the impulse is applied, or $t = 0 . 1 + 4 \tau = 0 . 1 6 6 7 \mathrm { ~ s ~ }$ .

Figure 7.12 shows the impulse response, which the reader should be able to sketch from the information computed in this example. The strength of the impulse 0.08 V-s might be an idealized representation of an 80-V pulse input that is applied for pulse duration of 0.001 s (or, 1 ms).

![](image/5ff1150bc47cad72d53075abfa6fcac7a2dda7ac1ba89666fe6fd0a05bb79b3c.jpg)

<details>
<summary>text_image</summary>

e_in(t)
0.08
t_1
t
e_in(t) = 0.08δ(t-t_1) V
+
-
R
L
I
</details>

Figure 7.11 Electrical system with impulse input (Example 7.6).

![](image/74368fe5a76cfffb29b604577d9c2b2f5112a34ae57cd1fe9d8bbdc791941781.jpg)

<details>
<summary>line</summary>

| Time, s | Current, I(t), A |
| --- | --- |
| 0.10 | 4.0 |
</details>

Figure 7.12 Impulse response of electrical system (Example 7.6).
