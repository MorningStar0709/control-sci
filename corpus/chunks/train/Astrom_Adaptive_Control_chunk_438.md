$$\bar {\theta} _ {\mathrm{MIT}} = \frac {k _ {0}}{k} \frac {\operatorname{avg} \left\{\left(G _ {m} u _ {c}\right) ^ {2} \right\}}{\operatorname{avg} \left\{\left(G _ {m} u _ {c}\right) \left(G u _ {c}\right) \right\}} \tag {6.55}\bar {\theta} _ {\mathrm{SPR}} = \frac {k _ {0}}{k} \frac {\operatorname{avg} \left\{u _ {c} \left(G _ {m} u _ {c}\right) \right\}}{\operatorname{avg} \left\{u _ {c} \left(G u _ {c}\right) \right\}}$$

The equilibrium values correspond to the true parameters for all command signals $u_{c}$ only if $G = G_{m}$ (i.e., there are no unmodeled dynamics). When $G \neq G_{m}$ , the equilibrium obtained will depend on the command signal as well as on the unmodeled dynamics. Notice that the equilibrium value obtained for the MIT rule minimizes the actual mean square error.

The stability conditions for the averaged equations (Eqs. 6.54) are

$$\gamma \operatorname{avg} \left\{\left(G _ {m} u _ {c}\right) \left(G u _ {c}\right) \right\} > 0 \quad (\text { MIT })\gamma \operatorname{avg} \left\{u _ {c} (G u _ {c}) \right\} > 0 \quad (\text { SPR })$$

The averaged equation when the MIT rule is used will thus give a stable equilibrium for all command signals if $G_{m} = G$ . The stability condition depends on the command signal and the process dynamics as well as on the response model.

For the SPR rule the stability condition depends only on the command signal and on the process dynamics. The equilibrium is stable for all command signals if G is SPR. For processes that are not SPR the equilibrium may well be unstable. Consider the case of a command signal composed of a constant and a sum of sinusoids:

$$u _ {c} (t) = a _ {0} + 2 \sum_ {k = 1} ^ {n} a _ {k} \sin \omega_ {k} t$$

If Lemma 6.5 is used, the stability conditions for $\gamma > 0$ become

$$\alpha_ {0} ^ {2} G _ {m} (0) + \sum_ {k = 1} ^ {n} \alpha_ {k} ^ {2} \left| G _ {m} \left(i \omega_ {k}\right) \right| \left| G \left(i \omega_ {k}\right) \right| \cos \left\{\arg G _ {m} \left(i \omega_ {k}\right) - \arg G \left(i \omega_ {k}\right) \right\} > 0a _ {0} ^ {2} G (0) + \sum_ {k = 1} ^ {m} a _ {k} ^ {2} \operatorname{Re} G (i \omega_ {k}) > 0$$

For a single sinusoidal command signal the MIT rule gives a stable equilibrium if the phase lags of $G_{m}$ and G differ by at most $90^{\circ}$ at the frequencies of the input signal. The SPR rule, on the other hand, gives a stable equilibrium if the phase lag of the process is at most $90^{\circ}$ .
