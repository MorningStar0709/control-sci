这里 $A \in M_{n \times n^{2m}}$ . $a_{d_i}^i$ 是对应长方形阵 $A$ 中的第 $i$ 对角元素. 确切地说, $A$ 中的 $(i, (i-1)n^{2m-1} + 1)$ 元是 $a_{d_i}^i$ 与 $\frac{\partial V}{\partial x_i}$ 中的 $x_i$ 的最高次项乘积. 于是在 $\dot{V}$ 中, $x_i$ 的最高阶项是由 $g_i$ 的对角元素生成的.

定理 8.6.6(整体行对角占优原理) 如果存在一个整数 m 满足 $2m > \max\{k_{1}, \cdots, k_{n}\}$ ，使得

$$
\begin{array}{l} - a _ {d _ {i}} ^ {i} > \sum_ {| S | = k _ {i}, S \neq d _ {i}} \left| a _ {S} ^ {i} \right| \left(\frac {s _ {i} + 2 m - k _ {i}}{2 m}\right) \\ + \sum_ {j = 1, j \neq i} ^ {n} \sum_ {| S | = k _ {j}} \left| a _ {S} ^ {j} \right| \left(\frac {s _ {i}}{2 m}\right), \quad i = 1, \dots , n, \tag {8.6.23} \\ \end{array}
$$

这里 $s=(s_{1},\cdots,s_{n})\in\mathbb{Z}_{+}^{n}$ ，则以上定义的向量场 g 在原点是渐近稳定的.

证明 选择一个LFHD

$$V = \sum_ {i = 1} ^ {n} \left(\frac {1}{2 m - k _ {i} + 1}\right) x _ {i} ^ {2 m - k _ {i} + 1},$$

则有

$$\dot {V} | _ {g} = \sum_ {i = 1} ^ {n} \sum_ {| S | = k _ {i}} a _ {S} ^ {i} x ^ {S} x _ {i} ^ {2 m - k _ {i}}. \tag {8.6.24}$$

这是一个阶数为 $2m$ 的齐次多项式。现用不等式 (8.6.20) 将式 (8.6.22) 中的每一项分开，由式 (8.6.22) 可得

$$\dot {V} | _ {g} < - \sum_ {i = 1} ^ {n} \varepsilon_ {i} x _ {i} ^ {2 m}, \qquad \text {对某个} \varepsilon_ {i} > 0,$$

由此结论显见.

一个显然可以改进的地方是非对角且负半定的项可以由上述估计中除去。对每个 $g_{i}$ 我们可以定义一组特殊的项集如下：

$$Q _ {i} = \{| S | = k _ {i} \mid s _ {j} (j \neq i) \text {偶数，且} a _ {S} ^ {i} < 0 \}.$$

显见 $Q_{i}$ 中的项在 $\frac{\partial V}{\partial x_i} g_i$ 中为负半定的．将式(8.6.23）中的这种项排除，则得

$$
\begin{array}{l} - a _ {d _ {i}} ^ {i} > \sum_ {| S | = k _ {i}, S \notin Q _ {i}} \left| a _ {S} ^ {i} \right| \left(\frac {s _ {i} + 2 m - k _ {i}}{2 m}\right) \\ + \sum_ {j = 1, j \neq i} ^ {n} \sum_ {| S | = k _ {j}, S \notin Q _ {j}} \left| a _ {S} ^ {j} \right| \left(\frac {s _ {i}}{2 m}\right), \quad i = 1, \dots , n. \tag {8.6.25} \\ \end{array}
$$

下面讨论中，我们将这个式 (8.6.25) 称为整体行对角原理 (CRDDP). 下面介绍一个比较简单的形式，它可对各项分行处理.

推论8.6.1(对角占优原理 (DDP)) 给定一多项式向量场，形同定理8.6.6中的 $g$ 。如果

$$- a _ {d _ {i}} ^ {i} > \sum_ {| S | = k _ {i}, S \notin Q _ {i}} \left| a _ {S} ^ {i} \right|, \quad i = 1, \dots , n, \tag {8.6.26}$$

则它在原点渐近稳定.

证明 由于在不等式 (8.6.23) 中， $m$ 可以任意大，令 $m \to \infty$ ，不等式 (8.6.23) 的右边变为不等式 (8.6.26) 的右边。因此，严格不等式 (8.6.26) 表示不等式 (8.6.23) 对足够大的 $m$ 成立。

利用不等式 (8.6.21)，我们可以将 $\deg = 4k$ 的多项式放大为一个关于变量 $x_{i}^{2k}, i = 1, \dots, n$ 的一个二次型.

下面提出一种算法，称为导出二次型算法 (QFRA):

设 $g=(g_{1},\cdots,g_{n})^{\mathrm{T}}$ , $\deg(g_{i})=k_{i}$ ，这里 $k_{i}$ 为奇数， $i=1,\cdots,n$ .

第一步．选择一个最小偶数 $m = 2k$ 使得

$$2 m > \max \{k _ {1}, \dots , k _ {n} \}.$$

构造一个 $2m$ 次齐次多项式 $q(x)$ 如下：

$$q (x) = \sum_ {i = 1} ^ {n} x _ {i} ^ {2 m - k _ {i}} g _ {i}.$$
