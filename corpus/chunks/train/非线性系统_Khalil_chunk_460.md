# 14.5.3 通过积分控制的调节

考虑单输入-单输出系统

$$\dot {x} = f (x, w) + g (x, w) [ u + \delta (x, u, w) ]y = h (x, w)$$

其中 $x \in R^n$ 是状态, $u \in R$ 是控制输入, $y \in R$ 是受控及被测输出, $w \in R^l$ 是由未知不变参数和扰动组成的向量, 函数 $f, g, h$ 和 $\delta$ 在 $(x, u)$ 上足够光滑, 在 $w$ 上连续, $x \in D \subset R^n$ , $u \in R$ , $w \in D_w \subset R^l$ , 其中 $D$ 和 $D_w$ 是开连通集。假设系统

$$\dot {x} = f (x, w) + g (x, w) uy = h (x, w)$$

在 $D$ 内对 $w$ 一致，具有相对阶 $\rho$ ，即对于所有 $(x,w)\in D\times D_w$ ，有

$$L _ {g} h (x, w) = \dots = L _ {g} L _ {f} ^ {\rho - 2} h (x, w) = 0, \quad L _ {g} L _ {f} ^ {\rho - 1} h (x, w) \geqslant a > 0$$

我们的目标是设计一个输出反馈控制器,使输出 y 渐近跟踪一个恒定的参考信号 $r \in D_{r} \subset R$ , 其中 $D_{r}$ 是开连通集。

这是14.1.4节研究过的输出反馈问题,唯一的区别是这里允许f和h与w有关,而在14.1.4节中限定f和h与w无关,这是必需的,因为要用变量 $h,L_{f}h,\cdots,L_{f}^{\rho-1}h$ 计算状态反馈控制。在输出反馈情况下,这些变量利用高增益观测器从测得的信号y计算。由于允许f与w有关, $\delta_{1}$ 被f吸收。这里不再重述14.1.4节中的假设及推导,只回顾滑模状态反馈控制器(14.29),即

$$\dot {e} _ {0} = e _ {1}u = - k \text { sat } \left(\frac {k _ {0} e _ {0} + k _ {1} e _ {1} + k _ {2} e _ {2} + \cdots + k _ {\rho - 1} e _ {\rho - 1} + e _ {\rho}}{\mu}\right)$$

其中， $e_{1}=y-r$ 是调节误差， $e_{2}$ 到 $e_{\rho}$ 是 $e_{1}$ 的导数 $^{①}$ 。该控制全局有界，信号 $e_{1}$ 在线可测。为了用输出反馈实现该控制器，我们利用线性高增益观测器估计 $e_{2}$ 到 $e_{\rho}$ 。这样，输出反馈控制器可取为

$$\dot {e} _ {0} = e _ {1}u = - k \text { sat } \left(\frac {k _ {0} e _ {0} + k _ {1} e _ {1} + k _ {2} \hat {e} _ {2} + \cdots + k _ {\rho - 1} \hat {e} _ {\rho - 1} + \hat {e} _ {\rho}}{\mu}\right)\dot {\hat {e}} _ {i} = \hat {e} _ {i + 1} + \left(\frac {\alpha_ {i}}{\varepsilon^ {i}}\right) \left(e _ {1} - \hat {e} _ {1}\right), \quad 1 \leqslant i \leqslant \rho - 1\dot {\hat {e}} _ {\rho} = \left(\frac {\alpha_ {\rho}}{\varepsilon^ {\rho}}\right) \left(e _ {1} - \hat {e} _ {1}\right)$$

其中,选择正常数 $\alpha_{1}$ 到 $\alpha_{\rho}$ ,使方程

$$s ^ {\rho} + \alpha_ {1} s ^ {\rho - 1} + \dots + \alpha_ {\rho - 1} s + \alpha_ {\rho} = 0$$

的根具有负实部。对于相对阶为1的系统 $(\rho = 1)$ ，可不用高增益观测器。在14.1.4节的假设条件下，状态反馈下的闭环系统在 $(z, e_0, e) = (0, \bar{e}, 0)$ 处有指数稳定的平衡点。关于当 $\varepsilon$ 足够小时，输出反馈控制器能够重现状态反馈控制器性能的证明，留给读者完成（见习题14.50）。
