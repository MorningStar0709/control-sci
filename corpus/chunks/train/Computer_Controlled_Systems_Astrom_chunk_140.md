# 2.8 Poles and Zeros

For single-input-single-output finite-dimensional systems, poles and zeros can be conveniently obtained from the denominator and numerator of the pulse-transfer function. Poles and zeros have good system-theoretic interpretation. A pole $z = a$ corresponds to a free mode of the system associated with the time function $z(k) = a^k$ . Poles are also the eigenvalues of the system matrix $\Phi$ . The zeros are related to how the inputs and outputs are coupled to the states.

Zeros can also be characterized by their signal blocking properties. A zero z = a means that the transmission of the input signal $u(k) = a^{k}$ is blocked by the system. This interpretation can be used to define zeros in terms of the state-space equation. It follows from (2.16) that the input $u(k) = u_{0}a^{k}$ gives the state $x(k) = x_{0}a^{k}$ and zero output if z = a such that

$$
\det \left( \begin{array}{c c} z I - \Phi & - \Gamma \\ C & D \end{array} \right) = 0
$$
