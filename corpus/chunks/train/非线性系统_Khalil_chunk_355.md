# 12.2 通过线性化实现稳定

我们利用稳定问题来说明线性化设计方法,首先讨论状态反馈控制情况,然后讨论输出反馈控制。

对于状态反馈稳定,考虑系统

$$\dot {x} = f (x, u) \tag {12.1}$$

其中 $f(0,0) = 0$ ，函数 $f(x,u)$ 在包含原点 $(x = 0,u = 0)$ 的定义域 $D_{x}\times D_{u}\subset R^{n}\times R^{p}$ 内是连续可微的。我们要设计的是能够稳定系统的状态反馈控制律 $u = \gamma (x)$ ，对方程（12.1）在点 $(x = 0,u = 0)$ 线性化，可得线性系统

$$\dot {x} = A x + B u \tag {12.2}$$

其中 $A = \frac{\partial f}{\partial x}(x,u)\Bigg|_{x = 0,u = 0};\quad B = \frac{\partial f}{\partial u}(x,u)\Bigg|_{x = 0,u = 0}$

假定矩阵对 $(A,B)$ 是可控的，或至少是可稳定的。设计一个矩阵 $K$ ，使 $A - BK$ 的特征值都在左半开复平面上期望的位置。接下来把线性状态反馈控制 $u = -Kx$ 运用于非线性系统(12.1)，则闭环系统为 $\dot{x} = f(x, - Kx)$ (12.3)

显然,原点是闭环系统的平衡点,方程(12.3)在原点x=0的线性化方程为

$$\dot {x} = \left[ \frac {\partial f}{\partial x} (x, - K x) + \frac {\partial f}{\partial u} (x, - K x) (- K) \right] _ {x = 0} x = (A - B K) x$$

由于 A-BK 是赫尔维茨矩阵, 所以满足定理 4.7, 即原点是闭环系统 (12.3) 的渐近稳定平衡点。实际上由定理 4.13 可知, 原点也是指数稳定的。作为线性化方法的附带结果, 我们总能找到闭环系统的李雅普诺夫函数。设 Q 为任意正定对称矩阵, 解关于 P 的李雅普诺夫方程

$$P (A - B K) + (A - B K) ^ {\mathrm{T}} P = - Q$$

由于 A-BK 是赫尔维茨矩阵, 所以李雅普诺夫方程有唯一正定解(定理 4.6), 二次函数 $V(x)=x^{\mathrm{T}}Px$ 是闭环系统原点的某邻域内的李雅普诺夫函数, 可以用 $V(x)$ 估计吸引区。

例12.2 考虑单摆方程

$$\ddot {\theta} = - a \sin \theta - b \dot {\theta} + c T$$

其中 $a = g / l > 0, b = k / m \geqslant 0, c = 1 / ml^2 > 0, \theta$ 为摆线与纵轴之间的夹角， $T$ 是作用于单摆的力矩，把力矩作为控制输入，并假设希望在 $\theta = \delta$ 处使单摆稳定。为使摆在 $\theta = \delta$ 处保持平衡，力矩必须有一个稳态分量 $T_{\mathrm{ss}}$ ，满足

$$0 = - a \sin \delta + c T _ {\mathrm{ss}}$$

选择状态变量为 $x_{1}=\theta-\delta, x_{2}=\dot{\theta}$ ，控制变量取为 $u=T-T_{ss}$ ，状态方程

$$
\begin{array}{l} \dot {x} _ {1} = x _ {2} \\ \dot {x} _ {2} = - a [ \sin (x _ {1} + \delta) - \sin \delta ] - b x _ {2} + c u \\ \end{array}
$$

为方程(12.1)的标准形式,其中 $f(0,0)=0$ 。将系统在原点线性化,可得

$$
A = \left[ \begin{array}{c c} 0 & 1 \\ - a \cos (x _ {1} + \delta) & - b \end{array} \right] _ {x _ {1} = 0} = \left[ \begin{array}{c c} 0 & 1 \\ - a \cos \delta & - b \end{array} \right]; \quad B = \left[ \begin{array}{c} 0 \\ c \end{array} \right]
$$

矩阵对 $(A,B)$ 是可控的。取 $K = [k_1k_2]$ ，容易验证当

$$k _ {1} > - \frac {a \cos \delta}{c}, \quad k _ {2} > - \frac {b}{c}$$

时， $A - BK$ 是赫尔维茨矩阵。力矩为

$$T = \frac {a \sin \delta}{c} - K x = \frac {a \sin \delta}{c} - k _ {1} (\theta - \delta) - k _ {2} \dot {\theta}$$

关于闭环系统李雅普诺夫法的继续分析留给读者(见习题12.1)。

对于输出反馈稳定,考虑系统 $\dot{x} = f(x,u)$ (12.4)

$$y = h (x) \tag {12.5}$$
