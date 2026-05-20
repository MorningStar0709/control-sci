# 6.2.6 State Estimation

Given output measurements, we can express the state estimation problem also in distributed form. Player one uses local measurements of $y _ { 1 }$ and knowledge of both inputs $u _ { 1 }$ and $u _ { 2 }$ to estimate state $x _ { 1 }$

$$\hat {x} _ {1} ^ {+} = A _ {1} \hat {x} _ {1} + \overline {{B}} _ {1 1} u _ {1} + \overline {{B}} _ {1 2} u _ {2} + L _ {1} (y _ {1} - C _ {1} \hat {x} _ {1})$$

Defining estimate error to be $e _ { 1 } = x _ { 1 } - \hat { x } _ { 1 }$ gives

$$e _ {1} ^ {+} = (A _ {1} - L _ {1} C _ {1}) e _ {1}$$

Because all the subsystems are stable, we know $L _ { 1 }$ exists so that $A _ { 1 } -$ $L _ { 1 } C _ { 1 }$ is stable and player one’s local estimator is stable. The estimate error for the two subsystems is then given by

$$
\left[ \begin{array}{l} e _ {1} \\ e _ {2} \end{array} \right] ^ {+} = \left[ \begin{array}{c c} A _ {L 1} & \\ & A _ {L 2} \end{array} \right] \left[ \begin{array}{l} e _ {1} \\ e _ {2} \end{array} \right] \tag {6.18}
$$

in which $A _ { L i } = A _ { i } - L _ { i } C _ { i }$ .

Closed-Loop Stability. The dynamics of the estimator are given by

$$
\begin{array}{l} \left[ \begin{array}{c} \hat {x} _ {1} \\ \hat {x} _ {2} \end{array} \right] ^ {+} = \left[ \begin{array}{c c} A _ {1} & \\ & A _ {2} \end{array} \right] \left[ \begin{array}{c} \hat {x} _ {1} \\ \hat {x} _ {2} \end{array} \right] + \left[ \begin{array}{c c} \overline {{B}} _ {1 1} & \overline {{B}} _ {1 2} \\ \overline {{B}} _ {2 1} & \overline {{B}} _ {2 2} \end{array} \right] \left[ \begin{array}{c} u _ {1} \\ u _ {2} \end{array} \right] + \\ \left[ \begin{array}{c c} L _ {1} C _ {1} & \\ & L _ {2} C _ {2} \end{array} \right] \left[ \begin{array}{c} e _ {1} \\ e _ {2} \end{array} \right] \\ \end{array}
$$

In the control law we use the state estimate in place of the state, which is unmeasured and unknown. We consider two cases.

Converged controller. In this case the distributed control law converges to the centralized controller, and we have

$$
\left[ \begin{array}{c} u _ {1} \\ u _ {2} \end{array} \right] = \left[ \begin{array}{c c} K _ {1 1} & K _ {1 2} \\ K _ {2 1} & K _ {2 2} \end{array} \right] \left[ \begin{array}{c} \hat {x} _ {1} \\ \hat {x} _ {2} \end{array} \right]
$$

The closed-loop system evolves according to
