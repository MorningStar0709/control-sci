$$
\begin{array}{l} \dot {V} = \frac {\partial W}{\partial \eta} (f (\eta) + f _ {1} (\eta , y) y) + y ^ {T} (u + p (\eta , y) w) \\ = \frac {1}{2} \left(\gamma^ {2} \| w \| ^ {2} - \| z \| ^ {2}\right) + \frac {\partial W}{\partial \eta} f (\eta) - \frac {1}{2} \left\| \frac {1}{\gamma} p _ {0} ^ {\mathrm{T}} (\eta , y) y - \gamma w \right\| ^ {2} \\ + y ^ {T} \left(u + \frac {1}{2 \gamma^ {2}} p (\eta , y) p ^ {T} (\eta , y) y + \frac {1}{2} h _ {0} ^ {T} (\eta , y) h _ {0} (\eta , y) y + \frac {\partial W}{\partial \eta} f _ {1}\right). \tag {6.9.9} \\ \end{array}
$$

因此，若取状态反馈律

$$u = - \frac {\partial W}{\partial \eta} f _ {1} (\eta , y) - y - \frac {1}{2 \gamma^ {2}} p (\eta , y) p ^ {T} (\eta , y) y - \frac {1}{2} h _ {0} ^ {T} (\eta , y) h _ {0} (\eta , y) y, \tag {6.9.10}$$

则对应的闭环系统满足 $\gamma-$ 耗散不等式

$$\dot {V} \leqslant \frac {1}{2} \left(\gamma^ {2} \| w \| ^ {2} - \| z \| ^ {2}\right), \tag {6.9.11}$$

而且利用上式以及式 (6.9.7) 还可以进一步证明，当 $w = 0$ 时沿闭环系统的状态轨迹有

$$\dot {V} < 0, \quad \forall \eta \neq 0, y \neq 0. \tag {6.9.12}$$

因此状态反馈控制器 (6.9.10) 是广义受控对象 (6.9.6) 所对应的 $H_{\infty}$ 状态反馈控制器.

综上所述，对于广义受控对象 (6.9.6)，我们有如下结论：

定理 6.9.1 对于受控对象 (6.9.6) 和给定的 $\gamma > 0$ ，如果存在正定函数 $W(\eta)$ 使得式 (6.9.7) 成立，那么由式 (6.9.10) 给定的控制器使得闭环系统具有小于 $\gamma$ 的 $L^{2}$ 增益，且 w = 0 时系统在原点渐近稳定。

注6.9.1 回顾上述定理的证明可知，我们并没有要求Hamilton-Jacobi偏微分不等式有解，而且只要 $y = 0$ 时的 $\eta-$ 子系统是渐近稳定的，那么对于任意给定的 $\gamma,$ 都可以找到理想的控制器．这意味着闭环系统的 $L^2$ 增益可以抑制到任意小．实际上，这主要是因为评价信号 $z$ 中不包含对控制输入信号的加权项．这类设计问题称为 $L^2$ 干扰近似解耦问题[13].

注6.9.2 系统(6.9.6)的结构要求 $\eta-$ 子系统可以表示为

$$\dot {\eta} = f _ {0} (\eta , y) = f (\eta) + f _ {1} (\eta , y) y.$$

实际上可以证明 $f(\eta, y)$ 的这种分解具有一般性 (参见文献 [12]).

注6.9.3 定理6.9.1的结果还可以推广到 $\eta-$ 子系统在原点不是渐近稳定的情况．如果存在光滑函数 $\alpha(\eta)(a(0)=0)$ 使得当 $y=\alpha(\eta)$ 时 $\eta-$ 子系统

$$\dot {\eta} = f _ {a} (\eta) = f (\eta) + f _ {1} (\eta , a (\eta)) a (\eta)$$

在原点 $\eta = 0$ 是渐近稳定的，即存在正定函数 $W(\eta)$ 使得

$$\dot {W} = \frac {\partial W}{\partial \eta} f _ {a} (\eta) < 0, \tag {6.9.13}$$

那么我们可以对受控对象进行如下坐标变换：

$$
\left[\begin{array}{c}\eta\\y\end{array}\right]\rightarrow \left[\begin{array}{c}\eta\\\widetilde {y}\end{array}\right],
$$

其中 $\widetilde{y} = y - a(\eta)$ . 在新的坐标下，受控对象 (6.9.6) 可以表示为

$$
\left\{ \begin{array}{l} \dot {\eta} = f _ {a} (\eta) + f _ {a 1} (\eta , \widetilde {y}) \widetilde {y}, \\ \dot {\widetilde {y}} = p (\eta , y) w + v, \end{array} \right. \tag {6.9.14}
$$

其中 $v = u - \dot{a} = u - \frac{\partial a}{\partial \eta} (f(\eta) + f_1(\eta, y)y)$ 是新的控制输入信号，且
