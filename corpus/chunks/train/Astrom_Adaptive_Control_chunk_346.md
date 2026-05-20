With the chosen degrees of P and Q it is straightforward to verify that the computation does not require taking derivatives of the signals $y, u, u_{c}$ , and $y_{m}$ . The error model of Eq. (5.76) is also linear in the parameters, and the transfer function $b_{0}Q/(A_{o}A_{m})$ is SPR. The error model thus satisfies the requirements of Step 2, and the parameters can then be updated by Eq. (5.62) or Eq. (5.63). So far, the derivation has been done along the lines developed in Sections 5.3 and 5.4. However, to show the stability of the closed-loop system, it is not sufficient that the system (5.70) is SPR. It is also necessary that the signals in $\varphi$ are bounded. This condition can be difficult to show. Furthermore, Eqs. (5.76) are valid only if the control signal is generated from Eq. (5.75). This implies, for instance, that the control signal cannot be saturated. Notice that it is necessary to know the parameter $b_{0}$ to compute the augmented error $\varepsilon$ .

The derived algorithm thus requires that the high-frequency gain $b_{0}$ be known. If the parameter is not known, it can be estimated as follows. The error model of Eq. (5.73) can be written as

$$e _ {f} = b _ {0} \left(\varphi_ {f} ^ {T} \theta^ {0} + u _ {f}\right) \tag {5.78}$$

where

$$\varphi_ {f} = \frac {Q}{A _ {o} A _ {m}} \varphiu _ {f} = \frac {Q}{A _ {o} A _ {m} P _ {1}} u$$

A simple gradient estimator for $b_{0}$ and $\theta^{0}$ is then given by

$$\frac {d \theta}{d t} = \gamma^ {\prime} \hat {b} _ {0} \varphi_ {f} \varepsilon_ {p} = \gamma \varphi_ {f} \varepsilon_ {p} \tag {5.79}\frac {d \hat {b} _ {0}}{d t} = \gamma \left(\varphi_ {f} ^ {T} \theta + u _ {f}\right) \varepsilon_ {p}$$

where $\varepsilon_{p}$ is the prediction error

$$\varepsilon_ {p} = e _ {f} - \hat {e} _ {f} = e _ {f} - \hat {b} _ {0} \left(\varphi_ {f} ^ {T} \theta + u _ {f}\right) \tag {5.80}$$

Notice that $\hat{b}_{0}$ can be absorbed in the adaptation gain if its sign is known.
