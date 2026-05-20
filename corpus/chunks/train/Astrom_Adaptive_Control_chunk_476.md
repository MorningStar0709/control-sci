# EXAMPLE 6.16 Bounded disturbances

Consider the system

$$y (t + 1) + a y (t) = u (t) + v (t + 1)$$

Use an adaptive control law with $A_{o}^{*} = A_{m}^{*} = 1$ . (The desired response is thus $y_{m}(t + 1) = u_{c}(t)$ .) The control law is

$$u (t) = - \hat {\theta} (t) y (t) + u _ {c} (t)$$

where

$$\hat {\theta} (t + 1) = \hat {\theta} (t) + \frac {y (t)}{1 + y ^ {2} (t)} e (t + 1)e (t + 1) = y (t + 1) - \hat {\theta} y (t) - u (t)$$

Introduce

$$\tilde {\theta} = \hat {\theta} - \theta^ {0}$$

where $\theta^{0} = -a$ . The closed-loop system can be described by the equations

$$\tilde {\theta} (t + 1) = \frac {1}{1 + y ^ {2} (t)} \tilde {\theta} (t) + \frac {y (t) v (t + 1)}{1 + y ^ {2} (t)} \tag {6.87}y (t + 1) = - \bar {\theta} (t) y (t) + u _ {c} (t) + v (t + 1)$$

To show that $y(t)$ may be unbounded, we want to construct a disturbance v and a command signal $u_{c}$ such that the parameter error goes to infinity. Assume that initial conditions are chosen such that $\tilde{\theta}(1)=0$ and $y(1)=1$ . Define

$$f (t) \triangleq \left(\sqrt {t (t - 1)} - (t - 1)\right) \left(1 + \frac {1}{t - 1}\right) \quad t = 2, 3, \dots , T - 5$$

for some large $T$ . Choose the following disturbance:

$$v (t) = 1 - \frac {1}{\sqrt {t - 1}} + f (t) \quad t = 2, 3, \dots , T - 5$$

and the following command signal:

$$u _ {c} (t - 1) = \frac {1}{\sqrt {t}} - f (t) \quad t = 2, 3, \dots , T - 5$$

The signals v and $u_{c}$ are bounded. A straightforward calculation gives

$$\tilde {\theta} (t) = \sqrt {t} - 1y (t) = \frac {1}{\sqrt {t}}$$

for $t = 1, \ldots, T - 5$ . Further, let

$$
v (t) = 0 \quad t = T - 4, \dots , T
u _ {c} (t - 1) = \left\{ \begin{array}{l l} 0 & t = T - 4 \\ 1 & t = T - 3, \dots , T \end{array} \right.
$$

It can then be verified that $\bar{\theta}(t)$ and $y(t)$ for large T are approximately given by the following table.

<table><tr><td>t</td><td> $\hat{\theta}(t)$ </td><td>y(t)</td></tr><tr><td>T-4</td><td> $\sqrt{T}$ </td><td>-1</td></tr><tr><td>T-3</td><td> $\frac{\sqrt{T}}{2}$ </td><td> $\sqrt{T}$ </td></tr><tr><td>T-2</td><td> $\frac{1}{2\sqrt{T}}$ </td><td> $-\frac{T}{2}$ </td></tr><tr><td>T-1</td><td> $\frac{1}{\sqrt{T}T^{2}}$ </td><td> $\frac{\sqrt{T}}{4}$ </td></tr><tr><td>T</td><td> $\frac{16}{\sqrt{T}T^{3}}$ </td><td>1</td></tr></table>

Now choose $v(T + 1)$ and $u_{c}(T)$ such that $\tilde{\theta}(T + 1) = 0$ and $y(T + 1) = 1$ . The state vector of Eqs. (6.87) is then equal to the initial state. By repeating the procedure for increasing values of $T$ , a subsequence of $y(t)$ will increase as $-T / 2$ and therefore is unbounded.

Example 6.16 shows that the algorithm may behave badly even if it is assumed that the disturbances are bounded. Robustness against bounded disturbances can be obtained by using conditional updating as shown in the following theorem.
