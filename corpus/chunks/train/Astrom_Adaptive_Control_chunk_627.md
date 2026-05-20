Determine values of a and b such that the closed-loop system is still asymptotically stable.

10.9 Assume that the nth-order single-input, single-output system

$$\frac {d x}{d t} = A x + B u$$

is in companion form and that the control law is of the form

$$u = - \sum_ {i = 1} ^ {n} l _ {i} x _ {i} - \mu \operatorname{sign} (\sigma (x))$$

Derive the necessary and sufficient conditions for the existence of a sliding mode. When will the sliding mode be stable?

10.10 Consider the process in Problem 1.9. Design a robust controller for the system. Investigate the disturbance rejection of the closed-loop system.

10.11 Consider the process in Problem 1.10. Design a robust controller for the system. Investigate the disturbance rejection of the closed-loop system.

10.12 Design an SOAS for the system in Problem 1.9, and investigate its properties.

10.13 Design an SOAS for the system in Problem 1.10, and investigate its properties.

10.14 Consider the process in Eqs. (10.7). Assume that the reference value is constant $y_r$ . The desired state is then

$$
x _ {d} = \left( \begin{array}{c c c c} 0 & \dots & 0 & y _ {r} \end{array} \right)
$$

Determine a controller such that $x = x_{d}$ is an asymptotically stable solution. (Hint: Introduce the state error $\tilde{x} = x - x_{d}$ , and consider the Lyapunov function $V(\tilde{x}) = \sigma^{2}(\bar{x})/2$ .)
