# Example 3.14 (Pendulum on a Cart)

Assess controllability for the inverted pendulum-and-cart system, using the linearized model of Example 2.9 in Chapter 2.

Solution The equations are given in Example 3.10. The controllability matrix is

$$
\mathcal {C} = \left[ \begin{array}{c c c c} 0 & \frac {1}{M} & 0 & \frac {g}{M \ell} \\ \frac {1}{M} & 0 & \frac {g}{M \ell} & 0 \\ 0 & - \frac {1}{m \ell} & 0 & - \frac {(M + m) g}{M ^ {2} \ell^ {2}} \\ - \frac {1}{m \ell} & 0 & - \frac {(M + m) g}{M ^ {2} \ell^ {2}} & 0 \\ \hline B & A B & A ^ {2} B & A ^ {3} B \end{array} \right]
$$

Because C is a square matrix (which is always the case with a single input), fullness of rank is assessed by verifying that $\det C \neq 0$ . In fact,

$$\det \mathcal {C} = \frac {g ^ {2}}{M ^ {4} \ell^ {4}}$$

so the system is controllable.
