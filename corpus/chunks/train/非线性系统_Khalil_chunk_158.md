# 5.1 $\mathcal{L}$ 稳定性

考虑一个系统,其输入-输出关系表示如下:

$$y = H u$$

其中 $H$ 是某种映射或算子，指定了 $y$ 与 $u$ 的关系。输入 $u$ 属于信号空间，信号空间把时间区间 $[0, \infty)$ 映射到欧几里得空间 $R^m$ ，即 $u: [0, \infty) \to R^m$ 。例如分段连续的有界函数空间 $\sup_{t \geqslant 0} \| u(t) \| < \infty$ 和分段连续的平方可积函数空间 $\int_0^\infty u^{\mathrm{T}}(t) u(t) dt < \infty$ 。为度量信号的大小，引入范数 $\| u\|$ ，它满足下面三个性质：

- 当且仅当信号恒为零时，信号的范数等于零，否则严格为正。  
- 对于任意正常数 $a$ 和信号 $u$ , 数乘信号的范数等于范数的数乘, 即 $\|au\| = a \|u\|$ 。  
- 对于任意信号 $u_{1}$ 和 $u_{2}$ , 范数满足三角不等式 $\| u_{1} + u_{2} \| \leqslant \| u_{1} \| + \| u_{2} \|$ 。

对于分段连续有界函数空间,其范数定义为:

$$\| u \| _ {\mathcal {L} _ {\infty}} = \sup _ {t \geqslant 0} \| u (t) \| < \infty$$

该空间表示为 $\mathcal{L}_{\infty}^{m}$ 。对于分段连续平方可积函数空间，其范数定义为

$$\| u \| _ {\mathcal {L} _ {2}} = \sqrt {\int_ {0} ^ {\infty} u ^ {\mathrm{T}} (t) u (t) d t} < \infty$$

该空间表示为 $L_{2}^{m}$ 。一般情况下，对于 $1\leqslant p<\infty$ ，空间 $L_{p}^{m}$ 定义为连续函数 $u:[0,\infty)\rightarrow R^{m}$ 的集合，满足

$$\| u \| _ {\mathcal {L} _ {p}} = \left(\int_ {0} ^ {\infty} \| u (t) \| ^ {p} d t\right) ^ {1 / p} < \infty$$

$L_{p}^{m}$ 的下标 p 用于表示定义空间 p 范数的类型, 而上标 m 表示信号 u 的维数。如果 m 和 p 通过上下文可知,则可省掉其一或两个都省略,例如 $L_{p},L^{m}$ 和L。为了区别空间L中向量u的范数与 $R^{m}$ 中向量 $u(t)$ 的范数,我们把前者记为 $\|\cdot\|_{L^{①}}$ 。

如果认为 $u \in \mathcal{L}^m$ 是“良态”输入，要问的问题是能否有“良态”输出 $y \in \mathcal{L}^q$ ，其中 $\mathcal{L}^m$ 与 $\mathcal{L}^q$ 空间相同，但通常输出变量数 $q$ 与输入变量数 $m$ 不同。由“良态”输入产生“良态”输出的系统定义为稳定系统。但不能把 $H$ 定义为从 $\mathcal{L}^m$ 到 $\mathcal{L}^q$ 的映射，因为必须处理不稳定系统，而不稳定系统的输入 $u \in \mathcal{L}^m$ 可能产生不属于 $\mathcal{L}^q$ 的输出 $y$ 。所以， $H$ 经常定义为从扩展空间 $\mathcal{L}_e^m$ 到扩展空间 $\mathcal{L}_e^q$ 的映射，其中 $\mathcal{L}_e^m$ 定义为

$$\mathcal {L} _ {e} ^ {m} = \left\{u \mid u _ {\tau} \in \mathcal {L} ^ {m}, \forall \tau \in [ 0, \infty) \right\}$$

$u$ 的舍位函数 $u_{\tau}$ 定义为 $u_{\tau}(t) = \left\{ \begin{array}{ll}u(t), & 0\leqslant t\leqslant \tau \\ 0, & t > \tau \end{array} \right.$

扩展空间 $\mathcal{L}_e^m$ 是以未扩展空间 $\mathcal{L}^m$ 作为其子空间的线性空间，它便于对无限增加的信号加以处理。例如，信号 $u(t) = t$ 不属于空间 $\mathcal{L}_{\infty}$ ，但对于每个有限的 $\tau$ ，其舍位函数

$$
u _ {\tau} (t) = \left\{ \begin{array}{l l} t, & 0 \leqslant t \leqslant \tau \\ 0, & t > \tau \end{array} \right.
$$

属于 $\mathcal{L}_{\infty}$ 。因此， $u(t) = t$ 属于扩展空间 $\mathcal{L}_{\infty e}$ 。

如果在任何时刻 $t$ ，输出 $(Hu)(t)$ 只与该时刻的输入值有关，则称映射 $\mathcal{L}_e^m\to \mathcal{L}_e^q$ 是因果的。这相当于 $(Hu)_{\tau} = (Hu_{\tau})_{\tau}$

因果性是状态模型表示的动力学系统的内蕴性质。

完成输入-输出信号空间定义之后,现在定义输入-输出稳定性。
