$$G (s) = \frac {2 5 1 2 . 3 s ^ {2} + 5 . 8 1 4 5 (1 0 ^ {6}) s + 1 . 5 8 0 6 (1 0 ^ {9})}{s ^ {4} + 1 0 0 . 4 8 4 s ^ {3} + 1 . 1 8 8 0 (1 0 ^ {5}) s ^ {2} + 5 . 8 1 4 5 (1 0 ^ {6}) s + 1 . 5 8 0 6 (1 0 ^ {9})} \tag {9.68}$$

The characteristic roots of the I/O equation (9.66) or the poles of G(s) are both determined by computing the roots of the fourth-order polynomial

$$s ^ {4} + 1 0 0. 4 8 4 s ^ {3} + 1. 1 8 8 0 (1 0 ^ {5}) s ^ {2} + 5. 8 1 4 5 (1 0 ^ {6}) s + 1. 5 8 0 6 (1 0 ^ {9}) = 0 \tag {9.69}$$

Table 9.2 Parameters for the Optical Disk Drive System [6]

<table><tr><td>Optical Disk Drive System Parameter</td><td>Numerical Value</td></tr><tr><td>PUH mass,  $m_{1}$ </td><td> $6(10^{-4})$  kg</td></tr><tr><td>PUH suspension stiffness,  $k_{1}$ </td><td>60 N/m</td></tr><tr><td>PUH suspension friction,  $b_{1}$ </td><td>0.03 N-s/m</td></tr><tr><td>Chassis/cart mass,  $m_{2}$ </td><td>0.124 kg</td></tr><tr><td>Chassis suspension stiffness,  $k_{2}$ </td><td>1960 N/m</td></tr><tr><td>Chassis suspension friction,  $b_{2}$ </td><td>6.23 N-s/m</td></tr></table>

The four roots (or poles) are two complex conjugate pairs:

$$s _ {1, 2} = - 2 4. 9 5 8 7 \pm j 1 2 2. 8 6 3 8 \quad \text { and } \quad s _ {3, 4} = - 2 5. 2 8 3 2 \pm j 3 1 6. 1 0 2 2$$

Consequently, the transient response of the PUH mass for an impulsive input $x _ { \mathrm { i n } } ( t )$ will be two exponentially damped sinusoidal functions. The two frequencies of the transient response are the imaginary parts of the two complex roots: 122.86 rad/s (or 19.6 Hz) and 316.10 rad/s (or 50.3 Hz). The PUH mass $m _ { 1 }$ will vibrate at these two frequencies after an impulsive frame displacement. These transient vibrations will die out in approximately $t _ { S } = 0 .$ .16 s because both roots have real parts equal to −25 and $e ^ { - 2 5 t _ { S } } = e ^ { - 4 }$ .
