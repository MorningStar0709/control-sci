$$
B _ {n} = \left[ \begin{array}{c c c c} (b _ {1}, \varphi_ {n 1}) & (b _ {2}, \varphi_ {n 1}) & \dots & (b _ {m}, \varphi_ {n 1}) \\ (b _ {1}, \varphi_ {n 2}) & (b _ {2}, \varphi_ {n 2}) & \dots & (b _ {m}, \varphi_ {n 2}) \\ \vdots & \vdots & & \vdots \\ (b _ {1}, \varphi_ {n r _ {n}}) & (b _ {2}, \varphi_ {n r _ {n}}) & \dots & (b _ {m}, \varphi_ {n r _ {n}}) \end{array} \right].
$$

为此我们先证明一个引理.

引理10.2.1 设两个复数列 $\{\lambda_n\}$ 和 $\{\alpha_n\}$ 满足

(1) $\lambda_{k} \neq \lambda_{l}, k \neq l$ ;   
(2) $\{\operatorname{Re} \lambda_k | k \geqslant 1\}$ 的任意非空子集有最大元;  
(3) $\sum_{k=1}^{\infty} |\alpha_k| < \infty$ .

那么

$$\sum_ {n = 1} ^ {\infty} \mathrm{e} ^ {\lambda_ {n} t} \alpha_ {n} = 0, \forall t \geqslant 0 \Longleftrightarrow \alpha_ {n} = 0, \forall n \geqslant 1.$$

证明 只需证明必要性. 用反证法, 假定

$$\sum_ {n = 1} ^ {\infty} \mathrm{e} ^ {\lambda_ {n} t} \alpha_ {n} = 0, \qquad \forall t \geqslant 0, \tag {10.2.19}$$

但 $J = \{k \mid \alpha_k \neq 0\}$ 是一非空集。容易看出 $J$ 不可能是有限集，因此 $J$ 是无限集，并且不妨设 $\alpha_k \neq 0, \forall k \geqslant 1$ 。记 $\mu_k = \operatorname{Re} \lambda_k, \nu_k = \operatorname{Im} \lambda_k$ 。于是根据假设 (2)，存在一标号 $k_0$ 使得

$$\mu_ {k _ {0}} = \max \left\{\mu_ {k} \mid k \geqslant 1 \right\}.$$

依据假设 (3), 存在一整数 $N > k_{0}$ 使得

$$\sum_ {k = N + 1} ^ {\infty} \left| \alpha_ {k} \right| < \left| \alpha_ {k _ {0}} \right| / 2. \tag {10.2.20}$$

从式 (10.2.19) 可得

$$
\alpha_{k_{0}} + \sum_{k = N + 1}^{\infty}\mathrm{e}^{\tilde{\lambda}_{k}t}\alpha_{k} + \sum_{\substack{1\leqslant k\leqslant N\\ k\neq k_{0}}}\mathrm{e}^{\tilde{\lambda}_{k}t}\alpha_{k} = 0,\qquad \forall t\geqslant 0,
$$

其中 $\widetilde{\lambda}_k = \lambda_k - \lambda_{k_0} \forall k \geqslant 1$ . 对上方程两边从 0 到 $t$ 积分并应用式 (10.2.20), 我们得到

$$
\left| \alpha_ {k _ {0}} \right| t \leqslant 2 \left| \int_ {0} ^ {t} \sum_ {\substack {1 \leqslant k \leqslant N \\ k \neq k _ {0}}} \mathrm{e} ^ {\bar {\lambda} _ {k} t} \alpha_ {k} \right|, \quad \forall t \geqslant 0. \tag{10.2.21}
$$

注意对于任意 $k \geqslant 1$ , 当 $\operatorname{Im} \tilde{\lambda}_k \neq 0$ 时 $\operatorname{Re} \tilde{\lambda}_k < 0$ 或 $\operatorname{Re} \tilde{\lambda}_k = 0$ , 故式 (10.2.21) 的右端对所有 $t \geqslant 0$ 有上确界. 于是从式 (10.2.21) 推出 $\alpha_{k_0} = 0$ , 矛盾. 证毕.

现在我们转到证明式 (10.2.18). 由于 $\{\varphi_{nk} \mid n \geqslant 1, 1 \leqslant k \leqslant r_n\}$ 是 $H$ 的一规范直交基，我们有
