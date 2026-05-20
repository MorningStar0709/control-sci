# 14.1.1 控制律设计

当忽略重力和外加干扰时，采用独立的 PD 控制，能满足机械手定点控制的要求 $^{[1]}$ 。

设 $n$ 关节机械手方程为

$$D (\boldsymbol {q}) \ddot {\boldsymbol {q}} + C (\boldsymbol {q}, \dot {\boldsymbol {q}}) \dot {\boldsymbol {q}} = \tau \tag {14.1}$$

式中， $D(q)$ 为 $n \times n$ 阶正定惯性矩阵； $C(q, \dot{q})$ 为 $n \times n$ 阶离心和哥氏力项。

独立的 PD 控制律为

$$\pmb {\tau} = \pmb {K} _ {\mathrm{d}} \dot {\pmb {e}} + \pmb {K} _ {\mathrm{p}} \pmb {e} \tag {14.2}$$

取跟踪误差为 $e = q_{\mathrm{d}} - q$ ，采用定点控制时， $q_{\mathrm{d}}$ 为常值，则 $\dot{q}_{\mathrm{d}} = \ddot{q}_{\mathrm{d}} = 0$ 。

此时，机械手方程为

$$\boldsymbol {D} (\boldsymbol {q}) \left(\ddot {\boldsymbol {q}} _ {\mathrm{d}} - \ddot {\boldsymbol {q}}\right) + \boldsymbol {C} (\boldsymbol {q}, \dot {\boldsymbol {q}}) \left(\dot {\boldsymbol {q}} _ {\mathrm{d}} - \dot {\boldsymbol {q}}\right) + \boldsymbol {K} _ {\mathrm{d}} \dot {\boldsymbol {e}} + \boldsymbol {K} _ {\mathrm{p}} \boldsymbol {e} = 0$$

亦即

$$\boldsymbol {D} (\boldsymbol {q}) \ddot {\boldsymbol {e}} + \boldsymbol {C} (\boldsymbol {q}, \dot {\boldsymbol {q}}) \dot {\boldsymbol {e}} + \boldsymbol {K} _ {\mathrm{p}} \boldsymbol {e} = - \boldsymbol {K} _ {\mathrm{d}} \dot {\boldsymbol {e}} \tag {14.3}$$

取 Lyapunov 函数为

$$V = \frac {1}{2} \dot {\boldsymbol {e}} ^ {\mathrm{T}} \boldsymbol {D} (\boldsymbol {q}) \dot {\boldsymbol {e}} + \frac {1}{2} \boldsymbol {e} ^ {\mathrm{T}} \boldsymbol {K} _ {\mathrm{p}} \boldsymbol {e}$$

由 $D(q)$ 及 $K_{\mathrm{p}}$ 的正定性知， $V$ 是全局正定的，则

$$\dot {V} = \dot {\boldsymbol {e}} ^ {\mathrm{T}} \boldsymbol {D} \ddot {\boldsymbol {e}} + \frac {1}{2} \dot {\boldsymbol {e}} ^ {\mathrm{T}} \dot {\boldsymbol {D}} \dot {\boldsymbol {e}} + \dot {\boldsymbol {e}} ^ {\mathrm{T}} \boldsymbol {K} _ {\mathrm{p}} \boldsymbol {e}$$

利用 $\dot{D}-2C$ 的斜对称性知 $\dot{e}^{T}\dot{D}\dot{e}=2\dot{e}^{T}C\dot{e}$ ，则

$$\dot {V} = \dot {\boldsymbol {e}} ^ {\mathrm{T}} \boldsymbol {D} \ddot {\boldsymbol {e}} + \dot {\boldsymbol {e}} ^ {\mathrm{T}} \boldsymbol {C} \dot {\boldsymbol {e}} + \dot {\boldsymbol {e}} ^ {\mathrm{T}} \boldsymbol {K} _ {\mathrm{p}} \boldsymbol {e} = \dot {\boldsymbol {e}} ^ {\mathrm{T}} (\boldsymbol {D} \ddot {\boldsymbol {e}} + \boldsymbol {C} \dot {\boldsymbol {e}} + \boldsymbol {K} _ {\mathrm{p}} \boldsymbol {e}) = - \dot {\boldsymbol {e}} ^ {\mathrm{T}} \boldsymbol {K} _ {\mathrm{d}} \dot {\boldsymbol {e}} \leqslant 0$$

![](image/543b0f2c6b36b8d84f7a42a9ecc87c9d58ce97ee02bde3e3f63ceb1ae9669454.jpg)
