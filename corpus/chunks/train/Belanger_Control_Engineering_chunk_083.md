# Solution

In a circuit, capacitance voltages and inductance currents are generally valid choices for the state variables, since they describe the circuit initial conditions. (The exceptions are the case in which capacitive loops or inductive cut sets are present.) Since dv/dt = i/C for a capacitance and di/dt = v/L for an inductance, calculating the derivatives of the state variables amounts to obtaining capacitance currents and inductance voltages, as functions of the voltage or current source inputs and the state variables.

![](image/57f6bbc9d618d44b4a6d7b5780cbead642df3213d53458e9e8776324b5bb7772.jpg)

<details>
<summary>text_image</summary>

C + x₁ -
R
iₛ
R
R
+ x₂ -
C
</details>

Figure 3.1 A symmetric circuit

Since the state variable derivatives are to be calculated as functions of the state variables, the latter may be assumed known, along with the source signals. This suggests replacing capacitances with voltage sources and inductances with current sources, as in Figure 3.2. Superposition is used to calculate the separate contributions of each source to the two capacitance currents, as shown in Figure 3.3. The result is

$$i _ {c 1} = - \frac {3 x _ {1}}{2 R} + \frac {x _ {2}}{2 R} + \frac {i _ {s}}{2}i _ {c 2} = \frac {x _ {1}}{2 R} - \frac {3 x _ {2}}{2 R} + \frac {i _ {s}}{2}$$

and therefore the state equations are

$$\dot {x} _ {1} = \frac {1}{C} i _ {c 1} = - \frac {3}{2 R C} x _ {1} + \frac {1}{2 R C} x _ {2} + \frac {1}{2 C} i _ {s}\dot {x} _ {2} = \frac {1}{C} i _ {c 2} = \frac {1}{2 R C} x _ {1} - \frac {3}{2 R C} x _ {2} + \frac {1}{2 C} i _ {s}.$$

![](image/2d6c8c74c8c03b693b2849c105de687704ea807c3b4baf0876c1c760ec784943.jpg)

<details>
<summary>text_image</summary>

i_{c1}
+
-
x_1
R
R
R
i_s
R
x_2
+
-
i_{c2}
</details>

Figure 3.2 Pertaining to the state equations of the circuit

![](image/24dfa7eb6b68e1bee4879e1c7d03e8e2f561a2e6874da6a2f918e69b471d9819.jpg)

<details>
<summary>text_image</summary>

i_{c1}
+
-
x_1
R
R
R
i_{c2}
</details>

![](image/ccfebba351301b768471eec61de67370236ba778f14fb5587b23bac99d448d46.jpg)

<details>
<summary>text_image</summary>

i_{c1} R R
R i_s R
i_{c2}
</details>

![](image/ea1d4d59600d42772154e0a5b6e59c1130b8a0e9597139e30e59bb745feefad5.jpg)

<details>
<summary>text_image</summary>

i_{c1}
R R
R R
i_{c2}
+
-
x_2
</details>

Figure 3.3 Application of a superposition to the circuit

For $R = C = 1$ , they become
