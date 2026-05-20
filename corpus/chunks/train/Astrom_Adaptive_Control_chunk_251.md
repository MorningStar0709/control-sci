# Minimum Control Effort

The control strategy that brings $y(t + d)$ to $y_{m}(t + d)$ while minimizing Eq. (4.56) will now be derived. Equation (4.54) is

$$
\begin{array}{l} y (t + d) = R _ {c} ^ {*} (q ^ {- 1}) u (t + d - d _ {0}) + \bar {y} _ {d} (t) \\ = r _ {d 0} u (t + \nu) + \dots + r _ {d \nu} u (t) - \bar {y} _ {d} (t) \\ \end{array}
$$

where $\nu = d - d_0$ . The condition

$$y (t + d) = y _ {m} (t + d) = \bar {y} _ {d} (t) + R _ {d} ^ {*} (q ^ {- 1}) u (t + d - d _ {0})$$

can be regarded as a constraint while minimizing Eq. (4.56). Introducing the Lagrangian multiplier $\lambda$ gives the loss function

$$2 J = u (t) ^ {2} + \dots + u (t + v) ^ {2} + 2 \lambda \left(y _ {m} (t + d) - \bar {y} _ {d} (t) - R _ {d} ^ {*} (q ^ {- 1}) u (t + v)\right)$$

Equating the partial derivatives with respect to $u(t), \cdots, u(t + \nu)$ and $\lambda$ to zero gives

$$u (t) = \lambda r _ {d v}$$

:

$$u (t + \nu) = \lambda r _ {d 0}y _ {m} (t + d) - \bar {y} _ {d} (t) = r _ {d 0} u (t + v) + \dots + r _ {d v} u (t)$$

This set of equations gives

$$u (t) = \frac {y _ {m} (t + d) - \bar {y} _ {d} (t)}{\mu}$$

where

$$\mu = \frac {\sum_ {i = 0} ^ {v} r _ {d i} ^ {2}}{r _ {d v}}$$

Using the definition of $\bar{y}_{d}(t)$ gives

$$\mu u (t) = y _ {m} (t + d) - \bar {R} _ {d} ^ {*} u (t - 1) - G _ {d} ^ {*} y (t)$$

or

$$u (t) = \frac {y _ {m} (t + d) - G _ {d} ^ {*} y (t)}{\mu + q ^ {- 1} \bar {R} _ {d} ^ {*}} = \frac {y _ {m} (t + d + n - 1) - G _ {d} (q) y (t)}{\mu q ^ {n - 1} + \bar {R} _ {d} (q)} \tag {4.60}$$

Using Eq. (4.60) and the model of Eq. (4.50) gives the closed-loop characteristic polynomial

$$P (q) = A (q) \left(q ^ {n - 1} \mu + \bar {R} _ {d} (q)\right) + G _ {d} (q) B (q)$$

This is of the same form as Eq. (4.56), with $R_{d}(1)$ replaced by $\mu$ . This implies that the closed-loop poles approach the zeros of $q^{n-1}A(q)$ when $A(q)$ is stable and when $d \to \infty$ . What will happen when the open-loop system is unstable? Consider the following example.
