# 6.2 Weighted $\mathcal { H } _ { 2 }$ and $\mathcal { H } _ { \infty }$ Performance

In this section, we consider how to formulate some performance objectives into mathematically tractable problems. As shown in Section 6.1, the performance objectives of a feedback system can usually be specified in terms of requirements on the sensitivity functions and/or complementary sensitivity functions or in terms of some other closedloop transfer functions. For instance, the performance criteria for a scalar system may be specified as requiring

$$
\left\{ \begin{array}{l l} | S (j \omega) | \leq \varepsilon , & \forall \omega \leq \omega_ {0}, \\ | S (j \omega) | \leq M, & \forall \omega > \omega_ {0} \end{array} \right.
$$

where $S ( j \omega ) = 1 / ( 1 + P ( j \omega ) K ( j \omega ) )$ . However, it is much more convenient to reflect the system performance objectives by choosing appropriate weighting functions. For example, the preceding performance objective can be written as

$$\left| W _ {e} (j \omega) S (j \omega) \right| \leq 1, \quad \forall \omega$$

with

$$
| W _ {e} (j \omega) | = \left\{ \begin{array}{l l} 1 / \varepsilon , & \forall \omega \leq \omega_ {0} \\ 1 / M, & \forall \omega > \omega_ {0} \end{array} \right.
$$

To use $W _ { e }$ in control design, a rational transfer function $W _ { e } ( s )$ is usually used to approximate the foregoing frequency response.

The advantage of using weighted performance specifications is obvious in multivariable system design. First, some components of a vector signal are usually more important than others. Second, each component of the signal may not be measured in the same units; for example, some components of the output error signal may be measured in terms of length, and others may be measured in terms of voltage. Therefore, weighting functions are essential to make these components comparable. Also, we might be primarily interested in rejecting errors in a certain frequency range (for example, low frequencies); hence some frequency-dependent weights must be chosen.

![](image/22fecbbfc7ff49093dec74dddaccb2d3f6356afccb882fc50e9df52393314325.jpg)

<details>
<summary>flowchart</summary>
