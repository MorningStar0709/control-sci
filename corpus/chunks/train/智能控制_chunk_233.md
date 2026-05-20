# 1. 基于两条模糊规则的设计

根据倒立摆模型可知，当 $x_{1}\rightarrow 0$ 时， $\sin x_1\to x_1,\cos x_1\to 1;x_1\to \pm \frac{\pi}{2}$ 时， $\sin x_1\to \pm 1\to \frac{2}{\pi} x_1$ 由此可得以下两条T-S模糊规则。

规则 1: IF $x_{1}(t)$ is about 0, THEN $\dot{\boldsymbol{x}}(t)=\boldsymbol{A}_{1}\boldsymbol{x}(t)+\boldsymbol{B}_{1}u(t)$

规则 2: IF $x_{1}(t)$ is about $\pm\frac{\pi}{2}\left(\left|x_{1}\right|<\frac{\pi}{2}\right)$ , THEN $\dot{\boldsymbol{x}}(t)=\boldsymbol{A}_{2}\boldsymbol{x}(t)+\boldsymbol{B}_{2}u(t)$

式中， $A_{1}=\begin{bmatrix}0&1\\ \frac{g}{4l/3-aml}&0\end{bmatrix},B_{1}=\begin{bmatrix}0\\ -\frac{\alpha}{4l/3-aml}\end{bmatrix},A_{2}=\begin{bmatrix}0&1\\ \frac{2g}{\pi(4l/3-aml\beta^{2})}&0\end{bmatrix},B_{2}=$ $\left[-\frac{0}{\alpha\beta}\right],\beta=\cos(88^{\circ})$

针对倒立摆模型，取 $g = 9.8 \, m/s^{2}$ ，摆的质量 $m = 2.0 \, kg$ ，小车质量 $M = 8.0 \, kg, 2l = 1.0 \, m$ 。根据倒立摆的运动情况，设计两条模糊控制规则。

Rule1: If $x_{1}(t)$ is about 0 then $u = K_{1}x(t)$

Rule2: If $x_{1}(t)$ is about $\pm \frac{\pi}{2} (|x_{1}(t)| < \frac{\pi}{2})$ then $u = K_{2}x(t)$

采用 PDC 方法, 根据式(4.15), 设计基于 T-S 模糊控制器为

$$u = w _ {1} \left(x _ {1}\right) \mathbf {K} _ {1} x (t) + w _ {2} \left(x _ {1}\right) \mathbf {K} _ {2} x (t) \tag {4.16}$$

式中， $w_{1} + w_{2} = 1$

根据倒立摆的两条 T-S 模糊模型规则,隶属函数应按图 4-32 进行设计。仿真中采用三角形隶属函数实现摆角度 $x_{1}(t)$ 的模糊化,仿真程序为 chap4\_9mf.m,如图 4-33 所示。

![](image/f214c7df9172df9157467083c3b446cb6033c6b01d0acb469e4df00d3bdfd1c9.jpg)

<details>
<summary>line</summary>

| x (deg) | y (approx) |
| --- | --- |
| -88 | 1 |
| 0 | 0 |
| 88 | 1 |
</details>

图4-32 模糊隶属度函数示意图

![](image/57c227b1e687571b957f86a0fb993be14731e11ccca6719da1e7ec2afba4e679.jpg)

<details>
<summary>line</summary>

| x₁ | Membership function |
| --- | --- |
| -2.0 | 1.0 |
| -1.5 | 0.0 |
| -1.0 | 0.5 |
| -0.5 | 0.8 |
| 0.0 | 1.0 |
| 0.5 | 0.8 |
| 1.0 | 0.5 |
| 1.5 | 0.0 |
| 2.0 | 1.0 |
</details>

图4-33 仿真中的模糊隶属度函数

选择期望的闭环极点 $(-3-3i,-3+3i)$ ，利用极点配置函数 $\mathrm{place}(A,B,P)$ ，可以得到系统的反馈增益矩阵： $K_{1}=[-418\quad-74]$ ， $K_{2}=[-10452\quad-2292]$ 。

采用 $u_{i} = -K_{i}x$ 的反馈控制，按式(4.16)设计控制器，运行Simulink主程序chap4\_9sim.mdl，仿真结果如图4-34和图4-35所示。

![](image/5ba5a0331a3e5851e4a6cb6b02bd48bcb03878d93c3206b2eef35ad91c32884d.jpg)

<details>
<summary>line</summary>

| time(s) | angle and angle speed response |
| --- | --- |
| 0.0 | 0.3 |
| 0.5 | -0.2 |
| 1.0 | -0.1 |
| 1.5 | -0.05 |
| 2.0 | -0.02 |
| 2.5 | -0.01 |
| 3.0 | -0.01 |
| 3.5 | -0.01 |
| 4.0 | -0.01 |
| 4.5 | -0.01 |
| 5.0 | -0.01 |
</details>

图4-34 角度和角速度响应

![](image/af10417ff8645cae83d11e9b76b37678089b0423bf0df97ce118417f93ed191b.jpg)

<details>
<summary>line</summary>

| time(s) | control input |
| --- | --- |
| 0 | 1000 |
| 1 | 0 |
| 2 | 0 |
| 3 | 0 |
| 4 | 0 |
| 5 | 0 |
</details>

图4-35 控制输入
