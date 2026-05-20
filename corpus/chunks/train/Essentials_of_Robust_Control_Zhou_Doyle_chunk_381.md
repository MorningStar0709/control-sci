# Relax (A3) and (A4)

Suppose that

$$
G = \left[ \begin{array}{c c c} 0 & 0 & 1 \\ \hline 0 & 0 & 1 \\ 1 & 1 & 0 \end{array} \right]
$$

which violates both (A3) and (A4) and corresponds to the robust stabilization of an integrator. If the controller $u = - \epsilon x$ , where $\epsilon > 0$ is used, then

$$T _ {z w} = \frac {- \epsilon s}{s + \epsilon}, \mathrm{with} \| T _ {z w} \| _ {\infty} = \epsilon .$$

Hence the norm can be made arbitrarily small as $\epsilon  0 .$ , but $\epsilon = 0$ is not admissible since it is not stabilizing. This may be thought of as a case where the $\mathcal { H } _ { \infty }$ optimum is not achieved on the set of admissible controllers. Of course, for this system, $\mathcal { H } _ { \infty }$ optimal control is a silly problem, although the suboptimal case is not obviously so.
