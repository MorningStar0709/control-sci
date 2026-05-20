# 2.2 Derive the discrete-time system corresponding to the following continuous-time systems when a zero-order-hold circuit is used:

(a)

$$
\frac {d x}{d t} = \left( \begin{array}{c c} 0 & 1 \\ - 1 & 0 \end{array} \right) x + \binom{0}{1} u

y = \left( \begin{array}{l l} 1 & 0 \end{array} \right) x
$$

(b)

$$\frac {d ^ {2} y}{d t ^ {2}} + 3 \frac {d y}{d t} + 2 y = \frac {d u}{d t} + 3 u$$

(c)

$$\frac {d ^ {3} y}{d t ^ {3}} = u$$

![](image/bdf6adcfd8da7af1b7f420dc5393ce12e0f371f134b75d909e808ff3170c1862.jpg)  
Figure 2.11 Poles (x) and zeros (O) when the system (2.38) is sampled with h = 0, 0.2, 0.5, 1, 2, and 3.

2.3 The following difference equations are assumed to describe continuous-time systems sampled using a zero-order-hold circuit and the sampling period h. Determine, if possible, the corresponding continuous-time systems.

(a)

$$y (k h) - 0. 5 y (k h - h) = 6 u (k h - h)$$

(b)

$$
x (k h + h) = \left( \begin{array}{c c} - 0. 5 & 1 \\ 0 & - 0. 3 \end{array} \right) x (k h) + \binom {0. 5} {0. 7} u (k h)

y (k h) = \left( \begin{array}{l l} 1 & 1 \end{array} \right) x (k h)
$$

(c)

$$y (k h) + 0. 5 y (k h - h) = 6 u (k h - h)$$

2.4 Consider the harmonic oscillator [see Example A.3 or Problem 2.2(a)]. Compute the step response at 0, h, 2h, ... when the sampling period is (a) $h = \pi/2$ , (b) $h = \pi/4$ . Compare with the continuous-time step response.

2.5 Sample the system

$$G (s) = \frac {1}{s ^ {2} (s + 2) (s + 3)}$$

using a zero-order-hold circuit and h = 1.

2.6 Consider the system in (2.1). Assume that the input is a sum of impulses at the sampling instants, that is,

$$u (t) = \sum \delta (t - k h) u (k h)$$

Determine the discrete-time representation.

2.7 Find the transformation matrix, T, that transforms the state-space representation of the double integrator (2.7) into diagonal or Jordan form.

2.8 Determine the pulse-transfer function of the system

$$
x (k h + h) = \left( \begin{array}{c c} 0. 5 & - 0. 2 \\ 0 & 0 \end{array} \right) x (k h) + \binom {2} {1} u (k h)

y (k h) = \left( \begin{array}{l l} 1 & 0 \end{array} \right) x (k h)
$$

2.9 Many physical systems can be described by the form

$$
\frac {d x}{d t} = \left( \begin{array}{c c} - a & b \\ c & - d \end{array} \right) x + \binom{f}{g} u
$$

where $a, b, c$ , and $d$ are nonnegative. Derive a formula for the sampled-data system when using a zero-order hold. (Hint: Show first that the poles of the system are real.)
