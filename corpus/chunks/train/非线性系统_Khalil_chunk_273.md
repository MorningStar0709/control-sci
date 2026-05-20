$$
\begin{array}{l} \dot {x} _ {i} = \frac {1}{C _ {i}} \dot {u} _ {i} = \frac {1}{C _ {i}} \left[ \sum_ {j} T _ {i j} g _ {j} \left(x _ {j} + u _ {j} ^ {*}\right) - \frac {1}{R _ {i}} \left(x _ {i} + u _ {i} ^ {*}\right) + I _ {i} \right] \\ = \frac {1}{C _ {i}} \left[ \sum_ {j} T _ {i j} \eta_ {j} \left(x _ {j}\right) - \frac {1}{R _ {i}} x _ {i} \right] \\ \end{array}
$$

其中 $\eta_{i}(x_{i}) = g_{i}(x_{i} + u_{i}^{*}) - g_{i}(u_{i}^{*})$

假设 $\eta_{i}(\cdot)$ 满足扇形区域条件

$$\sigma^ {2} k _ {i 1} \leqslant \sigma \eta_ {i} (\sigma) \leqslant \sigma^ {2} k _ {i 2}, \quad \sigma \in [ - r _ {i}, r _ {i} ]$$

其中， $k_{i1}$ 和 $k_{i2}$ 是正常数。图9.1表明，当 $g_{i}(u_{i})=(2V_{M}/\pi)\arctan(\lambda\pi u_{i}/2V_{M}),\lambda>0$ 时，该条件确实成立。以式(9.32)的形式重写该系统，其中

$$f _ {i} (x _ {i}) = - \frac {1}{C _ {i} R _ {i}} x _ {i} + \frac {1}{C _ {i}} T _ {i i} \eta_ {i} (x _ {i}), \quad g _ {i} (x) = \frac {1}{C _ {i}} \sum_ {j \neq i} T _ {i j} \eta_ {j} (x _ {j})$$

用 $V_{i}(x_{i}) = \frac{1}{2} C_{i}x_{i}^{2}$

作为第 $i$ 个孤立子系统的备选李雅普诺夫函数，可得

$$\frac {\partial V _ {i}}{\partial x _ {i}} f _ {i} (x _ {i}) = - \frac {1}{R _ {i}} x _ {i} ^ {2} + T _ {i i} x _ {i} \eta_ {i} (x _ {i})$$

如果 $T_{ii} \leqslant 0$ ，则 $T_{ii}x_i\eta_i(x_i) \leqslant -|T_{ii}|k_{i1}x_i^2$

且 $\frac{\partial V_i}{\partial x_i} f_i(x_i) \leqslant -\left(\frac{1}{R_i} + |T_{ii}|k_{i1}\right)x_i^2$

它是负定的。如果 $T_{ii} > 0$ ，则 $T_{ii}x_i\eta_i(x_i)\leqslant T_{ii}k_{i2}x_i^2$

且 $\frac{\partial V_i}{\partial x_i} f_i(x_i) \leqslant -\left(\frac{1}{R_i} - T_{ii} k_{i2}\right) x_i^2$

在这种情况下，假设 $T_{ii}k_{i2} < 1 / R_i$ ，使 $V_{i}$ 的导数负定。为了简化表示，设

$$
\delta_ {i} = \left\{ \begin{array}{l l} | T _ {i i} | k _ {i 1}, & T _ {i i} \leqslant 0 \\ - T _ {i i} k _ {i 2}, & T _ {i i} > 0 \end{array} \right.
$$

则 $V_{i}(x_{i})$ 在区间 $[-r_i, r_i]$ 上满足式(9.34)和式(9.35)，其中

$$\alpha_ {i} = \left(\frac {1}{R _ {i}} + \delta_ {i}\right), \beta_ {i} = C _ {i}, \phi_ {i} (x _ {i}) = | x _ {i} |$$

这里假设 $\alpha_{i}$ 是正的。互联项 $g_{i}(x)$ 满足不等式

$$| g _ {i} (x) | \leqslant \frac {1}{C _ {i}} \sum_ {j \neq i} | T _ {i j} | | \eta_ {j} (x _ {j}) | \leqslant \frac {1}{C _ {i}} \sum_ {j \neq i} | T _ {i j} | k _ {j 2} | x _ {j} |$$

这样， $g_{i}(x)$ 满足式(9.36)，其中 $\gamma_{ii} = 0$ ，当 $i\neq j$ 时， $\gamma_{ij} = k_{j2}|T_{ij}| / C_i$ 。现在可以由

$$
s _ {i j} = \left\{ \begin{array}{l l} \delta_ {i} + 1 / R _ {i}, & i = j \\ - | T _ {i j} | k _ {j 2}, & i \neq j \end{array} \right.
$$

构成矩阵 S。如果 S 是一个 M 矩阵，则平衡点 $u^{*}$ 是渐近稳定的。可以用集合
