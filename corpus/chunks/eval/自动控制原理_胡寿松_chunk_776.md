$$\left. \left(\frac {\partial L}{\partial \dot {\boldsymbol {x}}}\right) ^ {T} \right| _ {t _ {f}} \delta \boldsymbol {x} _ {f} + \left[ L \left(\boldsymbol {x} ^ {*}, \dot {\boldsymbol {x}} ^ {*}, t\right) - \dot {\boldsymbol {x}} ^ {T} (t) \frac {\partial L}{\partial \dot {\boldsymbol {x}}} \right] \Bigg | _ {t _ {f}} \delta t _ {f} = 0\boldsymbol {x} \left(t _ {0}\right) = \boldsymbol {x} _ {0} \tag {10-37}$$

因为 $\delta x_{f}$ 和 $\delta t_f$ 均任意，故 $t_f$ 自由、 $x(t_f)$ 自由时的横截条件和边界条件为

$$\boldsymbol {x} \left(t _ {0}\right) = \boldsymbol {x} _ {0}\left. \left(\frac {\partial L}{\partial \dot {\boldsymbol {x}}}\right) \right| _ {t _ {f}} = \mathbf {0} \tag {10-38}\left. \left[ L \left(\boldsymbol {x} ^ {*}, \dot {\boldsymbol {x}} ^ {*}, t\right) - \dot {\boldsymbol {x}} ^ {\mathrm{T}} \frac {\partial L}{\partial \dot {\boldsymbol {x}}} \right] \right| _ {t _ {f}} = 0$$

2）末端受约束时的横截条件。设末端约束方程为

$$\boldsymbol {x} (t _ {f}) = \boldsymbol {c} (t _ {f})$$

此时， $\delta x_{f}$ 不能任意。由式(10-27)知

$$\delta \boldsymbol {x} _ {f} = \dot {\boldsymbol {c}} (t _ {f}) \delta t _ {f}$$

将上式代入式(10-37)，整理得

$$\boldsymbol {x} \left(t _ {0}\right) = \boldsymbol {x} _ {0}\left. \left[ L \left(\boldsymbol {x} ^ {*}, \dot {\boldsymbol {x}} ^ {*}, t\right) + (\dot {\boldsymbol {c}} - \dot {\boldsymbol {x}}) ^ {\mathrm{T}} \frac {\partial L}{\partial \dot {\boldsymbol {x}}} \right] \right| _ {t _ {f}} \delta t _ {f} = 0$$

因为 $\delta t_{f}$ 任意，故 $t_f$ 自由、 $\pmb{x}(t_f)$ 受约束时的横截条件和边界条件为

$$\boldsymbol {x} \left(t _ {0}\right) = \boldsymbol {x} _ {0}\boldsymbol {x} \left(t _ {f}\right) = \boldsymbol {c} \left(t _ {f}\right) \tag {10-39}\left. \left[ L \left(\boldsymbol {x} ^ {*}, \dot {\boldsymbol {x}} ^ {*}, t\right) + (\dot {\boldsymbol {c}} - \dot {\boldsymbol {x}}) ^ {\mathrm{T}} \frac {\partial L}{\partial \dot {\boldsymbol {x}}} \right] \right| _ {t _ {f}} = 0$$

在初始时刻 $t_{0}$ 及初始状态 $x(t_{0})=x_{0}$ 固定的情况下，不同末端时刻和不同末端边界所对应的横截条件与边界条件，如表 10-1 所示。

表 10-1 不同边界情况下的横截条件

<table><tr><td colspan="2">J[x]=∫t0fL(x, x̂, t) dt</td><td>横截条件与边界条件</td></tr><tr><td>tf固定</td><td>x(tf)固定</td><td>x(tf)=x0, x(tf)=xf</td></tr><tr><td>(x(tf)固定)</td><td>x(tf)自由</td><td>x(tf)=x0, ∂L/∂x|tf=0</td></tr><tr><td>tf自由</td><td>x(tf)自由</td><td>x(tf)=x0, ∂L/∂x|tf=0</td></tr><tr><td>(x(tf)固定)</td><td>x(tf)约束</td><td>x(tf)=x0, x(tf)=c(tf)</td></tr></table>

例10-4 设性能指标泛函
