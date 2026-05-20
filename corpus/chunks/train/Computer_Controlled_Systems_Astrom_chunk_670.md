$$
\begin{array}{l} \Delta V (x (k)) = x ^ {T} (k + 1) \bar {S} x (k + 1) - x ^ {T} (k) \bar {S} x (k) \\ = x ^ {T} (k) (\Phi - \Gamma L) ^ {T} \bar {S} (\Phi - \Gamma L) x (k) - x ^ {T} (k) \bar {S} x (k) \\ = - x ^ {T} (k) \left(Q _ {1} + L ^ {T} Q _ {2} L - L ^ {T} Q _ {1 2} ^ {T} - Q _ {1 2} L\right) x (k) \\ = - \boldsymbol {x} ^ {T} (k) \left( \begin{array}{l l} I & - L ^ {T} \end{array} \right) Q \binom{I}{- L} x (k) \\ \end{array}
$$

where (11.17) and (11.21) have been used. Because $Q$ is positive definite and $[I - L^T]$ has full rank, $\Delta V$ is negative definite. The closed-loop system is thus asymptotically stable.

The case with Q positive definite in Theorem 11.3 is very special. Much more interesting results can be obtained. The poles of the closed-loop system can be obtained in several ways. When the LQ-controller is used the poles are obtained from

$$\det (\lambda I - \Phi + \Gamma L) = 0$$

It is possible to show that the poles are the $n$ stable eigenvalues of the generalized eigenvalue problem

$$
\det \left(\left( \begin{array}{c c c} {0} & {- I} & {0} \\ {\Phi^ {T}} & {0} & {0} \\ {\Gamma^ {T}} & {0} & {0} \end{array} \right) \lambda + \left( \begin{array}{c c c} {0} & {\Phi} & {\Gamma} \\ {- I} & {Q _ {1}} & {Q _ {1 2}} \\ {0} & {Q _ {1 2} ^ {T}} & {Q _ {2}} \end{array} \right)\right) = 0 \tag {11.34}
$$

Equation (11.34) is called the Euler equation of the LQ-problem.

Theorem 11.4 is given without proof for the single-input-single-output (SISO) case. A proof is given in Sec. 12.5.

THEOREM 11.4 THE CLOSED-LOOP POLES OF AN SISO SYSTEM Let the input and the output be scalar and assume that the steady-state optimal feedback is used for a time-invariant system. Further assume that only the output and the control signal are penalized in the loss function, that is, $Q_{1} = C^{T}C$ , $Q_{2} = \rho$ , and $Q_{12} = 0$ . The poles of the closed-loop system are the $n$ roots within the unit circle of the 2 $^{th}$ -order equation

$$\rho + H (z ^ {- 1}) H (z) = 0 \tag {11.35}$$

where

$$H (z) = C (z I - \Phi) ^ {- 1} \Gamma$$

is the open-loop pulse-transfer function.
