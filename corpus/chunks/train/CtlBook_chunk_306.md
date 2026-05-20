# Overshoot, %OS

Overshoot is expressed as a percentage of the input amplitude. In some applications a brief tansient overshoot is acceptable. In other applications, (think of a elevator controller) overshoot is unacceptable1.

The analytical calculation of overshoot from second order systems is somewhat involved. A few computational results gives a lookup table (Table 9.2) in which overshoot depends on the damping ratio, ζ (Chapter 5), or equivalently the angle formed by the complex conjugate poles $( \theta = \cos ^ { - 1 } ( \zeta ) . )$ )

<table><tr><td>%OS</td><td> $\zeta$ </td><td> $T_r$ </td><td> $\theta$ </td></tr><tr><td>10%</td><td>0.587</td><td> $1.8/\omega_n$ </td><td> $54^\circ$ </td></tr><tr><td>5%</td><td>0.695</td><td> $2.1/\omega_n$ </td><td> $46^\circ$ </td></tr><tr><td>2%</td><td>0.777</td><td> $2.3/\omega_n$ </td><td> $39^\circ$ </td></tr><tr><td>1%</td><td>0.829</td><td> $2.6/\omega_n$ </td><td> $34^\circ$ </td></tr></table>

Table 9.2: Table of numerically computed values of percent overshoot vs. damping ratio (ζ). $T _ { r }$ is also shown for completeness. Note that rise time gets longer as overshoot is reduced.
