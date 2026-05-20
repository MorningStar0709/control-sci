$$e _ {O} \left(1 + \frac {K R _ {1}}{R _ {1} + R _ {2}}\right) = - \frac {K R _ {2}}{R _ {1} + R _ {2}} e _ {\text { in }} (t) \tag {3.70}$$

Equation (3.70) can be simplified by multiplying both sides by $R _ { 1 } + R _ { 2 }$

$$e _ {O} (R _ {1} + R _ {2} + K R _ {1}) = - K R _ {2} e _ {\text { in }} (t) \tag {3.71}$$

Finally, the output voltage is

$$e _ {O} = \frac {- K R _ {2}}{R _ {1} + R _ {2} + K R _ {1}} e _ {\mathrm{in}} (t) \tag {3.72}$$

Because the gain K is extremely large, we can take the limit of Eq. (3.72) as K → ∞ to obtain the output voltage relationship for an ideal op-amp circuit

$$e _ {O} = \frac {- R _ {2}}{R _ {1}} e _ {\text { in }} (t) \tag {3.73}$$

Equation (3.73) shows that the output voltage of the op-amp circuit can be controlled by selecting the values of the two resistors $R _ { 1 }$ and $R _ { 2 }$ . Note that the particular value of the op-amp gain K does not factor into the output voltage – the only requirement is that the gain K is very high. Because the output voltage $e _ { O }$ has the opposite sign of the input voltage, the circuit in Fig. 3.13 is called an inverting amplifier. The input-output voltage relationship of Eq. (3.73) is an algebraic equation and is not an ODE because the circuit does not contain any energy-storage elements.

Note that the op-amp input voltage $e _ { A }$ can be obtained by substituting the output voltage defined by Eq. (3.73) into Eq. (3.68)

$$e _ {A} = \frac {R _ {2}}{R _ {1} + R _ {2}} e _ {\text { in }} (t) + \frac {R _ {1}}{R _ {1} + R _ {2}} \frac {- R _ {2}}{R _ {1}} e _ {\text { in }} (t) = 0 \tag {3.74}$$

Hence, the negative feedback connection in Fig. 3.13 between the op-amp output and input terminals results in $e _ { A } = 0$ . Because $e _ { B } = 0$ , the voltage difference at the input terminals is $e _ { B } - e _ { A } = 0$ , which is the second characteristic of an ideal op amp.
