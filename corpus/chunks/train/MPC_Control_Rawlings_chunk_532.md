# Example 4.37: What’s wrong with the simplest particle filter?

Consider the following linear system with Gaussian noise.

$$
\begin{array}{l} A = \left[ \begin{array}{c c} \cos \theta & \sin \theta \\ - \sin \theta & \cos \theta \end{array} \right] \quad \theta = 6 \qquad C = \left[ \begin{array}{c c} 0. 5 & 0. 2 5 \end{array} \right] \qquad G = I \qquad B = I \\ \overline {{{x}}} (0) = \left[ \begin{array}{l} 1 \\ 1 \end{array} \right] \quad Q _ {0} = \frac {1}{4} \left[ \begin{array}{l l} 7 & 5 \\ 5 & 7 \end{array} \right] \quad Q = 0. 0 1 I \quad R = 0. 0 1 \\ u (0, 1, \dots , 4) = \left[ \begin{array}{c} 7 \\ 2 \end{array} \right], \left[ \begin{array}{c} 5 \\ 5 \end{array} \right], \left[ \begin{array}{c} - 1 \\ 2 \end{array} \right], \left[ \begin{array}{c} - 1 \\ - 2 \end{array} \right], \left[ \begin{array}{c} 1 \\ - 3 \end{array} \right] \\ \end{array}
$$

(a) Plot the particle locations versus time from $k = 0$ to $k = 5$ . Plot also the 95% contour of the true conditional density $p ( x ( k ) | \mathbf { y } ( k ) )$ . Discuss the locations of the particles using the simplest particle filter.

(b) Write out the recursions for the conditional density of the particle locations $p ( x _ { i } ( k ) | \mathbf { y } ( k ) )$ as well as the true conditional density $p ( x ( k ) | \mathbf { y } ( k ) )$ . Discuss the differences.

![](image/e3c1a7b5964673d012f2e7e85bc91ecbeb6f86926365e3651178061b94c009ce.jpg)

<details>
<summary>scatter</summary>
