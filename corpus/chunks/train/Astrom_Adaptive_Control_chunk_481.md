# The High-Frequency Gain

For a process that has no right half-plane zeros, the standard direct discrete-time algorithm is based on the model

$$A _ {o} ^ {*} A _ {m} ^ {*} y (t + d) = b _ {0} \left(R ^ {*} u (t) + S ^ {*} y (t)\right)$$

where $b_{0}$ is the coefficient of the first nonvanishing term in the B polynomial. With some abuse of language this coefficient is called the high-frequency gain because it is the first nonvanishing coefficient of the impulse response. For continuous-time systems the transfer function of the process is approximately $G(s) = b_{0}s^{-dh}$ . In Theorem 6.7 it was required that the sign of the coefficient $b_{0}$ be known. There are several ways to deal with the parameter $b_{0}$ . It may be absorbed into R and S and estimated. The polynomial R then has the form

$$R (q) = r _ {0} q ^ {k} + r _ {1} q ^ {k - 1} + \dots + r _ {k}$$

The problem with this approach is that some safeguards must be taken to avoid the estimate $r_{0}$ becoming too small. Another possibility is to introduce a crude fixed estimate of $b_{0}$ . The following analysis shows what happens when this is done. Let the true system be

$$y (t + 1) = b _ {0} \left(u (t) + \psi^ {T} (t) \theta^ {0}\right)$$

and let the model be

$$y (t + 1) = r _ {0} (u (t) + \psi^ {T} (t) \theta) = r _ {0} u (t) + \varphi^ {T} (t) \theta$$

With zero command signal the control law becomes

$$u (t) = - \psi^ {T} (t) \hat {\theta} (t)$$

The equation for parameter updating is

$$\hat {\theta} (t + 1) = \hat {\theta} (t) + P (t + 1) \varphi (t) e (t + 1)$$

where

$$e (t + 1) = y (t + 1) = b _ {0} u (t) + b _ {0} \psi^ {T} (t) \theta^ {0}= - b _ {0} \psi^ {T} (t) (\hat {\theta} (t) - \theta^ {0}) = - \frac {b _ {0}}{r _ {0}} \varphi^ {T} (t) (\hat {\theta} (t) - \theta^ {0})$$

The estimation error is thus governed by

$$\tilde {\theta} (t + 1) = \left(I - \frac {b _ {0}}{r _ {0}} P (t + 1) \varphi (t) \varphi^ {T} (t)\right) \tilde {\theta} (t)$$

With a pure projection algorithm we have

$$P (t + 1) = \frac {1}{\varphi^ {T} (t) \varphi (t)}$$

In this case the matrix in large parentheses has one eigenvalue $(1 - b_{0}/r_{0})$ and the remaining eigenvalues 1. With least-squares updating, the averaged equation for $\tilde{\theta}$ becomes

$$\tilde {\theta} (t + 1) = \left(1 - \frac {b _ {0}}{r _ {0}}\right) \tilde {\theta} (t)$$

Hence, to remain stable, it must be required that

$$0 < \frac {b _ {0}}{r _ {0}} < 2$$

If an algorithm with a fixed $r_{0}$ is used, it is convenient to absorb $r_{0}$ in the scaling of the signals. This is discussed in more detail in Chapter 11. When the parameter $b_{0}$ is estimated, it can be treated like the other parameters. However, because of the special structure of the model it is useful to use special algorithms such as the ones discussed in Section 5.8.
