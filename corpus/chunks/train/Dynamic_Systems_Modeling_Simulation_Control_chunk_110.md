# Example 3.2

Figure 3.8 shows a series RLC circuit with a voltage source. Derive the mathematical model of the electrical system.

This circuit contains two energy-storage elements: inductor L and capacitor C. Therefore, the model consists of two first-order ODEs in terms of capacitor voltage $e _ { C }$ and inductor current $I _ { L }$

$\mathrm { C a p a c i t o r ~ v o l t a g e } { : } \quad { \cal C } \dot { e } _ { C } = { \cal I } _ { L }$ (3.20)

$\mathrm { I n d u c t o r ~ c u r r e n t : } \qquad L \dot { I } _ { L } = e _ { L }$ (3.21)

The two important dynamic variables are capacitor voltage $e _ { C }$ and inductor current $I _ { L } ,$ , and the system input is source voltage $e _ { \mathrm { i n } } ( t )$ . Hence, Eq. (3.20) is already complete, because its right-hand side is expressed in terms of the current $I _ { L } .$ Next, we must express the inductor voltage $e _ { L }$ in Eq. (3.21) in terms of $e _ { C } , I _ { L } ,$ , or $e _ { \mathrm { i n } } ( t )$ ). To do so, we apply Kirchhoff’s voltage law around the single loop in a clockwise direction

$$- e _ {R} - e _ {L} - e _ {C} + e _ {\mathrm{in}} (t) = 0 \tag {3.22}$$

Substituting Ohm’s law $( e _ { R } = R I _ { L } )$ into Eq. (3.22) and solving for inductor voltage $e _ { L }$ yields

$$e _ {L} = - R I _ {L} - e _ {C} + e _ {\text { in }} (t) \tag {3.23}$$

Equation (3.23) can be substituted into Eq. (3.21) to yield

$$L \dot {I} _ {L} = - R I _ {L} - e _ {C} + e _ {\text { in }} (t) \tag {3.24}$$

Finally, moving all terms involving the dynamic variables $e _ { C }$ and $I _ { L }$ in Eqs. (3.20) and (3.24) to the left-hand sides yields

$$C \dot {e} _ {C} - I _ {L} = 0 \tag {3.25}L \dot {I} _ {L} + R I _ {L} + e _ {C} = e _ {\text { in }} (t) \tag {3.26}$$

Equations (3.25) and (3.26) are the mathematical modeling equations for the series RLC electrical system. The complete system is linear and second order because it consists of two first-order, linear, coupled ODEs.

Because this electrical system is simple, we can derive another form of the mathematical model directly from Kirchhoff’s voltage law, Eq. (3.22), repeated below

$$- e _ {R} - e _ {L} - e _ {C} + e _ {\text { in }} (t) = 0 \tag {3.27}$$

Next, substitute the appropriate expressions for the voltage drops across each of the three passive elements

$$- R I _ {L} - L \dot {I} _ {L} - e _ {C} (0) - \frac {1}{C} \int I _ {L} d t + e _ {\text { in }} (t) = 0 \tag {3.28}$$

![](image/afa40240f6e459edf16042af93a84451865d74b97463b2847a44cd19ea0ec75f.jpg)

<details>
<summary>text_image</summary>

R
L
+
e_in(t)
-
I_L
C
</details>

Figure 3.8 Series RLC circuit for Example 3.2.
