# 10.6 Sampling a Stochastic Differential Equation

If process models are presented in continuous time as stochastic differential equations, it is useful to sample these equations to obtain a discrete-time model.

Consider a process described by

$$d x = A x d t + d v _ {c} \tag {10.34}$$

where the process $v_{c}$ has zero mean value and uncorrelated increments. The incremental covariance of $v_{c}$ is $R_{1}dt$ . Let the sampling instants be $\{t_{k}; k = 0, 1, \ldots\}$ . Integration of (10.34) over one sampling period gives

$$x (t _ {k + 1}) = e ^ {A (t _ {k + 1} - t _ {k})} x (t _ {k}) + \int_ {t _ {k}} ^ {t _ {k + 1}} e ^ {A (t _ {k, 1} - s)} d v _ {c} (s)$$

Consider the random variable

$$v (t _ {k}) = \int_ {t _ {k}} ^ {t _ {k + 1}} e ^ {A (t _ {k + 1} - s)} d v _ {c} (s)$$

This variable has zero mean because $v_{c}$ has zero mean. The random variables $v(t_{k})$ and $v(t_{l})$ are also uncorrelated for $k \neq l$ because the increments of v over disjoint intervals are uncorrelated. The covariance of $v(t_{k})$ is given by

$$\mathrm{E} \left(v \left(t _ {k}\right), v ^ {T} \left(t _ {k}\right)\right) = \mathrm{E} \iint_ {t _ {k}} ^ {t _ {k + 1}} e ^ {\mathbf {A} \left(t _ {k + 1} - t\right)} d v _ {c} (s) d v _ {c} ^ {T} (t) e ^ {\mathbf {A} ^ {T} \left(t _ {k + 1} - t\right)} \tag {10.35}= \int_ {t _ {h}} ^ {t _ {h + 1}} e ^ {A (t _ {h + 1} - s)} R _ {1} e ^ {A ^ {T} (t _ {h + 1} - s)} d s$$

It is thus found that the random sequence $\{x(t_k), k = 0,1,\ldots\}$ obtained by sampling the process $\{x(t)\}$ is described by the difference equation

$$x (t _ {k + 1}) = e ^ {A (t _ {k + 1} - t _ {k})} x (t _ {k}) + v (t _ {k})$$

where $\{v(t_{k})\}$ is a sequence of uncorrelated random variables with zero mean and covariance (10.35).
