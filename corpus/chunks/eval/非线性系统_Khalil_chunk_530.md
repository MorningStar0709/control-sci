# C. 17 证明定理 11.1

我们将解决由方程(11.10)和方程(11.11)以 $(x, y)$ 为变量给出的全部问题, 然后由式(11.9)的变量代换, 得出 $z$ 的误差估计。设 $y$ 属于定义域 $D_y$ , 式(11.9)映射 $D_x \times D_y$ 到 $D_z$ 。当分析方程(11.12)随 $t$ 和 $x$ 的缓慢变化的特性时, 希望用边界层模型的一致指数稳定性性质(11.15)。不等式(11.15)只有当 $x \in D_x$ 时成立, 因此为利用该式, 需要确认缓慢变化的 $x$ 总在 $D_x$ 内。我们预期其成立, 因为简化问题(11.8)的解 $\bar{x}$ 属于 $S$ , 而 $S$ 是 $D_x$ 内的一个紧子集, 此外还预期误差 $\| x(t, \varepsilon) - \bar{x}(t) \|$ 将为 $O(\varepsilon)$ , 则对于足够小的 $\varepsilon, x$ 将属于 $D_x$ 。但估计 $\| x(t, \varepsilon) - \bar{x}(t) \| = O(\varepsilon)$ 还未证明, 所以不能运用该式开始证明。我们将用一个特殊技巧解决这一难题①。如果 $D_x \neq R^n$ , 设 $E$ 是 $R^n$ 内 $D_x$ 的补集, 并定义

$$k = \frac {1}{2} \inf \left\{\| x - y \| \mid x \in S, y \in E \right\} > 0$$

如果 $D_{x}=R^{n}$ ，取 k 为任意正常数，集合

$$S _ {1} = \{x \in R ^ {n} \mid \operatorname{dist} (x, S) \leqslant k / 2 \}, \quad S _ {2} = \{x \in R ^ {n} \mid \operatorname{dist} (x, S) \leqslant k \}$$

是 $D_{x}$ 的紧子集，且 $S \subset S_{1} \subset S_{2}$ 。设 $\psi: R^{n} \to [0,1]$ 是光滑（无限多次连续可微）函数，当 $x \in S_{1}$ 时， $\psi(x) = 1$ ；当 $x$ 不属于 $S_{2}$ 时， $\psi(x) = 0^{①}$ 。定义 $F$ 和 $G$ 为

$$
\begin{array}{l} F (t, x, y, \varepsilon) = f (t, \varphi (x), y + h (t, \varphi (x)), \varepsilon) (C.67) \\ G (t, x, y, \varepsilon) = g (t, \varphi (x), y + h (t, \varphi (x)), \varepsilon) - \varepsilon \frac {\partial h}{\partial t} (t, \varphi (x)) (C.68) \\ - \varepsilon \frac {\partial h}{\partial x} (t, \varphi (x)) f (t, \varphi (x), y + h (t, \varphi (x)), \varepsilon) \\ \end{array}
$$

其中 $\varphi(x) = (x - \xi_0)\psi(x) + \xi_0$ 。容易看出，由于 $D_x$ 是凸集，因此对于所有 $x \in R^n$ ， $\varphi(x)$ 有界且属于 $D_x$ 。当 $x \in S_1$ 时，有 $\varphi(x) = x$ ，因此函数 $F$ 与 $f$ 是同一个函数。同样，函数 $G$ 和 $g - \varepsilon[(\partial h/\partial t) + (\partial h/\partial x)f]$ 也是同一函数。可以验证，对于所有 $(t, x, y, \varepsilon) \in [0, t_1] \times R^n \times \Omega_1 \times [0, \varepsilon_0]$ ，其中 $\Omega_1$ 是 $D_y$ 的任意紧子集，有

- $F$ 和 $G$ 及其对 $\varepsilon$ 的一阶偏导数是连续且有界的；  
- $F(t,x,y,0)$ 对 $(x,y)$ 的一阶偏导数有界；  
- $G(t,x,y,0)$ 和 $[\partial G(t,x,y,0) / \partial y]$ 对 $(t,x,y)$ 的一阶偏导数有界。

考虑修正奇异扰动问题

$$\dot {x} = F (t, x, y, \varepsilon), \quad x (t _ {0}) = \xi (\varepsilon) \tag {C.69}\varepsilon \dot {y} = G (t, x, y, \varepsilon), \quad y (t _ {0}) = \eta (\varepsilon) - h (t _ {0}, \xi (\varepsilon)) \tag {C.70}$$

当 $x \in S_1$ 时, 修正问题方程 (C.69) 和方程 (C.70) 等价于原始问题方程 (11.10) 和方程 (11.11)。在根据 $\bar{x}(t) \in S$ 预期解 $x(t, \varepsilon)$ 限制在 $S_1$ 内时已选择了 $S_1$ 。边界层模型

$$\frac {d y}{d \tau} = G (t, x, y, 0) \tag {C.71}$$
