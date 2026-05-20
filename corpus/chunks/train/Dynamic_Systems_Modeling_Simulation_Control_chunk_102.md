# Capacitor

Two conductors separated by a nonconducting medium form a capacitor. One example is metallic parallel plates separated by a thin dielectric material. Capacitors store energy in the electric field that results from a voltage potential across the two conductors. Figure 3.2 shows the symbol for a two-terminal capacitor with current I and voltage potential $e _ { C }$ across the two terminals. Ideal (linear) capacitors obey the charge–voltage relationship

$$q = C e _ {C} \tag {3.3}$$

where C is the capacitance in C/V or farads (F). Capacitance is a measure of the charge that can be stored for a given voltage across the conductors. Capacitance C depends on material and geometric properties, such as the area of the parallel plates and the distance between the two plates. We can relate capacitance to current by taking the time derivative of Eq. (3.3)

$$\dot {q} = I = C \dot {e} _ {C} \tag {3.4}$$

![](image/ef684d3e608b6d6311c26abf9d92e2f2ee5fc608dce1e80cd0591a5650f3a262.jpg)

<details>
<summary>chemical</summary>

Simple electrical circuit diagram with capacitor and current direction labels
</details>

Figure 3.2 Capacitor element.

The voltage drop across a capacitor can be obtained by integrating Eq. (3.4)

$$e _ {C} (t) = e _ {C} (0) + \frac {1}{C} \int_ {0} ^ {t} I (\tau) d \tau \tag {3.5}$$

Capacitors can store energy due to their voltage

$$\xi_ {C} = \frac {1}{2} C e _ {C} ^ {2} \tag {3.6}$$

The time derivative of Eq. (3.6) yields the power

$$\dot {\xi} _ {C} = C e _ {C} \dot {e} _ {C} \tag {3.7}$$

Substituting Eq. (3.4) for $C \dot { e } _ { C }$ in Eq. (3.7), we see that power is voltage × current.
