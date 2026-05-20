通过选择 $\alpha_{i}(i=1,2,3)$ 使 $\overline{A}$ 为 Hurwitz，则对于任意给定的对称正定阵 Q，存在对称正定阵 P 满足如下 Lyapunov 方程：

$$\overline {{{A}}} ^ {\mathrm{T}} P + P \overline {{{A}}} + Q = 0 \tag {5.41}$$

定义观测器的 Lyapunov 函数为

$$V _ {\mathrm{o}} = \varepsilon \boldsymbol {\eta} ^ {\mathrm{T}} \boldsymbol {P} \boldsymbol {\eta} \tag {5.42}$$

则

$$
\begin{array}{l} \dot {V} _ {\mathrm{o}} = \varepsilon \dot {\boldsymbol {\eta}} ^ {\mathrm{T}} \boldsymbol {P} \boldsymbol {\eta} + \varepsilon \boldsymbol {\eta} ^ {\mathrm{T}} \boldsymbol {P} \dot {\boldsymbol {\eta}} \\ = (\bar {A} \eta + \varepsilon \bar {B} f) ^ {\mathrm{T}} P \eta + \eta^ {\mathrm{T}} P (\bar {A} \eta + \varepsilon \bar {B} f) \\ = \boldsymbol {\eta} ^ {T} \overline {{\boldsymbol {A}}} ^ {T} \boldsymbol {P} \boldsymbol {\eta} + \varepsilon (\overline {{\boldsymbol {B}}} \dot {f}) ^ {T} \boldsymbol {P} \boldsymbol {\eta} + \boldsymbol {\eta} ^ {T} \boldsymbol {P} \overline {{\boldsymbol {A}}} \boldsymbol {\eta} + \varepsilon \boldsymbol {\eta} ^ {T} \boldsymbol {P} \overline {{\boldsymbol {B}}} \dot {f} \\ = \boldsymbol {\eta} ^ {T} (\overline {{\boldsymbol {A}}} ^ {T} \boldsymbol {P} + \boldsymbol {P} \overline {{\boldsymbol {A}}}) \boldsymbol {\eta} + 2 \varepsilon \boldsymbol {\eta} ^ {T} \boldsymbol {P} \overline {{\boldsymbol {B}}} \dot {f} \\ \leqslant - \boldsymbol {\eta} ^ {T} \boldsymbol {Q} \boldsymbol {\eta} + 2 \varepsilon \| \boldsymbol {P} \overline {{\boldsymbol {B}}} \| \cdot \| \boldsymbol {\eta} \| \cdot | \dot {f} | \\ \end{array}
$$

且

$$\dot {V} _ {\mathrm{o}} \leqslant - \lambda_ {\min} (\boldsymbol {Q}) \| \boldsymbol {\eta} \| ^ {2} + 2 \varepsilon L \| \boldsymbol {P} \overline {{\boldsymbol {B}}} \| \| \boldsymbol {\eta} \|$$

式中， $\lambda_{\min}(Q)$ 为 Q 的最小特征值。

由 $\dot{V}_{o}\leqslant0$ 可得观测器的收敛条件为

$$\| \eta \| \leqslant \frac {2 \varepsilon L \| P \overline {{{B}}} \|}{\lambda_ {\min} (Q)} \tag {5.43}$$

由式（5.43）可见， $\eta$ 与 $\varepsilon$ 有关，如果取 $\varepsilon$ 很小，可使观测器的收敛误差减小。

注：

（1）如果扩张观测器的初始值与对象的初值不同，对于很小的 $\varepsilon$ ，将产生峰值现象，造成观测器的收敛效果差。为了防止峰值现象，设计 $\varepsilon$ 为 $^{[8]}$

$$
\frac {1}{\varepsilon} = R = \left\{ \begin{array}{l l} 1 0 0 t ^ {3}, & 0 \leqslant t \leqslant 1 \\ 1 0 0, & t > 1 \end{array} \right. \tag {5.44}
$$

或
