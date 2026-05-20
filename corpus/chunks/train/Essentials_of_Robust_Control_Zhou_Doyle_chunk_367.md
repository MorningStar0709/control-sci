Complementarity failing at $\gamma = \gamma _ { 1 }$ means $\rho ( X _ { \infty } )  \infty { \mathrm { ~ a s ~ } } \gamma  \gamma _ { 1 } $ , so condition (iii) would fail at even larger values of $\gamma _ { : }$ , unless the eigenvectors associated with $\rho ( X _ { \infty } )$ as $\gamma \longrightarrow \gamma _ { 1 }$ are in the null space of $Y _ { \infty }$ . Thus condition (iii) is the most likely of all to fail first. If condition (i) or (ii) fails first because the stability property fails, the formulas in Theorem 14.1 as well as their descriptor versions are optimal at $\gamma = \gamma _ { \mathrm { o p t } }$ . This is illustrated in Example 14.3. If the complementarity condition fails first, [but (iii) does not fail], then obtaining formulas for the optimal controllers is a more subtle problem.

Example 14.3 Let an interconnected dynamical system realization be given by

$$
G (s) = \left[ \begin{array}{c c c} a & \left[ \begin{array}{c c} 1 & 0 \end{array} \right] & 1 \\ \hline \left[ \begin{array}{c} 1 \\ 0 \end{array} \right] & 0 & \left[ \begin{array}{c} 0 \\ 1 \end{array} \right] \\ 1 & \left[ \begin{array}{c c} 0 & 1 \end{array} \right] & 0 \end{array} \right].
$$

Then all assumptions for output feedback problem are satisfied and

$$
H _ {\infty} = \left[ \begin{array}{c c} a & \frac {1 - \gamma^ {2}}{\gamma^ {2}} \\ - 1 & - a \end{array} \right], \quad J _ {\infty} = \left[ \begin{array}{c c} a & \frac {1 - \gamma^ {2}}{\gamma^ {2}} \\ - 1 & - a \end{array} \right].
$$

The eigenvalues of $H _ { \infty }$ and $J _ { \infty }$ are given by

$$\left\{\pm \frac {\sqrt {(a ^ {2} + 1) \gamma^ {2} - 1}}{\gamma} \right\}.$$

If $\gamma > \frac { 1 } { \sqrt { a ^ { 2 } + 1 } }$ , then $\mathcal { X } _ { - } ( H _ { \infty } )$ and $\chi _ { - } ( J _ { \infty } )$ exist and

$$
\mathcal {X} _ {-} (H _ {\infty}) = \mathrm{Im} \left[ \begin{array}{c} \frac {\sqrt {(a ^ {2} + 1) \gamma^ {2} - 1} - a \gamma}{\gamma} \\ 1 \end{array} \right]

\mathcal {X} _ {-} (J _ {\infty}) = \mathrm{Im} \left[ \begin{array}{c} \frac {\sqrt {(a ^ {2} + 1) \gamma^ {2} - 1} - a \gamma}{\gamma} \\ 1 \end{array} \right].
$$

We shall consider two cases:

1) $a > 0 \colon$ In this case, the complementary property of dom(Ric) will fail before the stability property fails since

$$\sqrt {(a ^ {2} + 1) \gamma^ {2} - 1} - a \gamma = 0$$

when $\gamma = 1$ .

Nevertheless, ${ \mathrm { i f ~ } } \gamma > { \frac { 1 } { \sqrt { a ^ { 2 } + 1 } } }$ and $\gamma \neq 1$ , then $H _ { \infty } \in \mathrm { d o m } ( \mathrm { R i c } )$ and
