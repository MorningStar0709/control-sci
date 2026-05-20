$$
\begin{array}{l} \frac {d Q}{d t} = ((I _ {z} - I _ {x}) / I _ {y}) P R + (q S l _ {r e f} / I _ {y y}) \{C _ {M} + C _ {N} ((d _ {c g} - d _ {c g - r e f}) / l _ {r e f}) \\ \left. + C _ {M} \left(Q l _ {\text { ref }} / 2 V _ {M}\right) \right\} (3.38) \\ \frac {d R}{d t} = ((I _ {x} - I _ {y}) / I _ {z}) P Q + (q S l _ {r e f} / I _ {y y}) \{C _ {N} - C _ {Y} ((d _ {c g} - d _ {c g - r e f}) / l _ {r e f}) \\ + C _ {N} (R l _ {r e f} / 2 V _ {M}) \}. (3.39) \\ \end{array}
$$

Equations (3.38) and (3.39) are the rotational accelerations for pitch and yaw, respectively. The following definitions from second-order differential equations should also be noted:

$$\text { PitchDampingMoment: } \quad C _ {M} = \partial C _ {M} / \partial (Q l _ {r e f} / 2 V _ {M}),\text { YawDampingMoment: } \quad C _ {N} = \partial C _ {N} / \partial (R l _ {r e f} / 2 V _ {M}).$$

These damping moments are important to the missile designer, in that they are necessary to keep the missile from oscillating. The rotational rates $P , \ Q$ , and R can be obtained by integrating the equations for d $P / d t , d Q / d t$ , and $d R / d t$ . Thus,

$$\text { Roll Rate: } P = \int_ {0} ^ {t} \left(\frac {d P}{d t}\right) d t, \tag {3.40a}\text { Pitch Rate: } Q = \int_ {0} ^ {t} \left(\frac {d Q}{d t}\right) d t, \tag {3.40b}\text { Yaw Rate: } R = \int_ {0} ^ {t} \left(\frac {d R}{d t}\right) d t. \tag {3.40c}$$

In terms of the Euler angles $\phi$ (roll), θ (pitch), and $\psi ( \mathrm { y a w } )$ , the rotational rates $P , Q ,$ , and R (assuming that the missile $X _ { b } \mathrm { - a x i s }$ is along the longitudinal axis, the $Y _ { b }$ -axis out to the right, and the $Z _ { b }$ -axis down) can be expressed in the form [1]

$$P = \frac {d \phi}{d t} - \left(\frac {d \psi}{d t}\right) \sin \theta , \tag {3.41d}Q = \left(\frac {d \theta}{d t}\right) \cos \phi + \left(\frac {d \psi}{d t}\right) \cos \theta \sin \phi , \tag {3.41e}R = \left(\frac {d \psi}{d t}\right) \cos \theta \cos \phi - \left(\frac {d \theta}{d t}\right) \sin \phi , \tag {3.41f}$$

or in matrix form,

$$
\left[ \begin{array}{c} P \\ Q \\ R \end{array} \right] = \left[ \begin{array}{c c c} 1 & 0 & - \sin \theta \\ 0 & \cos \phi & \cos \theta \sin \phi \\ 0 & - \sin \phi & \cos \theta \cos \phi \end{array} \right] \left[ \begin{array}{c} \dot {\phi} \\ \dot {\theta} \\ \dot {\psi} \end{array} \right].
$$
