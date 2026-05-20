$$
\begin{array}{l} \frac {Y (s)}{X (s)} = \frac {1}{s \left[ \left(\frac {m K _ {2}}{A K _ {1}}\right) s + \frac {b K _ {2}}{A K _ {1}} + \frac {A \rho}{K _ {1}} \right]} \\ = \frac {K}{s (T s + 1)} \tag {4-29} \\ \end{array}
$$

where

$$K = \frac {1}{\frac {b K _ {2}}{A K _ {1}} + \frac {A \rho}{K _ {1}}} \quad \text { and } \quad T = \frac {m K _ {2}}{b K _ {2} + A ^ {2} \rho}$$

From Equation (4–29) we see that this transfer function is of the second order. If the ratio m ${ \cal K } _ { 2 } / \big ( b \bar { \cal K } _ { 2 } + { \cal A } ^ { 2 } \rho \big )$ is negligibly small or the time constant $T$ is negligible, the transfer function $Y ( s ) / X ( s )$ can be simplified to give

$$\frac {Y (s)}{X (s)} = \frac {K}{s}$$

It is noted that a more detailed analysis shows that if oil leakage, compressibility (including the effects of dissolved air), expansion of pipelines, and the like are taken into consideration, the transfer function becomes

$$\frac {Y (s)}{X (s)} = \frac {K}{s \left(T _ {1} s + 1\right) \left(T _ {2} s + 1\right)}$$

where $T _ { 1 }$ and $T _ { 2 }$ are time constants. As a matter of fact, these time constants depend on the volume of oil in the operating circuit. The smaller the volume, the smaller the time constants.

Hydraulic Integral Controller. The hydraulic servomotor shown in Figure 4–19 is a pilot-valve-controlled hydraulic power amplifier and actuator. Similar to the hydraulic servo system shown in Figure 4–17, for negligibly small load mass the servomotor shown in Figure 4–19 acts as an integrator or an integral controller. Such a servomotor constitutes the basis of the hydraulic control circuit.

In the hydraulic servomotor shown in Figure 4–19, the pilot valve (a four-way valve) has two lands on the spool. If the width of the land is smaller than the port in the valve sleeve,the valve is said to be underlapped.Overlapped valves have a land width greater than the port width. A zero-lapped valve has a land width that is identical to the port width. (If the pilot valve is a zero-lapped valve, analyses of hydraulic servomotors become simpler.)

In the present analysis, we assume that hydraulic fluid is incompressible and that the inertia force of the power piston and load is negligible compared to the hydraulic force at the power piston. We also assume that the pilot valve is a zero-lapped valve, and the oil flow rate is proportional to the pilot valve displacement.
