# E.5 Discretization methods

Discretization is done using a zero-order hold. That is, the input is only updated at discrete intervals and it’s held constant between samples (see figure E.21). The exact method of applying this uses the matrix exponential, but this can be computationally expensive. Instead, approximations such as the following are used.

1. Forward Euler method. This is defined as $y _ { n + 1 } = y _ { n } + f ( t _ { n } , y _ { n } ) \Delta t .$   
2. Backward Euler method. This is defined as $y _ { n + 1 } = y _ { n } + f ( t _ { n + 1 } , y _ { n + 1 } ) \Delta t .$   
3. Bilinear transform. The first-order bilinear approximation is s = 2T 1−z−11+z−1 . $\begin{array} { r } { s = \frac { 2 } { T } \frac { 1 - z ^ { - 1 } } { 1 + z ^ { - 1 } } } \end{array}$

where the function $f ( t _ { n } , y _ { n } )$ is the slope of y at n and T is the sample period for the discrete system. Each of these methods is essentially finding the area underneath a curve. The forward and backward Euler methods use rectangles to approximate that area while the bilinear transform uses trapezoids (see figures E.22 and E.23). Since these are approximations, there is distortion between the real discrete system’s poles and the approximate poles. This is in addition to the phase loss introduced by discretizing at a given sample rate in the first place. For fast-changing systems, this distortion can quickly lead to instability.

Figures E.24, E.25, and E.26 show simulations of the same controller for different sampling methods and sample rates, which have varying levels of fidelity to the real system.

Forward Euler is numerically unstable for low sample rates. The bilinear transform is a significant improvement due to it being a second-order approximation, but zero-order hold performs best due to the matrix exponential including much higher orders.

Table E.3 compares the Taylor series expansions of several common discretization methods (these are found using polynomial division). The bilinear transform does best with accuracy trailing off after the third-order term. Forward Euler has no secondorder or higher terms, so it undershoots. Backward Euler has twice the second-order term and overshoots the remaining higher order terms as well.

![](image/34491dcb96f9c2764c6b14d5b279cfcac51d173761d31b9cb4a83497ed96d2aa.jpg)

<details>
<summary>line</summary>
