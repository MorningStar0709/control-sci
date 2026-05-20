ii) 现在考察 $A$ 中的 $p \in (0,1)$ 情形.

记

$$y _ {k} = | x _ {k} | ^ {p} - E [ | x _ {k} | ^ {p} | \mathcal {F} _ {k - 1} ].$$

由于在 A 上

$$
\begin{array}{l} \sum_ {k = 1} ^ {\infty} E \left[ | y _ {k} | \left| \mathcal {F} _ {k - 1} \right| \leqslant \sum_ {k = 1} ^ {\infty} E \left[ \left(| x _ {k} | ^ {p} + E \left(| x _ {k} | ^ {p} \mid \mathcal {F} _ {k - 1}\right)\right) \mid \mathcal {F} _ {k - 1} \right] \right. \\ \leqslant 2 \sum_ {k = 1} ^ {\infty} E (| x _ {k} | ^ {p} | \mathcal {F} _ {k - 1}) <   \infty , \\ \end{array}
$$

所以根据已证的 i), 对鞅差 $\{y_k, \mathcal{F}_k\}$ , 其和 $\sum_{k=1}^{\infty} y_k$ 在 $A$ 上收敛. 也就是说

$$\left\{\sum_ {k = 1} ^ {\infty} E (| x _ {k} | ^ {p} | \mathcal {F} _ {k - 1}) < \infty \right\} \subset \left\{\sum_ {k = 1} ^ {\infty} (| x _ {k} | ^ {p} - E (| x _ {k} | ^ {p} | \mathcal {F} _ {k - 1})) \text {收敛} \right\},$$

而这个包含关系意味着

$$\left\{\sum_ {k = 1} ^ {\infty} E (| x _ {k} | ^ {p} | \mathcal {F} _ {k - 1}) < \infty \right\} \subset \left\{\sum_ {k = 1} ^ {\infty} | x _ {k} | ^ {p} < \infty \right\}.$$

也就是说，在 $A$ 上 $\sum_{k=1}^{\infty}|x_k|^p < \infty$ .

而对 $p \in (0,1)$ , 从 $\sum_{k=1}^{\infty} |x_k|^p < \infty$ 可知对充分大 $k$ , $|x_k| < 1$ . 所以 $|x_k|^p > |x_k|$ . 因此 $\sum_{k=1}^{\infty} |x_k| < \infty$ , 从而知 $\sum_{k=1}^{\infty} x_k$ 收敛. 所以在 $A$ 上 $\sum_{k=1}^{\infty} x_k$ 收敛.

推论 4.2.5 设 $\{x_{k}, F_{k}\}$ 为鞅差列，并对某个 $p \in (1, 2]$ ， $\sup_{k} E[|x_{k}|^{p} |F_{k-1}] < \infty$ a.s. 或 $\sup_{k} E|x_{k}|^{p} < \infty$ ，则对 q > 1

$$\sum_ {k = 1} ^ {\infty} \frac {x _ {k}}{k ^ {q / p}} \quad \text { a.s. } \quad \text { 收敛. }$$

证明 当 $\sup_k E|x_k|^p < \infty$ 时. 由于

$$E \left\{\sum_ {k = 1} ^ {\infty} E \left[ \left| \frac {x _ {k}}{k ^ {q / p}} \right| ^ {p} \mid \mathcal {F} _ {k - 1} \right] \right\} = \sum_ {k = 1} ^ {\infty} E \left| \frac {x _ {k}}{k ^ {q / p}} \right| ^ {p} < \infty ,$$

所以在两种条件下都有

$$\sum_ {k = 1} ^ {\infty} E \left[ \left| \frac {x _ {k}}{k ^ {q / p}} \right| ^ {p} \mid \mathcal {F} _ {k - 1} \right] < \infty \quad \text { a.s., }$$

对鞅差列 $\left(\frac{x_k}{k^q/p},\mathcal{F}_k\right)$ 用定理4.2.11便得推论.
