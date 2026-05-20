$$
E \{\mathbf {u} (t) \mathbf {u} ^ {T} (\tau) \} = Q (t) \delta (t - \tau), E \{\mathbf {u} (t) \} = \mathbf {0}, \tag {4.102a}E \{\mathbf {v} (t) \mathbf {v} ^ {T} (\tau) \} = R (t) \delta (t - \tau), \quad E \{\mathbf {v} (t) \} = \mathbf {0}, \tag {4.102b}E \{\mathbf {x} (t _ {o}) \} = 0, \tag {4.102c}E \{\mathbf {x} (t _ {o}) \mathbf {x} ^ {T} (t _ {o}) \} = P (t _ {o}); P (0) = P _ {o}, \tag {4.102d}
E \{\mathbf {u} (t) \mathbf {v} ^ {T} (\tau) \} = \left\{ \begin{array}{l l} C (t) \delta (t - \tau) & \text { if   the   process   and   measurement } \\ & \text { noises   are   correlated, } \\ 0 & \text { if   the   process   and   measurement } \\ & \text { noises   are   uncorrelated, } \end{array} \right. \tag {4.102e}
$$

where $\delta ( t - \tau )$ is the Dirac function, $Q ( t )$ and $R ( t )$ are the respective noise covariance matrices, $C ( t )$ is the correlation covariance matrix, and the symbol $\operatorname { E } \{ \dots \} ^ { * }$ denotes ensemble expectation or average value. Under the above conditions, the random state can be described in terms of its covariance matrix $P ( t )$ as follows:

$$P (t) \triangleq E \{\mathbf {x} (t) \mathbf {x} ^ {T} (t) \}. \tag {4.103}$$

The equation for the propagation of the covariance matrix for the system described by (4.100) is [3], [25]

$$\frac {d P (t)}{d t} = F (t) P (t) + P (t) F ^ {T} (t) + G (t) Q (t) G ^ {T} (t) - P (t) H ^ {T} (t) R ^ {- 1} (t) H (t) P (t) \tag {4.104a}$$

if $R ^ { - 1 } ( t )$ exists. The superscript T denotes the transpose of a vector or matrix, and the superscript (–1) denotes the inverse of a matrix. This equation is nonlinear in P and is referred to in the literature as the matrix Riccati equation. In the absence of measurements (4.104a) takes the simple form

$$\frac {d P (t)}{d t} = F (t) P (t) + P (t) F ^ {T} (t) + G (t) Q (t) G ^ {T} (t). \tag {4.104b}$$

Note that $G ( t ) Q ( t ) G ^ { T } ( t )$ accounts for the increase of uncertainty due to process noise, while the term $- \ P ( t ) H ^ { T } ( t ) R ^ { - 1 } ( t ) H ( t ) P ( t )$ accounts for the decrease of uncertainty as a result of measurements.
