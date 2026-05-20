# 线性二次最优调节

无穷时间区间上的线性定常二次最优控制问题工程上简称为线性二次最优调节问题。从定理7.3.3知，线性二次最优调节问题涉及求解Riccati矩阵代数方程(7.3.29).式(7.3.30)中的最优控制综合函数 $u(x)$ 是状态反馈形式的控制函数，工程上称为最优调节器， $r \times n$ 矩阵 $K \stackrel{\mathrm{def}}{=} - R^{-1} B^{\mathrm{T}} P$ 称为系统的最优增益矩阵，相应的最优闭环系统为

$$\dot {x} = A x + B u (x). \tag {7.3.31}$$

注意，任一 $n \times n$ 半正定对称矩阵 $Q$ 总能分解成 $Q = CC^{\mathrm{T}}$ ，其中 $C$ 为 $n \times m$ 矩阵， $m \leqslant n$ . 虽然分解不唯一，但有如下引理：

引理7.3.3 对于 $Q$ 的两个不同分解 $Q = CC^{\mathrm{T}}$ 和 $Q = C_1C_1^{\mathrm{T}}, [A, C^{\mathrm{T}}]$ 与 $[A, C_1^{\mathrm{T}}]$ 的能观测性等价.

该引理的证明见文献 [2].

定理 7.3.4 设定常线性系统 (7.3.1) 完全能控，且对式 (7.3.19) 中常值阵 Q 有分解 $Q = CC^{T}$ ，使得 $[A, C^{T}]$ 完全能观测。那么 Riccati 矩阵微分方程 (7.3.29) 存在唯一正定对称解矩阵 $P^{*}$ 。

证明 引理7.3.2已给出方程(7.3.29)半正定对称解阵 $P^{*}$ 的存在性. 现证 $P^{*}$ 的正定性. 设不然, 有 $\xi \in \mathbb{R}^n$ , $\xi \neq 0$ , 使得

$$\xi^ {\mathrm{T}} P ^ {*} \xi = 0.$$

根据定理 7.3.3, 存在式 (7.3.1) 和方程 (7.3.19) 以 $\xi$ 为初态的最优解 $(u^{*}(t), x^{*}(t))$ , 其相应最优性能指标值为

$$\frac {1}{2} \xi^ {T} P ^ {*} \xi = \frac {1}{2} \int_ {0} ^ {+ \infty} \left[ x ^ {* T} (t) Q x ^ {*} (t) + u ^ {* T} (t) R u ^ {*} (t) \right] d t.$$

从而有

$$
\begin{array}{l} \int_ {0} ^ {+ \infty} x ^ {* T} (t) Q x ^ {*} (t) \mathrm{d} t = \int_ {0} ^ {+ \infty} x ^ {*} (t) ^ {T} C C ^ {T} x ^ {*} (t) \mathrm{d} t = 0, \tag {7.3.32} \\ \int_ {0} ^ {+ \infty} u ^ {* T} (t) R u ^ {*} (t) \mathrm{d} t = 0. \\ \end{array}
$$

由 $R > 0$ 和 $u^{*}(t)$ 在 $[0, +\infty)$ 上的分段连续性知 $u^{*}(t) = 0, \forall t \in [0, +\infty)$ . 于是 $x^{*}(t)$ 满足

$$\dot {x} ^ {*} (t) = A x ^ {*} (t), \quad x ^ {*} (0) = \xi ,$$

从而

$$x ^ {*} (t) = \mathrm{e} ^ {A t} \xi .$$

再由方程 (7.3.32) 第一式得到

$$
\begin{array}{l} C ^ {T} e ^ {A t} \xi \equiv 0, \\ C ^ {T} A \mathrm{e} ^ {A t} \xi \equiv 0. \\ C ^ {T} A ^ {n - 1} \mathrm{e} ^ {A t} \xi \equiv 0, \\ \end{array}
$$

•
•
•

由此可见

$$
\operatorname{rank} \left[ \begin{array}{c} C ^ {\mathrm{T}} \\ C ^ {\mathrm{T}} A \\ \vdots \\ C ^ {\mathrm{T}} A ^ {n - 1} \end{array} \right] <   n,
$$

这与 $(A, C^{\mathrm{T}})$ 完全能观测性矛盾。从而知 $P^{*} > 0$ 。现假设式 (7.3.29) 存在两个正定对称解阵 $P^{*}, P_{1}^{*}$ 。任取 $x_{0} \in \mathbb{R}^{n}$ ，根据定理 7.3.3，存在式 (7.3.1) 和式 (7.3.19) 以 $x_{0}$ 为初态的唯一最优解 $(u^{*}(t), x^{*}(t))$ ，其相应的最优性能指标值为
