# 14.4.2 位置控制律设计

首先通过设计位置控制律 $v$ ，实现 $x$ 跟踪 $x_{\mathrm{d}}$ ， $y$ 跟踪 $y_{\mathrm{d}}$ 。取理想轨迹为 $[x_{\mathrm{d}} y_{\mathrm{d}}]$ ，则误

差跟踪方程为

$$\dot {x} _ {\mathrm{e}} = v \cos \theta - \dot {x} _ {\mathrm{d}}, \quad \dot {y} _ {\mathrm{e}} = v \sin \theta - \dot {y} _ {\mathrm{d}} \tag {14.20}$$

其中 $x_{e}=x-x_{d}$ ， $y_{e}=y-y_{d}$ 。

取

$$v \cos \theta = u _ {1} \tag {14.21}v \sin \theta = u _ {2}$$

则针对 $\dot{x}_{e}=v\cos\theta-\dot{x}_{d}$ ，有 $\dot{x}_{e}=u_{1}-\dot{x}_{d}$ ，取 P+前馈控制设计控制器，即

$$u _ {1} = - k _ {\mathrm{pl}} x _ {\mathrm{e}} + \dot {x} _ {\mathrm{d}} \tag {14.22}$$

则

$$\dot {x} _ {\mathrm{e}} = - k _ {\mathrm{p1}} x _ {\mathrm{e}}$$

取 $k_{pl}>0$ ，则 $t\to\infty$ 时， $x_{e}\to0$ 。

针对 $\dot{y}_{e}=v\sin\theta-\dot{y}_{d}$ ，有 $\dot{y}_{e}=u_{2}-\dot{y}_{d}$ ，取 P+前馈控制设计控制器，即

$$u _ {2} = - k _ {\mathrm{p} 2} y _ {\mathrm{e}} + \dot {y} _ {\mathrm{d}} \tag {14.23}$$

则

$$\dot {y} _ {\mathrm{e}} = - k _ {\mathrm{p2}} y _ {\mathrm{e}}$$

取 $k_{p2}>0$ ，则 $t\to\infty$ 时， $y_{e}\to0$ 。

由式（14.21）可得 $\frac{u_2}{u_1} = \tan \theta$ ，如果 $\theta$ 的值域是 $(- \pi / 2, \pi / 2)$ ，则可得到满足理想轨迹跟踪的 $\theta$ 为

$$\theta = \arctan \frac {u _ {2}}{u _ {1}} \tag {14.24}$$

上式所求得的 $\theta$ 为位置控制律式（14.22）和式（14.23）所要求的角度，如果 $\theta$ 与 $\theta_{d}$ 相等，则理想的轨迹控制律式（14.22）和式（14.23）可实现，但实际模型式（14.19）中的 $\theta$ 与 $\theta_{d}$ 不可能完全一致，尤其是控制的初始阶段，这会造成闭环跟踪系统式（14.20）的不稳定。

为此，需要将式（14.24）求得的角度 $\theta$ 当成理想值，即取

$$\theta_ {\mathrm{d}} = \arctan \frac {u _ {2}}{u _ {1}} \tag {14.25}$$

设计理想的位姿指令 $\left[x_{d}\quad y_{d}\right]$ 时，需要使 $\theta_{d}$ 的值域满足 $(-π/2,π/2)$ 。

实际的 $\theta$ 与 $\theta_{d}$ 之间的差异会造成位置控制律式（14.22）和式（14.23）无法精确实现，从而造成闭环系统的不稳定。较简单的解决方法是通过设计比位置控制律收敛更快的姿态控制算法，使 $\theta$ 尽快跟踪 $\theta_{d}$ 。

由式（14.21），可得到实际的位置控制律为

$$v = \frac {u _ {1}}{\cos \theta_ {\mathrm{d}}} \tag {14.26}$$

![](image/bfdc507d17008f3ddf7a11441c52cafaf1b2e1f156247250a12c9c6eef09a456.jpg)
