# 13.4 柔性机械臂分布式参数边界控制

为了在实现 $\theta \rightarrow \theta_{d}$ ， $\dot{\theta} \rightarrow \dot{\theta}_{d}$ 的基础上，同时实现整个机械臂振动的抑制，即实现 $y(x) \rightarrow 0$ 和 $\dot{y}(x) \rightarrow 0$ ，需要在末端加上边界控制输入 F，在机械臂的末端进行控制，以调节机械臂的振动。通过设计 Lyapunov 函数来设计 PD 边界控制律。

![](image/a24814b95191df7105de46d2f1f139b32971cc97dc338065a723ea93305d1c66.jpg)
