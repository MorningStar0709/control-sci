$$p _ {i r} y _ {r} ^ {- 1} \leqslant x _ {i} ^ {- 1} = a _ {i} y _ {j (i)} ^ {- 1}, \quad i = 1, \dots , n; r = 1, \dots , n N.$$

由于上式 $a_{i}y_{j(i)}^{-1}$ 为 $\tilde{B}$ 阵的行最大元，而 $p_{sj(i)}y_{j(i)}^{-1} = -\infty, \forall s \neq i$ 。因此 $\tilde{B}$ 满足引理 11.5.5 条件，方程 (11.5.7) 解唯一。

必要性. 把满足引理 11.5.5 条件的列 (即第 $i$ 行最大元为该列唯一最大元) 简称为 $j(i)$ 列. 由于 $p_{ir}x_i \leqslant y_r, p_{ir}y_r^{-1} \leqslant x_i^{-1}, \forall r$ , 因此

$$p _ {i r} y _ {r} ^ {- 1} = x _ {i} ^ {- 1} \tag {11.5.8}$$

是 $p_{ir}y_r^{-1}$ 为 $\tilde{B}$ 阵第 $i$ 行最大元的充分条件。现先证 $P_N$ 中必存在一列为 $e_1$ 。由于系统完全能观测，所以 $P_N$ 第一行必为非空行。记 $\neq -\infty$ 的所有第一行元素所在的列序号组成的集合为 $R_1$ 。下面来证明：必有非空集 $R_{m+1}$ 存在，使得对任意 $r \in R_{m+1}$ ，必有

$$p _ {1 r} \neq - \infty , \quad p _ {i r} = - \infty , \quad 1 < i \leqslant m + 1.$$

反设 $R_{m + 1} = \phi$ 但 $R_{m}\stackrel {\mathrm{def}}{=}\{r\mid p_{1r}\neq -\infty ,p_{ir} = -\infty ,1 <   i\leqslant m)\neq \phi .$ 于是有

$$p _ {m + 1, r} \neq - \infty , \quad \forall r \in R _ {m}.$$

对任意 $r \in R_1 / R_m$ ，由 $R_m$ 的定义易知必存在一个 $i(r)(1 < i(r) \leqslant m)$ ，使得 $p_{i(r),r} \neq -\infty$ 。取定一个 $i$ ，记 $\widehat{R}_i = \{r \mid i(r) = i\}$ 。显然， $R_1 \setminus R_m = \bigcup_{i=2}^m \widehat{R}_i$ 。取

$$x _ {1} = 0, \quad x _ {i} = d _ {i 1}, \quad (i \in i (r), r \in R _ {1} \backslash R _ {m}; i = m + 1) \text {其他} x _ {i} \text {足够小}, \tag {11.5.9}$$

其中有限数 $d_{i1}$ 为

$$d _ {i 1} = \max _ {r \in \hat {R} _ {i}} p _ {1 r} p _ {i r} ^ {- 1}; \quad d _ {m + 1, 1} = \max _ {r \in R _ {m}} p _ {1 r} p _ {m + 1, r} ^ {- 1}. \tag {11.5.10}$$

设 $r \in R_1 \backslash R_m$ ，对 $P_N$ 中取定的一个第 $r$ 列，必有 $r \in \widehat{R}_{i(r)}$ 。由式 (11.5.9)，(11.5.10) 得 $p_{1r} p_{i(r),r}^{-1} \leqslant x_{i(r)} x_1^{-1}$ ，于是

$$p _ {1 r} x _ {1} \leqslant p _ {i (r), r} x _ {i (r)}. \tag {11.5.11}$$

当

$$p _ {1 r} x _ {1} = \sum_ {i = 1} ^ {m + 1} \tilde {\Xi} p _ {i r} x _ {i} \tag {11.5.12}$$

时，由式(11.5.9)得 $p_{1r}x_1 = y_r$ ；上式中 $\sum_{\oplus}$ 表示按 $D$ 中 $\oplus$ 法求和。由式(11.5.8)知 $p_{1r}y_r^{-1}$ 为行最大元；但这时由式(11.5.11)，(11.5.12)得 $p_{i(r),r}x_{i(r)} = y_r, p_{i(r),r}y_r^{-1}$ 也为行最大元，所以，第 $r$ 列不是 $j(1)$ 列。当式(11.5.12)不成立时，必有 $1 < i_0 \leqslant m + 1$ 存在，使得

$$p _ {1 r} x _ {1} < p _ {i _ {0} r} x _ {i _ {0}} = \sum_ {i = 1} ^ {m + 1} \oplus p _ {i r} x _ {i} = y _ {r}$$
