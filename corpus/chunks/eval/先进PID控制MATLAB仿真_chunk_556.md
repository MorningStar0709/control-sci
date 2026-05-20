# 14.2.3 PD 控制器的设计

设 $\boldsymbol{x}_{\mathrm{d}}(t)$ 是在工作空间中的理想轨迹，则 $\dot{\boldsymbol{x}}_{\mathrm{d}}(t)$ 和 $\ddot{\boldsymbol{x}}_{\mathrm{d}}(t)$ 分别是理想的速度和加速度。定义

$$\boldsymbol {e} (t) = \boldsymbol {x} _ {\mathrm{d}} (t) - \boldsymbol {x} (t)\dot {\boldsymbol {e}} (t) = \dot {\boldsymbol {x}} _ {\mathrm{d}} (t) - \dot {\boldsymbol {x}} (t)$$

采用前馈控制及 PD 反馈控制相结合的形式设计控制律：

$$\boldsymbol {F} _ {x} = \boldsymbol {K} _ {\mathrm{p}} \boldsymbol {e} + \boldsymbol {K} _ {\mathrm{d}} \dot {\boldsymbol {e}} + \boldsymbol {D} _ {x} (\boldsymbol {q}) \ddot {\boldsymbol {x}} _ {\mathrm{d}} + \boldsymbol {C} _ {x} (\boldsymbol {q}, \dot {\boldsymbol {q}}) \dot {\boldsymbol {x}} _ {\mathrm{d}} + \boldsymbol {G} _ {x} (\boldsymbol {q}) \tag {14.11}$$

式中， $K_{p}>0;\quad K_{d}>0$ 。

此时，式（14.10）可写为

$$D _ {x} (\boldsymbol {q}) (\ddot {\boldsymbol {x}} _ {\mathrm{d}} - \ddot {\boldsymbol {x}}) + C _ {x} (\boldsymbol {q}, \dot {\boldsymbol {q}}) (\dot {\boldsymbol {x}} _ {\mathrm{d}} - \dot {\boldsymbol {x}}) + K _ {\mathrm{d}} \dot {\boldsymbol {e}} + K _ {\mathrm{p}} \boldsymbol {e} = 0$$

亦即

$$\boldsymbol {D} _ {x} (\boldsymbol {q}) \ddot {\boldsymbol {e}} + \boldsymbol {C} _ {x} (\boldsymbol {q}, \dot {\boldsymbol {q}}) \dot {\boldsymbol {e}} + \boldsymbol {K} _ {\mathrm{p}} \boldsymbol {e} = - \boldsymbol {K} _ {\mathrm{d}} \dot {\boldsymbol {e}} \tag {14.12}$$

即

$$\boldsymbol {D} _ {x} (\boldsymbol {q}) \ddot {\boldsymbol {e}} + \left(\boldsymbol {C} _ {x} (\boldsymbol {q}, \dot {\boldsymbol {q}}) + \boldsymbol {K} _ {\mathrm{d}}\right) \dot {\boldsymbol {e}} + \boldsymbol {K} _ {\mathrm{p}} \boldsymbol {e} = 0$$

控制目标为 $e\to0$ 和 $\dot{e}\to0$ 。

取 Lyapunov 函数为

$$V = \frac {1}{2} \dot {\boldsymbol {e}} ^ {\mathrm{T}} \boldsymbol {D} _ {x} (\boldsymbol {q}) \dot {\boldsymbol {e}} + \frac {1}{2} \boldsymbol {e} ^ {\mathrm{T}} \boldsymbol {K} _ {\mathrm{p}} \boldsymbol {e}$$

由 $D_{x}(\pmb{q})$ 及 $\pmb{K}_{\mathrm{p}}$ 的正定性知， $V$ 是全局正定的，则

$$\dot {V} = \dot {\boldsymbol {e}} ^ {\mathrm{T}} \boldsymbol {D} _ {x} \ddot {\boldsymbol {e}} + \frac {1}{2} \dot {\boldsymbol {e}} ^ {\mathrm{T}} \dot {\boldsymbol {D}} _ {x} \dot {\boldsymbol {e}} + \dot {\boldsymbol {e}} ^ {\mathrm{T}} \boldsymbol {K} _ {\mathrm{p}} \boldsymbol {e}$$

利用 $\dot{D}_{x}-2C_{x}$ 的斜对称性知 $\dot{e}^{T}\dot{D}_{x}\dot{e}=2\dot{e}^{T}C_{x}\dot{e}$ ，则
