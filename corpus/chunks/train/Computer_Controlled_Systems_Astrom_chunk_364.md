# 5.12 Problems

5.1 Use Euclid's algorithm to determine the largest common factor of the polynomials

$$
\begin{array}{l} B (z) = z ^ {3} - 2 z ^ {2} + 1. 4 5 z - 0. 3 5 \\ A (z) = z ^ {4} - 2. 6 z ^ {3} + 2. 2 5 z ^ {2} - 0. 8 z + 0. 1 \\ \end{array}
$$

5.2 Given the pulse-transfer function

$$H (z) = \frac {1}{z + a}$$

and let the desired system be given by

$$H _ {m} (z) = \frac {1 + \alpha}{z + \alpha}$$

(a) Determine a controller of the form (5.2) using Algorithm 5.1.   
(b) Determine the characteristic polynomial of the closed-loop system.

5.3 Consider the system given by the pulse-transfer function

$$H (z) = \frac {z + 0 . 7}{z ^ {2} - 1 . 8 z + 0 . 8 1}$$

Use polynomial design to determine a controller such that the closed-loop system has the characteristic polynomial

$$z ^ {2} - 1. 5 z + 0. 7$$

Let the observer polynomial have as low order as possible and place all observer poles in the origin. Consider the following two cases:

(a) The process zero is canceled.   
(b) The process zero is not canceled.

Simulate the two cases and discuss the differences between the two controllers. Which one should be preferred?

5.4 For the system in Problem 5.2, assume that the feedback can be made only from the error. Thus the controller has the form

$$u (k) = \frac {S}{R} \left(u _ {c} (k) - y (k)\right)$$

(a) Determine $S / R$ such that the desired closed-loop system is obtained.   
(b) Determine the characteristic equation of the closed-loop system and compare it with Problem 5.2. Consider, for instance, the case when $|a| > 1$ .

5.5 Consider the system in Problem 5.2 and assume that the closed-loop system should be able to eliminate step disturbances at the input of the process. This means that v in Fig. 5.3 is a step.

(a) Analyze what happens when the controller derived in Problem 5.2 is used and when $v$ is a step.   
(b) Redesign the controller such that the specifications will be fulfilled.

5.6 Show that (5.41) is correct.

5.7 Consider the system in Problem 5.2 and assume that $a = -0.9$ and $\alpha = -0.5$ .

(a) Use straightforward calculations to determine the influence of modeling errors. Assume that the design is made for $a = -0.9$ and determine the stability of the closed-loop system if the true process has a pole in $a^0$ .   
(b) Use Theorem 3.5 to determine the influence of modeling errors. What happens when $\alpha$ is decreased?
