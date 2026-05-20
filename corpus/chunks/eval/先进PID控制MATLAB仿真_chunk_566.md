$$\dot {V} = \dot {\boldsymbol {e}} ^ {\mathrm{T}} \boldsymbol {D} _ {x} \ddot {\boldsymbol {e}} + \frac {1}{2} \dot {\boldsymbol {e}} ^ {\mathrm{T}} \dot {\boldsymbol {D}} _ {x} \dot {\boldsymbol {e}} + \dot {\boldsymbol {e}} ^ {\mathrm{T}} \boldsymbol {K} _ {\mathrm{p}} \boldsymbol {e}$$

利用 $\dot{D}_{x}-2C_{x}$ 的斜对称性知 $\dot{e}^{T}\dot{D}_{x}\dot{e}=2\dot{e}^{T}C_{x}\dot{e}$ ，则

$$\dot {V} = \dot {\boldsymbol {e}} ^ {\mathrm{T}} \boldsymbol {D} _ {x} \ddot {\boldsymbol {e}} + \dot {\boldsymbol {e}} ^ {\mathrm{T}} \boldsymbol {C} _ {x} \dot {\boldsymbol {e}} + \dot {\boldsymbol {e}} ^ {\mathrm{T}} \boldsymbol {K} _ {\mathrm{p}} \boldsymbol {e} = \dot {\boldsymbol {e}} ^ {\mathrm{T}} \left(\boldsymbol {D} _ {x} \ddot {\boldsymbol {e}} + \boldsymbol {C} _ {x} \dot {\boldsymbol {e}} + \boldsymbol {K} _ {\mathrm{p}} \boldsymbol {e}\right) = - \dot {\boldsymbol {e}} ^ {\mathrm{T}} \boldsymbol {K} _ {\mathrm{d}} \dot {\boldsymbol {e}} \leqslant 0$$

由于 $\dot{V}$ 是半负定的，且 $K_{\mathrm{d}}$ 为正定，则当 $\dot{V} \equiv 0$ 时，有 $\dot{e} \equiv 0$ ，从而 $\ddot{e} \equiv 0$ 。代入式（14.6）中，有 $K_{\mathrm{p}} e \equiv 0$ ，再由 $K_{\mathrm{p}}$ 的可逆性知 $e \equiv 0$ 。由LaSalle定理[2]知， $(e, \dot{e}) = (0, 0)$ 是受控机械手全局渐进稳定的平衡点，即从任意初始条件 $(x_{0}, \dot{x}_{0})$ 出发，均有 $t \to \infty$ 时， $x \to x_{\mathrm{d}}$ ， $\dot{x} \to \dot{x}_{\mathrm{d}}$ 。

![](image/40a382ea31db37833fe3bd22782f7786caa8e1b76693ec3469e566fe5be78dc3.jpg)
