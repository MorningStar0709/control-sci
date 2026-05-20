# 1. 线性二次型问题

设线性时变系统的动态方程为

$$\dot {\boldsymbol {x}} (t) = \boldsymbol {A} (t) \boldsymbol {x} (t) + \boldsymbol {B} (t) \boldsymbol {u} (t), \quad \boldsymbol {x} \left(t _ {0}\right) = \boldsymbol {x} _ {0} \tag {10-92}\mathbf {y} (t) = \mathbf {C} (t) \mathbf {x} (t)$$

性能指标为

$$J = \frac {1}{2} e ^ {\mathrm{T}} (t _ {f}) F e (t _ {f}) + \frac {1}{2} \int_ {t _ {0}} ^ {t _ {f}} [ e ^ {\mathrm{T}} (t) Q (t) e (t) + u ^ {\mathrm{T}} (t) R (t) u (t) ] \mathrm{d} t \tag {10-93}$$

式中， $x(t)\in \mathbf{R}^n$ ； $u(t)\in \mathbf{R}^m$ ，无约束； $y(t)\in \mathbf{R}^l$ ， $0 < l\leqslant m\leqslant n$ ；输出误差向量 $e(t) = z(t) - y(t)$ ； $z(t)\in \mathbf{R}^l$ ，为理想输出向量； $\pmb {A}(t),\pmb {B}(t),\pmb {C}(t)$ 为维数适当的时变矩阵，其各元连续且有界；权阵 $\pmb {F} = \pmb {F}^{\mathrm{T}}\geqslant 0,\pmb {Q}(t) = \pmb {Q}^{\mathrm{T}}(t)\geqslant 0,\pmb {R}(t) = \pmb {R}^{\mathrm{T}}(t) > 0;t_{0}$ 及 $t_f$ 固定。要求确定最优控制 $\pmb{u}^{*}(t)$ ，使性能指标(10-93)极小。

在今后讨论中, 若非特别指出, 以上假设始终满足。为了便于工程应用, 式(10-93)中的权阵 $F, Q(t)$ 和 $R(t)$ 多取为对角阵, 则其对称性自然满足。

在二次型指标(10-93)中,其各项都有明确的物理含意,可分述如下:

1）末值项 $\frac{1}{2}e^{\mathrm{T}}(t_{f})Fe(t_{f})$ 。若取 $F=\mathrm{diag}(f_{1},f_{2},\cdots,f_{l})$ ，则有

$$\frac {1}{2} \boldsymbol {e} ^ {\mathrm{T}} (t _ {f}) \boldsymbol {F e} (t _ {f}) = \frac {1}{2} \sum_ {i = 1} ^ {l} f _ {i} e _ {i} ^ {2} (t _ {f})$$

上式表明，末值项是末态跟踪误差向量 $e(t_f)$ 与希望的零向量之间的距离加权平方和。式中，系数1/2是为了便于运算， $e_i(t_f)$ 为 $e(t_f)$ 的变量。

由此可见，末值项的物理含意是表示在控制过程结束后，对系统末态跟踪误差的要求。

2）积分项 $\frac{1}{2}\int_{t_{0}}^{t_{f}}\boldsymbol{e}^{\mathrm{T}}(t)\boldsymbol{Q}(t)\boldsymbol{e}(t)\mathrm{d}t$ 。若取 $\boldsymbol{Q}(t)=\mathrm{diag}\left\{q_{1}(t),q_{2}(t),\cdots,q_{l}(t)\right\}$ ，则有

$$\frac {1}{2} \int_ {t _ {0}} ^ {t _ {f}} e ^ {\mathrm{T}} (t) Q (t) e (t) \mathrm{d} t = \frac {1}{2} \int_ {t _ {0}} ^ {t _ {f}} \sum_ {i = 1} ^ {l} q _ {i} (t) e _ {i} ^ {2} (t) \mathrm{d} t$$

上式表明,该积分项表示在系统控制过程中,对系统动态跟踪误差加权平方和的积分要求,是系统在控制过程中动态跟踪误差的总度量,几何上以面积大小表示。该积分项与末值项反映了系

统的控制效果。

3）积分项 $\frac{1}{2}\int_{t_{0}}^{t_{f}}\boldsymbol{u}^{\mathrm{T}}(t)\boldsymbol{R}(t)\boldsymbol{u}(t)\mathrm{d}t$ 。若取 $\boldsymbol{R}(t)=\mathrm{diag}\left\{r_{1}(t),r_{2}(t),\cdots,r_{m}(t)\right\}$ ，则有

$$\frac {1}{2} \int_ {t _ {0}} ^ {t _ {f}} \boldsymbol {u} ^ {\mathrm{T}} (t) \boldsymbol {R} (t) \boldsymbol {u} (t) \mathrm{d} t = \frac {1}{2} \int_ {t _ {0}} ^ {t _ {f}} \sum_ {i = 1} ^ {m} r _ {i} (t) u _ {i} ^ {2} (t) \mathrm{d} t$$

因为控制信号的大小往往正比于作用力或力矩,所以上式表明,该积分项定量地刻画了在整个控制过程中所消耗的控制能量。

上述分析表明,使二次型指标(10-93)极小的物理意义是:使系统在整个控制过程中的动态跟踪误差与控制能量消耗,以及控制过程结束时的末端跟踪偏差综合最优。

从性能指标的物理意义可知，式(10-93)中权矩阵 $F, Q(t)$ 和 $R(t)$ 都必须至少取为非负矩阵，不能取为负定矩阵，否则性能指标(10-93)的数学描述就会违背物理现实和最优控制问题的本质。至于要求权矩阵 $R(t)$ 正定，那是由于最优控制律的需要，以保证最优解的存在。

线性二次型最优控制问题有如下几种类型：
