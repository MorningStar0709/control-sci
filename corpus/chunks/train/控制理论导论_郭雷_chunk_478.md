$$f (\eta) + f _ {1} (\eta , a (\eta) + \widetilde {y}) (a (\eta) + \widetilde {y}) = f _ {a} (\eta) + f _ {a 1} (\eta , \widetilde {y}) \widetilde {y},$$

即系统 (6.9.14) 与系统 (6.9.6) 是反馈等价的。因此只要我们能够对系统 (6.9.14) 得到满足 $L^2$ 增益条件且保证闭环系统稳定性的控制器，就可以得到系统 (6.9.6) 所对应的理想控制器。显然，系统 (6.9.14) 满足定理 6.9.1 的假设条件，即当 $\tilde{y} = 0$ 时， $\eta-$ 子系统在原点是渐近稳定的。

因此只要评价信号 $z$ 对于 $\tilde{y}$ 满足 $z = h_{\alpha}(\eta, \tilde{y})\tilde{y}$ , 或者等价地

$$h _ {0} (\eta , a (\eta)) a (\eta) = 0,$$

那么就可以利用定理6.9.1得到理想的控制器。实际上，即使 $z$ 不满足这个条件，本节后面的内容表明，我们也同样可以得到理想的控制器。

下面我们考虑更具一般性的系统。为了记号简洁，以下我们采用 Lie-微分等微分几何学的符号，可参阅本书第3章。

考虑如下非线性系统：

$$
\left\{ \begin{array}{l} \dot {x} = f (x) + g _ {1} (x) w + g _ {2} (x) u, \\ z = h (x). \end{array} \right. \tag {6.9.15}
$$

如果对于该系统，我们能够找到辅助的输出信号

$$y = h _ {a} (x), \tag {6.9.16}$$

使得 $y$ 对于控制输入 $u$ 的相对阶为 1, 并且 $g_{1}(x)$ 和 $g_{2}(x)$ 满足如下匹配条件:

$$g _ {1} (x) = g _ {2} (x) g _ {m} (x), \quad \forall x, \tag {6.9.17}$$

那么一定存在坐标变换

$$
\left[ \begin{array}{l} \xi \\ y \end{array} \right] = \phi (x) = \left[ \begin{array}{l} T (x) \\ h _ {a} (x) \end{array} \right], \tag {6.9.18}
$$

使得受控对象 (6.9.15) 与系统

$$
\left\{ \begin{array}{l} \dot {\xi} = f _ {0} (\xi , y), \\ \dot {y} = p (\xi , y) w + v, \\ z = h (\xi , y), \end{array} \right. \tag {6.9.19}
$$

是反馈等价的，其中 $v$ 是控制输入，而

$$p (\xi , y) = L _ {g _ {2}} h _ {a} \left(\phi^ {- 1} (x)\right) g _ {m} \left(\phi^ {- 1} (x)\right), \quad h (\xi , y) = h \left(\phi^ {- 1} (x)\right).$$

以下我们只讨论系统 (6.9.19) 的 $H_{\infty}$ 设计问题. 记 $y = 0$ 时的零输出动态为

$$\dot {\xi} = f _ {0} (\xi , 0) = f _ {*} (\xi). \tag {6.9.20}$$

定理 6.9.2 假设对零输出动态 (6.9.20) 存在正定函数 $W(\xi)(W(0)=0)$ 和正定函数 $Q(\xi)$ 使得

$$L _ {f.} W (\xi) \leqslant - Q (\xi), \tag {6.9.21}\frac {1}{2} h _ {*} ^ {\mathbf {T}} (\xi) h _ {*} (\xi) \leqslant Q (\xi), \forall \xi , \tag {6.9.22}$$

那么对于任意给定的 $\gamma > 0$ , 受控对象 (6.9.19) 所对应的 $H_{\infty}$ 控制器为

$$v = - y - L _ {F} ^ {\mathrm{T}} W (\xi) - H ^ {\mathrm{T}} (\xi , y) - \frac {1}{2 \gamma^ {2}} p (\xi , y) p ^ {\mathrm{T}} (\xi , y) y, \tag {6.9.23}$$

其中

$$h _ {*} (\xi) = h (\xi , 0),\frac {1}{2} h ^ {\mathrm{T}} (\xi , y) h (\xi , y) = \frac {1}{2} h _ {*} ^ {\mathrm{T}} (\xi) h _ {*} (\xi) + H (\xi , y) y,f _ {0} (\xi , y) = f _ {*} (\xi) + F (\xi , y) y.$$

证明 设定义正定函数 $V$ 如下：

$$V (\xi , y) = W (\xi) + \frac {1}{2} y ^ {\mathrm{T}} y, \tag {6.9.24}$$

则沿闭环系统的状态轨迹有
