# EXAMPLE 5.7 First-order MRAS based on stability theory

Consider the problem in Example 5.2. The desired response is given by

$$\frac {d y _ {m}}{d t} = - a _ {m} y _ {m} + b _ {m} u _ {c}$$

where $a_{m} > 0$ and the reference signal is bounded. The process is described by

$$\frac {d y}{d t} = - a y + b u$$

The controller is

$$u - \theta_ {1} u _ {c} - \theta_ {2} y$$

Introduce the error

$$e = y - y _ {m}$$

Since we are trying to make the error small, it is natural to derive a differential equation for the error. We get

$$\frac {d e}{d t} = - a _ {m} e - (b \theta_ {2} + a - a _ {m}) y + (b \theta_ {1} - b _ {m}) u _ {c}$$

Notice that the error goes to zero if the parameters are equal to the values given by Eqs. (5.8). We will now attempt to construct a parameter adjustment mechanism that will drive the parameters $\theta_{1}$ and $\theta_{2}$ to their desired values. For this purpose, assume that $b\gamma > 0$ and introduce the following quadratic function:

$$V \left(e, \theta_ {1}, \theta_ {2}\right) = \frac {1}{2} \left(e ^ {2} + \frac {1}{b \gamma} \left(b \theta_ {2} + a - a _ {m}\right) ^ {2} + \frac {1}{b \gamma} \left(b \theta_ {1} - b _ {m}\right) ^ {2}\right)$$

This function is zero when e is zero and the controller parameters are equal to the correct values. For the function to qualify as a Lyapunov function the derivative dV/dt must be negative. The derivative is

$$
\begin{array}{l} \frac {d V}{d t} = e \frac {d e}{d t} + \frac {1}{\gamma} (b \theta_ {2} + a - a _ {m}) \frac {d \theta_ {2}}{d t} + \frac {1}{\gamma} (b \theta_ {1} - b _ {m}) \frac {d \theta_ {1}}{d t} \\ = - a _ {m} e ^ {2} + \frac {1}{\gamma} (b \theta_ {2} + a - a _ {m}) \left(\frac {d \theta_ {2}}{d t} - \gamma y e\right) \\ + \frac {1}{\gamma} (b \theta_ {1} - b _ {m}) \left(\frac {d \theta_ {1}}{d t} + \gamma u _ {c} e\right) \\ \end{array}
$$

If the parameters are updated as

$$
\begin{array}{l} \frac {d \theta_ {1}}{d t} = - \gamma u _ {c} e \tag {5.27} \\ \frac {d \theta_ {2}}{d t} = \gamma y e \\ \end{array}
$$

we get

$$\frac {d V}{d t} = - a _ {m} e ^ {2}$$

The derivative of V with respect to time is thus negative semidefinite but not negative definite. This implies that $V(t) \leq V(0)$ and thus that e, $\theta_{1}$ , and $\theta_{2}$ must be bounded. This implies that $y = e + y_{m}$ also is bounded. To use Theorem 5.4, we determine

$$\frac {d ^ {2} V}{d t ^ {2}} = - 2 a _ {m} e \frac {d e}{d t} = - 2 a _ {m} e (- a _ {m} e - (b \theta_ {2} + a - a _ {m}) y + (b \theta_ {1} - b _ {m}) u _ {c})$$
