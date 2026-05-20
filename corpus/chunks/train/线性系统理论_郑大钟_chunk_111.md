为 $kq \times n$ 常阵，其中 $k$ 为正整数。并且，易知 $\overline{Q}_n = Q_n$ ，且 $\operatorname{rank} \overline{Q}_n = n$ 。现依次将 $k$ 由1增加，直到 $k = \nu$ 而使 $\operatorname{rank} \overline{Q}_n = n$ ，则称这个使上式成立的 $k$ 的最小正整数 $\nu$ 为系统的能观测性指数。可以证明 $^{1)}$ ，若 $\operatorname{rank} C = m$ ，则必成立

$$\frac {n}{q} \leqslant \nu \leqslant n - m + 1 \tag {3.91}$$

进而,如果令 $\bar{n}$ 为矩阵 A 的最小多项式的次数,那么式(3.91)还可表为

$$\frac {n}{q} \leqslant \nu \leqslant \min (\bar {n}, n - m + 1) \tag {3.92}$$

再若把 $\bar{Q}$ ，表为：

$$
\left[ \begin{array}{c} \mathbf {c} _ {1} \\ \mathbf {c} _ {2} \\ \vdots \\ \mathbf {c} _ {q} \\ \hline \mathbf {c} _ {1} A \end{array} \right]

\overline {{Q}} _ {v} = \left[ \begin{array}{c} c _ {2} A \\ \vdots \\ c _ {q} A \\ \vdots \\ c _ {1} A ^ {p - 1} \\ c _ {2} A ^ {p - 1} \\ \vdots \\ c _ {q} A ^ {p - 1} \end{array} \right] \tag {3.93}
$$

并且从上至下搜索 $Q$ ，中的 $n$ 个线性无关的行。考虑到 $C$ 的秩为 $m$ ，所以将这 $n$ 个线性无关的行重新排列后为：

$$
\begin{array}{l} \mathbf {c} _ {1} \\ \mathbf {c} _ {1} A \\ \vdots \\ \mathbf {c} _ {1} A ^ {\nu_ {1} - 1} \\ \vdots \\ \mathbf {c} _ {2} \\ \mathbf {c} _ {2} A \\ \vdots \\ \mathbf {c} _ {2} A ^ {\nu_ {2} - 1} \\ \vdots \\ \mathbf {c} _ {m} \\ \mathbf {c} _ {m} A \\ \vdots \\ \mathbf {c} _ {m} A ^ {\nu_ {m} - 1} \end{array} \tag {3.94}
$$

通常称 $\{\nu_{1},\nu_{2},\cdots,\nu_{m}\}$ 为系统 $(A,C)$ 的能观测性指数集。而且，显然有

$$\nu_ {1} + \nu_ {2} + \dots + \nu_ {m} = n \tag {3.95}$$

和

$$\nu = \max \left\{\nu_ {1}, \nu_ {2}, \dots , \nu_ {m} \right\} \tag {3.96}$$

不管是 $\nu$ 或是 $\{\nu_{1},\nu_{2},\cdots,\nu_{m}\}$ ，当对系统（3.75）作线性非奇异变换时，它们都是保持不变的。

此外，由(3.91)还可看到，当 $q = 1$ 即系统为单输出时，必有 $\nu = n$ 。同时，由(3.91)还可将判断能观测性的秩判据简化为：若 $\operatorname{rank} C = m$ ，则系统为能观测的充分必要条件为：

$$
\operatorname{rank} \bar {Q} _ {n - m + 1} = \operatorname{rank} \left[ \begin{array}{c} C \\ C A \\ \vdots \\ C A ^ {n - m} \end{array} \right] = n \tag {3.97}
$$

线性时变系统的能观测性判据 现转而讨论线性时变系统

$$\dot {\boldsymbol {x}} = A (t) \boldsymbol {x}, \boldsymbol {x} \left(t _ {0}\right) = \boldsymbol {x} _ {0}, t, t _ {0} \in J \tag {3.98}\boldsymbol {y} = C (t) \boldsymbol {x}$$

其中，J 为时间定义区间， $A(t)$ 和 $C(t)$ 分别为 $n \times n$ 和 $q \times n$ 时变矩阵。

下面,我们不加证明 $^{①}$ 地给出线性时变系统的能观测性的判据。

结论1[格拉姆矩阵判据] 线性时变系统（3.98）在时刻 $t_0$ 为完全能观测的充分必要条件是，存在一个有限时刻 $t_1 \in J, t_2 > t_0$ ，使如下定义的格拉姆矩阵

$$W _ {o} \left[ t _ {0}, t _ {1} \right] \triangleq \int_ {t _ {0}} ^ {t _ {1}} \Phi^ {T} (t, t _ {0}) C ^ {T} (t) C (t) \Phi (t, t _ {0}) d t \tag {3.99}$$

为非奇异,其中 $\Phi(\cdot,\cdot)$ 为系统(3.98)的状态转移矩阵。

一般地说,格拉姆矩阵判据主要用于理论分析中,而从应用的角度常采用如下的秩判据。

结论2[秩判据] 设 $A(t)$ 和 $C(t)$ 是 $(n - 1)$ 阶连续可微的，则线性时变系统(3.98)在时刻 $t_0$ 为完全能观测的一个充分条件是，存在一个有限时刻 $t_1 \in J, t_1 > t_0$ ，使成立

$$
\operatorname{rank} \left[ \begin{array}{c} N _ {0} \left(t _ {1}\right) \\ N _ {1} \left(t _ {1}\right) \\ \vdots \\ N _ {n - 1} \left(t _ {1}\right) \end{array} \right] = n \tag {3.100}
$$

其中

$$N _ {0} (t) = C (t)N _ {1} (t) = N _ {0} (t) A (t) + \frac {d}{d t} N _ {0} (t) \tag {3.101}$$

● ● ● ● ● ●

$$N _ {n - 1} (t) = N _ {n - 2} (t) A (t) + \frac {d}{d t} N _ {n - 2} (t)$$
