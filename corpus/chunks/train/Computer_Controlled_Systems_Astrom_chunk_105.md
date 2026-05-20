# Example 2.5 Harmonic oscillator

The discrete-time system

$$
x (k h + h) = \left( \begin{array}{c c} \cos \alpha h & \sin \alpha h \\ - \sin \alpha h & \cos \alpha h \end{array} \right) x (k h) + \binom {1 - \cos \alpha h} {\sin \alpha h} u (k h)
$$

can be obtained by sampling a continuous-time system with

$$
A = \left( \begin{array}{c c} 0 & \omega \\ - \omega & 0 \end{array} \right) \quad \text { and } \quad B = \binom{0}{\omega}
$$

where

$$\omega = \alpha + \frac {2 \pi}{h} \cdot n \quad n = 0, 1, \dots$$

In this case the inverse problem has many solutions (compare Examples A.3 and B.1). This is generally the case if the matrix $\Phi$ has complex eigenvalues. Notice that there always exists a unique $\omega$ in the interval $-\omega_{N} \leq \omega \leq \omega_{N}$ , where $\omega_{N} = \pi/h$ is the Nyquist frequency associated with the sampling period h.
