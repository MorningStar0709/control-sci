# 13.6 Stability Margins of $\mathcal { H } _ { 2 }$ Controllers

It is well-known that a system with LQR controller has at least $6 0 ^ { \mathrm { o } }$ phase margin and 6 dB gain margin. However, it is not clear whether these stability margins will be preserved if the states are not available and the output feedback $\mathcal { H } _ { 2 }$ (or LQG) controller has to be used. The answer is provided here through a counterexample from Doyle [1978]: There are no guaranteed stability margins for a $\mathcal { H } _ { 2 }$ controller.

Consider a single-input and single-output two-state generalized dynamical system:

$$
G (s) = \left[ \begin{array}{c c c} \left[ \begin{array}{c c} 1 & 1 \\ 0 & 1 \end{array} \right] & \left[ \begin{array}{c c} \sqrt {\sigma} & 0 \\ \sqrt {\sigma} & 0 \end{array} \right] & \left[ \begin{array}{c} 0 \\ 1 \end{array} \right] \\ \hline \left[ \begin{array}{c c} \sqrt {q} & \sqrt {q} \\ 0 & 0 \end{array} \right] & 0 & \left[ \begin{array}{c} 0 \\ 1 \end{array} \right] \\ \left[ \begin{array}{c c} 1 & 0 \end{array} \right] & \left[ \begin{array}{c c} 0 & 1 \end{array} \right] & 0 \end{array} \right].
$$

It can be shown analytically that

$$
X _ {2} = \left[ \begin{array}{c c} 2 \alpha & \alpha \\ \alpha & \alpha \end{array} \right], Y _ {2} = \left[ \begin{array}{c c} 2 \beta & \beta \\ \beta & \beta \end{array} \right]
$$

and

$$
F _ {2} = - \alpha \left[ \begin{array}{c c} 1 & 1 \end{array} \right], L _ {2} = - \beta \left[ \begin{array}{c} 1 \\ 1 \end{array} \right]
$$

where

$$\alpha = 2 + \sqrt {4 + q}, \quad \beta = 2 + \sqrt {4 + \sigma}.$$

Then the optimal output $\mathcal { H } _ { 2 }$ controller is given by

$$
K _ {\text {opt}} = \left[ \begin{array}{c c c} 1 - \beta & 1 & \beta \\ - (\alpha + \beta) & 1 - \alpha & \beta \\ \hline - \alpha & - \alpha & 0 \end{array} \right].
$$

Suppose that the resulting closed-loop controller (or plant $G _ { 2 2 } )$ has a scalar gain k with a nominal value $k = 1$ . Then the controller implemented in the system is actually

$$K = k K _ {\mathrm{opt}},$$

and the closed-loop system A matrix becomes

$$
\tilde {A} = \left[ \begin{array}{c c c c} 1 & 1 & 0 & 0 \\ 0 & 1 & - k \alpha & - k \alpha \\ \beta & 0 & 1 - \beta & 1 \\ \beta & 0 & - \alpha - \beta & 1 - \alpha \end{array} \right].
$$

It can be shown that the characteristic polynomial has the form

$$\det (s I - \tilde {A}) = s ^ {4} + a _ {3} s ^ {3} + a _ {2} s ^ {2} + a _ {1} s + a _ {0}$$

with

$$a _ {1} = \alpha + \beta - 4 + 2 (k - 1) \alpha \beta , \quad a _ {0} = 1 + (1 - k) \alpha \beta .$$
