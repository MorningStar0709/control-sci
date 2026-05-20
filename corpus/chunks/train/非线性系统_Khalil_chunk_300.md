定理 10.2 的 $O(\varepsilon^{N})$ 估计仅在原点是指数稳定的时候成立。如果是渐近稳定而不是指数稳定的，就不一定成立，如下例所示。

例10.6 考虑一阶系统

$$\dot {x} = - x ^ {3} + \varepsilon x$$

并假设 $\varepsilon > 0$ 。非扰动系统

$$\dot {x} = - x ^ {3}$$

的原点是全局渐近稳定的,但不是指数稳定的(见例4.23)。扰动系统在x=0和 $x=\pm\sqrt{\varepsilon}$ 处有3个平衡点。平衡点x=0是非稳定的,而其他两个平衡点是渐近稳定的。解这两个具有相同正初始条件 $x(0)=a$ 的系统,很容易看出,当t趋于无穷时,

$$x (t, \varepsilon) \rightarrow \sqrt {\varepsilon}, x _ {0} (t) \rightarrow 0$$

因为 $\sqrt{\varepsilon}$ 不是 $O(\varepsilon)$ , 显然对于所有 $t \geqslant 0$ , 逼近误差 $x(t, \varepsilon) - x_0(t)$ 不是 $O(\varepsilon)$ 。尽管如此, 由于原点是渐近稳定的, 应该能够得出当 $t$ 趋于无穷时逼近的渐近特性。尽管这一论述比定理10.2缺乏说服力, 但我们仍可以得到这个结论。因为非扰动系统的原点是渐近稳定的, 故当 $t$ 趋于无穷时, 解 $x_0(t)$ 趋于零, 即给定 $\delta > 0$ , 存在 $T_1 > 0$ , 使得

$$\| x _ {0} (t) \| < \delta / 2, \forall t \geqslant T _ {1}$$

扰动系统的解是毕竟有界的,最终边界随 $\varepsilon$ 减小。因此,给定任意 $\delta > 0$ , 存在 $T_{2} > 0$ 和 $\varepsilon^{*} > 0$ , 使得

$$\| x (t, \varepsilon) \| < \delta / 2, \forall t \geqslant T _ {2}, \forall \varepsilon < \varepsilon^ {*}$$

把这两个估计结合起来, 就可以说对于任意 $\delta > 0$ , 逼近误差满足

$$\left\| x (t, \varepsilon) - x _ {0} (t) \right\| < \delta , \quad \forall t \geqslant T, \forall \varepsilon < \varepsilon^ {*}$$

其中， $T=\max\{T_{1},T_{2}\}$ 。在阶O(1)时间区间[0,T]上，从定理10.1的有限时间结果可知逼近误差为 $O(\varepsilon)$ 。因此，可以说对于任意 $\delta>0$ ，存在 $\varepsilon^{**}>0$ ，使得

$$\| x (t, \varepsilon) - x _ {0} (t) \| < \delta , \forall t \in [ 0, \infty), \forall \varepsilon < \varepsilon^ {* *}$$

上一个不等式等于说当 $\varepsilon$ 趋于零时逼近误差趋于零, 对于所有 $t \geqslant 0$ 是关于 t 一致的。一般来讲, 在缺少指数稳定性的条件下, 这是我们可以得到的最好结果。当然, 在特殊的例子中, 可以得到 $x_{0}(t)$ 和 $x(t, \varepsilon)$ 的闭式解, 而且实际上还可以证明逼近误差为 $O(\sqrt{\varepsilon})$ 。
