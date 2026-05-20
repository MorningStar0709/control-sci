由上述讨论可知, 如果广义受控对象的状态可测, 且满足定理 6.8.1 和定理 6.8.2 的假设条件, 那么可以通过解 Hamilton-Jacobi 偏微分不等式得到 $H_{\infty}$ 标准设计问题的解. 为了引用方便, 我们给出如下推论:

推论 6.8.1 考虑广义受控对象 (6.7.16). 设式 (6.8.3) 成立, 且 $(f(x), h_{1}(x))$ 是零状态能检测的. 对于给定的 $\gamma > 0$ , 如果 Hamilton-Jacobi 不等式 (6.8.4) 具有半正定解 $V(x)$ , 那么式 (6.8.5) 所给定的状态反馈控制器是 $H_{\infty}$ 标准设计问题的一个解.

作为非线性系统的特例，考察如下线性系统：

$$
\left\{ \begin{array}{l} \dot {x} = A x + B _ {1} w + B _ {2} u, \\ z = C _ {1} x + D _ {1 2} u. \end{array} \right. \tag {6.8.14}
$$

根据推论6.8.1不难证明有如下结论：

推论 6.8.2 设受控对象 (6.8.14) 满足如下条件:

(s1) $D_{12}^{\mathbf{T}}[D_{12} C_1] = [I 0];$

(s2) $(C_1, A)$ 是可检测的.

对于给定的 $\gamma > 0$ ，如果 Riccati 不等式

$$A ^ {\mathrm{T}} P + P A + P \left(\gamma^ {- 2} B _ {1} B _ {1} ^ {\mathrm{T}} - B _ {2} B _ {2} ^ {\mathrm{T}}\right) P + C _ {1} ^ {\mathrm{T}} C _ {1} \leqslant 0 \tag {6.8.15}$$

有半正定解 $P \geqslant 0$ , 那么状态反馈控制器

$$u = - B _ {2} ^ {\mathrm{T}} P x \tag {6.8.16}$$

使得相应的闭环系统是内部稳定的，并且

$$\| z \| _ {T} \leqslant \gamma \| w \| _ {T}, \quad \forall w, \forall T > 0. \tag {6.8.17}$$

证明 设半正定函数

$$V (x) = \frac {1}{2} x ^ {\mathrm{T}} P x.$$

因为 $f(x) = Ax, g_1(x) = B_1, g_2(x) = B_2, h_1(x) = C_1, k_{12}(x) = D_{12}$ , 所以 $V(x)$ 满足 Hamilton-Jacobi 不等式 (6.8.4). 于是根据推论 6.8.1, 该推论成立.

最后，我们来讨论动态输出反馈问题.

定理 6.8.3 设广义受控对象 (6.7.16) 满足条件

$$k _ {1 2} ^ {\mathrm{T}} (x) \left[ k _ {1 2} (x) h _ {1} (x) \right] = [ I 0 ], \tag {6.8.18}k _ {2 1} (x) \left[ k _ {2 1} ^ {T} (x) g _ {1} ^ {T} (x) \right] = [ I 0 ], \tag {6.8.19}$$

并且 $(f_{1}(x), h_{1}(x))$ 是零状态能检测的。对于给定的 $\gamma > 0$ ，若存在正定函数 $V(x)$ 和 $W(x, \xi)$ 以及定常阵 $G$ 使得 Hamilton-Jacobi 不等式

$$\frac {\partial V}{\partial x} f (x) + \frac {1}{2} \frac {\partial V}{\partial x} \left(\frac {1}{\gamma^ {2}} g _ {1} (x) g _ {1} ^ {\mathrm{T}} (x) - g _ {2} (x) g _ {2} ^ {\mathrm{T}} (x)\right) \frac {\partial^ {\mathrm{T}} V}{\partial x} + \frac {1}{2} h _ {1} ^ {\mathrm{T}} (x) h _ {1} (x) \leqslant 0, \quad \forall x, \tag {6.8.20}\frac {\partial W}{\partial x _ {e}} f _ {e} \left(x _ {e}\right) + \frac {1}{2 \gamma^ {2}} \frac {\partial W}{\partial x _ {e}} E \left(x _ {e}\right) E ^ {T} \left(x _ {e}\right) \frac {\partial^ {T} W}{\partial x _ {e}} + \frac {1}{2} h _ {e} ^ {T} \left(x _ {e}\right) h _ {e} \left(x _ {e}\right) \leqslant 0, \quad \forall x _ {e} \tag {6.8.21}$$

成立，并且系统

$$\dot {\xi} = f (\xi) + \frac {1}{\gamma^ {2}} g _ {1} (\xi) \beta (\xi) - G h _ {2} (\xi) \tag {6.8.22}$$

在原点 $\xi = 0$ 是渐近稳定的，那么 $H_{\infty}$ 标准设计问题的解为
