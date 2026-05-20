$$
\begin{array}{l} \dot {V} = L _ {f.} W (\xi) + L _ {F} W (\xi) y + y ^ {\mathrm{T}} p (\xi , y) w + y ^ {\mathrm{T}} v \\ = L _ {f.} W (\xi) + \frac {1}{2} h ^ {\mathbf {T}} (\xi , y) h (\xi , y) + \frac {1}{2} \left(\gamma^ {2} \| w \| ^ {2} - \| z \| ^ {2}\right) \\ - \frac {1}{2} \left\| \frac {1}{\gamma} p ^ {\mathrm{T}} (\xi , y) y - \gamma w \right\| ^ {2} + y ^ {\mathrm{T}} \left(v + L _ {F} ^ {\mathrm{T}} W (\xi) + \frac {1}{2 \gamma^ {2}} p p ^ {\mathrm{T}} y\right) \\ \leqslant - Q (\xi) + \frac {1}{2} h _ {*} ^ {\mathrm{T}} (\xi) h _ {*} (\xi) + \frac {1}{2} \left(\gamma^ {2} \| w \| ^ {2} - \| z \| ^ {2}\right) \\ + y ^ {\mathrm{T}} \left(v + L _ {F} ^ {\mathrm{T}} W (\xi) + H ^ {\mathrm{T}} (\xi , y) + \frac {1}{2 \gamma^ {2}} p p ^ {\mathrm{T}} y\right). \tag {6.9.25} \\ \end{array}
$$

将反馈控制器 (6.9.23) 代入上式，得

$$\dot {V} \leqslant \frac {1}{2} \left(\gamma^ {2} \| w \| ^ {2} - \| z \| ^ {2}\right). \tag {6.9.26}$$

因此闭环系统是 $\gamma-$ 耗散的，从而闭环系统具有小于 $\gamma$ 的 $L^2$ 增益.

另外，当 $w = 0$ 时重复上述耗散不等式的证明过程得

$$\dot {V} \leqslant - Q (x) - y ^ {\mathrm{T}} y, \quad \forall t \geqslant 0. \tag {6.9.27}$$

此时闭环系统在原点的渐近稳定性由 Lyapunov 稳定性理论得证.

注6.9.4 上述定理要求受控对象的零输出动态是渐近稳定的，并且其“稳定余量”要足够大以使得 $Q(\xi)$ 满足不等式(6.9.22).实际上，如果零输出动态是指数稳定的，即存在 $\varepsilon >0$ 使得

$$L _ {f.} W (\xi) \leqslant - \varepsilon W (\xi), \tag {6.9.28}$$

那么可以验证，若取正定函数

$$W _ {0} (W) = W \sup _ {0 \leqslant \theta \leqslant 1} \frac {\mathrm{d} \kappa (\theta)}{\mathrm{d} \theta} + \int_ {W} ^ {2 W} \kappa (\theta) \mathrm{d} \theta , \tag {6.9.29}$$

其中 $\kappa(\cdot)$ 是满足如下条件的单调非递减函数：

$$\frac {1}{2 \varepsilon} \left| \left| h _ {*} (\xi) \right| \right| ^ {2} \leqslant \kappa (W), \tag {6.9.30}$$

并令正定函数 $Q(\xi) = \varepsilon \kappa(W)$ , 则 $W_0$ 和 $Q$ 将满足定理 6.9.2 的假设条件 (详细可参见文献 [14]).

现在我们再来讨论系统不满足匹配条件 (6.9.17) 的情况。这时系统 (6.9.15) 与如下系统是反馈等价的：

$$
\left\{ \begin{array}{l} \dot {\xi} = f _ {0} (\xi , y) + g _ {1 1} (\xi , y) w, \\ \dot {y} = g _ {1 2} (\xi , y) w + v, \\ z = h (\xi , y). \end{array} \right. \tag {6.9.31}
$$

与系统 (6.9.19) 相比，其不同在于后者的 $\xi$ -子系统有干扰信号的输入项.

定理 6.9.3 考虑系统 (6.9.31). 假设对其零输出动态, 存在正定函数 $W(\xi)$ ( $W(0) = 0$ ) 满足 Hamilton-Jacobi 不等式

$$L _ {f _ {*}} W (\xi) + \frac {1}{2 \gamma^ {2}} \| L _ {g _ {*}} W (\xi) \| ^ {2} + \frac {1}{2} \| h _ {*} (\xi) \| ^ {2} < 0, \quad \forall \xi \neq 0, \tag {6.9.32}$$

则 $H_{\infty}$ 控制器为

$$v = - y - L _ {F} ^ {\mathrm{T}} W (\xi) - H ^ {\mathrm{T}} (\xi , y) - \frac {1}{2 \gamma^ {2}} M ^ {\mathrm{T}} (\xi , y), \tag {6.9.33}$$
