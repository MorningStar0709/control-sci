# THEOREM 6.7 Boundedness and convergence

Consider a system described by Eq. (6.38). Let the system be controlled with the adaptive control algorithm given by Eqs. (6.40), (6.41), and (6.42) where the command signal $u_{c}$ is bounded. Assume that

A1: The time delay d is known.

A2: Upper bounds on the degrees of the polynomials $A^*$ and $B^*$ are known.

A3: The polynomial B has all its zeros inside the unit disc.

A4: The sign of $b_{0} = r_{0}$ is known.

Then

(i) The sequences $\{u(t)\}$ and $\{y(t)\}$ are bounded.

(ii) $\lim_{t\to \infty}\left|A_{m}^{*}(q^{-1})y(t) - t_0u_c(t - d)\right| = 0$

Proof: Introduce the control error

$$
\begin{array}{l} \varepsilon (t) = A _ {o} ^ {*} \left(A _ {m} ^ {*} y (t) - t _ {0} u _ {c} (t - d)\right) = P ^ {*} y (t) - t _ {0} A _ {o} ^ {*} u _ {c} (t - d) \\ = P ^ {*} y (t) - \theta^ {T} (t - d) \left(P ^ {*} \varphi (t - d)\right) \\ = P ^ {*} e (t) + P ^ {*} \left(\theta^ {T} (t - 1) \varphi (t - d)\right) - \theta^ {T} (t - d) \left(P ^ {*} \varphi (t - d)\right) \\ = P ^ {*} e (t) + \sum_ {i = 0} ^ {\deg P} p _ {i} (\theta (t - 1 - i) - \theta (t - d)) ^ {T} \varphi (t - d - i) \tag {6.45} \\ \end{array}
$$

where $P = A_{o}A_{m}$ has been introduced to simplify the writing. The first two equalities are trivial. The third is obtained from Eq. (6.39), the fourth from Eqs. (6.41), and the last by expanding the expression.

It now follows from properties (ii) and (iii) of Theorem 6.3 that

$$\lim _ {t \rightarrow \infty} \frac {\varepsilon (t)}{\sqrt {\alpha + \varphi^ {T} (t - d) \varphi (t - d)}} = 0$$

It follows from the first equality in Eq. (6.45) that

$$A _ {o} ^ {*} A _ {m} ^ {*} y (t) = \varepsilon (t) + t _ {0} A _ {o} ^ {*} u _ {c} (t)$$

Since the polynomials $A_{o}$ and $A_{m}$ are stable and since $u_{c}$ is bounded, it follows that

$$| y (t) | \leq \alpha_ {1} + \beta_ {1} \max _ {0 \leq k \leq t} | \varepsilon (k) |$$

Moreover, since the polynomial B is stable, it follows that

$$| u (t - d) | \leq \alpha_ {2} + \beta_ {2} \max _ {0 \leq k \leq t} | y (k) |$$

Hence

$$| \varphi (t - d) | \leq \alpha_ {3} + \beta_ {3} \max _ {0 \leq k \leq t} | \varepsilon (k) |$$

If we apply Lemma 6.2, it follows that $\varphi(t)$ is bounded and that $\varepsilon(t) \to 0$ as $t \to \infty$ . Since the polynomial $A_{o}^{*}$ is stable, property (ii) also follows.

Remark 1. We used an algorithm for which the details of the proof are simple. With minor modification the results can be extended to cover many of the direct algorithms given in Section 3.5.
