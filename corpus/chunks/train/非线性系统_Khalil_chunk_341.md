最后一个不等式的右边是 $\psi$ 的二次型。当

$$d (1 - d) \alpha_ {1} \left(\frac {\alpha_ {2}}{\varepsilon} - \gamma\right) > \frac {1}{4} [ (1 - d) \beta_ {1} + d \beta_ {2} ] ^ {2}$$

时,相当于 $\varepsilon<\frac{\alpha_{1}\alpha_{2}}{\alpha_{1}\gamma+\frac{1}{4d(1-d)}[(1-d)\beta_{1}+d\beta_{2}]^{2}}\stackrel{\mathrm{def}}{=} \varepsilon_{d}$ (11.45)

该二次型是负定的。图11.12绘出了 $\varepsilon_{d}$ 与 $d$ 的关系。很容易看出 $\varepsilon_{d}$ 的最大值出现在 $d^{*} = \beta_{1} / (\beta_{1} + \beta_{2})$ 处，且为

$$\varepsilon^ {*} = \frac {\alpha_ {1} \alpha_ {2}}{\alpha_ {1} \gamma + \beta_ {1} \beta_ {2}} \tag {11.46}$$

由此得出对于所有 $\varepsilon < \varepsilon^{*}$ ，方程(11.35)和方程(11.36)的原点是渐近稳定的。定理11.3总结了上述结果。

定理 11.3 考虑奇异扰动系统(11.35)\~(11.36)，假设存在李雅普诺夫函数 $V(x)$ 和 $W(x, y)$ ，满足式(11.39)到式(11.41)、式(11.43)和式(11.44)，并设 $\varepsilon_{d}$ 和 $\varepsilon^{*}$ 由式(11.45)和式(11.46)

定义。则对于所有 $0 < \varepsilon < \varepsilon^{*}$ ，方程(11.35)和方程(11.36)的原点是渐近稳定的。此外，对于 $\varepsilon \in (0, \varepsilon_{d})$ ，式(11.42)定义的 $\nu(x, y)$ 是一个李雅普诺夫函数。

引导出定理 11.3 的稳定性分析,刻画了构建奇异扰动系统(11.35)\~(11.36)的李雅普诺夫函数的过程。首先研究降阶系统和边界层系统，并寻找满足式(11.39)到式(11.41)的李雅普诺夫函数 $V(x)$ 和 $W(x,y)$ ，然后检验不等式(11.43)和不等式(11.44)。这两个不等式称为互联条件。在找到理想的李雅普诺夫函数前，需要多次试选V和W。作为搜寻过程中的方向，如果

![](image/5435dc1384cc3fc818d749d4f33ffefb0ca9d231da0961d94fdda5ed4cf31434.jpg)

<details>
<summary>line</summary>

| d | ε |
| --- | --- |
| d₁ | ε* |
| d* | ε* |
| d₂ | ε |
</details>

图11.12 $\varepsilon$ 的上界

$$
\begin{array}{l} \left\| \frac {\partial V}{\partial x} \right\| \leqslant k _ {1} \psi_ {1} (x); \| f (x, h (x)) \| \leqslant k _ {2} \psi_ {1} (x) \\ \left\| f (x, y + h (x)) - f (x, h (x)) \right\| \leqslant k _ {3} \psi_ {2} (y) \\ \left\| \frac {\partial W}{\partial y} \right\| \leqslant k _ {4} \psi_ {2} (y); \quad \left\| \frac {\partial W}{\partial x} \right\| \leqslant k _ {5} \psi_ {2} (y) \\ \end{array}
$$
