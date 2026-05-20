\overline {{{A}}} _ {i i} = \left[ \begin{array}{c c c c c c} 0 & \dots & \dots & \dots & 0 & * \\ 1 & 0 & \ddots & & 0 & * \\ 0 & 1 & \ddots & \ddots & 0 & * \\ \vdots & \ddots & & \ddots & \vdots & \vdots \\ \vdots & & \ddots & 1 & 0 & * \\ 0 & \dots & \dots & 0 & 1 & * \end{array} \right] _ {r _ {i} \times r _ {i}}.

\overline {{{A}}} _ {i j} = \left[ \begin{array}{c c c c} 0 & \dots & 0 & * \\ \vdots & & \vdots & \vdots \\ 0 & \dots & 0 & * \end{array} \right] _ {r _ {i} \times r _ {j}}, \quad i \neq j,

\overline {{{B}}} _ {i i} = \left[ \begin{array}{c c c c c c c} 0 & \dots & 0 & 1 & 0 & \dots & 0 \\ 0 & \dots & 0 & 0 & 0 & \dots & 0 \\ \vdots & & \vdots & \vdots & \vdots & & \vdots \\ 0 & \dots & 0 & 0 & 0 & \dots & 0 \end{array} \right] _ {r _ {1} \times r}, \quad i = 1, 2, \dots , r,
$$

第 $i$ 列

其中 \* 代表数字.

定理 1.4.5 设定常线性系统 (1.4.16) 是完全能控的，则在坐标变换 $\bar{x} = T_{1}^{-1}x$ 下，系统 (1.4.16) 变成标准形式 (1.4.18). 这里 $T_{1}$ 由式 (1.4.17) 给出。通常称这种标准形为系统 (1.4.16) 的 Luenberger 第一能控标准形。

关于 Luenberger 标准形还有一种形式. 用 $q_{i}^{\mathrm{T}}(i = 1,2,\dots ,r)$ 表示由式 (1.4.17) 定义的非奇异矩阵 $\pmb{T}_{1}$ 的逆矩阵 $\pmb{T}_{1}^{-1}$ 的第 $r_1 + r_2 + \dots +r_i$ 行，并取 $\pmb{T}_{2}$ 为

$$\boldsymbol {T} _ {2} = \left[ q _ {1}, \boldsymbol {A} ^ {\mathrm{T}} q _ {1}, \dots , \left(\boldsymbol {A} ^ {r _ {1} - 1}\right) ^ {\mathrm{T}} q _ {1}, \dots , q _ {r}, \boldsymbol {A} ^ {\mathrm{T}} q _ {r}, \dots , \left(\boldsymbol {A} ^ {r _ {r} - 1}\right) ^ {\mathrm{T}} q _ {r} \right] ^ {\mathrm{T}}. \tag {1.4.19}$$

不难验证 $T_{2}$ 是非奇异的．实际上，如果有 $x_0$ 使得 $T_{2}x_{0} = 0$ ，则有

$$\boldsymbol {q} _ {i} ^ {\mathrm{T}} \boldsymbol {A} ^ {j} x _ {0} = 0, \quad j = 1, 2, \dots , r _ {i}, i = 1, 2, \dots , r. \tag {1.4.20}$$

显然， $x_{0}$ 属于 $[q_{1}, q_{2}, \cdots, q_{r}]$ 的零空间。由定义可知，这个零空间是由向量 $b_{1}$ 、 $Ab_{1}, \cdots, A^{r_{1}-2}b_{1}, \cdots, b_{r}, Ab_{r}, \cdots, A^{r_{r}-2}b_{r}$ 构成的，因此有

$$x _ {0} = \sum_ {i = 0} ^ {r _ {1} - 2} \alpha_ {1 i} A ^ {i} b _ {1} + \sum_ {i = 0} ^ {r _ {2} - 2} \alpha_ {2 i} A ^ {i} b _ {2} + \dots + \sum_ {i = 0} ^ {r _ {r} - 2} \alpha_ {r i} A ^ {i} b _ {r}, \tag {1.4.21}$$

其中 $\alpha_{ji}, j = 1, 2, \cdots, r$ 都是实数。在式 (1.4.21) 两边左乘 $q_{1}^{T}A$ ，由式 (1.4.20) 知

$$q _ {1} ^ {\mathrm{T}} \boldsymbol {A} x _ {0} = \sum_ {i = 0} ^ {r _ {1} - 2} \alpha_ {1 i} q _ {1} ^ {\mathrm{T}} \boldsymbol {A} ^ {i + 1} b _ {1} + \sum_ {i = 0} ^ {r _ {2} - 2} \alpha_ {2 i} q _ {1} ^ {\mathrm{T}} \boldsymbol {A} ^ {i + 1} b _ {2} + \dots + \sum_ {i = 0} ^ {r _ {r} - 2} \alpha_ {r i} q _ {1} ^ {\mathrm{T}} \boldsymbol {A} ^ {i + 1} b _ {r} = 0.$$
