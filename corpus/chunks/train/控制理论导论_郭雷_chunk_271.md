# 3.12 辛几何

辛几何在Hamilton系统及无源性控制系统的研究中起着重要作用．实际上，它为Hamilton系统提供了几何框架.

定义3.12.1 一个 $2n$ 维流形 $M$ 连同一个2-形式 $\omega$ 称为一个辛流形，如果 $\omega$ 是反对称，非奇异且闭的.

一个 $k$ -形式 $\omega$ 称为闭的，如果 $d\omega = 0$ 。可以用以下方法检验一个2-形式是不是闭的。

命题3.12.1 设 $\omega$ 在一个坐标卡下的矩阵表现为 $M_{\omega} = (\sigma_{i,j})$ . 那么 $d\omega = 0$ 当且仅当

$$\frac {\partial}{\partial x _ {i}} \left(\sigma_ {j k}\right) + \frac {\partial}{\partial x _ {j}} \left(\sigma_ {k i}\right) + \frac {\partial}{\partial x _ {k}} \left(\sigma_ {i j}\right) = 0, \quad \forall i, j, k. \tag {3.12.1}$$

证明 由于 $\sigma = \sum_{i}\sum_{j}\sigma_{i,j}\mathrm{d}x^{i}\wedge \mathrm{d}x^{j}$ ，则

$$\mathrm{d} \sigma = \sum_ {k} \sum_ {i} \sum_ {j} \frac {\partial \sigma_ {i , j}}{\partial x _ {k}} \mathrm{d} x ^ {k} \wedge \mathrm{d} x ^ {i} \wedge \mathrm{d} x ^ {j}.$$

对一个给定的指标组 $I, J, K$ ，我们合并形为 $\mathrm{d}x^I \wedge \mathrm{d}x^J \wedge \mathrm{d}x^K$ 的项。设 $k = I, i = J$ ，及 $j = K$ ，则 $\mathrm{d}x^I \wedge \mathrm{d}x^J \wedge \mathrm{d}x^K$ 的系数为

$$\frac {\partial \sigma_ {J K}}{\partial x _ {I}} \mathrm{d} x ^ {I} \wedge \mathrm{d} x ^ {J} \wedge \mathrm{d} x ^ {K}.$$

设 $k = I, i = K,$ 及 $j = J$ . 由于反对称性，则相应的系数为

$$\frac {\partial \sigma_ {K J}}{\partial x _ {I}} \mathrm{d} x ^ {I} \wedge \mathrm{d} x ^ {K} \wedge \mathrm{d} x ^ {J} = - \frac {\partial \sigma_ {J K}}{\partial x _ {I}} \mathrm{d} x ^ {I} \wedge \mathrm{d} x ^ {K} \wedge \mathrm{d} x ^ {J} = \frac {\partial \sigma_ {J K}}{\partial x _ {I}} \mathrm{d} x ^ {I} \wedge \mathrm{d} x ^ {J} \wedge \mathrm{d} x ^ {K}.$$

同样地，对 $k = K, i = I$ ，及 $j = J$ （或 $i = J$ ，及 $j = I$ )，相应的系数为

$$\frac {\partial \sigma_ {I J}}{\partial x _ {K}} \mathrm{d} x ^ {I} \wedge \mathrm{d} x ^ {J} \wedge \mathrm{d} x ^ {K}.$$

对 $k = J, i = K,$ 及 $j = I$ (或 $i = I,$ 及 $j = K$ ), 相应的系数为

$$\frac {\partial \sigma_ {K I}}{\partial x _ {J}} \mathrm{d} x ^ {I} \wedge \mathrm{d} x ^ {J} \wedge \mathrm{d} x ^ {K}.$$

合并上述6项，则得 $\mathrm{d}x^{I}\wedge \mathrm{d}x^{J}\wedge \mathrm{d}x^{K}$ 的系数为

$$2 \frac {\partial}{\partial x _ {I}} (\sigma_ {J K}) + 2 \frac {\partial}{\partial x _ {J}} (\sigma_ {K I}) + 2 \frac {\partial}{\partial x _ {K}} (\sigma_ {I J}),$$

它应为零，从而式(3.12.1)成立.

例3.12.1 在 $\mathbb{R}^{2n}$ 中定义一个2-形式 $\omega$ , 它的矩阵表示为 $M_{\omega} = J$ , 这里

$$
\boldsymbol {J} = \left[ \begin{array}{c c} 0 & \boldsymbol {I} _ {n} \\ - \boldsymbol {I} _ {n} & 0 \end{array} \right], \tag {3.12.2}
$$

那么 $(R^{2n},\omega)$ 是一个辛流形.
