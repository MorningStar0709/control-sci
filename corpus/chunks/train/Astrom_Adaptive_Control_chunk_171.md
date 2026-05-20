# 3.4 CONTINUOUS-TIME SELF-TUNERS

Continuous-time self-tuners can be derived in the same way as discrete-time self-tuners. To show this, consider a system that can be described by the model (3.1) with v = 0, that is,

$$A (p) y (t) = B (p) u (t)$$

where $A(p)$ and $B(p)$ are polynomials in the differential operator, $p = d / dt$ :

$$A (p) = p ^ {n} + a _ {1} p ^ {n - 1} + \dots + a _ {n}B (p) = b _ {1} p ^ {n - 1} + \dots + b _ {n}$$

A self-tuning regulator can be obtained by applying Algorithm 3.1. The only complication is that we now must apply recursive least-squares estimation to the continuous-time model. This was discussed in Section 2.3. Let us recall the key idea. Since it is undesirable to take derivatives, a stable filtering transfer function $H_{f}$ with a pole excess of n or more is introduced.

If we introduce the filtered signals

$$y _ {f} (t) = H _ {f} y (t) \quad u _ {f} (t) = H _ {f} u (t)$$

the model (3.1) can be written as

$$p ^ {n} y _ {f} (t) = \varphi^ {T} (t) \theta$$

where

$$
\varphi (t) = \left( \begin{array}{l l l l l} - p ^ {n - 1} y _ {f} & \dots & - y _ {f} & p ^ {n - 1} u _ {f} & \dots & u _ {f} \end{array} \right) ^ {T}

\theta = \left( \begin{array}{c c c c c c} a _ {1} & \dots & a _ {n} & b _ {1} & \dots & b _ {n} \end{array} \right) ^ {T}
$$

By using least squares with exponential forgetting the parameter estimate is then obtained from Theorem 2.5:

$$\frac {d \hat {\theta} (t)}{d t} = P (t) \varphi (t) \left(P ^ {n} y _ {f} (t) \quad \varpi^ {T} (t) \hat {\theta} (t)\right)\frac {d P (t)}{d t} = \alpha P (t) - P (t) \varphi (t) \varphi^ {T} (t) P (t)$$

We illustrate the procedure given by Algorithm 3.1 by an example.
