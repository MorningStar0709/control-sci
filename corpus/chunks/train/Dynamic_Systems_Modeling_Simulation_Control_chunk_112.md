# Example 3.3

Figure 3.9 shows a parallel RLC circuit driven by a current source. Derive the mathematical model of the electrical system.

We begin the model development as we did in Example 3.2: this circuit contains two energy-storage elements, inductor L and capacitor C. Therefore, the model consists of two first-order ODEs in terms of capacitor voltage $e _ { C }$ and inductor current $I _ { L }$

$\mathrm { C a p a c i t o r v o l t a g e } ; \quad C \dot { e } _ { C } = I _ { C }$ (3.32)

$\mathrm { I n d u c t o r ~ c u r r e n t : } \qquad L \dot { I } _ { L } = e _ { L }$ (3.33)

Because the subsequent model involves only dynamic variables $e _ { C }$ and $I _ { L }$ and source current $I _ { \mathrm { i n } } ( t )$ , we must express capacitor current $I _ { C }$ and inductor voltage $e _ { L }$ in terms of these variables. We can apply Kirchhoff’s current law to the common node that connects the wires containing the current source, resistor, capacitor, and inductor. Figure 3.9 shows that currents $I _ { R } , I _ { L }$ , and $I _ { C }$ are flowing out of the top node, while source current $I _ { \mathrm { i n } } ( t )$ is flowing into the node. Hence, Kirchhoff’s current law yields

$$- I _ {R} - I _ {L} - I _ {C} + I _ {\mathrm{in}} (t) = 0 \tag {3.34}$$

which can be solved for capacitor current

$$I _ {C} = I _ {\text { in }} (t) - I _ {R} - I _ {L} \tag {3.35}$$

![](image/283b69302bbc3f96de11649bd36af8d7780e6b35ac39e86a9c292d1cc7a25370.jpg)

<details>
<summary>text_image</summary>

Iin(t)
IR
IL
IC
R
L
C
</details>

Figure 3.9 Parallel RLC circuit for Example 3.3.

Resistor current $I _ { R }$ must now be expressed in terms of $e _ { C } , I _ { L } ,$ , or $I _ { \mathrm { i n } } ( t )$ . We can apply Kirchhoff’s voltage law to any loop that contains two passive elements. For example, moving clockwise around the loop containing resistor R and inductor L yields

$$- e _ {L} + e _ {R} = 0 \tag {3.36}$$

In a similar fashion, moving clockwise around the right-end loop containing inductor L and capacitor C yields

$$- e _ {C} + e _ {L} = 0 \tag {3.37}$$

Clearly, Eqs. (3.36) and (3.37) show that all voltage drops are equal: $e _ { R } = e _ { L } = e _ { C }$ (we should recall from a university physics or elementary circuits course that two or more elements connected in a parallel circuit have the same voltage across their shared terminals). Using Ohm’s law, we can express resistor current as $I _ { R } = e _ { R } / R =$ $e _ { C } / R _ { ☉ }$ , and, therefore, the capacitor current in Eq. (3.35) becomes
