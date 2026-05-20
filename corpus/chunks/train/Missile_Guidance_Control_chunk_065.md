Pitch: $\frac { n _ { z } ( s ) } { n _ { z _ { \mathrm { c m d } } } ( s ) } = \frac { \omega ^ { 2 } ( \tau s + 1 ) } { s ^ { 2 } + 2 \zeta \omega s + \omega ^ { 2 } }$ ω2(τ s + 1)

Yaw: $\frac { n _ { y } ( s ) } { n _ { \mathrm { y _ { c m d } } } ( s ) } = \frac { \omega ^ { 2 } } { s ^ { 2 } + 2 \zeta \omega s + \omega ^ { 2 } }$ ny (s) ω2

where τ is the time constant, s is the Laplace operator, and ω is the frequency.

Under 6-DOF modeling, the $d \mu / d t , d \gamma / d t$ , and $d \beta / d t$ kinematic relationships are

$$\frac {d \mu}{d t} = P + \tan \gamma (Q \sin \mu + R \cos \mu),\frac {d \gamma}{d t} = Q \cos \mu - R \sin \mu ,\frac {d \beta}{d t} = \sec \gamma (Q \sin \mu + R \cos \mu),$$

where

$$P = \text { body axes roll rate },Q = \text { body axes pitch rate },R = \text { body axes yaw rate }.$$

Next, in order to eliminate the $d \beta / d t$ equations anomaly at $\gamma = \pm 9 0 ^ { \circ }$ , the quaternion system of coordinates will be used; the kinematic rate equations are [7]

$$\frac {d e _ {1}}{d t} = (- e _ {4} P - e _ {3} Q - e _ {2} R) / 2,\frac {d e _ {2}}{d t} = (- e _ {3} P - e _ {4} Q - e _ {1} R) / 2,\frac {d e _ {3}}{d t} = (- e _ {2} P + e _ {1} Q - e _ {4} R) / 2,\frac {d e _ {4}}{d t} = (- e _ {1} P - e _ {2} Q + e _ {3} R) / 2,$$

and the Earth-to-body direction cosine matrix is, as before,

$$
C _ {e} ^ {b} = \left[ \begin{array}{c c c} C _ {1 1} & C _ {1 2} & C _ {1 3} \\ C _ {2 1} & C _ {2 2} & C _ {2 3} \\ C _ {3 1} & C _ {3 2} & C _ {3 3} \end{array} \right],
$$

where

$$
\begin{array}{l} C _ {1 1} = e _ {1} ^ {2} - e _ {2} ^ {2} - e _ {3} ^ {2} + e _ {4} ^ {2}, \\ C _ {1 2} = 2 \left(e _ {3} e _ {4} + e _ {1} e _ {2}\right), \\ C _ {1 3} = 2 \left(e _ {2} e _ {4} - e _ {1} e _ {3}\right), \\ C _ {2 1} = 2 \left(e _ {3} e _ {4} - e _ {1} e _ {2}\right), \\ C _ {2 2} = e _ {1} ^ {2} - e _ {2} ^ {2} + e _ {3} ^ {2} - e _ {4} ^ {2}, \\ C _ {2 3} = 2 \left(e _ {2} e _ {3} + e _ {1} e _ {4}\right), \\ C _ {3 1} = 2 \left(e _ {1} e _ {3} + e _ {2} e _ {4}\right), \\ C _ {3 2} = 2 \left(e _ {2} e _ {3} - e _ {1} e _ {4}\right), \\ C _ {3 3} = e _ {1} ^ {2} + e _ {2} ^ {2} - e _ {3} ^ {2} - e _ {4} ^ {2}, \\ \end{array}
$$

and

$$
\begin{array}{l} \beta = \tan^ {- 1} (C _ {1 2} / C _ {1 1}), \\ \gamma = - \sin^ {- 1} (C _ {1 3}), \\ \mu = \tan^ {- 1} (C _ {2 3} / C _ {3 3}). \\ \end{array}
$$

Finally, we note that the same 6-DOF equations of motion can be used to model both aircraft and missiles.

Example 2. Based on the discussion thus far, let us now consider in this example a 6-DOF aerodynamic model. Furthermore, let us assume an NED coordinate system, in which all units are metric. This model is designed for a generic aircraft. A quaternion fast-processing technique will be employed to simulate aircraft navigation. This technique avoids not only time-consuming trigonometric computations in the fast-rate direction cosine updating, but also singularities in aircraft attitude determination [7].
