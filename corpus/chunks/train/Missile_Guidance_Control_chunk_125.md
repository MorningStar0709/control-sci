<table><tr><td>Feature</td><td>Sparrow-type weapon</td><td>Bank-to-turn weapon</td></tr><tr><td>Guidance Mode</td><td>Skid-to-Turn</td><td>Bank-to-Turn</td></tr><tr><td>Control Surfaces</td><td>Wing Control</td><td>Tail Control</td></tr><tr><td>Autopilot Sensors</td><td>Accelerometers/Rate Gyros</td><td>Accelerometers/Rate Gyros</td></tr><tr><td>Maximum Acceleration</td><td>45g&#x27;s (32 g&#x27;s per axis)</td><td>100 g&#x27;s in pitch, 10 g&#x27;s in yaw</td></tr><tr><td>Guidance Delay</td><td>0.75 seconds</td><td>0.40 seconds</td></tr><tr><td>Launch Speed</td><td>0.5–2.0 Mach</td><td>0.5–2.0 Mach</td></tr><tr><td>Speed Range</td><td>0.5–3.0 Mach</td><td>0.5–4.0 Mach</td></tr><tr><td>Maximum Roll Rate</td><td>Not Applicable</td><td> $\pm 600^{\circ}$ /sec</td></tr></table>

This configuration is suitable for highly maneuverable ramjet missiles. However, the asymmetrical airframe of this missile design requires rolling the missile to maintain target motion in the missile pitch plane. Another drawback of this design is that the bank angle causes a coupling between the pitch and yaw channel dynamics, which can vary considerably even for a short period of time. Table 3.2 summarizes the skid-to-turn and bank-to-turn missile characteristics.

Specifically, the pitch/yaw plane rotational responses behave like a spring– mass damper system. Mathematically, this system response can be expressed in the form

$$\frac {d ^ {2} y}{d t ^ {2}} + 2 \zeta \omega \left(\frac {d y}{d t}\right) + \omega^ {2} y = \omega^ {2} u (t). \tag {3.54}$$

Equation (3.54) can also be written in the usual frequency domain as follows:

$$y (s) / u (s) = \omega^ {2} / (s ^ {2} + 2 \zeta \omega s + \omega^ {2}), \tag {3.55}$$

where

$$
\begin{array}{l} y (s) = \text { output }, \\ u (s) = \text { input }, \\ \zeta = \text { damping   ratio   (dimensionless) }, \\ \omega = \text { frequency   (rad / sec) }, \\ s = \text { Laplace   operator   (rad / sec) }. \\ \end{array}
$$

The above continuous system can be constructed in a simulation as a feedback network that represents a load factor command system in both pitch/yaw planes (see also Section 3.5). Figure 3.17 represents a typical pitch/yaw network.

![](image/ed035b3ec08838221b5fbb7c82c2ea90e3f89ee049617de7d757969161c21277.jpg)

<details>
<summary>flowchart</summary>
