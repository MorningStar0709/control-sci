$$\bigcap_ {k = 1} ^ {\infty} \bigcup_ {j = k} ^ {\infty} B _ {j} = \left\{\sum_ {k = 1} ^ {\infty} P (B _ {k} | \mathcal {F} _ {k - 1}) = \infty \right\}. \tag {4.2.7}$$

证明 记

$$\xi_ {n} = \sum_ {k = 1} ^ {n} (I _ {B _ {k}} - E (I _ {B _ {k}} | \mathcal {F} _ {k - 1})). \tag {4.2.8}$$

显然 $(I_{B_k} - E(I_{B_k}|\mathcal{F}_{k - 1}),\mathcal{F}_k)$ 是鞅差列，而 $(\xi_n,\mathcal{F}_n)$ 是鞅.

注意到

$$\left| I _ {B _ {k}} - E \left(I _ {B _ {k}} \mid \mathcal {F} _ {k - 1}\right) \right| \leqslant 1,$$

用定理4.2.7知 $\xi_{n}$ 在

$$\{\sup _ {k} \xi_ {k} < \infty \} \bigcup \{\inf _ {k} \xi_ {k} > - \infty \} \tag {4.2.9}$$

上 a.s. 收敛.

设 $\sum_{k=1}^{\infty} I_{B_k} < \infty$ , 那么从式 (4.2.8) 知 $\sup_n \xi_n < \infty$ , 所以 $\xi_n$ 收敛. 由此从式 (4.2.8) 看出 $\sum_{k=1}^{\infty} P(B_k | \mathcal{F}_{k-1}) < \infty$ .

现设 $\sum_{k=1}^{\infty} P(B_k | \mathcal{F}_{k-1}) < \infty$ , 那么从式 (4.2.8) 知 $\inf_n \xi_n > -\infty$ . 据式 (4.2.9). 在 $\{\inf_k \xi_k > -\infty\}$ 上 $\xi_n$ a.s. 收敛. 又从式 (4.2.8) 知 $\sum_{k=1}^{\infty} I_{B_k} < \infty$ . 这样就证明了充分必要条件.

注意到

$$\left\{\sum_ {k = 1} ^ {\infty} I _ {B _ {k}} < \infty \right\} \quad \text {和} \quad \bigcup_ {k = 1} ^ {\infty} \bigcap_ {j = k} ^ {\infty} B _ {j} ^ {c}$$

不过是 $\{\omega$ 属于有穷个 $B_{k}\}$ 这个集合的不同写法，所以

$$\bigcup_ {k = 1} ^ {\infty} \bigcap_ {j = k} ^ {\infty} B _ {j} ^ {c} = \left\{\sum_ {k = 1} ^ {\infty} I _ {B _ {k}} < \infty \right\}.$$

据刚证明的充要条件，便知

$$\bigcup_ {k = 1} ^ {\infty} \bigcap_ {j = k} ^ {\infty} B _ {j} ^ {c} = \left\{\sum_ {k = 1} ^ {\infty} P (B _ {k} | \mathcal {F} _ {k - 1}) < \infty \right\}.$$

对上式左右端取补集，便得式(4.2.7).

定理 4.2.9 (Borel-Cantelli 引理) 设 $\{B_{k}\}$ 是事件列. i) 若 $\sum_{k=1}^{\infty} P(B_{k}) < \infty$ ，则 $B_{k}$ 无穷次出现的概率为 0，即 $P\left(\bigcap_{k=1}^{\infty} \bigcup_{j=k}^{\infty} B_{j}\right) = 0;$ ii) 若 $\{B_{k}\}$ 相互独立，则 $\sum_{k=1}^{\infty} P(B_{k}) < \infty$ 的充分必要条件是 $P\left(\bigcap_{k=1}^{\infty} \bigcup_{j=k}^{\infty} B_{j}\right) = 0.$

证明 用 $F_{n}$ 表示 $\{B_{1},\cdots,B_{n}\}$ 生成的 $\sigma$ -代数.

i) $\infty > \sum_{k=1}^{\infty} P(B_k) = E\left(\sum_{k=1}^{\infty} E(I_{B_k} | \mathcal{F}_{k-1})\right)$ , 也就是 $\sum_{k=1}^{\infty} E(I_{B_k} | \mathcal{F}_{k-1}) < \infty$ a.s. 用定理 4.3.3 知 $\sum_{k=1}^{\infty} I_{B_k} < \infty$ a.s. 所以 $P\left(\bigcup_{k=1}^{\infty} \bigcap_{j=k}^{c} B_j^c\right) = 1$ , 或 $P\left(\bigcap_{k=1}^{\infty} \bigcup_{j=k}^{c} B_j\right) = 0$ ;

ii) 只需证明当 $\{B_k\}$ 相互独立时，从 $P\left(\bigcap_{k=1}^{\infty} \bigcup_{j=k}^{n} B_j\right) = 0$ 可推出 $\sum_{k=1}^{\infty} P(B_k) <$

$\infty$ .反设 $\sum_{k = 1}^{\infty}PB_k = \infty$

从独立性知 $\sum_{k=1}^{\infty} P(B_k | \mathcal{F}_{k-1}) = \sum_{k=1}^{\infty} PB_k$ . 所以

$$\sum_ {k = 1} ^ {\infty} P (B _ {k} | \mathcal {F} _ {k - 1}) = \infty \quad \text { a.s. }$$

从式 (4.2.7) 知

$$P \left(\bigcap_ {k = 1} ^ {\infty} \bigcup_ {j = k} ^ {\infty} B _ {j}\right) = 1.$$

这和定理条件矛盾，所以必须有 $\sum_{k=1}^{\infty} P(B_k) < \infty$ .
