$$
\operatorname{sat} u = \left( \begin{array}{c} \operatorname{sat} u _ {1} \\ \operatorname{sat} u _ {2} \\ \vdots \\ \operatorname{sat} u _ {n} \end{array} \right) \tag {9.7}
$$

for a vector. The values $u_{low}$ and $u_{high}$ are chosen to correspond to the actuator limitations. A block diagram of a controller with a model for the actuator nonlinearity is shown in Fig. 9.4. Observe that even if the transfer function from y to u for (9.1) is unstable, the state of the system in (9.5) will always be bounded if the matrix $(I - KC)\Phi$ is stable. It is also clear that x will be a good estimate of the process state even if the valve saturates, provided that $u_{low}$ and $u_{high}$ are chosen properly.
