# 7.7 史密斯-麦克米伦形

史密斯-麦克米伦形是1952年由麦克米伦（B. McMillan）所提出的，它是将多项式矩阵的史密斯形推广于有理分式矩阵而得到的一种规范形。史密斯-麦克米伦形的意义，在于为系统分析，特别是分析多变量系统的极点和零点，提供了一种重要的概念性和理论性工具。

史密斯-麦克米伦形 令 $G(s)$ 为 $q \times p$ 的有理分式矩阵， $\operatorname{rank} G(s) = r \leqslant \min \{q, p\}$ ，则一定存在 $q \times q$ 和 $p \times p$ 的单模矩阵 $U(s)$ 和 $V(s)$ ，使可以导出

$$
U (s) G (s) V (s) \triangleq M (s) = \left[ \begin{array}{c c c c} \frac {\varepsilon_ {1} (s)}{\psi_ {1} (s)} & & & \\ & \ddots & & 0 \\ & & \frac {\varepsilon_ {r} (s)}{\psi_ {r} (s)} & \\ - & 0 & - & 0 \end{array} \right] \tag {7.95}
$$

其中， $\{\varepsilon_{i}(s),\psi_{i}(s)\}$ 为互质， $i=1,2,\cdots,r$ ，且满足整除性 $\phi_{i+1}(s)|\phi_{i}(s)$ 和 $\varepsilon_{i}(s)|\varepsilon_{i+1}(s)$ ， $i=1,\cdots,r-1$ 。进而，称(7.95)所示的 $M(s)$ 为传递函数矩阵 $G(s)$ 的史密

斯-麦克米伦形。

证 令多项式 $d(s)$ 为 $G(s)$ 的所有有理分式元的最小公分母, 则可将 $G(s)$ 表示为

$$G (s) = \frac {1}{d (s)} N (s) \tag {7.96}$$

其中 $N(s)$ 为一个多项式矩阵。显然，由(7.96)即可导出

$$N (s) = d (s) G (s) \tag {7.97}$$

而由多项式矩阵的史密斯形的基本结论可知，一定存在单模阵对 $\{U(s), V(s)\}$ ，使有

$$
U (s) d (s) G (s) V (s) = \Lambda (s) = \left[ \begin{array}{c c c} \lambda_ {1} (s) & & 0 \\ & \ddots & \\ & & \lambda_ {r} (s) \\ - & 0 & 0 \end{array} \right] \tag {7.98}
$$

再注意到 $d(s)$ 为标量多项式，所以上式可以进一步改写为

$$
M (s) = U (s) G (s) V (s) = \frac {\Lambda (s)}{d (s)} = \left[ \begin{array}{c c c c} \frac {\lambda_ {1} (s)}{d (s)} & & & \\ & \ddots & & 0 \\ & & \frac {\lambda_ {r} (s)}{d (s)} & \\ - & 0 & - & 0 \end{array} \right] \tag {7.99}
$$

因为 $G(s)$ 一般为可简约，所以在元有理分式

$$\lambda_ {i} (s) / d (s), \quad i = 1, 2, \dots , r \tag {7.100}$$

中可能包含公因子。这样，通过消去公因子，使有

$$\frac {\lambda_ {i} (s)}{d (s)} = \frac {\varepsilon_ {i} (s)}{\psi_ {i} (s)}, \left\{\varepsilon_ {i} (s), \psi_ {i} (s) \right\} \text {互质} \tag {7.101}$$

那么便得到了(7.95)所示的史密斯-麦克米伦形。此外，由整除性 $\lambda_{i}(s)|\lambda_{i+1}(s)$ 可导出

$$d (s) \frac {\varepsilon_ {i} (s)}{\psi_ {i} (s)} \left| d (s) \frac {\varepsilon_ {i + 1} (s)}{\psi_ {i + 1} (s)} \text {即} \frac {\varepsilon_ {i} (s)}{\psi_ {i} (s)} \right| \frac {\varepsilon_ {i + 1} (s)}{\psi_ {i + 1} (s)} \tag {7.102}$$

从而进一步可导出 $\varepsilon_{i}(s)|\varepsilon_{i + 1}(s)$ 和 $\psi_{i + 1}(s)|\psi_i(s)$ 。于是就完成了证明。

例 给定传递函数矩阵 $G(s)$ 如下:

$$
G (s) = \left[ \begin{array}{c c} \frac {s}{(s + 1) ^ {2} (s + 2) ^ {2}} & \frac {s}{(s + 2) ^ {2}} \\ \frac {- s}{(s + 2) ^ {2}} & \frac {- s}{(s + 2) ^ {2}} \end{array} \right]
$$

容易定出,其最小公分母 $d(s)$ 和相应的分子多项式矩阵 $N(s)$ 分别为
