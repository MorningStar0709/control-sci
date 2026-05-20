# 9.4 DISCRETE-TIME SYSTEMS

By way of introduction, let us consider the first-order system

$$\dot {y} = - y + u. \tag {9.15}$$

One way of approximating this in discrete time is to use the finite-difference formula for the derivative:

$$\frac {y (t + T _ {s}) - y (t)}{T _ {s}} = - y (t) + u (t)$$

or

$$y (t + T _ {s}) = (1 - T _ {s}) y (t) + T _ {s} u (t). \tag {9.16}$$

Higher-order derivatives are approximated by higher-order differences. For instance, the finite-difference formula for $\ddot{y}$ is

$$\frac {1}{T _ {s}} \left[ \frac {y (t + T _ {s}) - y (t)}{T _ {s}} - \frac {y (t) - y (t - T _ {s})}{T _ {s}} \right] = \frac {y (t + T _ {s}) - 2 y (t) + y (t - T _ {s})}{T _ {s} ^ {2}}.$$

In general, an $n$ th-order linear differential equation is rendered in discrete time as the $n$ th-order difference equation

$$
\begin{array}{l} y (t) + a _ {1} y \left(t - T _ {s}\right) + \dots + a _ {n} y \left(t - n T _ {s}\right) \\ = b _ {0} u (t) + b _ {1} u \left(t - T _ {s}\right) + \dots + b _ {n} u \left(t - n T _ {s}\right). \tag {9.17} \\ \end{array}
$$

If we now consider $y(t)$ and $u(t)$ , sampled at uniform intervals $T_s$ , Equation 9.17 becomes

$$
\begin{array}{l} (k) + a _ {1} \widehat {y} (k - 1) + \dots + a _ {n} \widehat {y} (k - n) \\ = b _ {0} \widehat {u} (k) + b _ {1} \widehat {u} (k - 1) + \dots + b _ {n} \widehat {u} (k - n). \tag {9.18} \\ \end{array}
$$

Recall that, in continuous time, the transfer function is the ratio of the output transform to the input transform, starting from rest. In discrete-time systems, initial rest means that the output was zero for k < 0. We assume that the input was also zero for k < 0. Use of the delay theorem on Equation 9.18 yields

$$\frac {\widehat {y} (z)}{\widehat {u} (z)} = G (z) = \frac {b _ {0} + b _ {1} z ^ {- 1} + \cdots + b _ {n} z ^ {- n}}{1 + a _ {1} z ^ {- 1} + \cdots + a _ {n} z ^ {- n}} \tag {9.19}= \frac {b _ {0} z ^ {n} + b _ {1} z ^ {n - 1} + \cdots + b _ {n}}{z ^ {n} + a _ {1} z ^ {n - 1} + \cdots + a _ {n}}. \tag {9.20}$$

This is known as the pulse transfer function.
