# PI Adjustments

All adjustment laws discussed so far have been integral controllers. That is, the parameter has always been obtained as the output of an integrator. There are, of course, many other possibilities for choosing the adaptation mechanism H in Fig. 5.18. For instance, it can be expected that quicker adaptation can be achieved by using a proportional and integral adjustment law. This means that the control law of Eq. (5.40) is replaced by

$$\theta (t) = - \gamma_ {1} u _ {c} (t) e (t) - \gamma_ {2} \int^ {t} u _ {c} (\tau) e (\tau) d \tau \tag {5.57}$$

Since a system with the transfer function

$$H (s) = \gamma_ {1} + \gamma_ {2} / s$$

is output strictly passive for positive $\gamma_{1}$ and $\gamma_{2}$ , it follows from Theorem 5.8 (the passivity theorem) that Eq. (5.57) gives a stable adjustment law if $GG_{c}$ is positive real.
