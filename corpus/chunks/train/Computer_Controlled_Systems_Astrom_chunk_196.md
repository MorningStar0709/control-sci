# Example 3.12 Loss of reachability and observability

The discrete-time model of the harmonic oscillator is given by (see Example A.3)

$$
x (k h + h) = \left( \begin{array}{c c} \cos \omega h & \sin \omega h \\ - \sin \omega h & \cos \omega h \end{array} \right) x (k h) + \binom {1 - \cos \omega h} {\sin \omega h} u (k)

y (k h) = \left( \begin{array}{l l} 1 & 0 \end{array} \right) x (k h)
$$

The determinants of the controllability and observability matrices are

$$\det W _ {c} = - 2 \sin \omega h (1 - \cos \omega h)$$

and

$$\det W _ {o} = \sin \omega h$$

Both reachability and observability are lost for $\omega h = n\pi$ , although the corresponding continuous-time system given by (A.7) is both controllable and observable.

The example shows one obvious way to lose observability and/or reachability. If the sampling period is half the period time (or a multiple thereof) of the natural frequency of the system, then this frequency will not be seen in the output.

The rules of thumb for the choice of the sampling period given in Chapter 2 are such that this situation should not occur. The rules imply about 20 samples per period, not 2.

Observability and/or reachability are lost when the pulse-transfer operator has common poles and zeros. The poles and zeros are functions of the sampling interval. This implies that there will be common factors only for isolated values of the sampling period. A change in sampling period will make the system observable and/or reachable again.
