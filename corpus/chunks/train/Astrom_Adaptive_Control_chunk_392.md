# 6.3 ADAPTATION OF A FEEDFORWARD GAIN

The special case of adaptation of a feedforward gain has been discussed many times because of its simplicity. Let us therefore consider the structure of the equations in this case too. For the system in Fig. 5.14 we get

$$
\frac {d \xi}{d t} = A \xi + B \theta u _ {c}e = C \xi - y _ {m} \tag {6.14}
\varphi = \left\{ \begin{array}{l l} - y _ {m} & \text { MIT   rule } \\ - u _ {c} & \text { Lyapunov   rule } \end{array} \right.
$$

where A, B, and C are matrices that give a realization of the transfer function $kG(s)$ . Notice that in this case the matrices A, B, and C, the regression vector $\varphi$ , and the error e do not depend on the controller parameters explicitly. Furthermore, the parameter is updated as

$$\frac {d \hat {\theta}}{d t} = \gamma \varphi e (\xi) \tag {6.15}$$

for a gradient scheme. If $u_{c}$ is a function of time, then $y_{m}$ is also a function of time, and Eqs. (6.14) and (6.15) are simply time-varying linear differential equations. Such equations can have a complex behavior. We illustrate this by an example before proceeding.
