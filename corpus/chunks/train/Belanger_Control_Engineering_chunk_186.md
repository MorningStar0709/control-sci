# 4.2.4 Sensitivity

The transfer functions associated with a control system are functions of the plant transfer function $P(s)$ . If $P(s)$ changes from $P_0(s)$ to $P_0(s) + \Delta P(s)$ , then $H_{d0}(s)$ , for example, becomes $H_{d0}(s) + \Delta H_d(s)$ . The sensitivity of $H_d$ with respect to $P$ is defined as

$$S _ {d} ^ {P} (s) = \frac {\Delta H _ {d} (s) / H _ {d o} (s)}{\Delta P (s) / P _ {0} (s)} \tag {4.11}$$

or, basically, the fractional (or percent) change in $H_{d}(s)$ divided by the fractional (or percent) change in $P(s)$ .

The formula is usually applied in the case of small—i.e., infinitesimal—changes, for which Equation 4.11 becomes

$$S _ {d} ^ {P} (s) = \frac {\partial H _ {d} (s)}{\partial P (s)} \frac {P _ {0} (s)}{H _ {d 0} (s)}. \tag {4.12}$$

(Students of economics may recognize Equation 4.12 as the elasticity of $H_{d}$ with respect to $P$ .)

A sensitivity “yardstick” is obtained by applying the signal $y_{d}$ directly to the plant input. In that case, $y(s) = P(s)y_{d}(s)$ , so $H_{d} = P$ , $\Delta H_{d} = \Delta P$ , and, from Equation 4.11, $S_{d}^{P} = 1$ . If a control system results in $|S_{d}^{P}(j\omega)| < 1$ , then sensitivity at $\omega$ has been reduced by the control system; the opposite is true if $|S_{d}^{P}(j\omega)| > 1$ . In general, sensitivity is reduced at some frequencies, increased at others. Specifications on sensitivity are expressed in the frequency domain, and generally attempt to limit $|S_{d}^{P}(j\omega)|$ at frequencies where $\Delta P/P$ is relatively large and where the input has significant spectral content.
