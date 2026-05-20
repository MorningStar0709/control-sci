# 10.1 扰动法

考虑系统

$$\dot {x} = f (t, x, \varepsilon) \tag {10.1}$$

其中， $f: [t_{0}, t_{1}] \times D \times [-\varepsilon_{0}, \varepsilon_{0}] \rightarrow R^{n}$ 在定义域 $D \subset R^{n}$ 上关于自变量是充分光滑的，所要求的光滑条件将在后续内容中讲述。假设对于给定初始状态

$$x (t _ {0}) = \eta (\varepsilon) \tag {10.2}$$

解状态方程(10.1)，其中，一般情况下允许初始状态“光滑地”依赖于 $\varepsilon$ 。方程(10.1)和方程(10.2)的解取决于参数 $\varepsilon$ ，为了强调这一点将解记为 $x(t,\varepsilon)$ 。扰动法的目的是寻找“小”扰动参数（以构造对足够小的 $|\varepsilon |$ 成立的近似解。在方程(10.1)和方程(10.2)中，设 $\varepsilon = 0$ 为最简单的近似，得出标称问题或非扰动问题

$$\dot {x} = f (t, x, 0), \quad x \left(t _ {0}\right) = \eta_ {0} \tag {10.3}$$

其中， $\eta_0 = \eta(0)$ 。假设该问题有定义在 $[t_0, t_1]$ 上的唯一解 $x_0(t)$ ，且对于所有 $t \in [t_0, t_1]$ ，有 $x_0(t) \in D$ 。进一步假设对于 $[t_0, t_1] \times D \times [-\varepsilon_0, \varepsilon_0]$ 内的 $(t, x, \varepsilon)$ ， $f$ 对 $(t, x, \varepsilon)$ 是连续的，对 $(x, \varepsilon)$ 是局部利普希茨的，对 $t$ 一致，而 $\eta$ 对 $\varepsilon$ 是局部利普希茨的。扰动与非扰动问题的闭式解是根据解相对于初始状态和参数的连续性得出的。特别地，定理3.5说明存在一个正常数 $\varepsilon_1 \leqslant \varepsilon_0$ ，使得对于所有 $|\varepsilon| \leqslant \varepsilon_1$ ，方程(10.1)和方程(10.2)在 $[t_0, t_1]$ 上有唯一解 $x(t, \varepsilon)$ 。更进一步，定理3.4说明存在一个正数 $k$ ，使得

$$\left\| x (t, \varepsilon) - x _ {0} (t) \right\| \leqslant k | \varepsilon |, \forall | \varepsilon | < \varepsilon_ {1}, \forall t \in \left[ t _ {0}, t _ {1} \right] \tag {10.4}$$

当近似误差满足式(10.4)的边界时,则称误差具有 $O(\varepsilon)$ 的数量级,记为

$$x (t, \varepsilon) - x _ {0} (t) = O (\varepsilon)$$

数量级的记法在本章和下一章中会经常用到,其定义如下。

定义10.1 如果存在正常数 $k$ 和 $c$ , 使得

$$\left| \delta_ {1} (\varepsilon) \right| \leqslant k \left| \delta_ {2} (\varepsilon) \right|, \quad \forall | \varepsilon | < c$$

则 $\delta_1(\varepsilon) = O(\delta_2(\varepsilon))$ 。

例10.1

\- 对于所有 $n \geqslant m$ ，有 $\varepsilon^n = O(\varepsilon^m)$ ，因为

$$| \varepsilon | ^ {n} = | \varepsilon | ^ {m} | \varepsilon | ^ {n - m} < | \varepsilon | ^ {m}, \forall | \varepsilon | < 1$$

\- $\varepsilon^2 / (0.5 + \varepsilon) = O(\varepsilon^2)$ , 因为

$$\left| \frac {\varepsilon^ {2}}{0 . 5 + \varepsilon} \right| < \frac {1}{0 . 5 - a} | \varepsilon | ^ {2}, \forall | \varepsilon | < a < 0. 5$$

\- $1 + 2\varepsilon = O(1)$ ，因为 $|1 + 2\varepsilon | <   1 + 2a,\forall |\varepsilon | <   a$

\- 当 $a$ 和 $\varepsilon$ 为正时, $\exp(-a/\varepsilon) = O(\varepsilon^n)$ , $n$ 为任意正整数, 因为

$$\frac {e ^ {- a / \varepsilon}}{\varepsilon^ {n}} \leqslant \left(\frac {n}{a}\right) ^ {n} e ^ {- n}, \forall \varepsilon > 0$$
