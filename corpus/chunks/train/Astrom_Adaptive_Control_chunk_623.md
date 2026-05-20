$$
\begin{array}{l} u (t) = - \frac {p ^ {T} A x}{p ^ {T} B} - \mu \mathrm{sign} (\sigma (x)) \\ = - \left( \begin{array}{l l} 2 & 0 \end{array} \right) x (t) - \mu \operatorname{sign} (\sigma (x)) \\ \end{array}
$$

The phase plane of the system is shown in Fig. 10.14 when $\mu = 0.5$ . The input and the output for one initial value are shown in Fig. 10.15(a). The trajectories hit the switching line $\sigma = 0$ and stay on it. This implies that the control signal will chatter. Using the control law (10.12),

$$
u (t) = - \left( \begin{array}{l l} 2 & 0 \end{array} \right) x (t) - \mu \mathrm{sat} (\sigma (x), \varepsilon)
$$

with $\varepsilon = 0.01$ , gives the behavior shown in Fig. 10.15(b). The control signal is now smooth, but the differences in the state trajectories are negligible. ☐
