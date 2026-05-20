# Equilibrium Values for the Parameters

It follows from Eqs. (6.57) that the parameters $\hat{\theta}_{1}$ and $\hat{\theta}_{2}$ are constant when the error e is zero. The conditions for e to be zero will now be investigated. The signal transmission from the command signal $u_{c}$ to the output y is described by the transfer function

$$G _ {c} = \frac {\hat {\theta} _ {1} G}{1 + \hat {\theta} _ {2} G}$$

and the control error becomes

$$e (t) = y (t) - y _ {m} (t) = \left(G _ {c} (p) - G _ {m} (p)\right) u _ {c} (t)$$

Let the reference signal be $u_{c} = u_{0} \sin \omega t$ . The error e is then zero if

$$G _ {c} (i \omega) = G _ {m} (i \omega)$$

or

$$\hat {\theta} _ {1} ^ {0} G (i \omega) = \hat {\theta} _ {2} ^ {0} G _ {m} (i \omega) G (i \omega) + G _ {m} (i \omega) \tag {6.58}$$

This equation can be solved for $\hat{\theta}_{1}^{0}$ and $\hat{\theta}_{2}^{0}$ by equating the real and imaginary parts. There is a unique solution if $\operatorname{Im}\{G(i\omega)\} \neq 0$ . The solutions are easily obtained by dividing Eq. (6.58) by $G_{m}G$ and G, respectively, and taking

imaginary parts. This gives

$$\hat {\theta} _ {1} ^ {0} = \frac {\operatorname{Im} \left\{1 / G (i \omega) \right\}}{\operatorname{Im} \left\{1 / G _ {m} (i \omega) \right\}} \tag {6.59}\hat {\theta} _ {2} ^ {0} = - \frac {\operatorname{Im} \left\{G _ {m} (i \omega) / G (i \omega) \right\}}{\operatorname{Im} G _ {m} (i \omega)}$$

In the nominal case we get $\hat{\theta}_{1}^{0}=b_{m}/b$ and $\hat{\theta}_{2}^{0}=(a_{m}-a)/b$ . These equilibrium values do not depend on the frequency of the command signal. They also correspond to the desired feedback gains.
