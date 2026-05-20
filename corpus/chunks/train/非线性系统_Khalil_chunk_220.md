则 $Z(s)$ 是严格正实的，其中 $G(j\omega) = \operatorname{Re}[G(j\omega)] + j\operatorname{Im}[G(j\omega)]$ 。以 $\omega$ 作为参数绘制 $\operatorname{Re}[G(j\omega)]$ 与 $\omega \operatorname{Im}[G(j\omega)]$ 的关系曲线。如果曲线位于以 $1 / \gamma$ 为斜率，过 $-(1 / k) + j0$ 点的直线右侧，则满足条件(7.19)。这样的曲线称为Popov曲线，而奈奎斯特曲线是 $\operatorname{Re}[G(j\omega)]$ 与 $\operatorname{Im}[G(j\omega)]$ 的关系曲线。如果仅当 $\omega \in (-\infty, \infty)$ 时满足条件(7.19)，而当 $\omega$ 趋于无穷时，式(7.19)的左边趋于零，那么需要用解析法验证

$$\lim _ {\omega \rightarrow \infty} \omega^ {2} \left\{\frac {1}{k} + \operatorname{Re} [ G (j \omega) ] - \gamma \omega \operatorname{Im} [ G (j \omega) ] \right\} > 0$$

![](image/244976e9793967dea1e1b7ff61c0a0672cba01c6cd7f4876e882714b54d0bdb0.jpg)

<details>
<summary>text_image</summary>

斜率 = 1/γ
ωIm [G(jω)]
-1/k
Re[G(jω)]
</details>

图7.13 Popov曲线

当 $k = \infty$ 且 $G(s)$ 的相对阶为2时出现这种情况。

当 $\gamma = 0$ 的时候, 条件(7.19)退化到圆判据的条件 $\operatorname{Re}[G(j\omega)] > -1 / k$ , 这说明对于系统(7.13)\~(7.15)来说, Popov 判据的条件比圆判据的条件弱。换句话说, 当 $\gamma > 0$ 的时候, 在条件不很严格的情况下便可以建立绝对稳定性。

例7.5 考虑二阶系统

$$\dot {x} _ {1} = x _ {2}\dot {x} _ {2} = - x _ {2} - h (y)y = x _ {1}$$

如果取 $\psi = h$ ，该系统与系统(7.13)\~(7.15)的形式相同，但矩阵 $A$ 不是赫尔维茨的。在第二个状态方程右边同时加减一项 $\alpha y, \alpha > 0$ ，并定义 $\psi(y) = h(y) - \alpha y$ ，这时系统为(7.13)\~(7.15)的形式，其中

$$
A = \left[ \begin{array}{c c} 0 & 1 \\ - \alpha & - 1 \end{array} \right], B = \left[ \begin{array}{l} 0 \\ 1 \end{array} \right], C = \left[ \begin{array}{l l} 1 & 0 \end{array} \right]
$$

假设 h 属于扇形区域 $[\alpha, \beta]$ , $\beta > \alpha$ , 那么 $\psi$ 属于扇形区域 $[0, k]$ , 其中 $k = \beta - \alpha$ 。条件 (7.19) 变为

$$\frac {1}{k} + \frac {\alpha - \omega^ {2} + \gamma \omega^ {2}}{(\alpha - \omega^ {2}) ^ {2} + \omega^ {2}} > 0, \forall \omega \in [ - \infty , \infty ]$$

选择 $\gamma > 1$ ，对于所有 $\alpha$ 和 $k$ 不等式成立。即使当 $k = \infty$ 时，前面的不等式仍对于所有 $\omega \in (-\infty, \infty)$ 成立，且有

$$\lim _ {\omega \rightarrow \infty} \frac {\omega^ {2} (\alpha - \omega^ {2} + \gamma \omega^ {2})}{(\alpha - \omega^ {2}) ^ {2} + \omega^ {2}} = \gamma - 1 > 0$$
