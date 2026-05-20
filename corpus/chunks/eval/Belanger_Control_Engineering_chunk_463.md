b. With $W = \begin{bmatrix} 0 & 0 \\ 0 & 1 \end{bmatrix}$ and $V > 0$ as design parameters, obtain an optimal observer. Calculate the transfer function $\widehat{x}_1 / y$ , and discuss its variation with $\omega$ and $V$ .

![](image/e142e751d08f5bd69f0accdcc290b5d44d1fcd54117bd3b527e2e605dc7f5584.jpg)

7.46 dc servo with flexible shaft For the dc servo with flexible shaft of Problem 2.5 (Chapter 2), we wish to study the effectiveness of state estimation, given different combinations of measurements. Suppose that $\theta_{2}, \omega_{2}$ , and $i$ are available, with respective precisions of $\pm 0.001$ rad, $\pm 0.05$ rad/s, and $\pm .005$ A. We model the disturbance input by assuming there is an external torque acting directly on the output shaft; this amounts to adding the vector

$$
\left[ \begin{array}{l} 0 \\ 0 \\ 0 \\ w \\ 0 \end{array} \right]
$$

to the right-hand side of the state equations.

a. Design an optimal observer, using $\theta_{2}$ , $\omega_{2}$ , and i as measurements. Use the design parameters

$$
V = \operatorname{diag} \left[ \begin{array}{c c c} 0. 0 0 1 ^ {2} & 0. 0 5 ^ {2} & 0. 0 0 5 ^ {2} \end{array} \right]
$$

and

$$
W = \left[ \begin{array}{c c c c c} 0 & 0 & 0 & w _ {0} & 0 \end{array} \right] ^ {T} \left[ \begin{array}{c c c c c} 0 & 0 & 0 & w _ {0} & 0 \end{array} \right].
$$

with $w_{0}=5$ .

b. Simulate the system and the observer with $w(t) = 5u_0(t)$ , with both the system and the observer in the zero state at $t = 0_{-}$ .

c. Repeat parts (a) and (b), but without the $\omega_{2}$ measurement. Discuss the usefulness of the angular velocity sensor in this case.

![](image/1e1d0aa943bd34abf691af43deb5e78fe9f126acff5e6c579faf00aa0e7d2cec.jpg)

7.47 Drum speed control The system of Problem 2.6 (Chapter 2) is to be provided with angular velocity sensors accurate to $\pm v_0$ rad/s. External disturbances are taken into account by modeling the load torque $T_0$ as an impulse $10^{5}u_{0}(t)$ .

a. Using the design parameters

$$
V = \operatorname{diag} \left[ v _ {0} ^ {2} \quad v _ {0} ^ {2} \quad v _ {0} ^ {2} \right]
W = \left[ \begin{array}{c c c c c} 0 & 0 & 1 0 ^ {- 4} & 0 & 0 \end{array} \right] ^ {T} 1 0 ^ {1 0} \left[ \begin{array}{c c c c c} 0 & 0 & 1 0 ^ {- 4} & 0 & 0 \end{array} \right]
$$

with $v_{0}=1.0$ rad/s, design an optimal observer, using $\omega_{0}$ , $\omega_{1}$ , and $\omega_{2}$ as outputs.
