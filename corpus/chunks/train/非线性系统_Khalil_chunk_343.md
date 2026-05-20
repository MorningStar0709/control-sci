把平衡点移至原点。为了简化表示,省去x和z上方的符号,状态方程为

$$
\begin{array}{l} \dot {x} = - x + z \\ \varepsilon \dot {z} = - \arctan (x + z) \\ \end{array}
$$

方程 $0 = -\arctan (x + z)$

有唯一根 $z = h(x) = -x$ 。应用变量代换 $y = z + x$ 得

$$
\begin{array}{l} \dot {x} = - 2 x + y \\ \varepsilon \dot {y} = - \arctan y + \varepsilon (- 2 x + y) \\ \end{array}
$$

对于降阶系统,取 $V(x)=(1/2)x^{2}$ , 当 $\alpha_{1}=2,\psi_{1}(x)=|x|$ 时, 满足式(11.39)。对边界层系统, 取 $W(y)=(1/2)y^{2}$ , 式(11.40) 的形式为

$$\frac {d W}{d y} [ - \arctan y ] = - y \arctan y \leqslant - \frac {\arctan \rho}{\rho} y ^ {2}$$

$y \in D_{y} = \{ y | | y | < \rho \}$ 。这样，当 $\alpha_{2} = (\arctan \rho) / \rho$ 和 $\psi_{2}(y) = |y|$ 时，满足式(11.40)。当 $\beta_{1} = 1, \beta_{2} = 2$ 和 $\gamma = 1$ 时，全局满足互联条件(11.43)和条件(11.44)。因此，对于所有 $\varepsilon < \varepsilon^{*} = (\arctan \rho) / 2\rho$ ，原点是渐近稳定的。实际上，因为 $\nu$ 和 $\dot{\nu}$ 的负定上界都是 $(x, y)$ 的二次型，所以原点是指数稳定的。

上面提出的李雅普诺夫分析可以扩展到非自治系统,这里不再详述①,我们只考虑指数稳定性的情况,并运用逆李雅普诺夫定理证明在概念上的重要结果。

定理11.4 考虑奇异扰动系统 $\dot{x} = f(t,x,z,\varepsilon)$ (11.47)

$$\varepsilon \dot {z} = g (t, x, z, \varepsilon) \tag {11.48}$$

假设下列条件对于所有

$$(t, x, \varepsilon) \in [ 0, \infty) \times B _ {r} \times [ 0, \varepsilon_ {0} ]$$

成立：

\- $f(t,0,0,\varepsilon) = 0, g(t,0,0,\varepsilon) = 0$ 。

\- 方程 $0 = g(t, x, z, 0)$

有一个孤立根 $z = h(t, x)$ ，使得 $h(t, 0) = 0$ 。

\- 对于 $z - h(t,x)\in B_{\rho}$ ，函数 $f,g$ 和 $h$ 及其一阶和二阶偏导数有界。

\- 降阶系统 $\dot{x} = f(t, x, h(t, x), 0)$

的原点是指数稳定的。

\- 边界层系统 $\frac{dy}{d\tau} = g(t,x,y + h(t,x),0)$

的原点是指数稳定的,关于 $(t,x)$ 是一致的。

则存在 $\varepsilon^{*} > 0$ ，使得对于所有 $\varepsilon < \varepsilon^{*}$ ，方程(11.47)和方程(11.48)的原点指数稳定。证明:根据定理4.14,对降阶系统存在一个李雅普诺夫函数 $V(t,x)$ ,满足

$$
\begin{array}{l} c _ {1} \| x \| ^ {2} \leqslant V (t, x) \leqslant c _ {2} \| x \| ^ {2} \\ \frac {\partial V}{\partial t} + \frac {\partial V}{\partial x} f (t, x, h (t, x), 0) \leqslant - c _ {3} \| x \| ^ {2} \\ \left\| \frac {\partial V}{\partial x} \right\| \leqslant c _ {4} \| x \| \\ \end{array}
$$

其中 $c_{i}$ 是正常数, $i=1,\cdots,4$ , 且 $x\in B_{r_{0}}$ , $r_{0}\leqslant r$ 。根据引理 9.8, 对边界层系统存在一个李雅普诺夫函数 $W(t,x,y)$ , 满足
