$$\operatorname{rank} [ G | F G | ^ {q} \dots | F ^ {n - q - 1} G ] = n - q _ {0}$$

第3步：求出方程 $TA - FT = GC$ 的唯一的 $(n - q) \times n$ 解阵 $T_{0}$

第4步：构成并判断矩阵

$$
P = \left[ \begin{array}{c} C \\ T \end{array} \right]
$$

的非奇异性。若 $P$ 为非奇异，计算 $H = TB$ ；若 $P$ 为奇异，返回第1步或第2步，重复计算过程。

第 5 步：组成降维状态观测器方程

$$\dot {z} = F z + G y + H u$$

表 $Q \triangle P^{-1} = [Q_1, Q_2]$ ，其中 $Q_1$ 和 $Q_2$ 分别为 $n \times q$ 和 $n \times (n - q)$ 阵，则估计状态 $\pmb{x}$ 就为：

$$\hat {x} = Q _ {1} y + Q _ {2} z$$

现在,我们来对降维状态观测器和全维状态观测器作一比较。从结构上看,降维观测器只需 $(n-q)$ 个积分器,远较全维观测器需要n个积分器为少。从抗干扰性能上看,由于降维观测器中y通过增益阵 $Q_{1}$ 直接传递到其输出端,所以若y中包含干扰时它们将全部出现于 $\hat{x}$ 中;而在全维观测器中,y需经积分器滤波后才传送到输出端,从而 $\hat{x}$ 中由y中包含的干扰所引起的影响已大为减小。这表明,在工程应用中,究竟是采用降维观测器还是全维观测器,应视具体情况来加以确定。

函数观测器 在很多情况下, 进行状态重构的目的是为了实现状态反馈; 而如前面分析中所指出的, 状态观测器的最小维数为 $n - q$ . 因此, 为了进一步减少观测器的维数, 可直接对状态函数 $Kx$ 进行重构, 并且称这样的观测器为函数观测器。

比之状态观测器, 函数观测器的综合不管是在理论上还是在计算上都要复杂得多。这里, 我们只对函数观测器作一概要性的介绍。

(1) 给定完全能控和完全能观测的线性定常系统:

$$
\begin{array}{l} \dot {x} = A x + B u, \quad x (0) = x _ {0} \\ \mathbf {y} = C \mathbf {x} \tag {5.347} \\ \end{array}
$$

其中，A, B 和 C 分别为 $n \times n, n \times p$ 和 $q \times n$ 实常阵。那么，以 Kx 为重构目标的函数观测器可取为：

$$
\begin{array}{l} \dot {z} = F z + G y + H u, \quad z (0) = z _ {0} \\ w = M z + N y \tag {5.348} \\ \end{array}
$$

其中， $F$ 为 $m \times m$ 矩阵， $G$ 为 $m \times q$ 矩阵， $H$ 为 $m \times p$ 矩阵， $M$ 为 $p \times m$ 矩阵， $N$ 为 $p \times q$ 矩阵， $m$ 为观测器的维数。并且，使函数观测器 (5.348) 的输出 $w(t)$ 渐近地趋于 $Kx(t)$ ，其中 $p \times n$ 常阵 $K$ 为已知，也即使成立

$$\lim _ {t \rightarrow \infty} w (t) = \lim _ {t \rightarrow \infty} K x (t) \tag {5.349}$$

的充分必要条件为:

① TA - FT = GC, T 为 $m \times n$ 实常阵。

② H = TB

③ F 的全部特征值均具有负实部。

④ $MT + NC = K$

我们仅来证明其充分性。由上述条件 ① 和 ② 成立，故可导出

$$
\begin{array}{l} \dot {z} - T \dot {x} = (F z + G y + H u) - T (A x + B u) \\ = (G C - T A) x + (H - T B) u + F z \\ = F \mathbf {z} - F T \mathbf {x} = F (\mathbf {z} - T \mathbf {x}) \tag {5.350} \\ \end{array}
$$

也即有

$$\boldsymbol {z} (t) - T \boldsymbol {x} (t) = e ^ {F t} \left(\boldsymbol {z} _ {0} - T \boldsymbol {x} _ {0}\right) \tag {5.351}$$

而由条件 ③ 可知当 $t \to \infty$ 时 $e^{Ft} \to 0$ ，从而成立

$$\lim _ {t \rightarrow \infty} z (t) = \lim _ {t \rightarrow \infty} T x (t) \tag {5.352}$$

再因条件 ④ 成立, 故由 (5.348) 和 (5.352) 就可进而得到:

$$
\begin{array}{l} \lim _ {t \rightarrow \infty} w (t) = \lim _ {t \rightarrow \infty} (M z (t) + N y (t)) \\ = \lim _ {t \rightarrow \infty} (M T + N C) x (t) \\ = \lim _ {t \rightarrow \infty} K x (t) \tag {5.353} \\ \end{array}
$$

于是，就完成了充分性的证明。
