$$
\begin{array}{l} \left\| \hat {\theta} (t) - \hat {\theta} (t - 1) \right\| ^ {2} = \frac {\gamma^ {2} \varphi^ {T} (t) \varphi (t) e ^ {2} (t)}{(\alpha + \varphi^ {T} (t) \varphi (t)) ^ {2}} \\ = \frac {\gamma^ {2} e ^ {2} (t)}{\alpha + \varphi^ {T} (t) \varphi (t)} \left(1 - \frac {\alpha}{\alpha + \varphi^ {T} (t) \varphi (t)}\right) \\ \end{array}
$$

It follows from property (ii) that the right-hand side of the preceding equation goes to zero as $t \to \infty$ if $\alpha > 0$ . Hence

$$
\begin{array}{l} \left\| \hat {\theta} (t) - \hat {\theta} (t - k) \right\| ^ {2} = \left\| \sum_ {i = 1} ^ {k} \hat {\theta} (t - i + 1) - \hat {\theta} (t - i) \right\| ^ {2} \\ \leq \sum_ {i = 1} ^ {k} \| \hat {\theta} (t - i + 1) - \hat {\theta} (t - i) \| ^ {2} \\ \end{array}
$$

where the right-hand side goes to zero as $t \rightarrow \infty$ for finite k.

Remark 1. For $\gamma = 1$ and $\alpha = 0$ the algorithm reduces to Kaczmarz's projection algorithm.

Remark 2. Notice that the result does not imply that the estimates $\hat{\theta}(t)$ converge.

Remark 3. The function $V(t)$ can be interpreted as a discrete-time Lyapunov function.

Theorem 6.3 is useful because it gives some properties of the estimator that are valid no matter how the regressors $\varphi(t)$ are generated. Additional conditions are required to guarantee that the estimates converge. The theorem will also be useful to prove convergence of the indirect adaptive schemes.
