$$H _ {2} \left(\boldsymbol {x}, \boldsymbol {u} ^ {*}, \boldsymbol {v}, \boldsymbol {\lambda} _ {2}, t\right) = F \left(\boldsymbol {x}, \boldsymbol {u} ^ {*}, \boldsymbol {v}, t\right) + \boldsymbol {\lambda} _ {2} ^ {\mathrm{T}} \boldsymbol {f} \left(\boldsymbol {x}, \boldsymbol {u} ^ {*}, \boldsymbol {v}, t\right) \tag {10-40}$$

于是 $J$ 取极大值的必要条件是： $x^{*}, v^{*}, \lambda_{2}$ 和 $t_{\mathrm{f}}$ 满足

① 正则方程

$$\dot {\lambda} _ {2} = - \frac {\partial H _ {2}}{\partial x} \tag {10-41}\dot {x} = \frac {\partial H _ {2}}{\partial \lambda_ {2}}$$

② 边界条件

$$\boldsymbol {x} \left(t _ {0}\right) = \boldsymbol {x} _ {0}, \quad \boldsymbol {G} \left[ \boldsymbol {x} \left(t _ {\mathrm{f}}\right), t _ {\mathrm{f}} \right] = \mathbf {0} \tag {10-42}$$

③ 横截条件

$$\boldsymbol {\lambda} _ {2} \left(t _ {\mathrm{f}}\right) = \frac {\partial \boldsymbol {\Phi}}{\partial \boldsymbol {x} \left(t _ {\mathrm{f}}\right)} + \frac {\partial \boldsymbol {G} ^ {\mathrm{T}}}{\partial \boldsymbol {x} \left(t _ {\mathrm{f}}\right)} \boldsymbol {v} \tag {10-43}$$

④ 最优终端时刻条件

$$H _ {2} \left(t _ {\mathrm{f}}\right) = - \frac {\partial \boldsymbol {\Phi}}{\partial t _ {\mathrm{f}}} - \frac {\partial \boldsymbol {G} ^ {\mathrm{T}}}{\partial t _ {\mathrm{f}}} \boldsymbol {v} \tag {10-44}$$

⑤ 在最优轨线 $\boldsymbol{x}^{*}(t)$ 和最优控制 $\boldsymbol{v}^{*}(t)$ 上，哈密顿函数取极大值

$$\max _ {\boldsymbol {v} \in V} H _ {2} \left(\boldsymbol {x} ^ {*}, \boldsymbol {u} ^ {*}, \boldsymbol {v}, \boldsymbol {\lambda} _ {2}, t\right) = H _ {2} \left(\boldsymbol {x} ^ {*}, \boldsymbol {u} ^ {*}, \boldsymbol {v} ^ {*}, \boldsymbol {\lambda} _ {2}, t\right) \tag {10-45}$$

3）双方极值(极大极小)原理

由 $(10-19)$ 、 $(10-20)$ 描述的微分对策问题的哈密顿函数为

$$H (\boldsymbol {x}, \boldsymbol {u}, \boldsymbol {v}, \boldsymbol {\lambda}, t) = F (\boldsymbol {x}, \boldsymbol {u}, \boldsymbol {v}, \boldsymbol {\lambda}, t) + \boldsymbol {\lambda} ^ {\mathrm{T}} \boldsymbol {f} (\boldsymbol {x}, \boldsymbol {u}, \boldsymbol {v}, \boldsymbol {\lambda}, t) \tag {10-46}$$

考察前面极大和极小控制的拉格朗日变量 $\lambda_{1}$ 和 $\lambda_{2}$ 所满足的方程式 (10-32) 和 (10-41)，有
