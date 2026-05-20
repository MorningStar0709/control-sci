定义 11.8.2 令 $R \stackrel{\text{def}}{=} \min(r, s)$ , $S \stackrel{\text{def}}{=} \max(r, s)$ , $j \stackrel{\text{def}}{=} \max\left\{i \mid i \in [R, S], t(i) = \sum_{k=R}^{S} t(k)\right\}$ , $\hat{t}(1) \stackrel{\text{def}}{=} \tilde{t}(1) \stackrel{\text{def}}{=} t(j)$ . 当 $r \leqslant s$ 时，令 $j_1 = j_1' = 0$ ; 当 $r > s$ 时，令 $j_1 = j_1' = r - s - 1$ . 若 $j_{u-1} < j < j_u$ 时，有 $t(r-j) \leqslant \hat{t}(u-1)$ , 但 $t(r-j_u) > \hat{t}(u-1)$ , 则对 $u > 1$ 定义 $\hat{t}(u) \stackrel{\text{def}}{=} t(r-j_u)$ , 直到 $t(r-j) = t(1)$ . 共定义出 $\hat{t}(1), \hat{t}(2), \cdots, \hat{t}(P)$ . 若 $j_{v-1}' < j < j_v'$ 时，有 $t(s+j) \leqslant \tilde{t}(v-1)$ , 但 $t(s+j_v') > \tilde{t}(v-1)$ , 则对 $v > 1$ 定义 $\tilde{t}(v) \stackrel{\text{def}}{=} t(s+j_v')$ , 直到 $t(s+j) = t(m)$ , 共定义出 $\tilde{t}(1), \tilde{t}(2), \cdots, \tilde{Q}$ . $\hat{t}(u), \tilde{t}(v)$ 也可简记为 $\hat{t}(u), \tilde{t}_v$ .

定理11.8.6 在上述记号和定义下，可得 $(A^M)^{\mathrm{T}}$ 元素的公式为

$$
a _ {r, s} (M) = \left\{ \begin{array}{l l} - \infty , & \text {当} v > s, M <   r - s; \\ \sum_ {u = 1} ^ {P} t \left(r - j _ {u}, s\right) \hat {t} (u) ^ {M - 1 - j _ {u}} \oplus \sum_ {v = 2} ^ {Q} t \left(r, s + j _ {v} ^ {\prime}\right) \tilde {t} (v) ^ {M - 1 - j _ {v} ^ {\prime}}, \end{array} \right. \tag {11.8.7}
$$

否则进一步，串行生产线批量生产的状态方程可用 $D$ 中运算列出，即

$$\left[ x _ {1} (k + 1), \dots , x _ {m} (k + 1) \right] ^ {\mathrm{T}} = A _ {N} \left[ x _ {1} (k), \dots , x _ {m} (k) \right] ^ {\mathrm{T}}, A _ {N} \stackrel {\text { def }} {=} A ^ {M} B, \tag {11.8.8}$$

其中 $x_{j}(k)$ 表示第 $k$ 批最后一个工件离开第 $j$ 台机器的时间。批生产周期为

$$\lambda = \sum_ {s = 1} ^ {m} a _ {s}, \tag {11.8.9}$$

这里 $a_{s}$ 为 $\pmb{A}_N$ 对角线上的元素，而求和 $\sum$ 为极大代数的加法求和.

证明 $\pmb{A}$ 阵的定义式表示，图 $G(A^{\mathrm{T}})$ 中有 $m$ 个点， $r \leqslant s$ 时 $r$ 到 $s$ 弧重为 $t(r, s), r = s + 1$ 时 $r$ 到 $s$ 的弧重为 $0, r > s + 1$ 时 $r$ 到 $s$ 没有弧。 $a_{r,s}(M)$ 表示 $G(A^{\mathrm{T}})$ 中 $r$ 到 $s$ 的长为 $M$ 的最重路的权重，下面就研究这种路。
