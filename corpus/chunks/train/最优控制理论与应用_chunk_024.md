例1-3 生产计划问题。设 $x(t)$ 表示商品存货量, $r(t) \geqslant 0$ 表示对商品的需求率, 是已知函数, $u(t)$ 表示生产率, 它将由计划人员来选取, 故是控制变量。 $x(t)$ 满足下面的微分方程

$$\dot {x} (t) = - r (t) + u (t) \quad t \in [ 0, t _ {\mathrm{f}} ] \tag {1-11}x (0) = x _ {0}$$

$x_0$ 是初始时刻的商品存货量，且 $x_0 \geqslant 0$ 。从 $x(t)$ 的实际意义来看，显然必须选取生产率 $u(t)$ 使得

$$x (t) \geqslant 0 \quad t \in [ 0, t _ {\mathrm{f}} ] \tag {1-12}$$

其次，生产能力应该有限制，即容许控制为

$$0 \leqslant u (t) \leqslant A \quad t \in [ 0, t _ {\mathrm{f}} ] \tag {1-13}$$

这里 A > 0 表示最大生产率, 另外为了保证满足需求, 必须有

$$A > r (t) \quad t \in [ 0, t _ {\mathrm{f}} ] \tag {1-14}$$

假定每单位时间的生产成本是生产率 $u(t)$ 的函数，即 $h[u(t)]$ 。设 $b > 0$ 是单位时间储存单位商品的费用，于是，单位时间的总成本为

$$f [ x (t), u (t), t ] = h [ u (t) ] + b x (t) \tag {1-15}$$

由 $t = 0$ 到 $t = t_{\mathrm{f}}$ 的总成本为

$$J (u) = \int_ {0} ^ {t _ {\mathrm{f}}} f [ x (t), u (t), t ] \mathrm{d} t \tag {1-16}$$

要求寻找最优控制 $u^{*}(t)$ ，使总成本 $J$ 最小。

由上面的例子可见,求解最优控制问题时要给定系统的状态方程、状态变量所满足的初始条件和终端条件、性能指标的形式(时间最短、消耗燃料最少、误差平方积分最小等)以及控制作用的容许范围等。

用数学语言来比较详细地表达最优控制问题的内容：

(1) 建立被控系统的状态方程

$$\dot {\boldsymbol {X}} = \boldsymbol {f} [ \boldsymbol {X} (t), \boldsymbol {U} (t), t ] \tag {1-17}$$

其中， $X(t)$ 为 $n$ 维状态向量， $\pmb {U}(t)$ 为 $m$ 维控制向量， $\pmb {f}[\pmb {X}(t),\pmb {U}(t),t]$ 为 $n$ 维向量函数，它可以是非线性时变向量函数，也可以是线性定常的向量函数。状态方程必须精确地知道。

（2）确定状态方程的边界条件。一个动态过程对应于 n 维状态空间中从一个状态到另一个状态的转移，也就是状态空间中的一条轨线。在最优控制中初态通常是已知的，即

$$\boldsymbol {X} \left(t _ {0}\right) = \boldsymbol {X} _ {0} \tag {1-18}$$

而到达终端的时刻 $t_{\mathrm{f}}$ 和状态 $\pmb {X}(t_{\mathrm{f}})$ 则因问题而异。例如，在流水线生产过程中， $t_\mathrm{f}$ 是固定的；在飞机快速爬高时，只规定爬高的高度 $\pmb {X}(t_{\mathrm{f}}) = \pmb {X}_{\mathrm{f}}$ 而 $t_\mathrm{f}$ 是自由的，要求 $t_\mathrm{f} - t_0$ 越小越好。终端状态 $\pmb {X}(t_{\mathrm{f}})$ 一般属于一个目标集 $S$ ，即

$$\boldsymbol {X} \left(t _ {\mathrm{f}}\right) \in S \tag {1-19}$$

当终端状态是固定的, 即 $X(t_{\mathrm{f}}) = X_{\mathrm{f}}$ 时, 则目标集退化为 $n$ 维状态空间中的一个点。而当终态满足某些约束条件, 即

$$\boldsymbol {G} \left[ \boldsymbol {X} \left(t _ {\mathrm{f}}\right), t _ {\mathrm{f}} \right] = 0 \tag {1-20}$$

这时 $X(t_{\mathrm{f}})$ 处在 n 维状态空间中某个超曲面上。若终态不受约束，则目标集便扩展到整个 n 维空间，或称终端状态自由。

(3) 选定性能指标 J。性能指标一般有下面的形式：

$$J = \phi [ \boldsymbol {X} (t _ {\mathrm{f}}), t _ {\mathrm{f}} ] + \int_ {t _ {0}} ^ {t _ {\mathrm{f}}} L [ \boldsymbol {X} (t), \boldsymbol {U} (t), t ] \mathrm{d} t \tag {1-21}$$
