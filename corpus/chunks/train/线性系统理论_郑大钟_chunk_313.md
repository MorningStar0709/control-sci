先证明(1)→(2): 采用反证法, 反设 $F(s)$ 不是列既约的, 则意味着必可通过初等列运算, 由 $F(s)$ 找到一个列既约的多项式矩阵 $\tilde{F}(s)$ :

$$
\left\{ \begin{array}{c} \tilde {F} (s) = \left[ \tilde {f} _ {1} (s), \tilde {f} _ {2} (s), \dots , \tilde {f} _ {\alpha} (s) \right] \\ \tilde {\mu} _ {1} \leqslant \tilde {\mu} _ {2} \leqslant \dots \leqslant \tilde {\mu} _ {\alpha} \end{array} \right. \tag {8.88}
$$

其中，至少有一个列(如列 $j$ )使 $\tilde{\mu}_j < \mu_j$ 。于是，由此就有

$$\sum_ {i = 1} ^ {a} \mu_ {i} > \sum_ {i = 1} ^ {a} \tilde {\mu} _ {i} \tag {8.89}$$

这表明 $\{f_{1}(s), f_{2}(s), \cdots, f_{a}(s)\}$ 不是最小多项式基，而这是和已知说法(1)相矛盾的。反设不成立，故知 $F(s)$ 必为列既约。再反设 $F(s)$ 是可简约的，则意味着其列只少对 s 的一个值（例如 s = a）为列相关。所以，一定存在一组不全为零的常数 $\{c_{i}\}$ ，使成立

$$\sum_ {i = 1} ^ {a} c _ {i} f _ {i} (a) = 0 \tag {8.90}$$

而且，显然下述定义的向量

$$\bar {F} (s) = \sum_ {i = 1} ^ {a} \frac {c _ {i} f _ {i} (s)}{(s - a)} \tag {8.91}$$

也是多项式向量。现假设，在对应于 $c_{i} \neq 0$ 的那些 $\pmb{f}_{i}(s)$ 中， $\pmb{f}_{k}(s)$ 具有最大次数。这样，就有

$$\deg \bar {f} (s) = \deg f _ {k} (s) - 1 < \deg f _ {k} (s) \tag {8.92}$$

进而，用 $\{f_{1}(s),\cdots,\overline{F}(s),\cdots,f_{a}(s)\}$ 代替原向量组 $\{f_{1}(s),\cdots,f_{k}(s),\cdots,f_{a}(s)\}$ 来构成同一空间的多项式基，但其中 $\bar{\mu}_{k}<\mu_{k}$ 。这表明， $\{f_{1}(s),\cdots,f_{a}(s)\}$ 不是最小多项式基。因此，和已知相矛盾，反设不成立，即 $F(s)$ 为不可简约。于是此部分证明完成。

再证明(2)→(1): 也采用反证法。反设 $\{f_{1}(s),\cdots,f_{n}(s)\}$ 不是最小多项式基，那么可规定另一个基为最小多项式基，如

$$
\left\{ \begin{array}{l} \left\{\boldsymbol {p} _ {1} (s), \boldsymbol {p} _ {2} (s), \dots , \boldsymbol {p} _ {\alpha} (s) \right\} \\ m _ {1} \leqslant m _ {2} \leqslant \dots \leqslant m _ {\alpha} \end{array} \right. \tag {8.93}
$$

其中， $\{\pmb{f}_i(s)\}$ 和 $\{\pmb{p}_i(s)\}$ 的次数之间，满足如下的关系：

$$m _ {1} = \mu_ {1}, \dots , m _ {j - 1} = \mu_ {j - 1}, m _ {j} < \mu_ {j} \tag {8.94}$$

式中 $j \in [2, \cdots, \alpha]$ 。进而，由于 $\{f_{i}(s)\}$ 为空间的基，所以每一个 $p_{k}(s)$ ， $k = 1, 2, \cdots, j$ ，都可表为

$$\boldsymbol {p} _ {k} (s) = \sum_ {i = 1} ^ {a} q _ {i} (s) \boldsymbol {f} _ {i} (s), k = 1, 2, \dots , j \tag {8.95}$$

而且，因已知 $F(s)$ 为不可简约，所以 $q_{i}(s)$ 均为多项式。再因已知 $F(s)$ 为列既约，故又有

$$\deg \boldsymbol {p} _ {k} (s) = \max _ {i} [ \deg q _ {i} (s) + \mu_ {i} ] \tag {8.96}$$

这表明，在 $F(s)$ 为列既约和不可简约的已知条件下，一定有

$$m _ {1} \geqslant \mu_ {1}, \dots , m _ {j} \geqslant \mu_ {j} \tag {8.97}$$

而这和反设 $m_{j} < \mu_{j}$ 显然是矛盾的。因此，反设不成立，即 $\{f_{1}(s), \cdots, f_{\alpha}(s)\}$ 为最小多项式基。此部分的证明完成。从而，也完成了整个结论的证明。

这个推论的意义在于,它为零空间的多项式基是否最小,提供了一个比较方便的判断准则。

例 给定传递函数矩阵 $G(s)$ 如下:
