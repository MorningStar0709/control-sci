# The Algorithm

Direct algorithms for adaptive control were discussed in Section 3.5. We give the proof for a simple algorithm of this type. Consider a process described by the difference equation

$$A ^ {*} (q ^ {- 1}) y (t) = B ^ {*} (q ^ {- 1}) u (t - d) \tag {6.38}$$

Let the desired response from command signal to process output be characterized by

$$A _ {m} ^ {*} (q ^ {- 1}) y (t) = t _ {0} u _ {c} (t - d)$$

This specification implies that all process zeros are canceled. Furthermore, let the observer polynomial be $A_{n}$ . A direct algorithm can then be formulated as follows. Estimate parameters of the model

$$A _ {0} ^ {*} A _ {m} ^ {*} y (t + d) = R ^ {*} u (t) + S ^ {*} y (t) = \varphi^ {T} (t) \theta \tag {6.39}$$

where

$$
\theta = \left( \begin{array}{c c c c c c c c} r _ {0} & r _ {1} & \dots & r _ {k} & s _ {0} & s _ {1} & \dots & s _ {l} \end{array} \right) ^ {T}

\varphi (t) = \left( \begin{array}{l l l l l l l l} u (t) & u (t - 1) & \dots & u (t - k) & y (t) & y (t - 1) & \dots & y (t - l) \end{array} \right) ^ {T} \tag {6.40}
$$

The parameters are estimated by using the following projection estimator:

$$\hat {\theta} (t) = \hat {\theta} (t - 1) + \frac {\gamma \varphi (t - d)}{\alpha + \varphi^ {T} (t - d) \varphi (t - d)} e (t) \tag {6.41}e (t) = y (t) - \varphi^ {T} (t - d) \hat {\theta} (t - 1)$$

with $0 < \gamma < 2$ and $\alpha > 0$ . This estimator is the same as Eqs. (6.22) except that $\varphi$ now has index t - d instead of t. The properties given in Theorem 6.3 are still valid.

The control law is

$$\hat {R} ^ {*} u (t) + \hat {S} ^ {*} y (t) = t _ {0} A _ {o} ^ {*} u _ {c} (t) \tag {6.42}$$

or, equivalently,

$$\hat {\theta} ^ {T} (t) \left(A _ {o} ^ {*} A _ {m} ^ {*} \varphi (t)\right) = t _ {0} A _ {o} ^ {*} u _ {c} (t) \tag {6.43}$$

where $u_{c}(t)$ is the desired setpoint. Notice that it must be required that $\hat{\theta}_1(t) = \hat{r}_0(t) \neq 0$ ; otherwise, the control law is not causal.
