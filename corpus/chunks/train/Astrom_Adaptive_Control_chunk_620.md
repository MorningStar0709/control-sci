To determine a control law that keeps the system on $\sigma(x) = 0$ , we introduce the Lyapunov function $V(x) = \sigma^2(x)/2$ . The time derivative of $V$ is given by

$$
\begin{array}{l} \frac {d V}{d t} = \sigma (x) \dot {\sigma} (x) = x ^ {T} p p ^ {T} \dot {x} \\ = x ^ {T} p \left(p ^ {T} f (x) + p ^ {T} g (x) u (t)\right) \\ \end{array}
$$

Choose the control law

$$u (t) = - \frac {p ^ {T} f}{p ^ {T} g} - \frac {\mu}{p ^ {T} g} \operatorname{sign} (\sigma (x)) \tag {10.10}$$

Then

$$\frac {d V}{d t} = - \mu \sigma (x) \operatorname{sign} (\sigma (x)) \tag {10.11}$$

which is negative definite. This implies that $\sigma(x)=0$ is asymptotically stable. Notice that there is a discontinuity in the control signal when the switching surface is passed.

Assume that the system has initial values such that $\sigma(x) = \sigma_{0} > 0$ , and let $t_{\sigma}$ be the time when the switching surface is reached the first time. From Eq. (10.11) we find that

$$\dot {\sigma} (x) = - \mu$$

Integrating this equation from 0 to $t_{\sigma}$ gives

$$0 - \sigma_ {0} = - \mu (t _ {\sigma} - 0)$$

which gives $t_{\sigma} = \sigma_{0}/\mu$ . Using the same arguments for $\sigma_{0} < 0$ shows that $t_{\sigma} = |\sigma_{0}|/\mu$ . With the control law given by Eq. (10.10) the state will thus reach the switching surface in finite time. The subspace $\sigma(x) = 0$ is asymptotically stable, and the state will stay on the switching surface once it is reached. The motion along the surface is determined by Eq. (10.9).

Uncertainties in $f$ and $g$ can be handled if $\mu$ is sufficiently large. Assume that the design of the control law is based on the approximate values $\hat{f}$ and $\hat{g}$ instead of the true ones. Then

$$\frac {d V}{d t} = \sigma \left(\frac {p ^ {T} (f \hat {g} ^ {T} - \hat {f} g ^ {T}) p}{p ^ {T} \hat {g}} - \mu \frac {p ^ {T} g}{p ^ {T} \hat {g}} \operatorname{sign} (\sigma)\right)$$

The right-hand side is negative if $\mu$ is sufficiently large, provided that $p^{T}\hat{g}$ and $p^{T}g$ have the same sign. The system will thus be insensitive to uncertainties in the process model.

One way to design a variable-structure system is to first transform the system to the form given by Eqs. (10.7). This is possible for controllable linear systems without zeros and for some classes of nonlinear systems. A stable switching surface in the transformed variables is then determined. The system and the switching criteria can then be transformed back to the original state variables. Notice, however, that all states must be measured.
