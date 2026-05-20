$$
\begin{array}{l} e ^ {A t} = \sum_ {k = 0} ^ {\infty} \frac {1}{k !} A ^ {k} t ^ {k} \\ = P \left[ \begin{array}{c c c} \sum_ {k = 0} ^ {\infty} \frac {1}{k !} \lambda_ {1} ^ {k} t ^ {k} & & \\ & \ddots & \\ & & \sum_ {k = 0} ^ {\infty} \frac {1}{k !} \lambda_ {n} ^ {k} t ^ {k} \end{array} \right] P ^ {- 1} \\ \end{array}

= P \left[ \begin{array}{c c c} e ^ {\lambda_ {1} t} & & \\ & \ddots & \\ & & e ^ {\lambda_ {n} t} \end{array} \right] P ^ {- 1} \tag {2.20}
$$

表明，当且仅当 $\mathrm{Re}\lambda_{i}<0\quad(i=1,\cdots,n)$ 时，式（2.18）成立。进而，考虑一般的情况，设 A 具有相异的 l 个特征值 $\lambda_{1}(\sigma_{1}$ 重）， $\lambda_{2}(\sigma_{2}$ 重）， $\cdots$ ， $\lambda_{l}(\sigma_{l}$ 重）， $(\sigma_{1}+\sigma_{2}+\cdots+\sigma_{l})=n$ ，则由（1.61）可导出：

$$A = Q \hat {A} Q ^ {- 1} \tag {2.21}$$

其中 $Q$ 为常数矩阵，而 $\hat{A}$ 为约当形矩阵。从而，可得到

$$e ^ {A t} = Q e ^ {\lambda t} Q ^ {- 1} \tag {2.22}$$

但由 $\hat{A}$ 为约当形可知， $e^{\lambda_{i}}$ 的每一个元都具有 $t^{m}e^{\lambda_{i}t}$ 的形式 $(m=0,1,\cdots,r_{i}-1,i=1,2,\cdots,l)$ ， $r_{i}$ 是 $\hat{A}$ 中与 $\lambda_{i}$ 相应的约当小块的最大维数。显然，当且仅当 $\operatorname{Re}\lambda_{i}<0\quad(i=1,\cdots,l)$ 时，有

$$\lim _ {t \rightarrow \infty} t ^ {m} e ^ {\lambda_ {i} t} = 0, \quad i = 1, \dots , l \tag {2.23}$$

于是，由此即可证得：

$$\lim _ {t \rightarrow \infty} e ^ {A t} = \lim _ {t \rightarrow \infty} Q e ^ {\hat {A} t} Q ^ {- 1} = 0 \tag {2.24}$$

④ 当对给定的系统 (2.10) 来确定其零输入响应 $\phi(t; 0, x_0, 0)$ 的解析表达式或数值结果时, 其核心的步骤是计算矩阵指数函数 $e^{At}$ 。因此, 在下一小节中, 我们要对 $e^{At}$ 的计算方法予以专门的讨论。

⑤ 在式(2.12)中我们把初始时间取为 $t_{0}=0$ ，考虑到定常系统的分析结果和初始时间的选取无关，因此这样做并不失去问题的一般性。但是，如果因某种需要而取 $t_{0}\neq0$ ，那么此时零输入响应的表达式应相应地表为：

$$\phi (t; t _ {0}, x _ {0}, 0) = e ^ {A (t - t _ {0})} x _ {0}, \quad t \geqslant t _ {0} \tag {2.25}$$

矩阵指数函数的性质和计算方法 考虑到矩阵指数函数 $e^{At}$ 在线性定常系统运动分析中的重要性, 因此这里对其性质和计算方法作一比较系统和详细的讨论。

从矩阵指数函数的定义式(2.11)出发,可导出 $e^{At}$ 具有如下的一些基本性质:

$$① \lim _ {t \rightarrow 0} e ^ {A t} = I$$

② 令 $\pmb{\tau}$ 和 $\pmb{\tau}$ 为两个自变量，则必成立

$$e ^ {A (t + \tau)} = e ^ {A t} \cdot e ^ {A \tau} = e ^ {A \tau} \cdot e ^ {A t} \tag {2.26}$$

③ $e^{At}$ 总是非奇异的，且其逆为：

$$(e ^ {A t}) ^ {- 1} = e ^ {- A t} \tag {2.27}$$

显然，在(2.26)中取 $\tau = -t$ ，就得(2.27)。

④ 设有 $n \times n$ 常阵 $A$ 和 $F$ , 如果 $A$ 和 $F$ 是可交换的, 即 $AF = FA$ , 则必成立

$$e ^ {(A + F) t} = e ^ {A t} \cdot e ^ {F t} = e ^ {F t} \cdot e ^ {A t} \tag {2.28}$$

⑤ $\varepsilon^{A_{t}}$ 对 t 的导数为：

$$\frac {d}{d t} e ^ {A t} = A e ^ {A t} = e ^ {A t} A \tag {2.29}$$

⑥ 对给定方阵 A，必成立

$$\left(e ^ {A t}\right) ^ {m} = e ^ {A (m t)}, \quad m = 0, 1, 2, \dots \tag {2.30}$$
