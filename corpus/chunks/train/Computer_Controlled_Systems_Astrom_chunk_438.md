# Predictive First-Order-Hold Sampling: A State-Space Approach

We will now consider a system in which the sampling period is constant and equal to h. In Chapter 2 we showed that the behavior of the system at the sampling interval at the sampling instants t = kh could be conveniently described by a difference equation. The key idea was that the system equations could be integrated over one sampling interval if the shape of the input signal was known. In Chapter 2 the calculations were based on the assumption that sampling was made by a zero-order hold, which implies that the control signal is constant over the sampling intervals. It is straightforward to repeat the calculations in Chapter 2 for the case when the control signal is affine over a sampling interval. The modifications required can also be obtained as follows.

Consider a continuous-time system described by

$$\frac {d x}{d t} = A x (t) + B u (t) \tag {7.13}y (t) = C x (t) + D u (t)$$

Assume that the input signal is linear between the sampling instants. Integration of $(7.13)$ over one sampling period gives

$$
\begin{array}{l} x (k h + h) = e ^ {A h} x (k h) \\ + \int_ {k h} ^ {k h + h} e ^ {A (k h + h - s)} B \left[ u (k h) + \frac {s - k h}{h} \left(u (k h + h) - u (k h)\right) \right] d s \tag {7.14} \\ \end{array}
$$

Hence

$$x (k h + h) = \Phi x (k h) + \Gamma u (k h) + \frac {1}{h} \Gamma_ {1} (u (k h + h) - u (k h))= \Phi x (k h) + \frac {1}{h} \Gamma_ {1} u (k h + h) + \left(\Gamma - \frac {1}{h} \Gamma_ {1}\right) u (k h)$$

where

$$\Phi = e ^ {A h}\Gamma = \int_ {0} ^ {h} e ^ {A s} d s B \tag {7.15}\Gamma_ {1} = \int_ {0} ^ {h} e ^ {A s} (h - s) d s B$$

The pulse-transfer function that corresponds to ramp-invariant sampling thus becomes

$$H (z) = D + C (z I - \Phi) ^ {- 1} \left(\frac {z}{h} \Gamma_ {1} + \Gamma - \frac {1}{h} \Gamma_ {1}\right) \tag {7.16}$$

It follows from (7.14) that the matrices $\Phi, \Gamma$ , and $\Gamma_1$ satisfy the differential equations

$$\frac {d \Phi (t)}{d t} = \Phi (t) A\frac {d \Gamma (t)}{d t} = \Phi (t) B\frac {d \Gamma_ {1} (t)}{d t} = \Gamma (t)$$

These equations can also be written as

$$
\frac {d}{d t} \left( \begin{array}{c c c} \Phi (t) & \Gamma (t) & \Gamma_ {1} (t) \\ 0 & I & I t \\ 0 & 0 & I \end{array} \right) = \left( \begin{array}{c c c} \Phi (t) & \Gamma (t) & \Gamma_ {1} (t) \\ 0 & I & I t \\ 0 & 0 & I \end{array} \right) \left( \begin{array}{c c c} A & B & 0 \\ 0 & 0 & I \\ 0 & 0 & 0 \end{array} \right)
$$

This implies that the matrices $\Phi$ , $\Gamma$ , and $\Gamma_{1}$ can be obtained as

$$
\left( \begin{array}{c c c} \Phi & \Gamma & \Gamma_ {1} \end{array} \right) = \left( \begin{array}{c c c} I & 0 & 0 \end{array} \right) \exp \left(\left( \begin{array}{c c c} A & B & 0 \\ 0 & 0 & I \\ 0 & 0 & 0 \end{array} \right) h\right) \tag {7.17}
$$

The calculation of ramp-invariant systems is illustrated by some examples.
