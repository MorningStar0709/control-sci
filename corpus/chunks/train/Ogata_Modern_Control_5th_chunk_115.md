where $J _ { 0 }$ is the inertia of the combination of the motor, load, and gear train referred to the motor shaft and $b _ { 0 }$ is the viscous-friction coefficient of the combination of the motor, load, and gear train referred to the motor shaft.

By eliminating $i _ { a }$ from Equations (3–46) and (3–47), we obtain

$$\frac {\Theta (s)}{E _ {v} (s)} = \frac {K _ {1} K _ {2}}{s \left(L _ {a} s + R _ {a}\right) \left(J _ {0} s + b _ {0}\right) + K _ {2} K _ {3} s} \tag {3-48}$$

We assume that the gear ratio of the gear train is such that the output shaft rotates n times for each revolution of the motor shaft. Thus,

$$C (s) = n \Theta (s) \tag {3-49}$$

The relationship among $E _ { v } ( s ) , R ( s )$ , and $C ( s )$ is

$$E _ {v} (s) = K _ {0} [ R (s) - C (s) ] = K _ {0} E (s) \tag {3-50}$$

The block diagram of this system can be constructed from Equations (3–48), (3–49), and (3–50), as shown in Figure 3–29(b). The transfer function in the feedforward path of this system is

$$G (s) = \frac {C (s)}{\Theta (s)} \frac {\Theta (s)}{E _ {v} (s)} \frac {E _ {v} (s)}{E (s)} = \frac {K _ {0} K _ {1} K _ {2} n}{s \left[ \left(L _ {a} s + R _ {a}\right) \left(J _ {0} s + b _ {0}\right) + K _ {2} K _ {3} \right]}$$

When $L _ { a }$ is small, it can be neglected, and the transfer function $G ( s )$ in the feedforward path becomes

$$
\begin{array}{l} G (s) = \frac {K _ {0} K _ {1} K _ {2} n}{s \left[ R _ {a} \left(J _ {0} s + b _ {0}\right) + K _ {2} K _ {3} \right]} \\ = \frac {K _ {0} K _ {1} K _ {2} n / R _ {a}}{J _ {0} s ^ {2} + \left(b _ {0} + \frac {K _ {2} K _ {3}}{R _ {a}}\right) s} \tag {3-51} \\ \end{array}
$$

The term $\big [ b _ { 0 } + \big ( K _ { 2 } K _ { 3 } / R _ { a } \big ) \big ] \iota$ indicates that the back emf of the motor effectively increases thes viscous friction of the system. The inertia $J _ { 0 }$ and viscous friction coefficient $b _ { 0 } + \left( K _ { 2 } K _ { 3 } / R _ { a } \right)$ are referred to the motor shaft. When $J _ { 0 }$ and $b _ { 0 } + \left( K _ { 2 } K _ { 3 } / R _ { a } \right)$ are multiplied by $1 / n ^ { 2 }$ , the inertia and viscous-friction coefficient are expressed in terms of the output shaft. Introducing new parameters defined by

$$J = J _ {0} / n ^ {2} = \text { moment of inertia referred to the output shaft }B = \left[ b _ {0} + \left(K _ {2} K _ {3} / R _ {a}\right) \right] / n ^ {2} = \text { viscous - friction coefficient referred to the output shaft }K = K _ {0} K _ {1} K _ {2} / n R _ {a}$$

the transfer function G(s) given by Equation (3–51) can be simplified, yielding

$$G (s) = \frac {K}{J s ^ {2} + B s}$$

or

$$G (s) = \frac {K _ {m}}{s \left(T _ {m} s + 1\right)}$$

where

$$K _ {m} = \frac {K}{B}, \quad T _ {m} = \frac {J}{B} = \frac {R _ {a} J _ {0}}{R _ {a} b _ {0} + K _ {2} K _ {3}}$$

The block diagram of the system shown in Figure 3–29(b) can thus be simplified as shown in Figure 3–29(c).
