In the ideal op amp, no current flows into the input terminals, and the output voltage is not affected by the load connected to the output terminal. In other words, the input impedance is infinity and the output impedance is zero. In an actual op amp, a very small (almost negligible) current flows into an input terminal and the output cannot be loaded too much. In our analysis here, we make the assumption that the op amps are ideal.

Inverting Amplifier. Consider the operational-amplifier circuit shown in Figure 3–14. Let us obtain the output voltage $e _ { o }$ .

![](image/d8b1776cce919bd2625c294eff952ea28f8b85a7fba4f623ea3e6e662750acf2.jpg)

<details>
<summary>text_image</summary>

i₁ R₁
eᵢ
i₂ R₂
-
+
e′
eₒ
</details>

Figure 3–14 Inverting amplifier.

The equation for this circuit can be obtained as follows: Define

$$i _ {1} = \frac {e _ {i} - e ^ {\prime}}{R _ {1}}, \quad i _ {2} = \frac {e ^ {\prime} - e _ {o}}{R _ {2}}$$

Since only a negligible current flows into the amplifier, the current $i _ { 1 }$ must be equal to current $i _ { 2 }$ . Thus

$$\frac {e _ {i} - e ^ {\prime}}{R _ {1}} = \frac {e ^ {\prime} - e _ {o}}{R _ {2}}$$

Since $K ( 0 - e ^ { \prime } ) = e _ { 0 }$ and $K \gg 1$ e¿ must be almost zero, or, $e ^ { \prime } \doteq 0$ Hence we have.

$$\frac {e _ {i}}{R _ {1}} = \frac {- e _ {o}}{R _ {2}}$$

or

$$e _ {o} = - \frac {R _ {2}}{R _ {1}} e _ {i}$$

Thus the circuit shown is an inverting amplifier. If $R _ { 1 } = R _ { 2 }$ , then the op-amp circuit shown acts as a sign inverter.

Noninverting Amplifier. Figure 3–15(a) shows a noninverting amplifier.A circuit equivalent to this one is shown in Figure 3–15(b). For the circuit of Figure 3–15(b), we have

$$e _ {o} = K \left(e _ {i} - \frac {R _ {1}}{R _ {1} + R _ {2}} e _ {o}\right)$$

where K is the differential gain of the amplifier. From this last equation, we get

$$e _ {i} = \left(\frac {R _ {1}}{R _ {1} + R _ {2}} + \frac {1}{K}\right) e _ {o}$$

Since ifK  1, $R _ { 1 } / { \left( R _ { 1 } + R _ { 2 } \right) } \gg 1 / K$ then,

$$e _ {o} = \left(1 + \frac {R _ {2}}{R _ {1}}\right) e _ {i}$$

This equation gives the output voltage $e _ { o } .$ . Since $e _ { o }$ and $e _ { i }$ have the same signs, the op-amp circuit shown in Figure 3–15(a) is noninverting.

Figure 3–15 (a) Noninverting operational amplifier; (b) equivalent circuit.   
![](image/43a61961d64952d179b29fcd9fee152d32f3cea2c93f0666306db1f305e50f6f.jpg)

<details>
<summary>text_image</summary>

R₁
R₂
eᵢ
eₒ
</details>

(a)

![](image/0ccf411f8c60733fdcf26c5d9aafdeb5a28132d23ae4ad77cf3691658c4ce0e8.jpg)

<details>
<summary>text_image</summary>

ei
+
-
R2
R1
eo
</details>

(b)
