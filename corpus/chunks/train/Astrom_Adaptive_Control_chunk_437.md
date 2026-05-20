# An Example of Averaging Analysis

Consider a process with the transfer function $kG(s)$ and an adjustable feedforward gain. Find a feedforward gain $\hat{\theta}$ such that the input-output behavior matches the transfer function $k_{0}G_{m}(s)$ as well as possible. It is assumed that k > 0 and $k_{0} > 0$ . The case $G_{m} = G$ was discussed in Chapter 5. Two different algorithms for updating the gain were proposed in Chapter 5: the MIT rule and the SPR rule. The algorithms are

$$\frac {d \hat {\theta}}{d t} = - \gamma y _ {m} e \quad (\text { MIT }) \tag {6.52}\frac {d \hat {\theta}}{d t} = - \gamma u _ {c} e \quad (\mathrm{SPR})$$

where $u_{c}$ is the command signal, $y_{m} = k_{0}G_{m}u_{c}$ is the model output, and e is the error defined by

$$e (t) = y - y _ {m} = k G (p) \left(\hat {\theta} (t) u _ {c} (t)\right) - k _ {0} G _ {m} (p) u _ {c} (t)$$

The analysis in Section 5.5 shows that the MIT rule gives a closed-loop system that is globally stable for any adaptation gain $\gamma$ in the “ideal” case, when $G = G_{m}$ and G is SPR. In the presence of unmodeled dynamics it is, of course, highly unrealistic to assume that a transfer function is SPR. So far, no stability result has been given for the MIT rule. However, Example 5.5 indicates that the

MIT rule will be unstable for sufficiently high adaptation gains if the system is not SPR.

We now investigate the algorithms under nonideal conditions, using averaging. Inserting the expressions for $y_{m}$ and e into the equations for the parameters, we get

$$\frac {d \hat {\theta}}{d t} + \gamma \left(k _ {0} G _ {m} u _ {c}\right) \left(k G \left(\hat {\theta} u _ {c}\right) - k _ {0} G _ {m} u _ {c}\right) = 0 \tag {6.53}\frac {d \hat {\theta}}{d t} + \gamma u _ {c} \left(k G (\hat {\theta} u _ {c}) - k _ {0} G _ {m} u _ {c}\right) = 0$$

where the first equation holds for the MIT rule and the second holds for the SPR rule. The corresponding averaging equations are

$$\frac {d \bar {\theta}}{d t} + \gamma (\bar {\theta} k k _ {0} \operatorname{avg} \left\{\left(G _ {m} u _ {c}\right) \left(G u _ {c}\right) \right\} - k _ {0} ^ {2} \operatorname{avg} \left\{\left(G _ {m} u _ {c}\right) ^ {2} \right\}) = 0 \tag {6.54}\frac {d \bar {\theta}}{d t} + \gamma (\bar {\theta} k \operatorname{avg} \left\{u _ {c} \left(G u _ {c}\right) \right\} - k _ {0} \operatorname{avg} \left\{u _ {c} \left(G _ {m} u _ {c}\right) \right\}) = 0$$

The equilibrium parameters are
