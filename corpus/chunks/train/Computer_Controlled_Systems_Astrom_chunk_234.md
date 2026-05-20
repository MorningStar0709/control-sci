# Deadbeat Control

If the desired poles are all chosen to be at the origin, the characteristic polynomial of the closed-loop system becomes

$$P (z) = z ^ {n}$$

The Cayley-Hamilton theorem then implies that the system matrix $\Phi_{c} = \Phi - \Gamma L$ of the closed-loop system satisfies

$$\Phi_ {c} ^ {n} = 0$$

This strategy has the property that it will drive all the states to zero in at most n steps after an impulse disturbance in the process state. The control strategy is called deadbeat control. Compare with Example 1.3 in Chapter 1.

It follows from Ackermann's formula, Eq. (4.14), that the deadbeat strategy is given by

$$
L = \left( \begin{array}{c c c c} 0 & \dots & 0 & 1 \end{array} \right) W _ {c} ^ {- 1} \Phi^ {n} \tag {4.18}
$$

If the matrix $\Phi$ is invertible we get

$$
L = \left( \begin{array}{c c c c} 0 & \dots & 0 & 1 \end{array} \right) \left( \begin{array}{c c c c} \Phi^ {- n} \Gamma & \Phi^ {- n + 1} \Gamma & \dots & \Phi^ {- 1} \Gamma \end{array} \right) ^ {- 1} \tag {4.19}
$$

Table 4.1 Control signals for deadbeat control of a double integrator with $x(0) = \operatorname{col}[1, 1]$ and different sampling periods. 

<table><tr><td>h</td><td>100</td><td>10</td><td>1</td><td>0.1</td><td>0.01</td></tr><tr><td>u(0)</td><td>-0.0151</td><td>-0.16</td><td>-2.5</td><td>-115</td><td>-10,150</td></tr><tr><td>u(h)</td><td>0.0051</td><td>0.06</td><td>1.5</td><td>105</td><td>10,050</td></tr></table>

In deadbeat control there is only one design parameter—the sampling period. Because the error goes to zero in at most n sampling periods, the settling time is at most nh. The settling time is thus proportional to the sampling period h. The sampling period also influences the magnitude of the control signal, which increases drastically with decreasing sampling period. This fact has given the deadbeat control an undeservedly bad reputation. It is thus important to choose the sampling period carefully when using deadbeat control. The deadbeat strategy is unique to sampled-data systems. There is no corresponding feature for continuous-time systems. The following example demonstrates some properties of deadbeat control.
