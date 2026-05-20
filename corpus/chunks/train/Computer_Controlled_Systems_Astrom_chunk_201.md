# Steady-State Values

When analyzing control systems, it is important to calculate steady-state values of the output and of the error of the system. Assume a simple feedback system, as shown in Fig. 3.5. To generalize, it can be assumed that -1 in the feedback path is replaced by $-H_{fb}(q)$ . The error $e(k)$ is then given by

$$e (k) = \frac {1}{1 + H (q) H _ {f b} (q)} u _ {c} (k) = \frac {1}{1 + \mathcal {L} (q)} u _ {c} (k) \tag {3.24}$$

The final-value theorem (Sec. 2.7, Table 2.2) can be used to calculate the steady-state value of $e(k)$ . Notice, however, that the stability of the system must be tested before the final-value theorem can be used. If the input signal is a step, the steady-state error can be calculated simply by putting q = 1 in (3.24).

The number of integrators in the open-loop system determines the class of reference values that can be followed without steady-state errors. If the open-loop system has p integrators, then the error will be zero in steady state (provided that the closed-loop system is asymptotically stable) for reference signals that are polynomials in k of order less than or equal to p - 1.
