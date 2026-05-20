The adaptive system is thus described by Eqs. (6.1) and (6.2), which have a very special structure. Equation (6.1) is linear in the states and the external driving signals. The controller parameters appear in the coefficients of matrices A, B, C, and D. Nonlinearities appear in the product $\varphi e$ in Eq. (6.2), in the design map $\chi$ , and in the functions $A(\vartheta)$ , $B(\vartheta)$ , $C(\vartheta)$ , and $D(\vartheta)$ in Eq. (6.1). The equations for an adaptive system have a similar form in the discrete-time case. For a system with recursive least-squares estimation the equations can be written as

$$
\begin{array}{l} \xi (t + 1) = A (\vartheta) \xi (t) + B (\vartheta) \nu (t) \\ \eta (t) = \binom {e (t)} {\varphi (t)} = C (\vartheta) \xi (t) + D (\vartheta) v (t) \tag {6.3} \\ \end{array}
\hat {\theta} (t + 1) = \hat {\theta} (t) + P (t + 1) \varphi (t) e (t)P (t + 1) = P (t) - P (t) \varphi (t) (\lambda + \varphi^ {T} (t) P (t) \varphi (t)) ^ {- 1} \varphi^ {T} (t) P (t)
$$

It is useful to try to exploit the special structure of the equations to get a deeper understanding of adaptive systems. One special feature is that the state of the closed-loop system is naturally separated into two parts, $\xi$ and $\hat{\theta}$ . Moreover, it is reasonable to assume that $\hat{\theta}$ changes more slowly than $\xi$ .
