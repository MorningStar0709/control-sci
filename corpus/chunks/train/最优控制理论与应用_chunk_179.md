# 10.4.1 微分对策的提法

给定动态系统

$$\dot {\boldsymbol {x}} = \boldsymbol {f} (\boldsymbol {x}, \boldsymbol {u}, \boldsymbol {v}, t), \quad \boldsymbol {x} (t _ {0}) = \boldsymbol {x} _ {0} \tag {10-19}$$

终端约束

$$\boldsymbol {G} \left[ \boldsymbol {x} \left(t _ {f}\right), t _ {f} \right] = \boldsymbol {0}$$

及指标函数(类似于前面的支付函数)

$$J = \Phi [ x (t _ {\mathrm{f}}), t _ {\mathrm{f}} ] + \int_ {t _ {0}} ^ {t _ {\mathrm{f}}} F (\boldsymbol {x}, \boldsymbol {u}, \boldsymbol {v}, t) \mathrm{d} t \tag {10-20}$$

对于甲方, 选 $\pmb{u} \in U$ , 使 $J$ 取最小可能的值; 对于乙方, 选 $\pmb{v} \in V$ , 以使 $J$ 取最大可能的值, 亦即寻求对策的最优解 $(\pmb{u}^{*}, \pmb{v}^{*})$ 使

$$J (\textbf {u} ^ {*}, \textbf {v}) \leqslant J (\textbf {u} ^ {*}, \textbf {v} ^ {*}) \leqslant J (\textbf {u}, \textbf {v} ^ {*}) \tag {10-21}$$

$(\pmb{u}^{*}, \pmb{v}^{*})$ 是 $J$ 的鞍点， $\pmb{u}^{*}$ 和 $\pmb{v}^{*}$ 分别称为甲、乙的最优策略， $J(\pmb{u}^{*}, \pmb{v}^{*})$ 称为（双方零和）最优微分对策值。

从微分对策问题的描述和最优策略的定义可以看出,微分对策问题和最优控制问题紧密相关,可以想像两者的处理方法也应该十分相似的。

下面将给出微分对策问题最优策略 $(u^{*}(t),v^{*}(t))$ 所应满足的必要条件,即双方极值原理;并将证明当哈密顿函数和性能指标函数可分解为两部分,一部分只与u有关,另一部分只与v有关时,则这个必要条件也就是充分条件。

定理 2 双方极值原理——最优策略的必要条件

引入哈密顿函数

$$H (\boldsymbol {x}, \boldsymbol {u}, \boldsymbol {v}, \boldsymbol {\lambda}, t) = F (\boldsymbol {x}, \boldsymbol {u}, \boldsymbol {v}, t) + \boldsymbol {\lambda} ^ {\mathrm{T}} f (\boldsymbol {x}, \boldsymbol {u}, \boldsymbol {v}, t) \tag {10-22}$$

和增广性能指标函数

$$J _ {a} = \boldsymbol {\Phi} [ x (t _ {\mathrm{f}}), t _ {\mathrm{f}} ] + \boldsymbol {v} ^ {\mathrm{T}} \boldsymbol {G} [ \boldsymbol {x} (t _ {\mathrm{f}}), t _ {\mathrm{f}} ] + \int_ {t _ {0}} ^ {t _ {\mathrm{f}}} \left\{F (\boldsymbol {x}, \boldsymbol {u}, \boldsymbol {v}, t) + \right.\boldsymbol {\lambda} ^ {\mathrm{T}} [ \boldsymbol {f} (\boldsymbol {x}, \boldsymbol {u}, \boldsymbol {v}, t) ] - \dot {\boldsymbol {x}} ] \} \mathrm{d} t \tag {10-23}$$

如果 $(\pmb{x}^{*}(t),\pmb{u}^{*}(t),\pmb{v}^{*}(t))$ 是双方零和微分对策问题(10-19)\~(10-20)的最优解，即 $(\pmb{u}^{*}(t),\pmb{v}^{*}(t))$ 为鞍点，则 $x^{*}(t), u^{*}(t), v^{*}(t), \lambda(t)$ ， $\pmb{v}$ 一起满足
