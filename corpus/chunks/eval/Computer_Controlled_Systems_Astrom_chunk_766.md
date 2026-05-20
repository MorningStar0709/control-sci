# Example 12.16 Intersample variation of the loss function

Consider the continuous-time system

$$d x = u d t + d v \tag {12.75}$$

where $v(t)$ is a Wiener process with incremental covariance $\sigma_{v}^{2}dt$ . Assume that the output is observed without antialiasing filters at times $t_{k}=k\cdot h$ , where h is the sampling period. Hence,

$$y (t _ {k}) = x (k) + \varepsilon (t _ {k})$$

where $\varepsilon(t_{k})$ is a sequence of independent random variables with zero mean and covariance $\sigma_{\varepsilon}^{2}$ . Sampling of the system gives

$$x (k h + h) = x (k h) + h u (k h) + v (k h + h) - v (k h)y (k h) = x (k h) + \varepsilon (k h)$$

Hence,

$$y (k h + h) = y (k h) + h u (k h) + \varepsilon (k h + h) - \varepsilon (k h) + v (k h + h) - v (k h)$$

The disturbance on the right-hand side may be represented as

$$w (k h + h) = e (k h + h) + c e (k h)$$

where $e(kh)$ is a sequence of independent zero-mean random variables with standard deviation $\sigma$ .

Simple calculations give

$$c = - 1 - \frac {h \sigma_ {v} ^ {2}}{2 \sigma_ {\varepsilon} ^ {2}} + \sqrt {\frac {h \sigma_ {v} ^ {2}}{\sigma_ {\varepsilon} ^ {2}} + \frac {h ^ {2} \sigma_ {v} ^ {4}}{4 \sigma_ {\varepsilon} ^ {4}}}\sigma^ {2} = - \frac {\sigma_ {\varepsilon} ^ {2}}{c}$$

The minimum-variance control law for the system is

$$u (k h) = - \frac {1 + c}{h} y (k h)$$

The standard deviation of the output under minimum-variance control is

$$\mathbf {E} y ^ {2} (t) = \sigma^ {2} \quad t = h, 2 h, \dots$$

The standard deviation of the state variable x is

$$\mathbf {E} x ^ {2} (t) = \sigma^ {2} - \sigma_ {\varepsilon} ^ {2} \quad t = h, 2 h, \dots$$

Equation (12.75) is integrated to determine the variance of the stete variable between the sampling instante. This gives

$$
\begin{array}{l} x (k h + s) = x (k h) + s u (k h) + v (k h + s) - v (k h) \\ = (1 - \alpha s) x (k h) - \alpha s \varepsilon (k h) + v (k h + s) - v (k h) \\ \end{array}
$$

where

$$\alpha = (1 + c) / h$$

We now introduce

$$P _ {x} (s) = \mathbf {E x} ^ {2} (k h + s)$$

It then follows that the output variance is

$$P _ {y} (s) = P _ {x} (s) + \sigma_ {\varepsilon} ^ {2} = (1 - \alpha s) ^ {2} (\sigma^ {2} - \sigma_ {\varepsilon} ^ {2}) + (\alpha s) ^ {2} \sigma_ {\varepsilon} ^ {2} + s \sigma_ {v} ^ {2} + \sigma_ {c} ^ {2}$$

The function $P_{y}(s)$ is shown in Fig. 12.10 when $\sigma_{\varepsilon} = \sigma_{v} = 1$ . Notice that

$$\max _ {s} \left(P _ {y} (0) - P _ {y} (s)\right) = h ^ {2} \sigma_ {v} ^ {2} / 2$$

The variation in $P_{y}$ over a sampling interval thus decreases with decreasing h.

The analysis is similar in the general case. The only difference is that Theorem 10.5 must be used to compute the state covariance. In the example the variance is largest at the sampling instants. This is not always the case. Also notice that the correct way of dealing with intersample ripple is to sample the continuous-time system and the continuous-time loss functions, as was discussed in Section 11.1.
