# Example 2.4 Inverse sampling

Consider the first-order difference equation

$$x (k h + h) = a x (k h) + b u (k h)$$

From Example 2.1 we find that the corresponding continuous-time system is obtained from

$$e ^ {\alpha h} = a\frac {\beta}{\alpha} (e ^ {\alpha h} - 1) = b$$

This gives

$$\alpha = \frac {1}{h} \ln a\beta = \frac {1}{h} \ln a \cdot \frac {b}{a - 1}$$

This example shows that a continuous-time system with real coefficients is obtained only when $\alpha$ is positive.

To investigate the process of sampling in the general case we note that it follows from (2.6) that

$$
\left( \begin{array}{c c} A & B \\ 0 & 0 \end{array} \right) = \frac {1}{h} \ln \left( \begin{array}{c c} \Phi & \Gamma \\ 0 & I \end{array} \right)
$$

where $\ln(\cdot)$ is the matrix logarithmic function. The continuous-time system is thus obtained by taking the matrix logarithm function of a block matrix. Computation of matrix logarithm is discussed in Appendix B. From the Cayley-Hamilton theorem it must be assumed that the logarithm exists only when the matrix $\Phi$ does not have any eigenvalues on the negative real axis. There is also a nonuniqueness in the matrix logarithmic function for complex arguments, which is illustrated by the following example.
