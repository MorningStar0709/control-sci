（4）设 $G_{o}(s)$ 为 $q \times p$ 的非循环真有理分式矩阵，构成图 11.14 所示形式的输出反馈系统，其中 K 为 $p \times q$ 常数矩阵。又知闭环有理分式矩阵为：

$$\bar {G} _ {o} (s) = \left[ I + G _ {o} (s) K \right] ^ {- 1} G _ {o} (s) = G _ {o} (s) \left[ I + K G _ {o} (s) \right] ^ {- 1} \tag {11.176}$$

则对几乎所有任意取定的常阵 $K$ ， $\overline{G}_o(s)$ 必是循环有理分式矩阵。

上述性质为化非循环有理分式矩阵为循环有理分式矩阵提供了一条简单和可行的途径。下面，来给出对此性质的证明。表

$$\Delta \left[ \bar {G} _ {o} (s) \right] = a _ {n} s ^ {n} + a _ {n - 1} s ^ {n - 1} + \dots + a _ {1} s + a _ {0} \tag {11.177}$$

其中， $a_{i}(i=0,1,\cdots,n)$ 均为矩阵K的元 $k_{\alpha\beta}$ 的函数， $\alpha=1,2,\cdots,p,\beta=1,2,\cdots,q_{0}$ 进而，将多项式 $\Delta[\bar{G}_{o}(s)]$ 对 s 求一次导数，可得

$$\frac {d}{d s} \Delta [ \bar {G} _ {o} (s) ] = n a _ {n} s ^ {n - 1} + (n - 1) a _ {n - 1} s ^ {n - 2} + \dots + a _ {1} \tag {11.178}$$

十分明显, 如果 $\Delta[\overline{G}_o(s)] = 0$ 包含重根, 则多项式(11.177)和(11.178)必包含多项式公因子, 所以此时 $\Delta[\overline{G}_o(s)]$ 和 $\frac{d}{ds} \Delta[\overline{G}_o(s)]$ 不是互质的。但由多项式间互质性的分析可知, $\Delta[\overline{G}_o(s)]$ 和 $\frac{d}{ds} \Delta[\overline{G}_o(s)]$ 是非互质的充分必要条件为

$$
\det \left[ \begin{array}{c c c c c c c c} a _ {0} & a _ {1} \dots & a _ {n - 1} & a _ {n} & 0 & 0 & \dots & 0 \\ 0 & a _ {0} \dots & a _ {n - 2} & a _ {n - 1} & a _ {n} & 0 & \dots & 0 \\ & & & \vdots & & \\ 0 & 0 \dots & a _ {0} & a _ {1} & a _ {2} & \dots & a _ {n} \\ \hline a _ {1} & 2 a _ {2} \dots & n a _ {n} & 0 & 0 & \dots & 0 \\ 0 & a _ {1} \dots (n - 1) a _ {n - 1} & n a _ {n} & 0 & \dots & 0 \\ & & \vdots & \\ 0 & 0 \dots & 0 & a _ {1} & 2 a _ {2} & \dots & n a _ {n} \end{array} \right] = \mu \left(k _ {\alpha \beta}\right) = 0 \tag {11.179}
$$

此外，考虑到 $K$ 中总共有 $p \times q$ 个元 $k_{\alpha \beta}$ ，对每一个选定的 $K$ 可认为 $\{k_{\alpha \beta}\}$ 是 $p \times q$ 维的实向量空间 $\mathcal{R}^{p \times q}$ 中的一个向量，而所有 $K$ 构成 $\mathcal{R}^{p \times q}$ 。显然， $\mu(k_{\alpha \beta}) = 0$ 的非零解 $\{k_{\alpha \beta}\}$ 只构成 $\mathcal{R}^{p \times q}$ 中的一个子空间。这表明，对几乎任意选取的所有 $K$ ，都有 $\mu(k_{\alpha \beta}) \neq 0$ ，即 $\Delta[\overline{G}_o(s)] = 0$ 的根为两两相异。但根据上述性质(2)，当 $\Delta[\overline{G}_0(s)] = 0$ 的根为两两相异时，必有 $\overline{G}_o(s)$ 为循环。从而，就完成了证明。

系统传递函数矩阵 $G_{o}(s)$ 为循环时的输出反馈极点配置问题 给定受控系统的传递函数矩阵为 $q \times p$ 的 $G_{o}(s)$ ，设其为真的或严格真的，且假定 $G_{o}(s)$ 是循环的有理分式矩阵。现选定 $p \times 1$ 实常向量 $t_{1}$ 或 $1 \times q$ 的实常向量 $t_{2}$ ，使满足关系式(11.171)。再组成具有补偿器的单位输出反馈系统，如图11.15所示。其中， $\bar{C}(s)$ 表征引入的补偿环节的传递函数矩阵,而补偿器的传递函数矩阵则为

![](image/bfc67a2ec8d605a66590ed584073c07c8725b970c56a12f0d93c7060ae1391cf.jpg)

<details>
<summary>flowchart</summary>
