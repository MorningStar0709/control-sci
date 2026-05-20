$$\frac {\partial^ {| S |} F (x)}{\partial x ^ {S}} = \frac {\partial^ {| S |} F (x)}{\partial x _ {1} ^ {s _ {1}} \partial x _ {2} ^ {s _ {2}} \cdots \partial x _ {n} ^ {s _ {n}}}.$$

我们定义若干必要的概念.

定义 8.6.2 (1) 设 $k_{i}$ 为 $f_{i}(x)$ ， $i=1,\cdots,n$ 的 Taylor 展式中最低阶次非零项。由系统 (8.6.15) 的最低阶次（即 $k_{i}$ ）项构成的系统称为系统 (8.6.15) 的最低阶近似系统，它可以形式地表示为

$$\dot {x} _ {i} = g _ {i} (x) := \sum_ {| S | = k _ {i}} \frac {1}{S !} \frac {\partial^ {| S |} f _ {i} (x)}{\partial x ^ {S}} (0) x ^ {S}, \qquad i = 1, \dots , n; \tag {8.6.16}$$

(2) 系统 (8.6.16) 称为系统 (8.6.15) 的奇次近似，如果所有的 $k_{i}$ 均为奇数；

(3) 系统 (8.6.15) 称为近似稳定的，如果系统

$$\dot {x} _ {i} = f _ {i} (x) + O \left(\| x \| ^ {k _ {i} + 1}\right), \quad i = 1, \dots , n$$

在原点局部渐近稳定.

注 8.6.1 (1) 在 (8.6.16) 中， $g_{i}$ 是一个 $k_{i}$ 阶齐次多项式，故 $g = [g_{1}, \cdots, g_{n}]^{T}$ 是分量齐次向量场；

(2) 当 $k_{1} = \cdots = k_{n} := k$ , 上述近似稳定性与经典近似稳定性一致. 推广的近似稳定性与坐标有关. 显然, 近似稳定系统必渐近稳定, 反之, 则未必成立.

定义 8.6.3 给定一分量齐次向量场 $g = [g_{1}, \cdots, g_{n}]^{T}$ ，一个正定多项式 V > 0 称为 g 的齐次导数 Lyapunov 函数 (LFHD)，如果它的 Lie 导数 $L_{g}V$ 是齐次的，即

$$\deg (L _ {g} V) = \deg \left(\frac {\partial V}{\partial x _ {i}}\right) + \deg (g _ {i}), \quad \forall i = 1, \dots , n.$$

以下两个例子是两个典型的 LFHD, 以后我们将用到它们.

例 8.6.2 设 $g = [g_{1}, \cdots, g_{n}]^{T}$ 是具有奇数次分量齐次向量场， $\deg(g_{i}) = k_{i}$ ， $i = 1, \cdots, n$ ，且设 m 为一个给定的整数，满足

$$2 m \geqslant \max \{k _ {1}, \dots , k _ {n} \} + 1.$$

(1) 设 $2m_{i} = 2m - k_{i} + 1, i = 1, \cdots, n, p_{i} > 0, i = 1, \cdots, n,$ 则

$$V = \sum_ {i = 1} ^ {n} p _ {i} x _ {i} ^ {2 m _ {i}} \tag {8.6.17}$$

是 g 的 LFHD;

(2) 设 $k_{1} = \cdots = k_{n_{1}} := k^{1}; k_{n_{1} + 1} = \cdots = k_{n_{1} + n_{2}} := k^{2}; \cdots, k_{n_{1} + \cdots + n_{r - 1} + 1} = \cdots = k_{n_{1} + \cdots + n_{r}} := k^{r}$ , 这里 $k^{i}$ 是奇数, 且 $\sum_{i=1}^{r} n_{i} = n$ . 令 $x = (x^{1}, \cdots, x^{r})$ , 这里 $\dim(x^{i}) = n_{i}$ 且设 $2m^{i} = 2m - k^{i} + 1, i = 1, \cdots, r$ . 如果 $P_{i}, i = 1, \cdots, r$ , 是维数为 $n_{i} \times n_{i}$ 的正定矩阵, 则

$$V = \sum_ {i = 1} ^ {r} \left[ (x _ {1} ^ {i}) ^ {m ^ {i}}, \dots , (x _ {n _ {i}} ^ {i}) ^ {m ^ {i}} \right] P _ {i} \left[ (x _ {1} ^ {i}) ^ {m ^ {i}}, \dots , (x _ {n _ {i}} ^ {i}) ^ {m ^ {i}} \right] ^ {\mathrm{T}} \tag {8.6.18}$$

是 g 的一个 LFHD.

注意，在式(8.6.16)或式(8.6.17)中， $V$ 对 $\pmb{g}$ 的导数是阶数为 $2m$ 的齐次多项式.

下面命题是 LFHD 的基本性质.

命题8.6.1 如果存在式(8.6.15)的近似系统(8.6.16)的一个LFHD,使得其沿着系统(8.6.16)的导数是负定的,则系统(8.6.15)在原点是渐近稳定的.

证明 设 $L_{g}V$ 是负定的，则它应该是偶数阶的，即 $\deg (L_gV) = 2m$ 。我们首先证明存在一个实数 $b > 0$ 使得

$$L _ {g} V (x) \leqslant - b \sum_ {i = 1} ^ {n} (x _ {i}) ^ {2 m}. \tag {8.6.19}$$

由于 $L_{g}V$ 是负定的，在一紧“球”
