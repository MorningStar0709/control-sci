# 10.4.2 最优策略的充分条件

当状态方程和性能指标可分解为一部分仅与策略 u 有关, 另一部分仅与策略 v 有关, 则可证明式(10-24)\~(10-27)所示的最优策略的必要条件也是充分条件, 也就是可满足指标鞍点条件式(10-21)。

定理3 设状态方程为

$$\dot {\boldsymbol {x}} = \boldsymbol {A} (t) \boldsymbol {x} + f _ {1} (\boldsymbol {u}, t) + f _ {2} (\boldsymbol {v}, t) \tag {10-57}$$

性能指标为

$$J [ \boldsymbol {u}, \boldsymbol {v} ] = \boldsymbol {c} ^ {\mathrm{T}} \boldsymbol {x} (t _ {\mathrm{f}}) + \int_ {t _ {0}} ^ {t _ {\mathrm{f}}} [ \boldsymbol {p} ^ {\mathrm{T}} (t) \boldsymbol {x} (t) +\left. L _ {1} (\boldsymbol {u} (t), t) + L _ {2} (\boldsymbol {v} (t), t) \right] \mathrm{d} t \tag {10-58}$$

其中 $A(t) \in \mathbf{R}^{n \times n}, p^{\mathrm{T}}(t) \in \mathbf{R}^{n}$ 对 $t$ 连续。 $c \in \mathbf{R}^{n}$ 是常向量， $t_{\mathrm{f}}$ 固定。 $f_{1}(u, t) \in \mathbf{R}^{n}, f_{2}(v, t) \in \mathbf{R}^{n}, L_{1}(u, t) \in \mathbf{R}^{1}, L_{2}(v, t) \in \mathbf{R}^{1}$ 关于变元 $u, v$ 都是连续的，而关于 $t$ 都是连续可微的。相应于 $(u^{*}, v^{*})$ 的轨迹为 $x^{*}$ ，它们满足

$$\dot {\boldsymbol {x}} ^ {*} (t) = \boldsymbol {A} (t) \boldsymbol {x} ^ {*} (t) + f _ {1} (\boldsymbol {u} ^ {*}, t) + f _ {2} (\boldsymbol {v} ^ {*}, t), \boldsymbol {x} ^ {*} (t _ {0}) = \boldsymbol {x} _ {0} \tag {10-59}$$

哈密顿函数为

$$H (\boldsymbol {x}, \boldsymbol {u}, \boldsymbol {v}, \boldsymbol {\lambda}, t) = \boldsymbol {p} ^ {\mathrm{T}} (t) \boldsymbol {x} (t) + L _ {1} (\boldsymbol {u}, t) + L _ {2} (\boldsymbol {v}, t) +\boldsymbol {\lambda} ^ {T} (t) [ \boldsymbol {A} (t) \boldsymbol {x} + f _ {1} (\boldsymbol {u}, t) + f _ {2} (\boldsymbol {v}, t) ] \tag {10-60}$$

若 $x^{*}, u^{*}, v^{*}, \lambda$ 一起满足条件式(10-24)\~(10-27)，将条件式(10-26)写成

$$H \left(\boldsymbol {x} ^ {*}, \boldsymbol {u} ^ {*}, \boldsymbol {v}, \boldsymbol {\lambda}, t\right) \leqslant H \left(\boldsymbol {x} ^ {*}, \boldsymbol {u} ^ {*}, \boldsymbol {v} ^ {*}, \boldsymbol {\lambda}, t\right) \leqslant H \left(\boldsymbol {x} ^ {*}, \boldsymbol {u}, \boldsymbol {v} ^ {*}, \boldsymbol {\lambda}, t\right) \tag {10-61}$$

则 $(u^{*},v^{*})$ 必是对策的最优策略。

证明 任取 $\pmb{u} \in U$ , 记状态方程 (10-57) 相对于 $(\pmb{u}, \pmb{v}^{*})$ 的解为 $\pmb{x}(t)$ , 它满足

$$\dot {\boldsymbol {x}} (t) = \boldsymbol {A} (t) \boldsymbol {x} (t) + f _ {1} (\boldsymbol {u}, t) + f _ {2} (\boldsymbol {v} ^ {*}, t), \boldsymbol {x} (t _ {0}) = \boldsymbol {x} _ {0} \tag {10-62}$$

注意到由式(10-60)可得
