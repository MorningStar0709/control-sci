# Example 5.5 Motor with cancellation of process zero

The pulse-transfer function of a DC motor can be written as

$$H (z) = \frac {K (z - b)}{(z - 1) (z - a)} \tag {5.34}$$

(see Example A.2), where

$$
\begin{array}{l} \boldsymbol {K} = e ^ {- h} - \mathbf {1} + h \\ \alpha = e ^ {- h} \\ b = 1 - \frac {h (1 - e ^ {- h})}{e ^ {- h} - 1 + h} \\ \end{array}
$$

Notice that b < 0; that is, the zero is on the negative real axis. It is first assumed that the desired closed-loop system is characterized by the pulse-transfer function

$$H _ {m} (z) = \frac {z (1 + p _ {1} + p _ {2})}{z ^ {2} + p _ {1} z + p _ {2}} \tag {5.35}$$

The pulse-transfer function H has a zero z = b that is not included in $H_{m}$ . With the given specifications, it is necessary to cancel the zero z = b. Factor B as

$$
\begin{array}{l} \boldsymbol {B} ^ {+} = z - b \\ \boldsymbol {B} ^ {-} = \boldsymbol {K} \\ \end{array}
$$

Then

$$\bar {B} _ {m} = \frac {B _ {m}}{K} = \frac {1 + p _ {1} + p _ {2}}{K} z$$

The observer polynomial can be chosen as

$$A _ {0} (z) = 1$$

The degree of the polynomials $\bar{R}$ and S are given by

$$\deg \bar {R} = \deg A _ {o} + \deg A _ {m} - \deg A = 0\deg S = \deg A - 1 = 1$$

We now introduce $\bar{R}$ as a zero-order polynomial and S as a first-order polynomial in the design equation. The following polynomial identity is then obtained.

$$(z - 1) (z - a) r _ {0} + K \left(s _ {0} z + s _ {1}\right) = z ^ {2} + p _ {1} z + p _ {2}$$

Equating coefficients of equal powers of z gives the equations

$$r _ {0} = 1- (1 + a) r _ {0} + K s _ {0} = p _ {1}a r _ {0} + K s _ {1} = p _ {2}$$

Hence

$$r _ {0} = 1s _ {0} = \frac {1 + a + p _ {1}}{K}s _ {1} = \frac {p _ {2} - a}{K}$$

Further

$$T (z) = A _ {0} (z) \hat {B} _ {m} (z) = \frac {z (1 + p _ {1} + p _ {2})}{K} = t _ {0} z$$

The control law can be written as

$$u (k) = t _ {0} u _ {c} (k) - s _ {0} y (k) - s _ {1} y (k - 1) + b u (k - 1) \tag {5.36}$$

A simulation of the step response of the system is shown in Fig. 5.4. Notice the "ringing," or the "ripple," in the control signal, which is caused by the cancellation of the zero on the negative real axis. The ripple is not noticeable in the output signal at the sampling instants. It is, however, seen as a ripple in the output between the sampling instants. The amplitude of the ripple in the output depends on the sampling period. It goes down rapidly as the sampling period is decreased.

(a)   
![](image/fad57bb1ab364211cb2abd0411fd19b95bc696b5e04cf54f3ddc94526f66967d.jpg)

<details>
<summary>line</summary>
