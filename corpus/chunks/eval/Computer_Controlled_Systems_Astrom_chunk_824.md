# Example B.2 Computation of matrix logarithm

Let

$$
\Phi = \left( \begin{array}{c c} 1 & h \\ 0 & 1 \end{array} \right)
$$

and compute $\ln\Phi$ . The eigenvalues are given by $(\lambda-1)^{2}=0$ —that is, multiple eigenvalues exist. The matrix logarithm can now be written as

$$\ln \Phi = \alpha_ {0} \Phi + \alpha_ {1} I$$

where $\alpha_0$ and $\alpha_{1}$ are given by

$$\ln 1 = \alpha_ {0} + \alpha_ {1}\left. \frac {\partial}{\partial \lambda} (\ln \lambda) \right| _ {\lambda - 1} = \alpha_ {0}$$

which gives

$$0 = \alpha_ {0} + \alpha_ {1}1 = \alpha_ {0}$$

Finally,

$$
\ln \Phi = \left( \begin{array}{l l} 1 & h \\ 0 & 1 \end{array} \right) - \left( \begin{array}{l l} 1 & 0 \\ 0 & 1 \end{array} \right) = \left( \begin{array}{l l} 0 & h \\ 0 & 0 \end{array} \right)
$$

Remark. Instead of starting with the characteristic polynomial, it is possible to use the minimal polynomial of the matrix. The degree of the series in (B.1) will then be the degree of the minimal polynomial minus one. In general, this will not reduce the computing time because the minimal polynomial—or, alternatively, the Jordan form—has to be computed.
