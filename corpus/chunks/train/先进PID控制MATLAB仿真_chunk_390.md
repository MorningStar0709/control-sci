# 8.2.1 问题描述

考虑如下 2 阶非线性系统:

$$\ddot {x} = f (x, \dot {x}) + g (x, \dot {x}) u \tag {8.4}$$

式中，f 为未知非线性函数，代表建模不确定部分或干扰；g 为已知非线性函数； $u \in R^{n}$ 和 $y \in R^{n}$ 分别为系统的输入和输出。

式（8.4）还可写为

$$
\begin{array}{l} \dot {x} _ {1} = x _ {2} \\ \dot {x} _ {2} = f \left(x _ {1}, x _ {2}\right) + g \left(x _ {1}, x _ {2}\right) u \tag {8.5} \\ y = x _ {1} \\ \end{array}
$$

设位置指令为 $x_{\mathrm{d}}$ ，令

$$e = x _ {\mathrm{d}} - y = x _ {\mathrm{d}} - x _ {1}, \quad E = \left(e \quad \dot {e}\right) ^ {\mathrm{T}}$$

选择 $K=\left[k_{p},k_{d}\right]^{T}$ ，使多项式 $s^{2}+k_{d}s+k_{p}=0$ 的所有根部都在复平面左半开平面上。取控制律为

$$u ^ {*} = \frac {1}{g (\boldsymbol {x})} \left[ - f (\boldsymbol {x}) + \ddot {x} _ {\mathrm{d}} + \boldsymbol {K} ^ {\mathrm{T}} \boldsymbol {E} \right] \tag {8.6}$$

将式（8.6）代入式（8.4），得到闭环控制系统的方程：

$$\ddot {e} + k _ {\mathrm{d}} \dot {e} + k _ {\mathrm{p}} e = 0 \tag {8.7}$$

由 K 的选取，可得 $t \to \infty$ 时 $e(t) \to 0$ ， $\dot{e}(t) \to 0$ ，即系统的输出 y 及其导数渐进地收敛于理想输出 $x_{d}$ 及其导数。

如果非线性函数 $f(x)$ 是已知的，则可以选择控制 u 来消除其非线性的性质，然后再根据线性控制理论设计控制器。

![](image/532b2d73408dd93735008cf0c7ed943ea6478712bcb7edb2e7f0d522909b8fb6.jpg)
