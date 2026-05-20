为满足式(5.28)，选取 $\alpha > 0, \gamma > 0$ ，使

$$- \alpha k + \frac {\alpha^ {2}}{2 \gamma^ {2}} + \frac {1}{2} \leqslant 0 \tag {5.31}$$

经过简单的代数运算,上面的不等式可写为

$$\gamma^ {2} \geqslant \frac {\alpha^ {2}}{2 \alpha k - 1}$$

因为我们希望得到可能的最小 $\gamma$ ，故选择 $\alpha$ 使上述不等式的右边最小。在 $\alpha = 1 / k$ 时取到最小值 $1 / k^2$ 。因此，选取 $\gamma = 1 / k$ ，可得系统是有限增益 $\mathcal{L}_2$ 稳定的，且系统的 $\mathcal{L}_2$ 增益小于或等于 $1 / k$ 。注意，在本例中定理5.1的条件并不满足，因为无激励系统的原点不是指数

稳定的。在原点线性化可得矩阵

$$
\left[ \begin{array}{c c} 0 & 1 \\ 0 & - k \end{array} \right]
$$

它是非赫尔维茨矩阵。

△

下例将对上一例的概念进行推广。

例 5.9 考虑非线性系统(5.26)～(5.27)，m=q，假设存在一个连续可微半正定函数 $W(x)$ ，对于所有 $x \in R^{n}$ 满足 $^{①}$

$$\frac {\partial W}{\partial x} f (x) \leqslant - k h ^ {\mathrm{T}} (x) h (x), k > 0 \tag {5.32}\frac {\partial W}{\partial x} G (x) = h ^ {T} (x) \tag {5.33}$$

取 $V(x) = \alpha W(x)(\alpha >0)$ 作为Hamilton-Jacobi不等式(5.28)的备选解，可证明

$$\mathcal {H} (V, f, G, h, \gamma) = \left(- \alpha k + \frac {\alpha^ {2}}{2 \gamma^ {2}} + \frac {1}{2}\right) h ^ {\mathrm{T}} (x) h (x)$$

为了满足式(5.28)，应选取 $\alpha > 0, \gamma > 0$ ，使

$$- \alpha k + \frac {\alpha^ {2}}{2 \gamma^ {2}} + \frac {1}{2} \leqslant 0$$

该不等式与例 5.8 中的不等式(5.31)相同。重复使用这种方法, 可证明该系统为有限增益 $L_{2}$ 稳定的, 且其 $L_{2}$ 增益小于或等于 $1/k$ 。

例 5.10 考虑非线性系统(5.26)\~(5.27)，其中 m=q，假设存在一个连续可微半正定函数 $W(x)$ ，对于所有 $x \in R^{n}$ 满足 $^{②}$

$$\frac {\partial W}{\partial x} f (x) \leqslant 0 \tag {5.34}\frac {\partial W}{\partial x} G (x) = h ^ {T} (x) \tag {5.35}$$

由输出反馈控制

$$u = - k y + v, \quad k > 0$$

得到闭环系统

$$\dot {x} = f (x) - k G (x) G ^ {\mathrm{T}} (x) \left(\frac {\partial W}{\partial x}\right) ^ {\mathrm{T}} + G (x) v \stackrel {\text {def}} {=} f _ {c} (x) + G (x) vy = h (x) = G ^ {T} (x) \left(\frac {\partial W}{\partial x}\right) ^ {T}$$

容易验证,对于闭环系统, $W(x)$ 满足上例中的式(5.32)和式(5.33)。因此,从v到y的输入-输出映射是有限增益 $L_{2}$ 稳定的,且其 $L_{2}$ 增益小于或等于1/k。实质上这说明通过选择足够大的反馈增益k,可使 $L_{2}$ 增益任意小。

例5.11 考虑线性时不变系统

$$\dot {x} = A x + B uy = C x$$

假设对某个 $\gamma > 0$ ，里卡蒂方程

$$P A + A ^ {\mathrm{T}} P - \frac {1}{\gamma^ {2}} P B B ^ {\mathrm{T}} P + C ^ {\mathrm{T}} C = 0 \tag {5.36}$$

存在半正定解 $P$ 。取 $V(x) = (1 / 2)x^{\mathrm{T}}Px$ ，由表达式 $[\partial V / \partial x] = x^{\mathrm{T}}P$ ，容易看出 $V(x)$ 满足Hamilton-Jacobi方程

$$\mathcal {H} (V, A x, B, C x) = x ^ {\mathrm{T}} P A x + \frac {1}{2 \gamma^ {2}} x ^ {\mathrm{T}} P B ^ {\mathrm{T}} B P x + \frac {1}{2} x ^ {\mathrm{T}} C ^ {\mathrm{T}} C x = 0$$
