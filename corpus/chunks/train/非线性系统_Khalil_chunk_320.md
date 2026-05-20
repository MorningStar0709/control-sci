$\dot{x}_1 = \varepsilon [(-1 + 1.5\cos^2 t)x_1 + (1 - 1.5\sin t\cos t)x_2]$

(3) $\dot{x} = \varepsilon (-x\sin^2 t + x^2\sin t + xe^{-t}),\quad \varepsilon >0$

10.11 设系统为 $\dot{x}_{1} = \varepsilon[(-1 + 1.5\cos^{2}t)x_{1} + (1 - 1.5\sin t\cos t)x_{2}]$

$$\dot {x} _ {2} = \varepsilon [ (- 1 - 1. 5 \sin t \cos t) x _ {1} + (- 1 + 1. 5 \sin^ {2} t) x _ {2} ] + e ^ {- t}$$

证明存在 $\varepsilon^{*}>0$ , 使得对于所有 $0<\varepsilon<\varepsilon^{*}$ 和所有 $x(0)\in R^{2}$ , 当 t 趋于无穷时, $x(t)$ 趋于零。

10.12 考虑系统 $\dot{y}=Ay+\varepsilon g(t,y,\varepsilon),\varepsilon>0$ , 其中 $n\times n$ 矩阵 A 仅在虚轴上有一个单阶特征值。

(a) 证明对于所有 $t \geqslant 0$ , $\exp(At)$ 和 $\exp(-At)$ 有界。

(b) 证明通过变量代换 $y = \exp (At)x$ ，可将系统变换为 $\dot{x} = \varepsilon f(t,x,\varepsilon)$ ，其中 $f = \exp (-At)g(t,\exp (At)x,\varepsilon)$ 。

10.13（见文献[166]）应用平均化法研究Mathieus方程 $\ddot{y} + (1 + 2\varepsilon \cos 2t)y = 0,\varepsilon >0$

提示: 利用习题 10.12。

10.14 （见文献[166]）应用平均化法研究方程 $\ddot{y} + y = 8 \varepsilon(\dot{y})^{2}$ 。

提示: 利用习题 10.12。

10.15 对下列各二阶系统,运用平均化法研究极限环的存在性。如果存在极限环,估计其在状态平面中的位置和振荡周期,并确定其是否稳定。

(1) $\ddot{y} + y = -\varepsilon\dot{y}(1 - y^{2})$

(2) $\ddot{y} + y = \varepsilon \dot{y}(1 - y^2) - \varepsilon y^3$

(3) $\ddot{y} + y = -\varepsilon \left(1 - \frac{3\pi}{4} |y|\right) \dot{y}$

(4) $\ddot{y} + y = -\varepsilon \left(1 - \frac{3\pi}{4} |\dot{y}|\right) \dot{y}$

(5) $\ddot{y} + y = -\varepsilon(\dot{y} - y^{3})$

(6) $\ddot{y} + y = \varepsilon \dot{y}(1 - y^2 - \dot{y}^2)$

10.16 设二阶系统为

$$\dot {x} _ {1} = x _ {2}, \quad \dot {x} _ {2} = - x _ {1} + \varepsilon [ x _ {1} + x _ {2} (1 - x _ {1} ^ {2} - x _ {2} ^ {2}) ], \quad \varepsilon > 0$$

(a) 证明对于充分小的 $\varepsilon$ ，系统有一个稳定极限环。

(b) 证明当 $\varepsilon > 1$ 时, 系统无周期轨道。

10.17 考虑瑞利方程 $m\frac{d^2u}{dt^2} + ku = \lambda \left[1 - \alpha \left(\frac{du}{dt}\right)^2\right]\frac{du}{dt}$

其中 $m, k, \lambda$ 和 $\alpha$ 是正常数。

(a) 用无量纲变量 $y = u / u^{*}$ , $\tau = t / t^{*}$ 和 $\varepsilon = \lambda / \lambda^{*}$ 证明方程可归一化为

$$\ddot {y} + y = \varepsilon \left(\dot {y} - \frac {1}{3} \dot {y} ^ {3}\right)$$

其中， $(u^{*})^{2}\alpha k=m/3,t^{*}=\sqrt{m/k}$ 和 $\lambda^{*}=\sqrt{km}$ 。在方程中 y 表示关于 y 的 $\tau$ 的导数。

(b) 运用平均化法证明归一化瑞利方程有一个稳定极限环, 并估计极限环在平面 $(y, \dot{y})$ 中的位置。

(c) 当(i) $\varepsilon=1$ , (ii) $\varepsilon=0.1$ , (iii) $\varepsilon=0.01$

时,运用数值方法在相平面 $(y,\dot{y})$ 内画出归一化瑞利方程的相图,并与(b)的结果进行比较。

10.18 考虑达芬方程 $m\ddot{y} + c\dot{y} + ky + ka^{2}y^{3} = A \cos \omega t$

其中，A, a, c, k, m 和 $\omega$ 是正常数。
