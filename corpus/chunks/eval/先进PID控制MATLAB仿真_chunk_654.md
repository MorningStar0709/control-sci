# 17.5.2 控制律设计

基本反演控制方法设计步骤：

(1) 定义位置误差

$$e _ {1} = x _ {1} - y _ {\mathrm{d}} \tag {17.23}$$

式中， $y_{d}$ 为位置指令信号。则

$$\dot {e} _ {1} = \dot {x} _ {1} - \dot {y} _ {\mathrm{d}} = x _ {2} - \dot {y} _ {\mathrm{d}}$$

定义 Lyapunov 函数

$$V _ {1} = \frac {1}{2} e _ {1} ^ {2} \tag {17.24}$$

则

$$\dot {V} _ {1} = e _ {1} \dot {e} _ {1} = e _ {1} \left(x _ {2} - \dot {y} _ {\mathrm{d}}\right)$$

为了实现 $\dot{V}_1 \leqslant 0$ ，取 $x_2 = s - c_1 e_1 + \dot{y}_\mathrm{d}$ ， $s$ 为虚拟控制项，即 $s = x_2 + c_1 e_1 - \dot{y}_\mathrm{d} = c_1 e_1 + \dot{e}_1$ ， $c_1 > 0$ ，则

$$\dot {V} _ {1} = e _ {1} s - c _ {1} e _ {1} ^ {2}$$

如果 s=0，则 $\dot{V}_{1}\leqslant0$ 。为此，需要进行下一步设计。

(2) 定义 Lyapunov 函数

$$V _ {2} = V _ {1} + \frac {1}{2} s ^ {2} \tag {17.25}$$

由于 $\dot{s} = \dot{x}_2 + c_1\dot{e}_1 - \ddot{y}_{\mathrm{d}} = f(x,t) + b(x,t)u + d(x,t) + c_1\dot{e}_1 - \ddot{y}_{\mathrm{d}}$ ，则

$$\dot {V} _ {2} = \dot {V} _ {1} + s \dot {s} = e _ {1} s - c _ {1} e _ {1} ^ {2} + s (f (x, t) + b (x, t) u + d (x, t) + c _ {1} \dot {e} _ {1} - \ddot {y} _ {\mathrm{d}})$$

为使 $\dot{V}_{2}\leqslant0$ ，设计控制器为

$$u = \frac {1}{b (x , t)} (- f (x, t) - c _ {2} s - e _ {1} - c _ {1} \dot {e} _ {1} + \ddot {y} _ {\mathrm{d}} - \eta \operatorname{sgn} (s)) \tag {17.26}$$

式中， $c_{2} > 0$ ； $\eta \geqslant D$ ，则

$$\dot {V} _ {2} = - c _ {1} e _ {1} ^ {2} - c _ {2} s ^ {2} + s d (x, t) - \eta | s | \leqslant - c _ {1} e _ {1} ^ {2} - c _ {2} s ^ {2} \leqslant - \lambda V _ {2} \leqslant 0$$

式中， $\lambda=\min\left\{c_{1},c_{2}\right\}$ 。

根据不等式求解引理，解上述不等式，可得

$$V _ {2} ^ {\prime} (t) \leqslant \mathrm{e} ^ {- \lambda t} V _ {2} (0)$$

通过控制律的设计，使得系统满足了李亚普诺夫稳定性理论条件， $e_{1}$ 和 $e_{2}$ 以指数形式渐进稳定。

![](image/01988a8eb51d89fc1a55d7bf89c457106cacf775e91818a4880924ce9e17dbba.jpg)
