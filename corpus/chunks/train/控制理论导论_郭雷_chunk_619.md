$$
(F ^ {- 1}) _ {*} (f) = \left[ \begin{array}{c} \mathrm{e} ^ {z _ {2} - z _ {3}} (z _ {4} + 1) ^ {- 1} + \mathrm{e} ^ {- z _ {2} - z _ {3}} - \mathrm{e} ^ {- z _ {3}} + 1 \\ \mathrm{e} ^ {z _ {2}} (z _ {4} + 1) - 1 \\ - \mathrm{e} ^ {z _ {2} - z _ {3}} (z _ {4} + 1) ^ {- 1} + \mathrm{e} ^ {- z _ {3}} - 1 \\ \mathrm{e} ^ {z _ {2}} (z _ {4} + 1) ^ {2} \end{array} \right],

(F ^ {- 1}) _ {*} (g) = \left[ \begin{array}{c} \left(\mathrm{e} ^ {z _ {1} + z _ {3}} - 2\right) ^ {- 1} \mathrm{e} ^ {- z _ {3}} + z _ {2} \\ \mathrm{e} ^ {z _ {1} + z _ {3}} - \mathrm{e} ^ {z _ {3}} \\ - \left(\mathrm{e} ^ {z _ {1} + z _ {3}} - 2\right) ^ {- 1} \mathrm{e} ^ {- z _ {3}} \\ (z _ {4} + 1) ^ {3} \left(\mathrm{e} ^ {z _ {1} + z _ {3}} - 2\right) ^ {- 1} \end{array} \right].
$$

现在我们选择

$$
b (z) = \left[ \begin{array}{c} - \mathrm{e} ^ {- z _ {3}} \\ (z _ {4} + 1) ^ {3} \end{array} \right].
$$

那么 $\beta_0$ 和 $\beta_{1}$ 可计算如下：

$$\beta_ {0} = \left(\mathrm{e} ^ {z _ {1} + z _ {3}} - 2\right), \quad \beta_ {1} = 1,$$

故 $\beta = \beta_0$ .

现将 $f^2$ 改写为

$$
f ^ {2} = \left[ \begin{array}{c} - \mathrm{e} ^ {z _ {3} - z _ {3}} (z _ {4} + 1) ^ {- 1} \\ \mathrm{e} ^ {z _ {2}} (z _ {4} + 1) ^ {2} \end{array} \right] + \left[ \begin{array}{c} \mathrm{e} ^ {- z _ {3}} - 1 \\ 0 \end{array} \right] := Y _ {1} + Y _ {2}.
$$

因此 $Y_{2}$ 不依赖于 $z^{1} = (z_{1}, z_{2})$ ，我们可用 $Y_{1}$ 代替 $f^{2}$ . 再利用式 (8.4.13) 可得

$$\alpha = - \beta_ {0} (b ^ {\mathrm{T}} b) ^ {- 1} b ^ {\mathrm{T}} Y _ {1} = - (\mathrm{e} ^ {z _ {1} + z _ {3}} - 2) \mathrm{e} ^ {z _ {2}} (z _ {4} + 1) ^ {- 1}.$$

最后，对上述 $(\alpha, \beta)$ 我们有

$$
f + g \alpha = \left[ \begin{array}{c} \mathrm{e} ^ {- z _ {2} - z _ {3}} - \mathrm{e} ^ {- z _ {3}} + 1 - z _ {2} (z _ {4} + 1) ^ {- 1} \mathrm{e} ^ {z _ {2}} (\mathrm{e} ^ {z _ {1} + z _ {3}} - 2) \\ \mathrm{e} ^ {z _ {2}} (z _ {4} + 1) - 1 - z _ {2} (z _ {4} + 1) ^ {- 1} \mathrm{e} ^ {z _ {2}} (\mathrm{e} ^ {z _ {1} + z _ {3}} - 2) (\mathrm{e} ^ {z _ {1} + z _ {3}} - \mathrm{e} ^ {z _ {3}}) \\ \mathrm{e} ^ {- z _ {3} - 1} \\ 0 \end{array} \right],

g \beta = \left[ \begin{array}{c} e ^ {- z _ {2}} + z _ {2} (e ^ {z _ {1} + z _ {3}} - 2) \\ (e ^ {z _ {1} + z _ {3}} - 2) (e ^ {z _ {1} + z _ {3}} - e ^ {z _ {3}}) \\ e ^ {- z _ {3}} \\ (z _ {4} + 1) ^ {3} \end{array} \right].
$$

容易验证式 (8.4.2) 成立.

$(f,g)$ 不变分布的一个直接应用是局部干扰解耦．考虑系统

$$
\left\{ \begin{array}{l} \dot {x} = f (x) + \sum_ {i = 1} ^ {m} g _ {i} u _ {i} + \sum_ {j = 1} ^ {s} p _ {j} (x) w _ {j} := f (x) + g (x) u + p (x) w, \\ y = h (x), \quad x \in \mathbb {R} ^ {n}, y \in \mathbb {R} ^ {p}, \end{array} \right. \tag {8.4.18}
$$

这里 u 是控制，w 是干扰.

在平衡点 $x_0$ 处的局部干扰解耦问题定义如下：

定义8.4.3 系统(8.4.18)在 $x_0$ 的局部干扰解耦问题是指寻找 $x_0$ 的一个邻域 $U$ 和一个正则反馈
