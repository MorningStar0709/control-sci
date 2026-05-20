Figure 3.25 MEMS comb-drive actuator.

![](image/bfa16c5da85ae177183c8ef58ef29ca1a461490c91aa9b68c455aa4ae557959e.jpg)

<details>
<summary>text_image</summary>

R
e_in(t)
+
-
C(x)
I
Comb circuit
x
Drive comb
mass, m
F_es
k
b
</details>

Figure 3.26 Schematic diagram of a MEMS comb-drive actuator.

where n is the number of fingers, $\varepsilon _ { 0 }$ is the dielectric constant in air (in F/m), A is the overlapping area of the fingers, and d is the gap spacing between fingers [3–5]. Overlapping area A is the product of finger width w and overlap distance $x _ { 0 } + x ,$ , where $x _ { 0 }$ is the initial overlap between fingers when the comb is uncharged and undeflected (zero electrostatic force). Figures 3.25 and 3.26 and Eq. (3.105) show that pulling the drive comb to the left (x > 0) increases the overlap area and therefore increases the capacitance C(x).

As with the electromagnetic actuators, we develop the complete mathematical model of the comb-drive actuator by applying Kirchhoff’s laws to the comb circuit and Newton’s laws to the single inertia element. However, computing the comb capacitor voltage $e _ { C }$ is somewhat complicated because capacitance changes with position x. We begin with the capacitor’s basic charge–voltage relation (3.3):

$$q = C (x) e _ {C} \tag {3.106}$$

The time derivative of the charge is current, I

$$\dot {q} = \frac {d C}{d t} e _ {C} + C \frac {d e _ {C}}{d t} = I \tag {3.107}$$

Using the chain rule to expand dC∕dt, Eq. (3.107) becomes

$$\dot {q} = \frac {d C}{d x} \frac {d x}{d t} e _ {C} + C \frac {d e _ {C}}{d t} = I \tag {3.108}$$

or, using the compact notation

$$\dot {q} = C _ {x} \dot {x} e _ {C} + C (x) \dot {e} _ {C} = I \tag {3.109}$$

where $C _ { x }$ is short-hand notation for the derivative dC∕dx. Using Eq. (3.105), the derivative dC∕dx is

$$C _ {x} \equiv \frac {d C}{d x} = \frac {n \varepsilon_ {0} w}{d} \tag {3.110}$$

Hence, the change in capacitance because of position x is a constant. We can substitute Ohm’s law $I = e _ { R } / R$ for current in Eq. (3.109) and determine resistor voltage $e _ { R }$ by applying Kirchhoff’s voltage law around the loop

$$- e _ {R} - e _ {C} + e _ {\text { in }} (t) = 0 \tag {3.111}$$

Substituting $I = ( e _ { \mathrm { i n } } ( t ) - e _ { C } ) / R$ into Eq. (3.109) yields

$$R C (x) \dot {e} _ {C} + e _ {C} = e _ {\text { in }} (t) - R C _ {x} \dot {x} e _ {C} \tag {3.112}$$
