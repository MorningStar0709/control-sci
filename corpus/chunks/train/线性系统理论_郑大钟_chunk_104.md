$$\operatorname{rank} Q _ {n - r + 1} = \operatorname{rank} [ B | A B | \dots | A ^ {n - r} B ] = n \tag {3.53}$$

注意到矩阵 B 的秩易于计算,所以利用 $(3.53)$ 来判断能控性可使计算得到简化。

③ 令 $\bar{n}$ 为矩阵 $A$ 的最小多项式 $^{1)}$ 的次数, 且必有 $\bar{n} \leqslant n$ , 则能控性指数 $\mu$ 的估计不等式 (3.52) 可进而表为:

$$\frac {n}{p} \leqslant \mu \leqslant \min (\bar {n}, n - r + 1) \tag {3.54}$$

可容易证明这一点：按最小多项式定义有

$$\psi (A) = A ^ {n} + a _ {n - 1} A ^ {n - 1} + \dots + a _ {1} A + a _ {0} I = 0 \tag {3.55}$$

从而，可得

$$A ^ {n} B = - a _ {n - 1} A ^ {n - 1} B - \dots - a _ {1} A B - a _ {0} B \tag {3.56}$$

表明 $A^{n}B$ 的所有列均线性相关于 $Q_{n + 1}$ 中其左方各列向量。因此，据能控性指数的定义，可知必成立 $\mu \leqslant \bar{n}$ 。由此，并利用(3.52)，即可导出关系式(3.54)。

④ 将 $Q_{\mu}$ 表为

$$Q _ {\mu} = \left[ b _ {1}, b _ {2}, \dots , b _ {p} \mid A b _ {1}, A b _ {2}, \dots , A b _ {p} \mid A ^ {2} b _ {1}, A ^ {2} b _ {2}, \dots , \right.A ^ {2} \boldsymbol {b} _ {p} | \dots | A ^ {\mu - 1} \boldsymbol {b} _ {1}, A ^ {\mu - 1} \boldsymbol {b} _ {2}, \dots , A ^ {\mu - 1} \boldsymbol {b} _ {p} ] \tag {3.57}$$

且依次从左至右搜索 $Q_{\mu}$ 中的 $\pmb{n}$ 个线性无关的列。若某个列不能表为其左方各列之线性组合则为线性无关，否则便是线性相关。考虑到 $B$ 的秩为 $\pmb{r}$ ，故可将得到的 $\pmb{n}$ 个线性无关的列重新排列如下：

$$\boldsymbol {b} _ {1}, A \boldsymbol {b} _ {1}, \dots , A ^ {\mu_ {1} - 1} \boldsymbol {b} _ {1}; \boldsymbol {b} _ {2}, A \boldsymbol {b} _ {2}, \dots , A ^ {\mu_ {2} - 1} \boldsymbol {b} _ {2}; \dots ;\boldsymbol {b} _ {r}, A \boldsymbol {b} _ {r}, \dots , A ^ {\mu_ {r} - 1} \boldsymbol {b} _ {r} \tag {3.58}$$

且对能控系统显然有

$$\mu_ {1} + \mu_ {2} + \dots + \mu_ {r} = n \tag {3.59}$$

而能控性指数 $\mu$ 满足关系式

$$\mu = \max \left\{\mu_ {1}, \mu_ {2}, \dots , \mu_ {r} \right\} \tag {3.60}$$

通常，称 $\{\mu_{1},\mu_{2},\cdots,\mu_{r}\}$ 为系统 $(A,B)$ 的能控性指数集。

⑤ 对系统的状态方程（3.7）作线性非奇异变换，其能控性指数 $\mu$ 和能控性指数集 $\{\mu_{1}, \mu_{2}, \cdots, \mu_{r}\}$ 保持不变。

这是因为，在线性非奇异变换下有 $\vec{A} = PAP^{-1}$ 和 $\vec{B} = PB$ ， $P$ 为非奇异常阵，故可导出

$$[ \bar {b} _ {1}, \bar {A} \bar {b} _ {1}, \dots , \bar {A} ^ {\mu_ {1} - 1} \bar {b} _ {1}; \bar {b} _ {2}, \bar {A} \bar {b} _ {2}, \dots , \bar {A} ^ {\mu_ {2} - 1} \bar {b} _ {2}; \dots ;\bar {b} _ {r}, \bar {A} \bar {b} _ {r}, \dots , \bar {A} ^ {\mu_ {r} - 1} \bar {b} _ {r} ] = P [ b _ {1}, A b _ {1}, \dots , A ^ {\mu_ {1} - 1} b _ {1};\left. \boldsymbol {b} _ {2}, A \boldsymbol {b} _ {2}, \dots , A ^ {\mu_ {2} - 1} \boldsymbol {b} _ {2}; \dots ; \boldsymbol {b} _ {r}, A \boldsymbol {b} _ {r}, \dots , A ^ {\mu_ {r} - 1} \boldsymbol {b} _ {r} \right] \tag {3.61}$$

和

$$\bar {Q} _ {\mu} = [ \bar {B} | \bar {A} \bar {B} | \dots | \bar {A} ^ {\mu - 1} \bar {B} ] = P Q _ {\mu} \tag {3.62}$$
