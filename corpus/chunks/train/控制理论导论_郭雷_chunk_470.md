$$\dot {V} \leqslant - \frac {1}{2} \left\| \frac {1}{\gamma} g _ {1} ^ {\mathrm{T}} (x) \frac {\partial^ {\mathrm{T}} V}{\partial x} - \gamma w \right\| ^ {2} + \frac {\gamma^ {2}}{2} \| w \| ^ {2} - \frac {1}{2} \left(\| \alpha (x) \| ^ {2} + \| h _ {1} (x) \| ^ {2}\right). \tag {6.8.7}$$

注意当条件 (6.8.3) 成立时，对于闭环系统有

$$\| z \| ^ {2} = \left\| \alpha (x) \right\| ^ {2} + \left\| h _ {1} (x) \right\| ^ {2}.$$

因此沿闭环系统的任意轨迹， $V(x)$ 满足如下耗散不等式：

$$\dot {V} \leqslant \frac {1}{2} \left\{\gamma^ {2} \| w \| ^ {2} - \| z \| ^ {2} \right\}. \tag {6.8.8}$$

必要性 设存在状态反馈控制器 (6.8.5) 使得闭环系统具有 $\gamma$ -耗散性。由于此时的闭环系统可以描述为

$$
\left\{ \begin{array}{l l} \dot {x} = f _ {\alpha} (x) + g _ {1} (x) w, \\ z = h _ {\alpha} (x), \end{array} \right. \tag {6.8.9}
$$

其中 $f_{\alpha}(x) = f(x) + g_2(x)\alpha (x), h_{\alpha}(x) = h_1(x) + d_{12}(x)\alpha (x)$ ，所以根据定理6.7.1，存在半正定函数 $V(x)$ 满足不等式

$$\frac {\partial V}{\partial x} f _ {\alpha} (x) + \frac {1}{2 \gamma^ {2}} \frac {\partial V}{\partial x} g _ {1} (x) g _ {1} ^ {\mathrm{T}} (x) \frac {\partial^ {\mathrm{T}} V}{\partial x} + \frac {1}{2} h _ {\alpha} ^ {\mathrm{T}} (x) h _ {\alpha} (x) \leqslant 0, \quad \forall x. \tag {6.8.10}$$

利用式 (6.8.3), 不难证明上式等价于

$$
\begin{array}{l} \frac {\partial V}{\partial x} f (x) + \frac {1}{2} \frac {\partial V}{\partial x} \left(\frac {1}{\gamma^ {2}} g _ {1} (x) g _ {1} ^ {T} (x) - g _ {2} (x) g _ {2} ^ {T} (x)\right) \frac {\partial^ {T} V}{\partial x} \\ + \frac {1}{2} h _ {1} ^ {\mathrm{T}} (x) h _ {1} (x) \leqslant - \left\| g _ {2} ^ {\mathrm{T}} (x) \frac {\partial^ {\mathrm{T}} V}{\partial x} + \alpha (x) \right\| ^ {2} \leqslant 0. \tag {6.8.11} \\ \end{array}
$$

[NO TEXT]

如前所述，定理6.8.1给出的控制器能够保证闭环系统满足性能指标(H2)，但是并不能保证(H1).为此，我们需要进一步的条件.

定理 6.8.2 设广义受控对象 (6.7.16) 满足式 (6.8.3)，并且反馈控制器由定理 6.8.1 给定。如果对于系统 (6.7.16)，x = 0 是开环系统的平衡点，即 $f(0) = 0$ ，且 $(f(x), h_{1}(x))$ 是零状态能检测的，那么当 w = 0 时，闭环系统在 x = 0 是渐近稳定的。

证明 从定理6.8.1的证明可知, 对于由广义受控对象(6.7.16)和控制器(6.8.5)构成的闭环系统, 存在半正定函数 $V(x)$ 使得耗散不等式(6.8.8)对任意 $w$ 成立. 因此当 $w = 0$ 时, 有

$$\dot {V} \leqslant - \frac {1}{2} \| z \| ^ {2} \leqslant 0, \quad \forall t. \tag {6.8.12}$$

于是该系统是 Lyapunov 稳定的，并且 $\dot{V} = 0$ 仅当 $z = 0$ ，或等价地， $h_1(x) = 0, \alpha(x) = 0$ 时成立。因此，显然有

$$E \subseteq \Omega_ {0}, \tag {6.8.13}$$

其中

$$E = \{x \mid \dot {V} = 0 \}, \quad \Omega_ {0} = \{x \mid h _ {1} (x) = 0, \alpha (x) = 0 \},$$

而且在集合 $\Omega_0$ 中，系统状态轨迹满足

$$\dot {x} = f (x), \quad h _ {1} (x) = 0.$$

因此根据零状态能检测性假设以及 LaSalle 不变集定理可知， $x(t) \rightarrow 0$ .
