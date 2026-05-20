$$z = \binom{x}{w}$$

and we find that the system can be described by

$$
\frac {d}{d t} \binom{x}{w} = \left( \begin{array}{c c} A & C _ {w} \\ 0 & A _ {w} \end{array} \right) \binom{x}{w} + \binom{B}{0} u \tag {4.20}
$$

Thus we have a problem of the same form as the basic pole-placement problem. There is, however, one important difference: The system of (4.20) is not completely reachable. The poles associated with the description of the disturbance—that is, the eigenvalues of $A_{w}$ —cannot be influenced by the feedback. This is very natural because the disturbances are exogenous variables that are not influenced by the control. Compare with Example 4.3. Sampling the system gives the following discrete-time system:

$$
\binom {x (k + 1)} {w (k + 1)} = \left( \begin{array}{c c} \Phi & \Phi_ {x w} \\ 0 & \Phi_ {w} \end{array} \right) \binom {x (k)} {w (k)} + \binom {\Gamma} {0} u (k)
$$

The general linear-state feedback is given by

$$u (k) = - L x (k) - L _ {w} w (k) \tag {4.21}$$

This control law gives the following closed-loop system:

$$
\begin{array}{l} x (k + 1) = (\Phi - \Gamma L) x (k) + (\Phi_ {x w} - \Gamma L _ {w}) w (k) \\ (1 - 1) = \Phi_ {x w} (1) \end{array} \tag {4.22}
w (k + 1) = \Phi_ {w} w (k)
$$

which tells how the closed-loop system is influenced by the control. Notice that the control law in (4.21) can be interpreted as a combination of a feedback term Lx and a feedforward term $L_{w}w$ from the measured disturbances. If the pair $(\Phi,\Gamma)$ is reachable, the matrix L can be chosen so that the matrix $\Phi-\Gamma L$ has prescribed eigenvalues. This would ensure that the term of the solution that is caused by the initial values decays properly. The matrix $\Phi_{w}$ cannot be influenced by feedback. The effect of the disturbance on the vector x can, however, be reduced by a proper choice of the vector $L_{w}$ , which should be chosen so that the matrix $\Phi_{xw}-\Gamma L_{w}$ is small. In some cases it is possible to make this matrix zero. We illustrate this by an example.
