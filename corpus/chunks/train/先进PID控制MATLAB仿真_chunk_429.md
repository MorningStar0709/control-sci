# 9.3.1 问题描述

考虑如下 2 阶非线性系统：

$$\ddot {x} = f (x, \dot {x}) + g (x, \dot {x}) u \tag {9.12}$$

式中，f 为未知非线性函数；g 为已知非线性函数； $u \in R^{n}$ 和 $y \in R^{n}$ 分别为系统的输入和输出。

式（9.12）还可写为

$$
\begin{array}{l} \dot {x} _ {1} = x _ {2} \\ \dot {x} _ {2} = f \left(x _ {1}, x _ {2}\right) + g \left(x _ {1}, x _ {2}\right) u \tag {9.13} \\ y = x _ {1} \\ \end{array}
$$

设位置指令为 $y_{d}$ ，令

$$
e = y _ {\mathrm{d}} - \bar {y} = y _ {\mathrm{d}} - x _ {1}, \quad E = \left( \begin{array}{c c} e & \dot {e} \end{array} \right) ^ {\mathrm{T}}
$$

选择 $\boldsymbol{K}=\left(k_{\mathrm{p}},k_{\mathrm{d}}\right)^{\mathrm{T}}$ ，使多项式 $s^{2}+k_{d}s+k_{p}=0$ 的所有根部都在复平面左半开平面上。设计基于前馈加补偿的 PD 控制律为

$$u ^ {*} = \frac {1}{g (\boldsymbol {x})} \left[ - f (\boldsymbol {x}) + \ddot {y} _ {\mathrm{d}} + \boldsymbol {K} ^ {\mathrm{T}} \boldsymbol {E} \right] \tag {9.14}$$

将式（9.14）代入式（9.12），得到闭环控制系统的方程：

$$\ddot {e} + k _ {\mathrm{p}} e + k _ {\mathrm{d}} \dot {e} = 0 \tag {9.15}$$

由 K 的选取，可得 $t \to \infty$ 时 $e(t) \to 0$ ， $\dot{e}(t) \to 0$ ，即系统的输出 y 及其导数渐进地收敛于理想输出 $y_{d}$ 及其导数。

如果非线性函数 $f(x)$ 是已知的，则可以选择控制 u 来消除其非线性的性质，然后再根据线性控制理论设计控制器。

![](image/01bf64b0b53eb95d928460561a4c40578df07f70b624f7c516df1e03e35cf3b4.jpg)
