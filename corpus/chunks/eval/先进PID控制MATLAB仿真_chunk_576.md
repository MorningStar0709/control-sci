# 14.4.3 姿态控制律设计

下面的任务是通过设计姿态控制律 $\omega$ ，实现角度 $\theta$ 跟踪 $\theta_{d}$ 。

取 $\theta_{e}=\theta-\theta_{d}$ ，则 $\dot{\theta}_{e}=\omega-\dot{\theta}_{d}$ ，取 P+前馈控制设计控制器，即

$$\omega = - k _ {\mathrm{p3}} \theta_ {\mathrm{e}} + \dot {\theta} _ {\mathrm{d}} \tag {14.27}$$

则

$$\dot {\theta} _ {\mathrm{e}} = - k _ {\mathrm{p3}} \theta_ {\mathrm{e}}$$

取 $k_{p3}>0$ ，则 $t\to\infty$ 时， $\theta_{e}\to0$ 。

![](image/1798247819a93eb42e17cf3dcd213af509cb27e34df64df8b2a83f3d3b614383.jpg)
