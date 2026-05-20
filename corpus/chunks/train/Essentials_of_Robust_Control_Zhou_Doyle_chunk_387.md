This gives the following generalized system:

$$
G (s) = \left[ \begin{array}{c c c c c c c} - \alpha & 0 & 1 & - 2 & 1 & 1 & 0 \\ 0 & - 1 0 0 & 0 & 0 & 0 & 0 & - 9 0 \\ 0 & 0 & 0 & - 2 \alpha & \alpha & \alpha & 0 \\ 0 & 0 & 0 & 0 & 1 & 0 & 0 \\ 0 & 0 & 0 & 3 & 2 & 0 & 1 \\ \hline 1 & 0 & 0 & 0 & 0 & 0 & 0 \\ 0 & 1 & 0 & 0 & 0 & 0 & 1 \\ \hline 0 & 0 & 1 & - 2 & 1 & 1 & 0 \end{array} \right].
$$

The suboptimal $\mathcal { H } _ { \infty }$ controller $\hat { K } _ { \infty }$ for each α can be computed easily as

$$\hat {K} _ {\infty} = \frac {- 2 0 6 0 3 8 1 . 4 (s + 1) (s + \alpha) (s + 1 0 0) (s - 0 . 1 5 5 7)}{(s + \alpha) ^ {2} (s + 3 2 . 1 7) (s + 2 6 2 3 4 3) (s - 1 9 . 8 9)},$$

which gives the closed-loop $\mathcal { H } _ { \infty }$ norm 7.854. Hence the controller $K _ { \infty } = - \hat { K } _ { \infty } ( s ) M ( s )$ is given by

$$K _ {\infty} (s) = \frac {2 0 6 0 3 8 1 . 4 (s + 1) (s + 1 0 0) (s - 0 . 1 5 5 7)}{s (s + 3 2 . 1 7) (s + 2 6 2 3 4 3) (s - 1 9 . 8 9)} \approx \frac {7 . 8 5 (s + 1) (s + 1 0 0) (s - 0 . 1 5 5 7)}{s (s + 3 2 . 1 7) (s - 1 9 . 8 9)},$$

which is independent of α as expected. Similarly, we can solve an optimal $\mathcal { H } _ { 2 }$ controller

$$\hat {K} _ {2} = \frac {- 4 3 . 4 8 7 (s + 1) (s + \alpha) (s + 1 0 0) (s - 0 . 0 6 9)}{(s + \alpha) ^ {2} (s ^ {2} + 3 0 . 9 4 s + 4 1 1 . 8 1) (s - 7 . 9 6 4)}$$

and

$$K _ {2} (s) = - \hat {K} _ {2} (s) M (s) = \frac {4 3 . 4 8 7 (s + 1) (s + 1 0 0) (s - 0 . 0 6 9)}{s (s ^ {2} + 3 0 . 9 4 s + 4 1 1 . 8 1) (s - 7 . 9 6 4)}.$$

An approximate integral control can also be achieved without going through the preceding process by letting

$$W _ {e} = \tilde {W} _ {e} = \frac {1}{s + \epsilon}, M (s) = 1$$

for a sufficiently small $\epsilon > 0$ . For example, a controller for $\epsilon = 0 . 0 0 1$ is given by

$$K _ {\infty} = \frac {3 1 6 8 8 0 (s + 1) (s + 1 0 0) (s - 0 . 1 5 4 5)}{(s + 0 . 0 0 1) (s + 3 2) (s + 4 0 3 7 0) (s - 2 0)} \approx \frac {7 . 8 5 (s + 1) (s + 1 0 0) (s - 0 . 1 5 4 5)}{s (s + 3 2) (s - 2 0)},$$

which gives the closed-loop $\mathcal { H } _ { \infty }$ norm of 7.85. Similarly, an approximate $\mathcal { H } _ { 2 }$ integral controller is obtained as

$$K _ {2} = \frac {4 3 . 4 7 (s + 1) (s + 1 0 0) (s - 0 . 0 6 7 9)}{(s + 0 . 0 0 1) (s ^ {2} + 3 0 . 9 3 s + 4 1 1 . 7) (s - 7 . 9 7 2)} \approx \frac {4 3 . 4 7 (s + 1) (s + 1 0 0) (s - 0 . 0 6 7 9)}{s (s ^ {2} + 3 0 . 9 3 s + 4 1 1 . 7) (s - 7 . 9 7 2)}.$$
