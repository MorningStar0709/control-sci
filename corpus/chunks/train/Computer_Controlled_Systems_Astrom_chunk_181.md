# Robustness

We will now consider the situation when the design of the controller is based on the nominal model H, but the true open-loop pulse-transfer function is $H^{0}(z)$ . The closeness of H to $H^{0}$ needed to make the closed-loop system stable is of concern. Consider the simple closed-loop system in Fig. 3.10 with $H(z)$ replaced by $H^{0}(z)$ . The pulse-transfer function of the closed-loop system is

$$H _ {c l} (z) = \frac {H _ {f f} H ^ {0} (z)}{1 + \mathcal {L} ^ {0} (z)} \tag {3.12}$$

The poles of the closed-loop system are thus the zeros of the function

$$
\begin{array}{l} f (z) = 1 + H _ {f b} (z) H ^ {0} (z) \\ = 1 + H _ {f b} (z) H (z) + H _ {f b} (z) H ^ {0} (z) - H _ {f b} (z) H (z) \\ = 1 + H _ {f b} (z) H (z) + H _ {f b} (z) \left[ H ^ {0} (z) - H (z) \right] \\ \end{array}
$$

If

$$\left| H _ {f b} \left(H ^ {0} (z) - H (z)\right) \right| < | 1 + L (z) | = \left| \frac {H}{H _ {c l}} \right| \cdot \left| H _ {f f} \right| \tag {3.13}$$

on the unit circle, then it follows from the principle of variation of the argument that the differences between the number of poles and zeros outside the unit disc for the functions $1 + L$ and $1 + L^{0}$ are the same.

The relative precision needed for stability robustness is obtained by dividing (3.13) by L

$$\left| \frac {H ^ {0} (z) - H (z)}{H} \right| \leq \left| \frac {1 + \mathcal {L}}{\mathcal {L}} \right| = \left| \frac {1}{\mathcal {T}} \right|$$

where the last equality is obtained from (3.11). The complementary sensitive function thus makes it possible to determine bounds for stability robustness. The following theorem results.

THEOREM 3.5 ROBUSTNESS 1 Consider the closed-loop systems S and $S^{0}$ obtained by applying unit negative feedback around systems with pulse-transfer functions H and $H^{0}$ , respectively. The system $S^{0}$ is stable if the following conditions are true:

1. $S$ is stable.   
2. H and $H^{0}$ have the same number of poles outside the unit disc.   
3. The inequality (3.13) is fulfilled for $|z| = 1$ .

The result shows that it is important to know the number of unstable modes in order to design a regulator for the system. The theorem is, however, conservative. The inequality also gives the frequency range in which it is important to have a good description of the process. Notice in particular that the precision requirements are very modest for the frequencies where the loop gain is large. Good precision is needed for frequencies where $H^{0}(z) \approx -1$ .
