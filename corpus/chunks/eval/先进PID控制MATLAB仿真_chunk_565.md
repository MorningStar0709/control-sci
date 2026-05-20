# 14.3.3 控制器的设计

设 $\boldsymbol{x}_{\mathrm{d}}(t)$ 是在工作空间中的理想轨迹，则 $\dot{\boldsymbol{x}}_{\mathrm{d}}(t)$ 和 $\ddot{\boldsymbol{x}}_{\mathrm{d}}(t)$ 分别是理想的速度和加速度。定义

$$\boldsymbol {e} (t) = \boldsymbol {x} _ {\mathrm{d}} (t) - \boldsymbol {x} (t)$$

采用基于前馈补偿和阻力补偿的 PD 控制方法，控制律设计为

$$\boldsymbol {F} _ {x} = \boldsymbol {D} _ {x} (\boldsymbol {q}) \ddot {\boldsymbol {x}} _ {\mathrm{d}} + \boldsymbol {C} _ {x} (\boldsymbol {q}, \dot {\boldsymbol {q}}) \dot {\boldsymbol {x}} _ {\mathrm{d}} + \boldsymbol {G} _ {x} (\boldsymbol {q}) + \boldsymbol {F} _ {\mathrm{e}} + \boldsymbol {K} _ {\mathrm{p}} \boldsymbol {e} + \boldsymbol {K} _ {\mathrm{d}} \dot {\boldsymbol {e}} \tag {14.17}$$

式中， $K_{p}>0;\quad K_{d}>0$ 。

将控制律式（14.17）代入式（14.15），得

$$\boldsymbol {D} _ {x} (\boldsymbol {q}) \ddot {\boldsymbol {x}} + \boldsymbol {C} _ {x} (\boldsymbol {q}, \dot {\boldsymbol {q}}) \dot {\boldsymbol {x}} + \boldsymbol {G} _ {x} (\boldsymbol {q}) + \boldsymbol {F} _ {\mathrm{e}} = \boldsymbol {D} _ {x} (\boldsymbol {q}) \ddot {\boldsymbol {x}} _ {\mathrm{d}} + \boldsymbol {C} _ {x} (\boldsymbol {q}, \dot {\boldsymbol {q}}) \dot {\boldsymbol {x}} _ {\mathrm{d}} + \boldsymbol {G} _ {x} (\boldsymbol {q}) + \boldsymbol {F} _ {\mathrm{e}} + \boldsymbol {K} _ {\mathrm{p}} \boldsymbol {e} + \boldsymbol {K} _ {\mathrm{d}} \dot {\boldsymbol {e}}$$

则

$$\boldsymbol {D} _ {x} (\boldsymbol {q}) \ddot {\boldsymbol {e}} + \boldsymbol {C} _ {x} (\boldsymbol {q}, \dot {\boldsymbol {q}}) \dot {\boldsymbol {e}} + \boldsymbol {K} _ {\mathrm{p}} \boldsymbol {e} = - \boldsymbol {K} _ {\mathrm{d}} \dot {\boldsymbol {e}}$$

即

$$\boldsymbol {D} _ {x} (\boldsymbol {q}) \ddot {\boldsymbol {e}} + \left(\boldsymbol {C} _ {x} (\boldsymbol {q}, \dot {\boldsymbol {q}}) + \boldsymbol {K} _ {\mathrm{d}}\right) \dot {\boldsymbol {e}} + \boldsymbol {K} _ {\mathrm{p}} \boldsymbol {e} = 0$$

控制目标为 $e\to0$ 和 $\dot{e}\to0$ 。

稳定性分析如下：取 Lyapunov 函数为

$$V = \frac {1}{2} \dot {\boldsymbol {e}} ^ {\mathrm{T}} \boldsymbol {D} _ {x} (\boldsymbol {q}) \dot {\boldsymbol {e}} + \frac {1}{2} \boldsymbol {e} ^ {\mathrm{T}} \boldsymbol {K} _ {\mathrm{p}} \boldsymbol {e}$$

由 $D_{x}(q)$ 及 $K_{\mathrm{p}}$ 的正定性知， $V$ 是全局正定的，则
