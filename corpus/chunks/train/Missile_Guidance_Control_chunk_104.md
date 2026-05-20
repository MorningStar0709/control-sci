# Rotation Equations

(4) Roll Acceleration

$$\frac {d P}{d t} = \left(q S l _ {r e f} / I _ {x}\right) \left[ C _ {L} \left(\delta_ {a}\right) + C _ {L} \left(\alpha_ {p}\right) + C _ {L} \left(\alpha_ {y}\right) \right] + Q R \left[ \left(I _ {y} - I _ {z}\right) / I _ {x} \right]. \tag {3.53d}$$

(5) Pitch Acceleration

$$
\begin{array}{l} \frac {d Q}{d t} = (q S l _ {r e f} / I _ {y}) [ C _ {M} + C _ {N} ((d _ {c g} - d _ {c g - r e f}) / l _ {r e f}) + C _ {M} (Q l _ {r e f} / 2 V _ {M}) ] \\ + P R \left[ \left(I _ {z} - I _ {x}\right) / I _ {y} \right]. \tag {3.53e} \\ \end{array}
$$

(6) Yaw Acceleration

$$
\begin{array}{l} \frac {d R}{d t} = \left(q S l _ {r e f} / I _ {z}\right) \left[ C _ {N} - C _ {Y} \left(\left(d _ {c g} - d _ {c g - r e f}\right) / l _ {r e f}\right) + C _ {N} \left(R l _ {r e f} / 2 V _ {M}\right) \right] \\ + P Q \left[ \left(I _ {x} - I _ {y}\right) / I _ {z} \right]. \tag {3.53f} \\ \end{array}
$$

Example 1. In Section 2.1, the transformation matrix from the Earth to body axes was developed. Consider now the free-flight dynamic model of a missile. The mathematical model describing the missile motion consists of six rigid-body degrees of freedom (i.e., three body inertial position coordinates and three Euler-angle body attitudes). In this example, we will use the Earth’s surface (or ground) as the inertial reference frame. The body frame is defined in the conventional manner, and the dynamic equations are written with respect to this coordinate system [9]. The missile’s translation and rotation kinematic and dynamic equations are given by

$$
\left[ \begin{array}{c} \dot {x} \\ \dot {y} \\ \dot {z} \end{array} \right] = \left[ \begin{array}{c c c} c _ {\theta} c _ {\psi} & s _ {\phi} s _ {\theta} c _ {\psi} - c _ {\phi} s _ {\psi} & c _ {\phi} s _ {\theta} c _ {\psi} + s _ {\phi} s _ {\psi} \\ c _ {\theta} s _ {\psi} & s _ {\phi} s _ {\theta} s _ {\psi} + c _ {\phi} c _ {\psi} & c _ {\phi} s _ {\theta} s _ {\psi} - s _ {\phi} c _ {\psi} \\ - s _ {\theta} & s _ {\phi} c _ {\theta} & c _ {\phi} c _ {\theta} \end{array} \right] \left[ \begin{array}{c} u \\ v \\ w \end{array} \right], \tag {1}

\left[ \begin{array}{c} \dot {\phi} \\ \dot {\theta} \\ \dot {\psi} \end{array} \right] = \left[ \begin{array}{c c c} 1 & s _ {\phi} t _ {\theta} & c _ {\phi} t _ {\theta} \\ 0 & c _ {\theta} & - s _ {\phi} \\ 0 & s _ {\phi} / c _ {\theta} & c _ {\phi} / c _ {\theta} \end{array} \right] \left[ \begin{array}{c} P \\ Q \\ R \end{array} \right], \tag {2}
