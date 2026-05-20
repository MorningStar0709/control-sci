# LEMMA 6.1 Stability of a time-varying system

Consider the time-varying system

$$x (t + 1) = A (t) x (t) \tag {6.24}y (t) = C (t) x (t)$$

Assume that there exists a symmetric matrix $P(t) > 0$ such that

$$\boldsymbol {A} ^ {T} (t) \boldsymbol {P} (t + 1) \boldsymbol {A} (t) - \boldsymbol {P} (t) = - \boldsymbol {C} ^ {T} (t) \boldsymbol {C} (t) \tag {6.25}$$

Then Eqs. (6.24) are stable. Moreover, if the system is uniformly completely observable, that is, if there exist $\beta_{1} > 0$ , $\beta_{2} > 0$ , and N > 1 such that

$$0 < \beta_ {1} I \leq \sum_ {k = t} ^ {t + N - 1} \Phi^ {T} (k, t) C ^ {T} (k) C (k) \Phi (k, t) \leq \beta_ {2} I < \infty$$

for all t and where $\Phi(k,t)$ is the fundamental matrix, then Eqs. (6.24) are also exponentially stable.

Proof: Introduce the function

$$V (t) = x ^ {T} (t) P (t) x (t)$$

Hence

$$
\begin{array}{l} V (t + 1) - V (t) = x ^ {T} (t) A ^ {T} (t) P (t + 1) A (t) x (t) - x ^ {T} (t) P (t) x (t) \\ = - x ^ {T} (t) C ^ {T} (t) C (t) x (t) \leq 0 \\ \end{array}
$$

The function V can be considered a Lyapunov function for a discrete-time system. To prove stability for a discrete-time system using Lyapunov theory, we have to show that the difference

$$\Delta V (t) = V (t + 1) - V (t) \leq 0$$

and that the matrix $P(t)$ is positive definite. Iterating the system equations N steps gives

$$
\begin{array}{l} V (t + N) - V (t) = - \sum_ {k - t} ^ {t - N - 1} x ^ {T} (k) C ^ {T} (k) C (k) x (k) \\ = - x ^ {T} (t) \left(\sum_ {k = t} ^ {t + N - 1} \Phi^ {T} (k, t) C ^ {T} (k) C (k) \Phi (k, t)\right) x (t) \\ \leq - \beta_ {1} x ^ {T} (t) x (t) \leq - \frac {\beta_ {1}}{\lambda_ {\max} P (t)} V (t) \\ \end{array}
$$

where $\lambda_{max}(Pt)$ is the largest eigenvalue of $P(t)$ . Hence

$$V (t + N) \leq \left(1 - \frac {\beta_ {1}}{\lambda_ {\max} P (t)}\right) V (t) = \beta_ {3} V (t)$$

From Eq. (6.25) it follows that

$$
\begin{array}{l} P (t) = C ^ {T} (t) C (t) + A ^ {T} (t) P (t + 1) A (t) \\ = C ^ {T} (t) C (t) \\ + \boldsymbol {A} ^ {T} (t) \left(\boldsymbol {C} ^ {T} (t + 1) \boldsymbol {C} (t + 1) + \boldsymbol {A} ^ {T} (t + 1) \boldsymbol {P} (t + 2) \boldsymbol {A} (t + 1)\right) \boldsymbol {A} (t) \\ = \sum_ {k = t} ^ {\infty} \Phi^ {T} (k, t) C ^ {T} (k) C (k) \Phi (k, t) \\ > \sum_ {k = t} ^ {t + N - 1} \Phi^ {T} (k, t) C ^ {T} (k) C (k) \Phi (k, t) \geq \beta_ {1} I \\ \end{array}
$$

:

This shows that $\lambda_{max}(P(t)) > \beta_1$ and $\beta_3 < 1$ , which implies that $V(t)$ goes to zero exponentially. Furthermore,

$$P (t + N) = P (t) - \sum_ {k = t} ^ {t + N - 1} \Phi^ {T} (k, t) C ^ {T} (k) C (k) \Phi (k, t) \leq \beta_ {3} P (t)$$

or

$$P (t) \leq \frac {1}{1 - \beta_ {3}} \sum_ {k = t} ^ {t + N - 1} \Phi^ {T} (k, t) C ^ {T} (k) C (k) \Phi (k, t) \leq \frac {\beta_ {2}}{1 - \beta_ {3}} I$$

The matrix $P(t)$ is thus bounded from above and below. Since $V(t)$ goes to zero exponentially and $P(t)$ is bounded, it follows that the system (6.24) is exponentially stable. ☐

Applying this lemma to Eq. (6.23), we get the following theorem.
