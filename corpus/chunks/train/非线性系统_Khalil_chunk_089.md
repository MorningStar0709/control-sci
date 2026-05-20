其中 $\gamma = \| y_0 - z_0\|$ 。对函数 $\| y(t) - z(t)\|$ 应用Gronwall-Bellman不等式（见引理A.1），得到

$$\| y (t) - z (t) \| \leqslant \gamma + \mu (t - t _ {0}) + \int_ {t _ {0}} ^ {t} L [ \gamma + \mu (s - t _ {0}) ] \exp [ L (t - s) ] d s$$

对右边进行分步积分,得

$$
\begin{array}{l} \left\| y (t) - z (t) \right\| \leqslant \gamma + \mu \left(t - t _ {0}\right) - \gamma - \mu \left(t - t _ {0}\right) + \gamma \exp \left[ L \left(t - t _ {0}\right) \right] \\ + \int_ {t _ {0}} ^ {t} \mu \exp [ L (t - s) ] d s \\ = \gamma \exp [ L (t - t _ {0}) ] + \frac {\mu}{L} \left\{\exp [ L (t - t _ {0}) ] - 1 \right\} \\ \end{array}
$$

证毕。

![](image/3cf6332d185a3dacdc0e3c484efb3be03a461c91ff353f8c55b6e182c8e9e349.jpg)

有了定理 3.4, 就可以证明下面的定理, 该定理说明解的连续性与初始状态和参数的关系。

定理3.5 设 $f(t, x, \lambda)$ 在 $[t_0, t_1] \times D \times \{\| \lambda - \lambda_0 \| \leqslant c\}$ 上对 $(t, x, \lambda)$ 分段连续，且对 $x$ 是局部利普希茨的（对 $t$ 和 $\lambda$ 是一致的），其中 $D \subset R^n$ 是开连通集。设 $y(t, \lambda_0)$ 是 $\dot{x} = f(t, x, \lambda_0)$ ， $y(t_0, \lambda_0) = y_0 \in D$ 的解。假设对于所有 $t \in [t_0, t_1]$ ， $y(t, \lambda_0)$ 有定义，且属于 $D$ ，那么对于给定的 $\varepsilon > 0$ ，存在 $\delta > 0$ ，如果

$$\left\| z _ {0} - y _ {0} \right\| < \delta , \quad \left\| \lambda - \lambda_ {0} \right\| < \delta$$

那么 $\dot{x} = f(t,x,\lambda),z(t_0,\lambda) = z_0$ ，有定义在 $[t_0,t_1]$ 上的唯一解 $z(t,\lambda)$ ，且 $z(t,\lambda)$ 满足

$$\left\| z (t, \lambda) - y (t, \lambda_ {0}) \right\| < \varepsilon , \quad \forall t \in [ t _ {0}, t _ {1} ]$$

证明:由 $y(t,\lambda_{0})$ 对 t 的连续性和在 $[t_{0},t_{1}]$ 上的紧性可知, $y(t,\lambda_{0})$ 在 $[t_{0},t_{1}]$ 上是有界的。在解 $y(t,\lambda_{0})$ 周围由

$$U = \{(t, x) \in [ t _ {0}, t _ {1} ] \times R ^ {n} \mid \| x - y (t, \lambda_ {0}) \| \leqslant \varepsilon \}$$

定义一条管子 $U$ (见图3.1)。假设 $U \subset [t_0, t_1] \times D$ , 如果不满足该条件, 应用 $\varepsilon_1 < \varepsilon$ 代换 $\varepsilon$ , $\varepsilon_1$ 足够小, 以保证 $U \subset [t_0, t_1] \times D$ , 并继续用 $\varepsilon_1$ 进行证明。 $U$ 是紧集, 因此 $f(t, x, \lambda)$ 在 $U$ 上对 $x$ 是利普希茨的, 其利普希茨常数为 $L$ 。由 $f$ 对 $\lambda$ 的连续性, 对于任意 $\alpha > 0$ , 存在 $\beta > 0 (\beta < c)$ , 使

$$\| f (t, x, \lambda) - f (t, x, \lambda_ {0}) \| < \alpha , \forall (t, x) \in U, \forall \| \lambda - \lambda_ {0} \| < \beta$$

取 $\alpha < \varepsilon$ ，且 $\| z_0 - y_0\| < \alpha$ 。根据局部存在性和唯一性定理，在某一时间区间 $[t_0,t_0 + \Delta ]$ 内，一定存在唯一解 $z(t,\lambda)$ 。这个解从管子 $U$ 内部开始，并且只要在管内就可以扩展。我们将证明，选择一个足够小的 $\alpha$ ，使对于所有 $t\in [t_0,t_1]$ ，解总保持在 $U$ 内。特别地，设 $\tau$ 为解离开管子的第一时间，证明可以使 $\tau >t_1$ 。在时间区间 $[t_0,\tau ]$ 上，当 $\mu = \alpha$ 时满足定理3.4的条件。因此
