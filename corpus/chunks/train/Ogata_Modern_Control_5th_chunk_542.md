(b)   
Figure 7–123   
(a) Nyquist plot; (b) complete Nyquist plot in the G plane.

Solution. Figure 7–123(b) shows a complete Nyquist plot in the G plane.The answers to the three questions are as follows:

(a) The closed-loop system is stable, because the critical point $( - 1 + j 0 )$ is not encircled by the Nyquist plot. That is, since P=0 and $N = 0 ;$ , we have $Z = N + P = 0$ .   
(b) The open-loop transfer function has one pole in the right-half s plane. Hence, $P = 1$ . (The open-loop system is unstable.) For the closed-loop system to be stable, the Nyquist plot must encircle the critical point $( - 1 + j 0 )$ once counterclockwise. However, the Nyquist plot does not encircle the critical point. Hence, N=0.Therefore, $Z = N + P = 1$ .The closed-loop system is unstable.   
(c) Since the open-loop transfer function has one zero, but no poles, in the right-half s plane, we have $Z = N + P = 0$ . Thus, the closed-loop system is stable. (Note that the zeros of the open-loop transfer function do not affect the stability of the closed-loop system.)

A–7–8. Is a closed-loop system with the following open-loop transfer function and with K=2 stable?

$$G (s) H (s) = \frac {K}{s (s + 1) (2 s + 1)}$$

Find the critical value of the gain K for stability.

Solution. The open-loop transfer function is

$$
\begin{array}{l} G (j \omega) H (j \omega) = \frac {K}{j \omega (j \omega + 1) (2 j \omega + 1)} \\ = \frac {K}{- 3 \omega^ {2} + j \omega (1 - 2 \omega^ {2})} \\ \end{array}
$$

This open-loop transfer function has no poles in the right-half s plane. Thus, for stability, the $- 1 + j 0$ point should not be encircled by the Nyquist plot. Let us find the point where the Nyquist plot crosses the negative real axis. Let the imaginary part of $G ( j \omega ) H ( j \omega )$ be zero, or

$$1 - 2 \omega^ {2} = 0$$

from which

$$\omega = \pm \frac {1}{\sqrt {2}}$$

Substituting $\omega = 1 / \sqrt { 2 }$ into $G ( j \omega ) H ( j \omega )$ , we obtain

$$G \left(j \frac {1}{\sqrt {2}}\right) H \left(j \frac {1}{\sqrt {2}}\right) = - \frac {2 K}{3}$$

The critical value of the gain K is obtained by equating $- 2 K / 3$ to –1, or

$$- \frac {2}{3} K = - 1$$

Hence,

$$K = \frac {3}{2}$$

The system is stable if $\textstyle 0 < K < { \frac { 3 } { 2 } }$ Hence, the system with K=2 is unstable. .

Figure 7–124   
Closed-loop system.   
![](image/9ddc4f4c06a18572577f5f196d098c41397d9284475d94c26506c28911c5e407.jpg)

<details>
<summary>flowchart</summary>
