# THEOREM 5.1 Lyapunov's stability theorem: time-invariant systems

If there exists a function $V: R^n \to R$ that is positive definite such that its derivative along the solution of Eq. (5.17),

$$\frac {d V}{d t} = \frac {\partial V ^ {T}}{\partial x} \frac {d x}{d t} = \frac {\partial V ^ {T}}{\partial x} f (x) = - W (x) \tag {5.19}$$

is negative semidefinite, then the solution $x(t) = 0$ to Eq. (5.17) is stable. If dV/dt is negative definite, then the solution is also asymptotically stable. The function V is called a Lyapunov function for the system (5.17).

Moreover if

$$\frac {d V}{d t} < 0 \quad \text { and } \quad V (x) \to \infty \quad \text { when } \quad \| x \| \to \infty$$

then the solution is globally asymptotically stable.

Proof: Given $\varepsilon > 0$ such that $\{x||x|| \leq \varepsilon\} \in U$ , determine $\ell$ and $\delta$ such that

$$\ell = \min _ {\| x \| = \varepsilon} V (x) = \max _ {\| x \| \leq \delta} V (x) \tag {5.20}$$

Consider initial conditions such that

$$\| x (0) \| < \delta$$

Since $V$ is positive definite, it then follows from Definition 5.2 that

$$V (x (0)) < \ell$$

To prove that inequality (5.18) holds, we proceed by contradiction. Assume that $t_1$ is the smallest value such that $\| x(t_1) \| - \varepsilon$ . It follows from Eq. (5.20) that

$$V \left(x (t _ {1})\right) \geq \ell$$

Furthermore,

$$V (x \left(t _ {1}\right)) = V (x (0)) + \int_ {0} ^ {t _ {1}} \frac {d V}{d t} d t = V (x (0)) - \int_ {0} ^ {t _ {1}} W (x (s)) d s \tag {5.21}$$

Since $W(x)$ is positive semidefinite, it follows that

$$V (x (t _ {1})) \leq V (x (0)) < \ell$$

and we have thus obtained a contradiction and it can be concluded that $\|x(t)\| < \varepsilon$ for all t, which by Definition 5.1 implies that the solution $x(t) = 0$ is stable. To prove asymptotic stability, we notice that it follows from Eq. (5.21) that

$$0 \leq \int_ {0} ^ {t} W (x (s)) d s = V (x (0)) - V (x (t)) \leq \ell$$

Since $W(x)$ and $x(t)$ are continuous, it then follows that

$$\lim _ {t \rightarrow \infty} W (x (t)) = 0$$

If $W(x)$ is positive definite, this implies that $x(t) \to 0$ as $t \to \infty$ .

Remark. Notice that it follows from the proof that if the derivative of the Lyapunov function is negative semidefinite, the solution converges to the set $\{x \mid W(x) = 0\}$ .
