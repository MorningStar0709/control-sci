# 3–3 MATHEMATICAL MODELING OF ELECTRICAL SYSTEMS

Basic laws governing electrical circuits are Kirchhoff’s current law and voltage law. Kirchhoff’s current law (node law) states that the algebraic sum of all currents entering and leaving a node is zero. (This law can also be stated as follows: The sum of currents entering a node is equal to the sum of currents leaving the same node.) Kirchhoff’s voltage law (loop law) states that at any given instant the algebraic sum of the voltages around any loop in an electrical circuit is zero. (This law can also be stated as follows: The sum of the voltage drops is equal to the sum of the voltage rises around a loop.) A mathematical model of an electrical circuit can be obtained by applying one or both of Kirchhoff’s laws to it.

This section first deals with simple electrical circuits and then treats mathematical modeling of operational amplifier systems.

LRC Circuit. Consider the electrical circuit shown in Figure 3–7. The circuit consists of an inductance L (henry), a resistance R (ohm), and a capacitance C (farad). Applying Kirchhoff’s voltage law to the system, we obtain the following equations:

$$L \frac {d i}{d t} + R i + \frac {1}{C} \int i d t = e _ {i} \tag {3-24}\frac {1}{C} \int i d t = e _ {o} \tag {3-25}$$

![](image/b1a7ac2cf4ec96bf3ca84c7b6be7c279f9b71f31dc91883ccc3757ef595a4e8d.jpg)

<details>
<summary>chemical</summary>

Electrical circuit diagram with inductor, resistor, and capacitor components labeled L, R, C, and input/output voltages ei and eo
</details>

Figure 3–7 Electrical circuit.

Equations (3–24) and (3–25) give a mathematical model of the circuit.

A transfer-function model of the circuit can also be obtained as follows: Taking the Laplace transforms of Equations (3–24) and (3–25), assuming zero initial conditions, we obtain

$$L s I (s) + R I (s) + \frac {1}{C} \frac {1}{s} I (s) = E _ {i} (s)\frac {1}{C} \frac {1}{s} I (s) = E _ {o} (s)$$

If $e _ { i }$ is assumed to be the input and $e _ { o }$ the output, then the transfer function of this system is found to be

$$\frac {E _ {o} (s)}{E _ {i} (s)} = \frac {1}{L C s ^ {2} + R C s + 1} \tag {3-26}$$

A state-space model of the system shown in Figure 3–7 may be obtained as follows: First, note that the differential equation for the system can be obtained from Equation (3–26) as

$$\ddot {e} _ {o} + \frac {R}{L} \dot {e} _ {o} + \frac {1}{L C} e _ {o} = \frac {1}{L C} e _ {i}$$

Then by defining state variables by
