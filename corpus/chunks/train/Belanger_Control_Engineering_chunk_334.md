If $T$ is large enough to ensure that $1 / \alpha T \ll |s^*|$ , then $\theta_z \approx \theta_p$ , and Equation 6.33 is approximately satisfied. Therefore, some point near $s^*$ will in fact satisfy the angle condition, and the Root Locus will be only slightly perturbed by the lag compensator, for $|s| \gg 1 / T$ .

With the lag, the Root Locus gain condition is

$$k \frac {\alpha T s ^ {*} + 1}{T s ^ {*} + 1} P (s ^ {*}) = - 1.$$

By Equation 6.32,

$$k = k ^ {*} \frac {T s ^ {*} + 1}{\alpha T s ^ {*} + 1}.$$

If $|s^{*}| \gg 1 / \alpha T$ , then $|\alpha Ts^{*}| \gg 1$ and

$$k \approx k ^ {*} \frac {T s ^ {*}}{\alpha T s ^ {*}} = \frac {k ^ {*}}{\alpha}.$$

Since $\alpha < 1$ , it follows that $k > k^*$ . In essence, the lag compensator allows a higher gain to be used for the same closed-loop poles as in the pure-gain case. The same stability properties are thus achieved with a higher gain, improving the dc steady-state behavior.

There is one important difference in the Root Locus. As Figure 6.21 shows, there is a new real closed-loop pole between $-1/T$ and $-1/\alpha T$ ; it is relatively near the origin, and hence relatively slow. This pole accounts for the slow tail in the load torque response of Figure 6.19. The tail is also present in the set-point response of Figure 6.20, since the output must eventually go to 1, but is much less obvious then in Figure 6.19. This is because $y/y_d = T(s)$ has the zeros of $L(s)$ as its zeros, so that $T(s)$ has a zero at $-1/\alpha T$ that almost cancels the slow closed-loop pole. On the other hand, the closed-loop transmission from $T_L$ to $y$ has the same poles but does not have a zero that would cause near cancellation of the slow lag pole; hence the sizeable contributions of that pole to the response. One conclusion can be drawn from this discussion: we should not make $T$ larger than necessary, because the slow closed-loop pole created by the lag may appear in some of the transients.
