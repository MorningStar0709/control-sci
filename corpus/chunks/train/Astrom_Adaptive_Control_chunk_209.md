# EXAMPLE 4.2 Minimum-variance control of a first-order system

Consider the first-order system

$$y (t + 1) + a y (t) = b u (t) + e (t + 1) + c e (t) \tag {4.4}$$

where $|c| < 1$ and $\{e(t)\}$ is a sequence of independent random variables with unit variance.

Consider the output at time $t + 1$ . From (4.4) it follows that by using $u(t)$ it is possible to change $y(t + 1)$ arbitrarily. Further, $e(t + 1)$ is independent of $y(t)$ and $u(t)$ ; thus

$$\operatorname{var} y (t + 1) \geq \operatorname{var} e (t + 1) = 1$$

Given measurements up to time $t$ , we can use Eq. (4.4) to compute $e(t)$ . The controller

$$u (t) = \frac {a y (t) - c e (t)}{b} \tag {4.5}$$

gives

$$y (t + 1) = e (t + 1) \tag {4.6}$$

which gives the lower bound of the variance of $y$ . If Eq. (4.5) is used all the time, then from Eq. (4.6), it follows that $y(t) = e(t)$ , and we get the controller

$$u (t) = \frac {a - c}{b} y (t) \tag {4.7}$$

□

The minimum-variance controller can in the general case be derived by using similar ideas as Example 4.2. Define

$$d _ {0} = \deg A - \deg B$$

as the pole excess of the system. This is the same as the time delay in the system. The input at time t will influence the output first at time $t + d_{0}$ . Now consider

$$y (t + d _ {0}) = \frac {B}{A} u (t + d _ {0}) + \frac {C}{A} e (t + d _ {0}) \tag {4.8}$$

Let the polynomial $F$ of degree $d_0 - 1$ be the quotient, and let the polynomial $G$ of degree $n - 1$ be the remainder when $q^{d_0 - 1}C$ is divided by $A$ . Hence

$$\frac {q ^ {d _ {0} - 1} C (q)}{A (q)} = F (q) + \frac {G (q)}{A (q)}$$

This can be interpreted as a Diophantine equation,

$$q ^ {d _ {1}} ^ {- 1} C (q) = A (q) F (q) + G (q) \tag {4.9}$$

Hence the output at $t + d_0$ can be written as

$$y (t + d _ {0}) = \frac {B}{A} u (t + d _ {0}) + F e (t + 1) + \frac {q G}{A} e (t)$$

where

$$F (q) = q ^ {d _ {0} - 1} + f _ {1} q ^ {d _ {0} - 2} + \dots + f _ {d _ {0} - 1} \tag {4.10}G (q) = g _ {0} q ^ {n - 1} + g _ {1} q ^ {n - 2} + \dots + g _ {n - 1} \tag {4.11}$$

From Eq. (4.1) we can determine $e(t)$ :

$$e (t) = \frac {A}{C} y (t) - \frac {B}{C} u (t)$$

From the measurement of $y(t)$ and $u(t)$ it is thus possible to compute the noise sequence, the innovations. This equation is an observer in which the dynamics are given by the C polynomial. It now follows that

$$
\begin{array}{l} y (t + d _ {0}) = F e (t + 1) + \left(\frac {B}{A} q ^ {d _ {0}} - \frac {q G B}{A C}\right) u (t) + \frac {q G A}{A C} y (t) \\ = F e (t + 1) + \frac {B q}{A C} \left(q ^ {a _ {0} - 1} C - G\right) u (t) + \frac {q G}{C} y (t) \\ = F e (t + 1) + \frac {q B F}{C} u (t) + \frac {q G}{C} y (t) \tag {4.12} \\ \end{array}
$$
