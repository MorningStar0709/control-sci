$$\dot {z} _ {k} = \sum_ {2 | T | + | S | = L} \frac {1}{T ! S !} \frac {\partial^ {| T | + | S |} q _ {k}}{\partial (x _ {1}) ^ {\mathrm{T}} \partial z ^ {S}} (0) z ^ {S} \left(\prod_ {i = 1} ^ {m} (\psi_ {i}) ^ {T _ {i}} (z)\right), \quad k = 1, \dots , t \tag {8.6.41}$$

在原点渐近稳定，则系统(8.6.29)是一个状态反馈能镇定系统，并且，如果上述条件满足，令 $\psi_i^{(2)} = \psi_i$ ，则式(8.6.31)就是可行控制.

证明 利用控制 (8.6.31), 条件 (8.6.36) 和条件 (8.6.37) 确保闭环系统的中心流形的动力系统的最低阶为 $L$ . 注意在这种情况下 $d_{i} = e = L, i = 1, \dots, m$ . 条件 (8.6.35)\~ 条件 (8.6.37) 保证确保中心流形可表示为

$$
\begin{array}{l} x _ {1} ^ {i} = \psi_ {i} (z) + R _ {i}, \quad R _ {i} = 0 (\| z \| ^ {L + 1}); \\ \overline {{{x}}} _ {1} ^ {i} = 0 \left(\| z \| ^ {L + 1}\right), \quad i = 1, \dots , m; \\ w = 0 (\| z \| ^ {L + 1}). \\ \end{array}
$$

利用式 (8.6.36)\~式 (8.6.37), $R_{i}, \overline{x}_{1}^{i}$ 和 $w$ 将不会出现在阶数为 $L$ 的项, 故最后闭环系统中所有的阶为 $L$ 的项正好是系统 (8.6.41) 右边的动力系统, 因此系统 (8.6.41) 是中心流形动力系统的近似系统. 由于系统 (8.6.41) 在原点齐次渐近稳定, 定理 8.6.5 保证了闭环系统中心流形动力系统的近似稳定性. 由定理 8.6.7 可知闭环系统的渐近稳定性.

当 $d_{k} = 3, k = 1, \dots, t$ , 这是一种有趣情况. 设 $h = 2$ , 及 $L = 3$ , 则可得如下简单结论:

推论8.6.2 系统(8.6.29)(其中 $C = 0$ )是状态反馈能镇定的，如果

(1) $\frac{\partial p}{\partial x_1^i}(0) = 0,\quad \frac{\partial^2p}{\partial x_1^i\partial z}(0) = 0,\quad i = 1,\dots ,m,$

$$\frac {\partial p}{\partial z} (0) = 0, \quad \frac {\partial^ {2} p}{\partial z ^ {2}} (0) = 0, \quad \frac {\partial^ {3} p}{\partial z ^ {3}} (0) = 0;$$

(2) $\frac{\partial q}{\partial x} (0) = 0, \quad \frac{\partial q}{\partial z} (0) = 0, \quad \frac{\partial^2 q}{\partial z^2} (0) = 0;$

(3) 存在一个二次齐次向量场

$$\psi (z) = \operatorname{col} (\psi_ {1}, \dots , \psi_ {m}),$$

使得

$$\dot {z} = D (z) \psi (z) + E (z) \tag {8.6.42}$$

是渐近稳定的，这里 $D(z)$ 和 $E(z)$ 是 $t \times m$ 及 $t \times 1$ 矩阵，其元素分别为

$$D _ {i j} = \sum_ {k = 1} ^ {t} \frac {\partial^ {2} q _ {i}}{\partial x _ {1} ^ {j} \partial z _ {k}} (0) z _ {k}, \quad i = 1, \dots , t, \quad j = 1, \dots , m,E _ {i} = \sum_ {| S | = 3} \frac {\partial^ {3} q _ {i}}{S ! \partial z ^ {S}} (0) z ^ {S}, \quad i = 1, \dots , t.$$

进而若令 $\psi_i^{(2)} = \psi_i$ ，则式 (8.6.31) 是系统 (8.6.29) 的可行镇定控制。

下面说明注入阶为3时，我们只要解一个代数不等式即可得到所要求的控制.

例 8.6.5 考虑以下系统:

$$
\left\{ \begin{array}{l} \dot {x} _ {1} = x _ {2}, \\ \dot {x} _ {2} = f _ {1} (x, z) + g _ {1} (x, z) u _ {1}, \\ \dot {x} _ {3} = f _ {2} (x, z) + g _ {2} (x, z) u _ {2}, \\ \dot {z} _ {1} = q _ {1} (x, z), \\ \dot {z} _ {2} = q _ {2} (x, z), \end{array} \right. \tag {8.6.43}
$$

这里 $f_{i}(0) = 0, g_{i}(0) \neq 0, q_{i}, i = 1,2$ 满足推论8.6.2中的条件(2). 我们的目的是找到系统(8.6.43)能反馈镇定的充分条件. 记
