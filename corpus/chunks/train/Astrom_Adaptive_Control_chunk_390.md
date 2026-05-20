# EXAMPLE 6.1 Lack of excitation leads to instability

Consider the model-reference adaptive system shown in Fig. 5.14(b). Assume that the input signal is $u_{c}(t) = e^{-t}$ . The system can then be described by the equations

$$\frac {d e}{d t} = - e + k \tilde {\theta} u _ {c}\frac {d \tilde {\theta}}{d t} = - \gamma e u _ {c}\frac {d u _ {c}}{d t} = - u _ {c}$$

where $\hat{\theta} = \hat{\theta} - \theta_{0}$ . The equilibrium is $e = \hat{\theta} = u_{c} = 0$ . Linearization around this point gives a linear system with the system matrix.

$$
A = \left( \begin{array}{c c c} - 1 & 0 & 0 \\ 0 & 0 & 0 \\ 0 & 0 & - 1 \end{array} \right)
$$

This matrix has the eigenvalues -1, 0, and -1, and the system is clearly not stable.
