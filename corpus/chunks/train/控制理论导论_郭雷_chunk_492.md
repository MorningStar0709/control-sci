$$
\left\{ \begin{array}{l} \dot {\psi} ^ {T} + \frac {\partial H (x ^ {*} (t) , u ^ {*} (t) , \psi)}{\partial x} = 0, \\ \psi^ {T} (t _ {f}) + \frac {\partial k (x ^ {*} (t _ {f}))}{\partial x} = 0 \end{array} \right. \tag {7.1.16}
$$

在 $[t_0, t_f]$ 上有唯一解。现选方程 (7.1.16) 的解 $\psi(t)$ 作为 Lagrange 乘子向量值函数。于是从式 (7.1.15) 得

$$\int_ {t _ {\mathrm{D}}} ^ {t _ {f}} \left. \frac {\partial H}{\partial u} \right| _ {*} \delta u (t) \mathrm{d} t = 0.$$

由此及 $\delta u$ 的任意性，根据引理7.1.1即得

$$\left. \frac {\partial H}{\partial u} \right| _ {*} = \frac {\partial H (x ^ {*} (t) , u ^ {*} (t) , \psi (t))}{\partial u} - 0, \quad \forall t \in [ t _ {0}, l _ {f} ]. \tag {7.1.17}$$

这样，由 $\delta J_{1}[u] = 0$ 和式(7.1.12)知

$$\Delta J _ {1} (\varepsilon) = J _ {1} (\varepsilon) - J _ {1} (0) = \frac {\varepsilon^ {2}}{2} \left[ \delta^ {2} J _ {1} [ u ] + o (1) \right] \geqslant 0, \quad (\varepsilon \rightarrow 0).$$

于是

$$
\begin{array}{l} \delta^ {2} J _ {1} [ u ] = \left(\delta x \left(t _ {f}\right)\right) ^ {\mathrm{T}} \frac {\partial^ {2} k}{\partial x ^ {2}} \Big | _ {*} (\delta x \left(t _ {f}\right)) \\ - \int_ {t _ {0}} ^ {t _ {f}} \left[ \delta x (t), \delta u (t) \right] \left[ \begin{array}{l l} \frac {\partial^ {2} H}{\partial x ^ {2}} \Big | _ {*} & \frac {\partial^ {2} H}{\partial x \partial u} \Big | _ {*} \\ \frac {\partial^ {2} H}{\partial u \partial x} \Big | _ {*} & \frac {\partial^ {2} H}{\partial u ^ {2}} \Big | _ {*} \end{array} \right] \left[ \begin{array}{l} \delta x (t) \\ \delta u (t) \end{array} \right] d t \geqslant 0. \\ \end{array}
$$

下面证明，当 $u^{*}(t)$ 在 $t \in [t_0, t_f]$ 连续时， $\left.\frac{\partial^2 H}{\partial u^2}\right|_*$ 为半负定阵，即

$$\left. \frac {\partial^ {2} H}{\partial u ^ {2}} \right| _ {*} = \frac {\partial^ {2} H (x ^ {*} (t) , u ^ {*} (t) , \psi (t))}{\partial u ^ {2}} \leqslant 0. \tag {7.1.18}$$

为简单起见，对任意函数 $f:[a,b]\to \mathbb{R}^r$ ，记 $\Omega (a,b;f) = \{t\in [a,b]\mid f$ 在 $t$ 处连续}.事实上，设 $\bar{t}\in \Omega (t_0,t_f;u^*)$ ，对任意 $h\in \mathbb{R}^n$ 和充分小正数 $\varepsilon_{1}$ ，取特定的 $\delta u(t)$ 为

$$
\delta u (t) = \left\{ \begin{array}{l l} 0, & t \in [ t _ {0}, \bar {t} ], \\ h, & t \in [ \bar {t}, \bar {t} + \varepsilon_ {1} ], \\ 0, & t \in [ \bar {t} + \varepsilon_ {1}, t _ {f} ]. \end{array} \right. \tag {7.1.19}
$$

于是变分方程 (7.1.9) 相应于上述 $\delta u(t)$ 的解 $\delta x(t)$ 为
