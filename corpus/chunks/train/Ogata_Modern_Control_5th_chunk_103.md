(b)   
Figure 3–18 (a) Operational-amplifier circuit; (b) operational-amplifier circuit used as a lead or lag compensator.

where

$$T = R _ {1} C _ {1}, \quad \alpha T = R _ {2} C _ {2}, \quad K _ {c} = \frac {R _ {4} C _ {1}}{R _ {3} C _ {2}}$$

Notice that

$$K _ {c} \alpha = \frac {R _ {4} C _ {1}}{R _ {3} C _ {2}} \frac {R _ {2} C _ {2}}{R _ {1} C _ {1}} = \frac {R _ {2} R _ {4}}{R _ {1} R _ {3}}, \quad \alpha = \frac {R _ {2} C _ {2}}{R _ {1} C _ {1}}$$

This network has a dc gain of $K _ { c } \alpha = R _ { 2 } R _ { 4 } / ( R _ { 1 } R _ { 3 } )$ .

Note that this network, whose transfer function is given by Equation (3–36), is a lead network if $R _ { 1 } C _ { 1 } > R _ { 2 } C _ { 2 }$ or, $\alpha < 1$ . It is a lag network if $R _ { 1 } C _ { 1 } < R _ { 2 } C _ { 2 }$ .

PID Controller Using Operational Amplifiers. Figure 3–19 shows an electronic proportional-plus-integral-plus-derivative controller (a PID controller) using operational amplifiers. The transfer function $E ( s ) / E _ { i } ( s )$ is given by

$$\frac {E (s)}{E _ {i} (s)} = - \frac {Z _ {2}}{Z _ {1}}$$

where

$$Z _ {1} = \frac {R _ {1}}{R _ {1} C _ {1} s + 1}, \quad Z _ {2} = \frac {R _ {2} C _ {2} s + 1}{C _ {2} s}$$

Thus

$$\frac {E (s)}{E _ {i} (s)} = - \left(\frac {R _ {2} C _ {2} s + 1}{C _ {2} s}\right) \left(\frac {R _ {1} C _ {1} s + 1}{R _ {1}}\right)$$

Noting that

$$\frac {E _ {o} (s)}{E (s)} = - \frac {R _ {4}}{R _ {3}}$$

![](image/6bbf88912c90c273dbf42bddf52478838b4ed2fb9c67c0f2d10d1a032d1622ed.jpg)

<details>
<summary>text_image</summary>

Z1
C1
R1
Z2
R2 C2
Ei(s)
+
-
E(s)
R3
R4
+
-
Eo(s)
</details>

Figure 3–19 Electronic PID controller.

we have

$$
\begin{array}{l} \frac {E _ {o} (s)}{E _ {i} (s)} = \frac {E _ {o} (s)}{E (s)} \frac {E (s)}{E _ {i} (s)} = \frac {R _ {4} R _ {2}}{R _ {3} R _ {1}} \frac {\left(R _ {1} C _ {1} s + 1\right) \left(R _ {2} C _ {2} s + 1\right)}{R _ {2} C _ {2} s} \\ = \frac {R _ {4} R _ {2}}{R _ {3} R _ {1}} \left(\frac {R _ {1} C _ {1} + R _ {2} C _ {2}}{R _ {2} C _ {2}} + \frac {1}{R _ {2} C _ {2} s} + R _ {1} C _ {1} s\right) \\ = \frac {R _ {4} \left(R _ {1} C _ {1} + R _ {2} C _ {2}\right)}{R _ {3} R _ {1} C _ {2}} \left[ 1 + \frac {1}{\left(R _ {1} C _ {1} + R _ {2} C _ {2}\right) s} + \frac {R _ {1} C _ {1} R _ {2} C _ {2}}{R _ {1} C _ {1} + R _ {2} C _ {2}} s \right] \tag {3-37} \\ \end{array}
$$

Notice that the second operational-amplifier circuit acts as a sign inverter as well as a gain adjuster.

When a PID controller is expressed as

$$\frac {E _ {o} (s)}{E _ {i} (s)} = K _ {p} \bigg (1 + \frac {T _ {i}}{s} + T _ {d} s \bigg)$$
