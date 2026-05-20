# 15.1.1 VTOL 模型描述

利用机理分析法可建立 VTOL 动力学平衡方程为 $^{[1]}$

$$
\left. \begin{array}{l} \dot {x} _ {1} = x _ {2} \\ \dot {x} _ {2} = - u _ {1} \sin \theta + \varepsilon_ {0} u _ {2} \cos \theta + \Delta_ {1} (t) \\ \dot {y} _ {1} = y _ {2} \\ \dot {y} _ {2} = u _ {1} \cos \theta + \varepsilon_ {0} u _ {2} \sin \theta - g + \Delta_ {2} (t) \\ \dot {\theta} = \omega \\ \dot {\omega} = u _ {2} + \Delta_ {3} (t) \end{array} \right\} \tag {15.1}
$$

式中， $u_{1}$ 和 $u_{2}$ 为控制输入，即飞行器底部推力力矩和滚动力矩；g 为重力加速度； $\varepsilon_{0}$ 为描述 $u_{1}$ 和 $u_{2}$ 之间耦合关系的系数； $\Delta_{1}(t)$ 、 $\Delta_{2}(t)$ 和 $\Delta_{3}(t)$ 为外界干扰力矩。

不考虑耦合系数 $\varepsilon_{0}$ 和扰动 $\Delta_{1}(t)$ 、 $\Delta_{2}(t)$ 和 $\Delta_{3}(t)$ ，VTOL 动力学模型可简化为

$$
\left. \begin{array}{l} \dot {x} _ {1} = x _ {2} \\ \dot {x} _ {2} = - u _ {1} \sin \theta \\ \dot {y} _ {1} = y _ {2} \\ \dot {y} _ {2} = u _ {1} \cos \theta - g \\ \dot {\theta} = \omega \\ \dot {\omega} = u _ {2} \end{array} \right\} \tag {15.2}
$$

跟踪指令分别为 $x_{d}$ 和 $y_{d}$ ，则式（15.2）转化为跟踪子系统

$$
\left. \begin{array}{l} \dot {\tilde {x}} _ {1} = \tilde {x} _ {2} \\ \dot {\tilde {x}} _ {2} = - u _ {1} \sin \theta - \ddot {x} _ {\mathrm{d}} \\ \dot {\tilde {y}} _ {1} = \tilde {y} _ {2} \\ \dot {\tilde {y}} _ {2} = u _ {1} \cos \theta - g - \ddot {y} _ {\mathrm{d}} \\ \dot {\theta} = \omega \\ \dot {\omega} = u _ {2} \end{array} \right\} \tag {15.3}
$$

式中， $\tilde{x}_{1}=x_{1}-x_{d}$ ； $\tilde{x}_{2}=x_{2}-\dot{x}_{d}$ ； $\tilde{y}_{1}=y_{1}-y_{d}$ ； $\tilde{y}_{2}=y_{2}-\dot{y}_{d}$ 。

控制任务：通过设计控制律 $u_{1}$ 和 $u_{2}$ ，实现 $x_{1} \rightarrow x_{d}$ ， $x_{2} \rightarrow \dot{x}_{d}$ ， $y_{1} \rightarrow y_{d}$ ， $y_{2} \rightarrow \dot{y}_{d}$ ，从而实现 VTOL 飞行器的轨迹跟踪。

![](image/c8b19fd94ae4fcb41d2c64820b99e210a1a32a01f9d80a50dbb4a4391a98e6e0.jpg)
