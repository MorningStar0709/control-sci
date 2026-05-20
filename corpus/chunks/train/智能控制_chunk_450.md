# 2. 稳定性分析

参考文献[21], 下面给出控制系统的稳定性分析。

定义 Lyapunov 函数

$$L = \frac {1}{2} \boldsymbol {r} ^ {\mathrm{T}} \boldsymbol {D r} + \frac {1}{2} \operatorname{tr} (\tilde {\boldsymbol {W}} ^ {\mathrm{T}} \boldsymbol {F} _ {\mathrm{w}} ^ {- 1} \tilde {\boldsymbol {W}})$$

其中，D 和 $F_{w}$ 为正定阵。则

$$\dot {L} = \boldsymbol {r} ^ {\mathrm{T}} \boldsymbol {D} \dot {\boldsymbol {r}} + \frac {1}{2} \boldsymbol {r} ^ {\mathrm{T}} \dot {\boldsymbol {D}} \boldsymbol {r} + \operatorname{tr} (\tilde {\boldsymbol {W}} ^ {\mathrm{T}} \boldsymbol {F} _ {\mathrm{w}} ^ {- 1} \dot {\tilde {\boldsymbol {W}}})$$

将式 $(9.71)$ 代入上式,得

$$\dot {L} = - \boldsymbol {r} ^ {\mathrm{T}} \boldsymbol {K} _ {\mathrm{v}} \boldsymbol {r} + \frac {1}{2} \boldsymbol {r} ^ {\mathrm{T}} (\dot {\boldsymbol {D}} - 2 \boldsymbol {C}) \boldsymbol {r} + \operatorname{tr} \tilde {\boldsymbol {W}} ^ {\mathrm{T}} \left(\boldsymbol {F} _ {\mathrm{w}} ^ {- 1} \dot {\tilde {\boldsymbol {W}}} + \boldsymbol {\varphi r} ^ {\mathrm{T}}\right) + \boldsymbol {r} ^ {\mathrm{T}} (\boldsymbol {\varepsilon} + \tau_ {\mathrm{d}} + \nu)$$

根据机器人物理特性有 $\boldsymbol{r}^{\mathrm{T}}(\dot{\boldsymbol{D}}-2\boldsymbol{C})\boldsymbol{r}=0$ 。取 $\tilde{W}=-F_{w}\varphi r^{T}$ ，即神经网络自适应律为

$$\dot {\hat {W}} = F _ {\mathrm{w}} \boldsymbol {\varphi} \mathbf {r} ^ {\mathrm{T}} \tag {9.73}$$

则

$$\dot {L} = - \boldsymbol {r} ^ {\mathrm{T}} \boldsymbol {K} _ {\mathrm{v}} \boldsymbol {r} + \boldsymbol {r} ^ {\mathrm{T}} (\boldsymbol {\varepsilon} + \boldsymbol {\tau} _ {\mathrm{d}} + \boldsymbol {v})$$

由于

$$\boldsymbol {r} ^ {\mathrm{T}} (\boldsymbol {\varepsilon} + \boldsymbol {\tau} _ {\mathrm{d}} + \boldsymbol {v}) = \boldsymbol {r} ^ {\mathrm{T}} (\boldsymbol {\varepsilon} + \boldsymbol {\tau} _ {\mathrm{d}}) + \boldsymbol {r} ^ {\mathrm{T}} \boldsymbol {v} = \boldsymbol {r} ^ {\mathrm{T}} (\boldsymbol {\varepsilon} + \boldsymbol {\tau} _ {\mathrm{d}}) - \| \boldsymbol {r} \| (\boldsymbol {\varepsilon} _ {\mathrm{N}} + \boldsymbol {b} _ {\mathrm{d}}) \leqslant 0$$

则 $\dot{L} = -r^{\mathrm{T}}K_{\mathrm{v}}r + r^{\mathrm{T}}(\pmb {\varepsilon} + \pmb{\tau}_{\mathrm{d}} + \pmb {v})\leqslant 0$

由于当且仅当 r=0 时， $\dot{V}=0$ ，即当 $\dot{V}\equiv0$ 时， $r\equiv0$ 。根据 LaSalle 不变性原理 $^{[35]}$ ，闭环系统

为渐近稳定，即当 $t \to \infty$ 时， $r \to 0$ ，系统的收敛速度取决于 $K_{\mathrm{v}}$ 。

由于 $L \geqslant 0, \dot{L} \leqslant 0$ ，则当 $t \to \infty$ 时， $L$ 有界，从而 $\widetilde{W}$ 有界。
