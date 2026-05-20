$R_{d}^{*}(q^{-1})u(t+d-d_{0})$ depends on $u(t),\ldots,u(t+d-d_{0})$ , and $\bar{y}_{d}(t)$ is a function of $u(t-1),u(t-2),\ldots,$ and $y(t),y(t-1),\ldots$ . The variable $\bar{y}_{d}(t)$ can be interpreted as the constrained prediction of $y(t+d)$ under the assumption that $u(t)$ and future control signals are zero. The output at time $t+d$ thus depends on future control signals (if $d>d_{0}$ ), the control signal to be chosen, and old inputs and outputs. If $d>d_{0}$ , it is necessary to make some assumptions about the future control signals. One possibility is to assume that the control signal will remain constant, that is, that

$$u (t) = u (t + 1) = \dots = u (t + d - d _ {0}) \tag {4.55}$$

Another way is to determine the control law that brings $y(t+d)$ to a desired value while minimizing the control effort over the prediction horizon, that is, to minimize

$$\sum_ {k = t} ^ {t + d} u (k) ^ {2} \tag {4.56}$$

A third way is to assume that the increment of the control signal will be zero after some time. This is used, for instance, in generalized predictive control (GPC), which is discussed below.
