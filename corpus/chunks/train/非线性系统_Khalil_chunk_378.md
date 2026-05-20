# 13.2 输入-输出线性化

考虑单输入-单输出系统

$$\dot {x} = f (x) + g (x) u \tag {13.7}y = h (x) \tag {13.8}$$

其中 $f, g$ 和 $h$ 在定义域 $D \subset R^n$ 上足够光滑。映射 $f: D \to R^n$ 和 $g: D \to R^n$ 称为 $D$ 上的向量场。导数 $\dot{y}$ 为

$$\dot {y} = \frac {\partial h}{\partial x} [ f (x) + g (x) u ] \stackrel {\mathrm{def}} {=} L _ {f} h (x) + L _ {g} h (x) u$$

其中 $L_{f}h(x)=\frac{\partial h}{\partial x}f(x)$

称为 h 关于 f 或沿 f 的 Lie 导数, 这种表示方法类似于 h 沿系统 $\dot{x}=f(x)$ 轨迹的导数。当重复计算关于同一向量场或一新向量场的导数时, 这种新表示法较为方便。例如, 要用到以下表示:

$$L _ {g} L _ {f} h (x) = \frac {\partial \left(L _ {f} h\right)}{\partial x} g (x)L _ {f} ^ {2} h (x) = L _ {f} L _ {f} h (x) = \frac {\partial \left(L _ {f} h\right)}{\partial x} f (x)L _ {f} ^ {k} h (x) = L _ {f} L _ {f} ^ {k - 1} h (x) = \frac {\partial \left(L _ {f} ^ {k - 1} h\right)}{\partial x} f (x)L _ {f} ^ {0} h (x) = h (x)$$

如果 $L_{g}h(x) = 0$ ，则 $\dot{y} = L_f h(x)$ ，与 $u$ 无关。如果继续计算 $y$ 的二阶导数，记为 $y^{(2)}$ ，得

$$y ^ {(2)} = \frac {\partial (L _ {f} h)}{\partial x} [ f (x) + g (x) u ] = L _ {f} ^ {2} h (x) + L _ {g} L _ {f} h (x) u$$

同样，如果 $L_{g}L_{f}h(x) = 0$ ，则 $y^{(2)} = L_f^2 h(x)$ ，且与 $u$ 无关。重复这一过程可看出，如果 $h(x)$ 满足

$$L _ {g} L _ {f} ^ {i - 1} h (x) = 0, \quad i = 1, 2, \dots , \rho - 1; \quad L _ {g} L _ {f} ^ {\rho - 1} h (x) \neq 0$$

则 u 不会出现在 $y, \dot{y}, \cdots, y^{(\rho-1)}$ 的方程中，但出现在 $y^{(\rho)}$ 的方程中，带一个非零系数，即

$$y ^ {(\rho)} = L _ {f} ^ {\rho} h (x) + L _ {g} L _ {f} ^ {\rho - 1} h (x) u$$

上述方程清楚地表明系统是可输入-输出线性化的,因为由状态反馈控制

$$u = \frac {1}{L _ {g} L _ {f} ^ {\rho - 1} h (x)} \left[ - L _ {f} ^ {\rho} h (x) + v \right]$$

把输入-输出映射简化为

$$y ^ {(\rho)} = v$$

这是一个 $\rho$ 积分器链。这时，整数 $\rho$ 称为系统的相对阶，下面是其定义。

定义13.2 如果对于所有 $x \subset D_0$ ，有

$$L _ {g} L _ {f} ^ {i - 1} h (x) = 0, \quad i = 1, 2, \dots , \rho - 1; \quad L _ {g} L _ {f} ^ {\rho - 1} h (x) \neq 0 \tag {13.9}$$

则称非线性系统(13.7)\~(13.8)在区域 $x\in D_{0}$ 上具有相对阶 $\rho,1\leqslant\rho\leqslant n$ 。

例13.1 考虑受控范德波尔方程

$$
\begin{array}{l} \dot {x} _ {1} = x _ {2} \\ \dot {x} _ {2} = - x _ {1} + \varepsilon \left(1 - x _ {1} ^ {2}\right) x _ {2} + u, \quad \varepsilon > 0 \\ \end{array}
$$

其输出为 $y = x_{1}$ 。计算输出导数, 得

$$
\begin{array}{l} \dot {y} = \dot {x} _ {1} = x _ {2} \\ \ddot {y} = \dot {x} _ {2} = - x _ {1} + \varepsilon \left(1 - x _ {1} ^ {2}\right) x _ {2} + u \\ \end{array}
$$

因此，系统在 $R^2$ 上的相对阶为2。当输出 $y = x_{2}$ 时，有

$$\dot {y} = - x _ {1} + \varepsilon (1 - x _ {1} ^ {2}) x _ {2} + u$$

系统在 $R^2$ 上的相对阶为1。当输出 $y = x_{1} + x_{2}^{2}$ 时，有

$$\dot {y} = x _ {2} + 2 x _ {2} \left[ - x _ {1} + \varepsilon \left(1 - x _ {1} ^ {2}\right) x _ {2} + u \right]$$

系统在 $D_0 = \{x\in R^2 |x_2\neq 0\}$ 上的相对阶为1。
