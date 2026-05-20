# 14.1.3 跟踪

考虑单输入-单输出系统

$$\dot {x} = f (x) + \delta_ {1} (x) + g (x) [ u + \delta (t, x, u) ] \tag {14.19}y = h (x) \tag {14.20}$$

其中 $x, u$ 和 $y$ 分别是状态、控制输入和受控输出。假设 $f, g, h$ 和 $\delta_1$ 在定义域 $D \subset R^n$ 内充分光滑， $\delta$ 对 $t$ 是分段连续的，且在 $(x, u)$ 上充分光滑， $(t, x, u) \in [0, \infty) \times D \times R$ 。进一步假设 $f$ 和 $h$ 已知，而 $g, \delta$ 和 $\delta_1$ 可以是不确定的。对于 $g$ 中所有可能的不确定项，假设系统

$$\dot {x} = f (x) + g (x) u \tag {14.21}y = h (x) \tag {14.22}$$

在 D 内相对阶为 $\rho$ ，即对于所有 $x \in D^{①}$ ，有

$$L _ {g} h (x) = \dots = L _ {g} L _ {f} ^ {\rho - 2} h (x) = 0, \quad L _ {g} L _ {f} ^ {\rho - 1} h (x) \geqslant a > 0$$

我们的目标是设计一个状态反馈控制律,使输出 y 渐近跟踪一个参考信号 $r(t)$ , 其中

- $r(t)$ 及其导数直到 $r^{(\rho)}(t)$ 对于所有 $t \geqslant 0$ 都是有界的，且第 $\rho$ 阶导数 $r^{(\rho)}(t)$ 是 $t$ 的分段连续函数。  
- 信号 $r, \cdots, r^{(\rho)}$ 可在线获得。

从对输入-输出线性化(13.2节)的研究可以知道,系统(14.21)\~(14.22)通过变量代换

$$
\left[ \begin{array}{c} \eta \\ - \frac {}{} - \frac {}{} - \xi \end{array} \right] = \left[ \begin{array}{c} \phi (x) \\ - \frac {}{} - \frac {}{} - \psi (x) \end{array} \right] = \left[ \begin{array}{c} \phi_ {1} (x) \\ \vdots \\ \phi_ {n - \rho} (x) \\ - \frac {}{} - \frac {}{} - h (x) \\ \vdots \\ L _ {f} ^ {\rho - 1} h (x) \end{array} \right] = T (x) \tag {14.23}
$$

可转换为标称形式,其中 $\phi_{1}$ 到 $\phi_{n-\rho}$ 满足偏微分方程

$$\frac {\partial \phi_ {i}}{\partial x} g (x) = 0, 1 \leqslant i \leqslant n - \rho , \forall x \in D$$

假设 $T(x)$ 在 $D$ 上是微分同胚的，由于 $f$ 和 $h$ 已知，而 $g$ 可能不确定，因此函数 $\psi$ 是已知的，而 $\phi$ 可能未知。我们希望对扰动 $\delta$ 和 $\delta_{1}$ 加以限制，使得当变量代换式(14.23)运用于扰动系统(14.19)\~(14.20)时，系统仍保持标称形式结构。由相对阶条件，显然关于 $\eta$ 的状态方程与 $u$ 无关。下面计算关于 $\xi$ 的状态方程

$$\dot {\xi} _ {1} = \frac {\partial h}{\partial x} [ f + \delta_ {1} + g (u + \delta) ] = \frac {\partial h}{\partial x} (f + \delta_ {1})$$

如果 $\delta_{1}$ 属于 $[\partial h / \partial x]$ 的零空间，即对于所有 $x\in D,\left[\partial h / \partial x\right]\delta_1(x) = 0$ ，那么

$$\dot {\xi} _ {1} = L _ {f} h (x) = \xi_ {2}$$

同样 $\dot{\xi}_2 = \frac{\partial(L_f h)}{\partial x} [f + \delta_1 + g(u + \delta)] = \frac{\partial(L_f h)}{\partial x} (f + \delta_1)$

如果对于所有 $x \in D, \delta_1$ 属于 $[\partial (L_f h) / \partial x]$ 的零空间，则

$$\dot {\xi} _ {2} = L _ {f} ^ {2} h (x) = \xi_ {2}$$

如此反复即可推出,如果

$$\frac {\partial (L _ {f} ^ {i} h)}{\partial x} \delta_ {1} (x) = 0, \quad 1 \leqslant i \leqslant \rho - 2, \quad \forall x \in D \tag {14.24}$$

式 $(14.23)$ 的变量代换产生系统的标称形式
