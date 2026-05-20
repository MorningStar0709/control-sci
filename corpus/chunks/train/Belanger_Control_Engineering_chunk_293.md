a. With $v = v_{sp} - k\theta_2$ , write the state equations describing the closed-loop system, with $v_{sp}$ as the new input.   
b. Following Example 5.8, write the closed-loop system A matrix as a constant matrix plus another matrix, linear in K.   
c. Follow Example 5.8 and write the system as a new pure-gain system, where $K$ is the gain (set $v_{sp}$ to zero; it does not affect the poles).   
d. Obtain the Root Locus with K as the parameter.

![](image/a4953ce4b468e12785fb77d18ae323cd4b6101ef01f7761fa4273f64544c7cbd.jpg)

5.23 Compute the Nyquist plot $(\omega \geq 0)$ for the loop gain of Problem 5.3, with $k = 1$ , and determine the range(s) of $k$ for which the closed-loop system is stable.

![](image/a5f0124f47952072389657cca99cbac562c749c2bd8abe41c7cc2bc8c87ee783.jpg)

5.24 Repeat Problem 5.23 for the loop gain of Problem 5.4.

![](image/2bab50963bab4a7abf0927c028102b19ca702cc28b1d4ac4da46199d05a07739.jpg)

5.25 Repeat Problem 5.23 for the loop gain of Problem 5.5.

5.26 Use the Nyquist method to prove the result of Problem 5.6.

5.27 Repeat Problem 5.26 for the loop gain of Problem 5.7.

![](image/7ec3af07232b243b52a59ad4fff7685339bf7aecfa4fe362e5879db13286a7ee.jpg)

5.28 Plot magnitude and phase Bode plots for the loop gain of Problem 5.3, with k = 1. From the Bode plots, identify the real-axis crossings of the Nyquist plot, and give the range of k for which the closed-loop system is stable.

![](image/e99188d706ea7346229ddb6914bbbf8e0f27890fc61bf4b858b149059c83bc1e.jpg)

5.29 Repeat Problem 5.28 for the loop gain of Problem 5.4.

5.30 Figure 5.33 shows Bode plots for the loop gain of a system. Identify the real-axis crossings of the Nyquist plot. What is the range of stabilizing gains if the loop gain has no poles in the open RHP? What is the range if the loop gain has one RHP pole?

5.31 Repeat Problem 5.30 for the Bode plots of Figure 5.34.

![](image/4f200cc8a67971fcfeaa49561c0549b9e624bfa60c78fb0e4f899f9416e89789.jpg)

5.32 High-wire artist In Problem 4.31 (Chapter 4), an $H^{\infty}$ optimal control was designed, leading (as usual) to a nonproper controller. We wish to redesign the controller, taking into account actuator limitations and model uncertainty. We propose to achieve this by replacing the controller $F(s)$ with $[F(s)] / (\tau s + 1)^n$ , where $n$ is chosen to ensure that the new controller will have one more pole than zeros.
