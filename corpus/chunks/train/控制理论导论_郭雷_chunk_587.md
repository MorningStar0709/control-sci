这里 $X_{i}\in F$ 及 $t\in \mathbb{R}^m$ .根据Chow定理

$$R ^ {*} (x _ {0}) = \mathcal {I} (F, x _ {0}).$$

因为积分子流形 $\mathcal{I}(F, x_0)$ 在 $x_0$ 的一个邻域秩为 $n$ , 故 $R^*(x_0)$ 包括一个非空内点集.

下面对一个自然数 $N$ ，定义

$$R _ {i} ^ {*} (x _ {0}, N) := \bigcup_ {| t | \leqslant N} \varphi_ {i} (t, x _ {0}), \tag {8.1.9}$$

这里

$$\| t \| = \sum_ {i = 1} ^ {m} | t _ {i} |.$$

由于

$$J := \{t \in \mathbb {R} ^ {m} | \| t \| \leqslant N \} \subset \mathbb {R} ^ {m}$$

是一个紧集， $R_{i}^{*}(x_{0},N)$ 是 $J$ 在连续映射 $\varphi_{i}(t,x_{0})$ 下的像，故为紧集.

由定义可知

$$R ^ {*} (x _ {0}) = \bigcup_ {i, N} R _ {i} ^ {*} (x _ {0}, N). \tag {8.1.10}$$

现在由于 $F$ 是有限集，故它的有限选择 $i$ 是可数的（为 $k^i, i = 0,1,2,\dots$ ）。因此式(8.1.9)右式是一个可数并集，而其左式因含一个非空开集，是第二纲的。根据Baire纲定理，至少有一个 $R_i^*(x_0,N)$ 不是无处稠的。譬如说 $R_i^*(x_0,N)$ 不是无处稠的，即它的闭包 $\overline{R_i^*(x_0,N)}$ 包含一个非空开集。但因为 $R_i^*(x_0,N)$ 是紧的，故 $R_i^*(x_0,N) = \overline{R_i^*(x_0,N)}$ 包含一个非空开集。对于这个特殊的 $i$ 我们有 $X_{i_1},\ldots ,X_{i_m}\in F$ 。定义映射 $P:\mathbb{R}^m\to M$ 为

$$P (t _ {1}, \dots , t _ {m}) = \phi_ {t _ {1}} ^ {X _ {i _ {1}}} \phi_ {t _ {2}} ^ {X _ {i _ {2}}} \dots \phi_ {t _ {m}} ^ {X _ {i _ {m}}} (x _ {0}).$$

那么

$$R _ {i} ^ {*} (x _ {0}, N) \subset P (\mathbb {R} ^ {m}). \tag {8.1.11}$$

由于上式左边包含一个非空开集，故利用Sard定理，至少存在一个点 $t_0$ ，使 $P$ 的Jacobi矩阵 $J_{P}$ 满秩，即 $\operatorname{rank}(J_P(t_0)) = n$ .由解析性可知

$$S := \{t \in R ^ {m} \mid \operatorname{rank} (J _ {P} (t)) < n \} \subset \mathbb {R} ^ {m}$$

没有内点，否则 $\operatorname{rank}(J_P(t)) < n$ ， $\forall t$ 。于是它的余集

$$S ^ {c} = \mathbb {R} ^ {m} \backslash S = \{t \in \mathbb {R} ^ {m} | \operatorname{rank} (J _ {P} (t)) = n \}$$

是一个开稠集.

现在令 $T > 0$ 且设点 $\pmb{y}$ 为

$$y \in \bigcup_ {0 \leqslant t \leqslant T} R (x _ {0}, t). \tag {8.1.12}$$

我们将证明 $y$ 属于 $\bigcup_{0\leqslant t\leqslant T}R(x_0,t)$ 内点的闭包，即

$$y \in \overline {{\operatorname{Int} \left(\bigcup_ {0 \leqslant t \leqslant T} R (x _ {0} , t)\right)}}.$$

利用式 (8.1.11), 我们有

$$y \in \overline {{\bigcup_ {0 \leqslant t < T} R (x _ {0} , t)}}.$$

不失一般性，设存在 $t_0 \in [0, T)$ ，使得

$$y \in R (x _ {0}, t _ {0}).$$

这是因为，如不然则可选一序列 $y_{k} \to y$ ，且 $y_{k} \in R(x_{0}, t_{0})$ 。只要能证明 $y_{k}$ 对所有的 $k$ 均属于内点集的闭包，则 $y$ 也属于内点集的闭包。

根据定义存在 $X_{j_1}, \cdots, X_{j_r} \in F$ 及 $s = (s_1, \cdots, s_r) \in \mathbb{R}_+^r$ , 且 $\|s\| = t_0$ , 使得

$$y = \varphi_ {j} (s, x _ {0}).$$

其次，我们定义一个集合 $U$ 为

$$U = S ^ {c} \cap \{t \mid \| t \| < T - t _ {0} \} \cap \{t \in R _ {+} ^ {m} \},$$

它显然是 $\mathbb{R}^m$ 中的一个开集，且 $0 \in \bar{U}$ . 因为 $P$ 在 $U$ 上的秩为 $n$ , 故根据秩定理， $P(U)$ 为 $M$ 的一个开集. 令
