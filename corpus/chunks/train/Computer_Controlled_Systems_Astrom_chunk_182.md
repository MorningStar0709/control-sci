A closely related result that gives additional insight is obtained as follows. The pulse-transfer function of the closed-loop system given in (3.12) can also be written as

$$H _ {c l} = \frac {1}{\mathbf {1} + 1 / \mathcal {L} ^ {0}}$$

The poles of the closed-loop system are thus given by the zeros of the function.

$$
\begin{array}{l} f _ {c} (z) = 1 + \frac {1}{H _ {f b} (z) H ^ {0} (z)} \\ = 1 + \frac {1}{H _ {f b} (z) H (z)} + \frac {1}{H _ {f b} (z) H ^ {0} (z)} - \frac {1}{H _ {f b} (z) H (z)} \\ \end{array}
$$

It follows from the principle of variation of the argument that the differences between the zeros and poles outside the unit disc of the functions $1 + 1/L^{0}$ and $1 + 1/L$ are the same if

$$\left. \frac {1}{\mathcal {L} ^ {0} (z)} - \frac {1}{\mathcal {L} (z)} \right| < \left| 1 + \frac {1}{\mathcal {L} (z)} \right| \tag {3.14}$$

on the unit circle. The following result is thus obtained.

THEOREM 3.6 ROBUSTNESS 2 Consider the closed-loop systems S and $S^{0}$ obtained by applying unit negative feedback around systems with the pulse-transfer functions H and $H^{0}$ , respectively. The system $S^{0}$ is stable if the following conditions are true:

1. $S$ is stable.   
2. $H$ and $H^0$ have the same number of zeros outside the unit disc.   
3. The inequality (3.14) is fulfilled for $|z| = 1$ .

The theorem indicates the importance of knowing the number of zeros outside the unit disc. The theorem shows that stability can be maintained in spite of large differences between H and $H^{0}$ provided that the loop gain is large.

From the conclusions of Theorems 3.5 and 3.6, the following rules are obtained for design of a feedback system based on approximate or uncertain models.

It is important to know the number of unstable poles and zeros.

It is not important to know the model precisely for those frequencies for which the loop gain can be made large.

It is necessary to make the loop gain small for those frequencies for which the relative error $\Delta H/H$ is large.

It is necessary to have a model that describes the system precisely for those frequencies for which $H^{0}(z) \approx -1$ .
