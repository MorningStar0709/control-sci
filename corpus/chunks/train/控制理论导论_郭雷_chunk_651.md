$$S = \left\{z \mid \sum_ {i = 1} ^ {n} (z _ {i}) ^ {2 m} = 1 \right\}$$

上， $L_{g}V(x)$ 有最大值 $-b < 0$ 即

$$L _ {g} V (z) \leqslant - b < 0, \quad z \in S.$$

注意任意 $x \in \mathbb{R}^n$ 能表示为 $x = kz$ , 其中 $z \in S$ , 因此

$$L _ {g} V (x) = L _ {g} V (k z) = k ^ {2 m} L _ {g} V (z) \leqslant - b k ^ {2 m} = - b \sum_ {i = 1} ^ {n} (x _ {i}) ^ {2 m}.$$

利用方程 (8.6.18), LFHD 的导数满足

$$\dot {V} | _ {f} = \dot {V} | _ {g + O (\| x \| ^ {K + 1})} \leqslant - b \sum_ {i = 1} ^ {n} (x _ {i}) ^ {2 m} + O (\| x \| ^ {2 m + 1}), \tag {8.6.20}$$

这里 $g + O(\| x\|^{K + 1})$ 表示

$$g (x) = \left[ g _ {1} (x) + O (\| x \| ^ {k _ {1} + 1}), \dots , g _ {n} (x) + O (\| x \| ^ {k _ {n} + 1}) \right] ^ {\mathrm{T}}.$$

对于齐次向量场，文献 [19] 给出以下结果 (这里用我们的术语表述):

定理 8.6.5 设系统 (8.6.15) 有 $k_{1} = \cdots = k_{n} = k$ 且其近似系统 (8.6.16) 是渐近稳定的，则系统 (8.6.15) 是渐近稳定的.

命题 8.6.1 和定理 8.6.5 是我们检验近似稳定的主要工具.

下面我们给出一些充分条件，用以保证具有奇次近似系统的动力系统的近似稳定性。下面的不等式在以后的讨论中是基本的。

引理 8.6.2 设 $s = [s_{1}, \cdots, s_{n}] \in Z_{+}^{n}$ 及 $x \in R^{n}$ ，则下列不等式成立：

$$\left| x ^ {s} \right| \leqslant \sum_ {j = 1} ^ {n} \frac {s _ {j}}{| s |} \left| x _ {j} \right| ^ {| s |}. \tag {8.6.21}$$

证明 设 $z = [z_1, \dots, z_n] \in \mathbb{R}_+^n$ ，由于 $\ln(\xi)$ 是一凸函数 (下凸)，故有

$$\sum_ {i = 1} ^ {n} \left(\frac {s _ {i}}{\sum_ {k = 1} ^ {n} s _ {k}} \ln (z _ {i})\right) \leqslant \ln \left(\sum_ {i = 1} ^ {n} \frac {s _ {i}}{\sum_ {k = 1} ^ {n} s _ {k}} z _ {i}\right).$$

若令 $s = \sum_{k=1}^{n} s_k$ ，则上式等价于

$$\ln \prod_ {i = 1} ^ {n} z _ {i} ^ {\left(\frac {s _ {i}}{s}\right)} \leqslant \ln \left(\sum_ {i = 1} ^ {n} \frac {s _ {i}}{s} z _ {i}\right),$$

或

$$\prod_ {i = 1} ^ {n} z _ {i} ^ {\left(\frac {s _ {1}}{s}\right)} \leqslant \sum_ {i = 1} ^ {n} \frac {s _ {i}}{s} z _ {i}.$$

上式中用 $|x_{i}|$ 代替 $z_{i}^{(\frac{1}{s})}$ ，则得不等式 (8.6.20).

给定一个分量齐次向量场

$$g = \operatorname{col} (g _ {1}, \dots , g _ {n})$$

这里 $\mathrm{rank}(g_{i}) = k_{i}, i = 1, \cdots, n.$ 将 $g_{i}$ 表示成

$$g _ {i} (x) = a _ {d _ {i}} ^ {i} x _ {i} ^ {k _ {i}} + \sum_ {S \neq d _ {i}} a _ {S} ^ {i} x ^ {S}, \quad i = 1, \dots , n, \tag {8.6.22}$$

这里 $d_{i}=k_{i}\delta_{i}=(0,\cdots,k_{i},\cdots,0)$ ，它对应 g 的对角项.

“对角项”在LFHD的讨论中极为重要。我们给出如下解释：设 $V$ 是对以下分量齐次向量场 $\pmb{g}$ 的一个LFHD:

$$\dot {x} = g (x),$$

则有

$$
\left[ \begin{array}{c} \frac {\partial V}{\partial x _ {1}} g _ {1} \\ \vdots \\ \frac {\partial \dot {V}}{\partial x _ {n}} g _ {n} \end{array} \right] = A x ^ {2 m},
$$
