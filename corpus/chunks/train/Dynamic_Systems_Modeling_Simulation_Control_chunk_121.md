# Example 3.7

Figure 3.14 shows an op-amp circuit with input voltage $e _ { \mathrm { i n } } ( t )$ , output voltage $e _ { O } ,$ , and a capacitor C in a branch connecting output and input terminals. Derive the relationship between input and output voltages.

Because this op-amp circuit contains a negative feedback connection between output and input terminals, we use the ideal op-amp characteristics and set $e _ { A } = 0$ (positive input terminal $e _ { B } = 0$ as it is connected to the ground). Furthermore, the op amp draws no current $( I _ { A } = 0 )$ , so applying Kirchhoff’s current law at the top node yields

$$I _ {1} = I _ {2} + I _ {3} \tag {3.75}$$

We can substitute Ohm’s law for currents $I _ { 1 }$ and $I _ { 2 }$ and the governing equation for a capacitor, Eq. (3.4) for current $I _ { 3 }$ into Eq. (3.75) to yield

$$\frac {e _ {\text { in }} (t) - e _ {A}}{R _ {1}} = \frac {e _ {A} - e _ {O}}{R _ {2}} + C \frac {d}{d t} (e _ {A} - e _ {O}) \tag {3.76}$$

![](image/f4bb4aa09315d0c7750be5332466dbcfabccde19b59543b3299f9cbf8a862a85.jpg)

<details>
<summary>text_image</summary>

C
→ I₃
R₁ R₂
I₁ Iₐ
eₐ
K
eₐ
+
-
eᵢₙ(t)
-
</details>

Figure 3.14 Op-amp circuit for Example 3.7.

Setting $e _ { A } = 0$ because of the negative feedback connection between output and input terminals, Eq. (3.76) becomes

$$\frac {e _ {\text {in}} (t)}{R _ {1}} = \frac {- e _ {O}}{R _ {2}} + C \frac {d}{d t} (- e _ {O}) \tag {3.77}$$

which can be rewritten as

$$R _ {2} C \dot {e} _ {O} + e _ {O} = \frac {- R _ {2}}{R _ {1}} e _ {\text { in }} (t) \tag {3.78}$$

Equation (3.78) is a first-order ODE model of the op-amp circuit in Fig. 3.14. We obtain a dynamic model (an ODE) as the circuit includes an energy-storage element (capacitor C). Clearly, if the capacitor is removed, the circuit becomes the inverting amplifier in Example 3.6 and Eq. (3.78) becomes Eq. (3.73).
