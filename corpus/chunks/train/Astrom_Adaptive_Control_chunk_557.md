# EXAMPLE 8.3 Limit cycle period

Consider the same process as in Example 8.1. To apply Theorem 8.1, the system $G(s)$ is sampled with period $h$ . The pulse transfer function is

$$H _ {h} (z) = \frac {K h}{(z - 1)} - \frac {K \alpha (1 - e ^ {- h})}{(\alpha - 1) (z - e ^ {- h})} + \frac {K (1 - e ^ {- \alpha h})}{\alpha (\alpha - 1) (z - e ^ {- \alpha h})}$$

Hence

$$
\begin{array}{l} H _ {h} (- 1) = - \frac {K h}{2} + \frac {K \alpha (1 - e ^ {- h})}{(\alpha - 1) (1 + e ^ {- h})} - \frac {K (1 - e ^ {- \alpha h})}{\alpha (\alpha - 1) (1 + e ^ {- \alpha h})} \\ = - \frac {K h}{2} + \frac {K \alpha}{\alpha - 1} \left(\frac {1 - e ^ {- h}}{1 + e ^ {- h}} - \frac {1}{\alpha^ {2}} \frac {1 - e ^ {- \alpha h}}{1 + e ^ {- \alpha h}}\right) = 0 \\ \end{array}
$$

Numerical search for the value of h that satisfies this equation gives $h = 1.035$ . This gives $T_{u} = 2.07$ , which agrees with the simulation in Fig. 8.4. ☐

Stable periodic solutions will not be obtained for all systems. A double integrator under pure relay control, for example, will give periodic solutions with an arbitrary period.
