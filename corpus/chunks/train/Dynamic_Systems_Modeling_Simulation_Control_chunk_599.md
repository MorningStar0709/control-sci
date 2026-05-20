This example has essentially validated the results obtained in Example 10.6, which also used a PD controller (both examples use the same mechanical-system plant). In Example 10.6, the PD gains were set at $K _ { P } = 1 6 \mathrm { V } / \mathrm { m }$ and $K _ { D } = 4 \mathrm { V - s / m } ;$ ; in this example, the PD gains gleaned from the root-locus design point are $K = K _ { D } = 5 . 5 1 4 { \mathrm { V } } -$ s/m and $K _ { P } = 3 K = 1 6 . 5 4 2 \ : \mathrm { V / m }$ . Because these two PD gain settings are similar, the two corresponding closed-loop responses are similar (compare Figs. 10.20 and 10.43). However, this example has demonstrated how the rootlocus method can be used to visualize the effect of adding a PD controller and select the gains for a good transient response.

As a final note, we briefly investigate the consequences of placing the open-loop zero of the PD controller even farther to the left. Suppose we double the open-loop zero and use a PD controller with a zero at s = −6

$$G _ {C} (s) = K (s + 6) = K _ {P} + K _ {D} s$$

Hence, the open-loop transfer function is

$$G (s) H (s) = \frac {2 (s + 6)}{s ^ {2} + 0 . 3 s}$$
