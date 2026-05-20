# C. 18 证明定理 11.2

该定理的证明与定理11.1的证明极其相似,这里仅指出两个主要的不同点。一是关于证明x属于 $D_{x}$ ,要用到降阶系统的李雅普诺夫函数V;另一个是分析误差 $x-\bar{x}$ ,利用了降价系统的稳定性质。

下面利用李雅普诺夫函数 $V$ ，讨论对于所有 $t \geqslant t_0, x$ 属于紧集 $\{W_1(x) \leqslant c\}$ 。因此，不必像证明定理 11.1 那样用函数 $\psi(x)$ 截短 $x$ ，函数 $F$ 和 $G$ 仍然由式 (C.67) 和式 (C.68) 定义，但要用 $x$ 代换 $\varphi(x)$ 。与前一定理的证明一样，对于所有 $(t, x, y, \varepsilon) \in [0, \infty) \times \{W_1(x) \leqslant c\} \times \Omega_1 \times [0, \varepsilon_0]$ ，函数 $F$ 和 $G$ 性质相同，而且 $[\partial F / \partial x](t, x, 0, 0)$ 对 $x$ 是利普希茨的，对 $t$ 一致。对于所有 $x \in \{W_1(x) \leqslant c\}$ ，可重复前面的推导，证明 $y(t, \varepsilon)$ 满足式 (C.80)。因此有

$$\dot {V} \leqslant - W _ {3} (x) + k _ {6} \varepsilon + k _ {7} \exp \left[ \frac {- \alpha (t - t _ {0})}{\varepsilon} \right]$$

由 $\xi_0\in \{W_2(x)\leqslant \rho c\}$ 可看出，存在与 $\varepsilon$ 无关的时间 $T_{1} > 0$ ，使得对于足够小的 $\varepsilon$ ，对于所有 $t\in [t_0,t_0 + T_1]$ ，有 $x(t,\varepsilon)\in \{W_2(x)\leqslant c\}$ 。当 $t\geqslant t_0 + T_1$ 时，指数项 $\exp [-\alpha (t - t_0) / \varepsilon ]$ 为 $O(\varepsilon)$ ，故

$$\dot {V} \leqslant - W _ {3} (x) + k _ {8} \varepsilon$$

利用该不等式,可以证明 $\dot{V}$ 在边界 $V(t,x)=c$ 上为负。因此,对于所有 $t\geqslant t_{0},x(t,\varepsilon)\in\{W_{1}(x)\leqslant c\}$ 。

为分析逼近误差 $u(t, \varepsilon) = x(t, \varepsilon) - \bar{x}(t)$ ，把方程(C.69)看成降价系统(C.73)的扰动。这里不用Gronwall-Bellman引理推导 $u$ 的估计，而是用李雅普诺夫分析法研究方程(C.73)原点的指数稳定性。李雅普诺夫分析法与证明定理11.1中的边界层分析法非常相似，因此只做简要描述。误差 $u$ 满足方程 $\dot{u} = F(t, u, 0, 0) + \Delta F$ (C.86)

其中 $\Delta F = [F(t, \bar{x} + u, 0, 0) - F(t, \bar{x}, 0, 0) - F(t, u, 0, 0)] + [F(t, x, y, \varepsilon) - F(t, x, 0, 0)]$

可以验证 $\| \Delta F\| \leqslant \tilde{k}_4\| u\|^2 +\tilde{k}_5\| u\| \| \bar{x}\| +\tilde{k}_6\exp \left[\frac{-\alpha(t - t_0)}{\varepsilon}\right] + \varepsilon \tilde{k}_7$

把系统(C.86)看成系统 $\dot{u}=F(t,u,0,0)$ (C.87)

的扰动。由于系统(C.87)的原点是指数稳定的,故可利用定理4.14得到一个李雅普诺夫函数 $\tilde{V}(t,u)$ ,利用该函数及方程(C.86),可得

$$
\begin{array}{l} \dot {\tilde {V}} = \frac {\partial \tilde {V}}{\partial t} + \frac {\partial \tilde {V}}{\partial u} F (t, u, 0, 0) + \frac {\partial \tilde {V}}{\partial u} \Delta F \\ \leqslant - \tilde {c} _ {3} \| u \| ^ {2} + \tilde {c} _ {4} \| u \| \left\{\tilde {k} _ {4} \| u \| ^ {2} + \tilde {k} _ {5} \| u \| \| \bar {x} \| + \tilde {k} _ {6} \exp \left[ \frac {- \alpha (t - t _ {0})}{\varepsilon} \right] + \varepsilon \tilde {k} _ {7} \right\} \\ \end{array}
$$

当 $\| u\| \leqslant \tilde{c}_3 / 2\tilde{c}_4\tilde{k}_4$ 时，有
