证明 引入拉格朗日乘子 $\lambda(t) \in R^n$ 和 $\gamma \in R^r$ ，构造等价末值型性能指标

$$\widetilde {J} (\boldsymbol {u}) = \bar {\varphi} [ \boldsymbol {x} (t _ {f}), t _ {f} ] = \varphi [ \boldsymbol {x} (t _ {f}), t _ {f} ] + \boldsymbol {\gamma} ^ {\mathrm{T}} \boldsymbol {\psi} [ \boldsymbol {x} (t _ {f}), t _ {f} ]$$

则最优控制问题等同于定理10-9。

根据定理10-9，横截条件为

$$\boldsymbol {\lambda} (t _ {f}) = \frac {\partial \bar {\varphi}}{\partial \boldsymbol {x} (t _ {f})} = \frac {\partial \varphi}{\partial \boldsymbol {x} (t _ {f})} + \frac {\partial \boldsymbol {\psi} ^ {\mathrm{T}}}{\partial \boldsymbol {x} (t _ {f})} \boldsymbol {\gamma}$$

沿最优轨线哈密顿函数变化律为

$$H \left[ \boldsymbol {x} ^ {*} \left(t _ {f} ^ {*}\right), \boldsymbol {u} ^ {*} \left(t _ {f} ^ {*}\right), \lambda \left(t _ {f} ^ {*}\right), t _ {f} ^ {*} \right] = - \frac {\partial \bar {\varphi}}{\partial t _ {f}} = - \frac {\partial \varphi}{\partial t _ {f}} - \boldsymbol {\gamma} ^ {\mathrm{T}} \frac {\partial \boldsymbol {\psi}}{\partial t _ {f}}$$

最优解必要条件中其余的结论与 $\tilde{\varphi} [x(t_f),t_f]$ 无关，等同于定理10-9。于是，本定理得证。

利用扩充变量法, 还可以导出其他各种情况下的极小值原理形式。表 10-3 分别给出了各种具体最优控制问题的极小值原理结论, 以供查阅。

表 10-3 连续系统极小值原理的必要条件
