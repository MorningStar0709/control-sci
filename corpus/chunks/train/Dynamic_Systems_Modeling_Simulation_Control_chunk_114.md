# Example 3.4

Figure 3.10 shows a dual-loop electrical system driven by a current source. Derive the mathematical model of the electrical system.

Because this system has only one energy-storage element, we begin with the basic modeling equation for a capacitor

$$\text { Capacitor voltage: } \quad C \dot {e} _ {C} = I _ {C} \tag {3.43}$$

Next, we use Kirchhoff’s current law at the node marked $\ " { } ^ { 6 6 } { \mathrm { A } } ^ { 3 5 }$ in Fig. 3.10

$$I _ {\text { in }} (t) - I _ {C} - I _ {2} = 0 \tag {3.44}$$

![](image/af0e18cd56d27be6009b1a5420c61f61486b2cdf5d926f6e19265f1108a7e72e.jpg)

<details>
<summary>text_image</summary>

Iin(t)
A
R1
IC
C
R2
I2
</details>

Figure 3.10 Electrical system for Example 3.4.

Therefore, substituting Eq. (3.44) for capacitor current in Eq. (3.43) we obtain

$$C \dot {e} _ {C} = I _ {\mathrm{in}} (t) - I _ {2} \tag {3.45}$$

Hence, we need an expression for current through resistor $R _ { 2 } .$ . Applying Kirchhoff’s voltage law to the right-hand loop in Fig. 3.10 (moving clockwise) yields

$$- e _ {R _ {2}} + e _ {C} + e _ {R _ {1}} = 0 \tag {3.46}$$

We can express both resistor voltage drops in Eq. (3.46) using Ohm’s law

$$- R _ {2} I _ {2} + e _ {C} + R _ {1} I _ {C} = 0 \tag {3.47}$$

Substituting $I _ { C } = I _ { \mathrm { i n } } ( t ) - I _ { 2 }$ in Eq. (3.47) yields

$$- R _ {2} I _ {2} + e _ {C} + R _ {1} (I _ {\mathrm{in}} (t) - I _ {2}) = 0 \tag {3.48}$$

Grouping terms in Eq. (3.48) that involve current through resistor $R _ { 2 } { \mathrm { : } }$ , we obtain

$$(R _ {1} + R _ {2}) I _ {2} = e _ {C} + R _ {1} I _ {\text { in }} (t) \tag {3.49}$$

Finally, we can solve Eq. (3.49) for current $I _ { 2 }$ and substitute the result into Eq. (3.45) to obtain the dynamic equation for the capacitor

$$C \dot {e} _ {C} = I _ {\text { in }} (t) - \frac {e _ {C}}{R _ {1} + R _ {2}} - \frac {R _ {1} I _ {\text { in }} (t)}{R _ {1} + R _ {2}} \tag {3.50}$$

Multiplying Eq. (3.50) by $R _ { 1 } + R _ { 2 }$ and rearranging yields

$$(R _ {1} + R _ {2}) C \dot {e} _ {C} + e _ {C} = R _ {2} I _ {\text { in }} (t) \tag {3.51}$$

Equation (3.51) is the mathematical modeling equation for the electrical system. The system is a linear firstorder ODE as the circuit consists of a single capacitor. The reader should note that all terms in Eq. (3.51) are voltages.
