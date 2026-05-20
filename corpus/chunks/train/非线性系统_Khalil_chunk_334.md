$$\dot {x} = 1 - x - \frac {1}{2} [ \psi (x + z) + \psi (x - z) ], \quad x (0) = \xi_ {0}\varepsilon \dot {z} = - (\varepsilon + 2) z - \frac {\varepsilon}{2} [ \psi (x + z) - \psi (x - z) ], \quad z (0) = \eta_ {0}$$

并假设 $\psi (v) = a\left[\exp \left(\frac{v}{b}\right) - 1\right], a > 0, b > 0$

这些方程来自例 11.3, 但省略了下标 r。在 $(x, z)$ 的任何紧集上, 都满足定理 11.2 的可微性和利普希茨条件。降阶模型

$$\dot {x} = 1 - x - a \left[ \exp \left(\frac {x}{b}\right) - 1 \right] \stackrel {\text { def }} {=} f _ {o} (x)$$

在 $x=p^{*}$ 处有唯一平衡点, 其中 $p^{*}$ 是 $f_{o}(p^{*})=0$ 的唯一根, 很容易看出 $0<p^{*}<1$ 。

雅可比函数 $\left.\frac{df_o}{dx}\right|_{x = p^*} = -1 - \frac{a}{b}\exp \left(\frac{p^*}{b}\right) < -1$

为负,因此平衡点 $x=p^{*}$ 是指数稳定的。此外由函数 $f_{o}(x)$ 的曲线可以看出, $x=p^{*}$ 是全局渐近稳定的。通过变量代换 $\tilde{x}=x-p^{*}$ 把平衡点移到原点,则边界层模型

$$\frac {d z}{d \tau} = - 2 z$$

与 x 无关,且其原点是全局指数稳定的。这样,定理 11.2 的所有条件全局满足,且当 h=0 时,式(11.23)至式(11.25)的估计对于所有 $t \geqslant 0$ 和任何有界初始状态 $(\xi_{0}, \eta_{0})$ 都成立。

例 11.9 考虑一个设备的自适应控制,由二阶传递函数

$$\tilde {P} (s) = \frac {k _ {p}}{(s - a _ {p}) (\varepsilon s + 1)}$$

表示,其中 $a_{p}, k_{p} > 0$ 和 $\varepsilon > 0$ 是未知参数。参数 $\varepsilon$ 代表一个小的“寄生”时间常数。假设忽略 $\varepsilon$ , 则传递函数简化为

$$P (s) = \frac {k _ {p}}{s - a _ {p}}$$

现在对该一阶传递函数设计自适应控制器。在1.2.6节给出了参考模型自适应控制器

$$u = \theta_ {1} r + \theta_ {2} y _ {p}\dot {\theta} _ {1} = - \gamma \left(y _ {p} - y _ {m}\right) r\dot {\theta} _ {2} = - \gamma \left(y _ {p} - y _ {m}\right) y _ {p}$$

其中 $y_{p}, u, r$ 和 $y_{m}$ 分别是设备输出、控制输入、参考输入及参考模型输出。设备（一阶模型）和参考模型分别为 $\dot{y}_{p} = a_{p} y_{p} + k_{p} u$

和 $\dot{y}_{m}=a_{m}y_{m}+k_{m}r,\quad k_{m}>0$

由 1.2.6 节可知,闭环自适应控制系统可以由三阶状态方程

$$\dot {e} _ {o} = a _ {m} e _ {o} + k _ {p} \phi_ {1} r + k _ {p} \phi_ {2} \left(e _ {o} + y _ {m}\right)\dot {\phi} _ {1} = - \gamma e _ {o} r\dot {\phi} _ {2} = - \gamma e _ {o} \left(e _ {o} + y _ {m}\right)$$

表示,其中 $e_{o}=y_{p}-y_{m},\phi_{1}=\theta_{1}-\theta_{1}^{*},\phi_{2}=\theta_{2}-\theta_{2}^{*},\theta_{1}^{*}=k_{m}/k_{p}$ 和 $\theta_{2}^{*}=(a_{m}-a_{p})/k_{p}$ 。定义状态向量为 $x=\left[e_{o}\quad\phi_{1}\quad\phi_{2}\right]^{T}$

重写状态方程为

$$\dot {x} = f _ {0} (t, x)$$

其中 $f_{0}(t,0)=0$ 。我们把这个三阶状态方程称为标称自适应控制系统，作为用于稳定性分析的模型。假设模型的原点是指数稳定的 $^{①}$ ，当自适应控制器应用于实际环境时，闭环系统将与该标称模型有所不同，我们把这种情况表示为奇异扰动问题。实际设备的二阶

模型可以由奇异扰动模型

$${\dot {y} _ {p}} = {a _ {p} y _ {p} + k _ {p} z}\varepsilon \dot {z} = - z + u$$

表示。重复1.2.6节中的推导，可以看出实际的自适应控制系统可以表示为奇异扰动模型

$$\dot {x} = f _ {0} (t, x) + K [ z - h (t, x) ]\varepsilon \dot {z} = - z + h (t, x)$$
