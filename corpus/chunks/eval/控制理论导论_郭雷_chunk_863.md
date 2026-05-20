# 11.7 稳定性与其他

本节讨论稳定性问题，给出稳定与一致稳定的定义与判据，证明能一致稳定的充要条件，还给出不稳定的例子.

线性多变量控制的几何方法在 DEDS 中有何进展？DEDS 的最小实现问题近况如何？本节将对这两个问题作简单论述。

稳定性是动态系统的一个基本而重要的问题，对 DEDS 有多种类型的稳定性定义，本节仅介绍两种较重要的稳定性定义。系统 (11.5.1) 当 $U(k) = \phi$ 时，称为自治系统，这时

$$\boldsymbol {X} (k) = \boldsymbol {X} (k - 1) \boldsymbol {A}. \tag {11.7.1}$$

定义 11.7.1 记 $X(k)=[x_{1}(k),x_{2}(k),\cdots,x_{n}(k)]$ . 设 $n_{0}$ 为足够大的正整数，当 $k>n_{0}$ 时，若有 $d,\lambda_{j}$ 存在，使得对任意取定初态有 $x_{j}(k+d)=\lambda_{j}^{d}x_{j}(d),1\leqslant j\leqslant n,$ 则称系统 (11.7.1) 为稳定的. $\lambda_{j}$ 称为 $x_{j}$ 的周期 (取不同初态时 $x_{j}$ 可能有不同周期).

DEDS 是一类复杂的非线性系统。定义 11.7.1 中要求的周期性对应于非线性微分方程中的稳定方程中的稳定极限环，极限环的各分量可有不同大小的“周期”。因此定义 11.7.1 中各 $\lambda_{j}$ 可以不相同。实际运行的工程系统可以是多周期系统，同时又是稳定的。另外，在工程制造系统中，中间库是普遍存在的，实际生产过程又是有限时间区间内进行的。所以各 $\lambda_{j}$ 不相同可能形成各 $x_{j}$ 的中间库存量不同，整个系统仍可认为是按一定节奏进行配套稳定生产。至于计算机网等其他 DEDS，各 $\lambda_{j}$ 更可以不同。

不稳定的系统是存在的，见下面例子.

例11.7.1 令

$$
\boldsymbol {A} = \left[ \begin{array}{l l l l l l} \varepsilon & 1 & 1 & \varepsilon & \varepsilon & 1 \\ 1 & \varepsilon & \varepsilon & \varepsilon & \varepsilon & \varepsilon \\ \varepsilon & \varepsilon & \varepsilon & 4 & \varepsilon & 1 \\ \varepsilon & \varepsilon & 4 & \varepsilon & \varepsilon & \varepsilon \\ \varepsilon & \varepsilon & \varepsilon & \varepsilon & \varepsilon & 3 \\ \varepsilon & \varepsilon & \varepsilon & \varepsilon & 3 & \varepsilon \end{array} \right],
\boldsymbol {X} (k) = [ x _ {1} (k), x _ {2} (k), \dots , x _ {6} (k) ] = \boldsymbol {X} (0) \boldsymbol {A} ^ {k}.
$$

经计算得 $(A^{2k + 1})_{1,6} = 6k + 1,(A^{2k})_{1.6} = 8k - 6.$ 取 $X(0) = [0\varepsilon \varepsilon \varepsilon \varepsilon ]$ ，得 $x_{6}(k)$ 如表11.7.1.该系统显然不稳定.

表 11.7.1 不确定的例子

<table><tr><td>k</td><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td><td>7</td><td>8</td><td>9</td></tr><tr><td> $x_6(k)$ </td><td>1</td><td>2</td><td>7</td><td>10</td><td>13</td><td>18</td><td>19</td><td>26</td><td>25</td></tr></table>

定义11.7.2 设 $n_0$ 为足够大的正整数. 当 $k > n_0$ 时, 若有 $d, \lambda$ 存在, 使得对任意初态有 $x_j(k + d) = \lambda^d x_j(k), 1 \leqslant j \leqslant n$ , 则我们称系统 (11.7.1) 为一致稳定的.

稳定性与分块周期阵有密切联系，文献[13]首先原则上给出了下面定理11.7.1中周期阵与分块周期阵的条件（见11.4节定理11.4.2与定理11.4.3).但附加了次要的假设 $H_{1}$ 或 $H_{2}$ .文献[3]用图论方法对上述结果作了很好的改进、推广与注释，去掉了假设 $H_{1}$ 或 $H_{2}$ ，得以下定理：
