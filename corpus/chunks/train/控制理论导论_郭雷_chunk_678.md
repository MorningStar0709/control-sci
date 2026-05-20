$$
\begin{array}{l} B _ {k} ^ {\mathrm{T}} P _ {k + 1} ^ {- 1} B _ {k} = B _ {k} ^ {\mathrm{T}} \left[ B _ {k} P _ {k} B _ {k} ^ {\mathrm{T}} + Q _ {k} \right] ^ {- 1} B _ {k} = P _ {k} ^ {- 1} - \left[ P _ {k} + P _ {k} B _ {k} ^ {\mathrm{T}} Q _ {k} ^ {- 1} B _ {k} P _ {k} \right] ^ {- 1} \\ = P _ {k} ^ {- 1 / 2} \left\{I - \left[ I + P _ {k} ^ {1 / 2} B _ {k} ^ {\mathrm{T}} Q _ {k} ^ {- 1} B _ {k} P _ {k} ^ {1 / 2} \right] ^ {- 1} \right\} P _ {k} ^ {- 1 / 2} \\ \leqslant \left\{1 - \left[ 1 + \left\| Q _ {k} ^ {- 1} B _ {k} P _ {k} B _ {k} ^ {\mathrm{T}} \right\| \right] ^ {- 1} \right\} P _ {k} ^ {- 1} \\ \leqslant \left(1 - \frac {1}{1 + \| Q _ {k} ^ {- 1} P _ {k + 1} \|}\right) P _ {k} ^ {- 1}. \\ \end{array}
$$

于是，利用式(9.3.7)得

$$V _ {k + 1} \leqslant \left(1 - \frac {1}{1 + \| Q _ {k} ^ {- 1} P _ {k + 1} \|}\right) V _ {k}.$$

从而

$$V _ {n} \leqslant \prod_ {k = m} ^ {n - 1} \left(1 - \frac {1}{1 + \| Q _ {k} ^ {- 1} P _ {k + 1} \|}\right) V _ {m}.$$

因此，我们有

$$
\begin{array}{l} \left\| \prod_ {k = m} ^ {n - 1} (I - F _ {k}) \right\| ^ {2} = \max _ {\| x _ {m} \| = 1} \| x _ {n} \| ^ {2} = \max _ {\| x _ {m} \| = 1} \| x _ {n} ^ {\mathrm{T}} P _ {n} ^ {- 1 / 2} P _ {n} ^ {1 / 2} \| ^ {2} \\ \leqslant \max _ {\| x _ {m} \| = 1} \| x _ {n} ^ {T} P _ {n} ^ {- 1 / 2} \| ^ {2} \cdot \| P _ {n} ^ {1 / 2} \| ^ {2} = \max _ {\| x _ {m} \| = 1} (V _ {n} \| P _ {n} \|) \\ \leqslant \left\{\prod_ {k = m} ^ {n} \left(1 - \frac {1}{1 + \| Q _ {k} ^ {- 1} P _ {k + 1} \|}\right) \right\} \cdot \left\{\| P _ {n} \| \cdot \max _ {\| x _ {m} \| = 1} V _ {m} \right\} \\ \leqslant \left\{\prod_ {k = m} ^ {n} \left(1 - \frac {1}{1 + \| Q _ {k} ^ {- 1} P _ {k + 1} \|}\right) \right\} \cdot \{\| P _ {n} \| \cdot \| P _ {m} ^ {- 1} \| \}. \\ \end{array}
$$

因此，利用 Hölder 不等式易知定理的结论成立.

在上一定理中, 我们把验证矩阵序列 $\{F_k\} \in S_p$ 的问题转化为验证由 Lyapunov 方程决定的某一标量序列是否属于 $S^0$ 的问题. 下面我们进一步讨论 $S^0$ 的性质.

命题9.3.1 设 $\{\alpha_k, \mathcal{F}_k\}$ 与 $\{\beta_k, \mathcal{F}_k\}$ 是两个适应过程，使得 $\beta_k \in [0,1]$ 且

$$E [ \beta_ {k + 1} | \mathcal {F} _ {k} ] \geqslant \alpha_ {k}, \quad k \geqslant 0,$$

则 $\{\alpha_{k}\} \in S^{0}$ 意味着 $\{\beta_{k}\} \in S^{0}$ .

证明 首先假设 $0 \leqslant \alpha_{k} < 1$ . 对任何 $n > m, k \in [m, n]$ 定义

$$
\begin{array}{l} A _ {k} = \left\{\prod_ {i = m} ^ {k} (1 - \alpha_ {i}) \right\} ^ {- 1}, \quad A _ {m - 1} = 1, \\ x _ {k + 1} = (1 - \beta_ {k + 1}) x _ {k}, \quad x _ {m} = 1. \\ \end{array}
$$

于是

$$x _ {n + 1} = \prod_ {i = m} ^ {n} (1 - \beta_ {i + 1}).$$

注意到

$$E A _ {k} x _ {k + 1} = E \left\{A _ {k} \left[ 1 - E \left(\beta_ {k + 1} \mid \mathcal {F} _ {k}\right) \right] x _ {k} \right\} \leqslant E A _ {k} \left(1 - \alpha_ {k}\right) x _ {k} = E A _ {k - 1} x _ {k},$$

故
