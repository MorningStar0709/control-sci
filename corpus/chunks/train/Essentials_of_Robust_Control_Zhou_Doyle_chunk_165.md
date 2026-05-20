Problem 6.9 Suppose that $P$ is proper and has one right half plane zero at $s = z > 0$ . Suppose that $\begin{array} { r } { y = \frac { w } { 1 + P K } } \end{array}$ , where w is a unit step at time $t = 0$ , and that our performance specification is

$$
| y (t) | \leq \left\{ \begin{array}{l l} \alpha , & \text { if } 0 \leq t \leq T; \\ \beta , & \text { if } T <   t \end{array} \right.
$$

for some $\alpha > 1 > \beta > 0$ . Show that for a proper, internally stabilizing, LTI controller K to exist that meets the specification, we must have that

$$\ln \left(\frac {\alpha - \beta}{\alpha - 1}\right) \leq z T.$$

What tradeoffs does this imply?

Problem 6.10 Let K be a stabilizing controller for the plant

$$P = \frac {s - \alpha}{(s - \beta) (s + \gamma)}$$

$\alpha > 0 , \beta > 0 , \gamma \geq 0$ . Suppose $| S ( j \omega ) | \le \delta < 1$ , ∀ω $\in [ - \omega _ { 0 } , \omega _ { 0 } ]$ where

$$S (s) = \frac {1}{1 + P K}.$$

Find a lower bound for $\| S \| _ { \infty }$ and calculate the lower bound for $\alpha = 1 , \beta = 2 , \gamma = 1 0$ , $\delta = 0 . 2$ , and $\omega _ { 0 } = 1$ .
