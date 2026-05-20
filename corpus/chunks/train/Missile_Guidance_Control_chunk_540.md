We note here that $\mathbf { V } _ { R }$ has either two or three components, depending on the number of guidance constraints to be satisfied. The implicit dependence on choosing a time of flight in order to obtain the one-parameter family of $V _ { R }$ and $\gamma$ may be avoided if it is more desirable to obtain a flight path angle such that one obtains a given range for a minimum burnout velocity. The flight path angle that satisfies this condition is the optimum burnout angle $\gamma ^ { * }$ , obtained by differentiating (6.89) with respect to $\gamma$ and equating the resulting expression to zero. Performing this, one obtains the optimum burnout angle in the form

$$\gamma^ {*} = \frac {1}{2} \tan^ {- 1} [ \sin \phi / (\cos \phi - (r _ {i} / r _ {t})) ]. \tag {6.90}$$

Equation (6.90) gives the well-known minimum energy trajectory. Therefore, once the target is chosen and the vehicle’s position is determined, the required spherical Earth velocity may be computed and processed to provide input information for the autopilot. Finally, we need to compute the spherical-Earth time of flight. The time of flight for a ballistic trajectory, besides determining $V _ { R }$ and $\gamma$ uniquely, serves certain tactical purposes for an ICBM mission. It specifies the location of the target at the time of arrival when inertial coordinates are used, thus taking into account the effect of the Earth’s rotation (see Section 6.4.3.1).

The time of flight to reach the target can be derived in a similar manner as was done in the derivation of Lambert’s theorem, in Section 6.3. If we assume that $E _ { v }$ is the eccentric anomaly of the vehicle, and $E _ { t }$ the eccentric anomaly of the target, then

$$E _ {v} = \cos^ {- 1} [ (1 / e) (1 - (r _ {i} / a)) ], \tag {6.91a}E _ {t} = \cos^ {- 1} [ (1 / e) (1 - (r _ {t} / a)) ], \tag {6.91b}$$

where

$$e = \{[ (r _ {i} V _ {R} \cos \gamma) ^ {2} / \mu a ] + (1 - (r _ {i} / a) ^ {2}) \} ^ {1 / 2}.$$

Substituting these equations into (6.50), we have

$$t _ {f f} = (\sqrt {a ^ {3} / \mu}) [ (E _ {t} - E _ {v}) - e (\sin E _ {t} - \sin E _ {v}) ]. \tag {6.92}$$
