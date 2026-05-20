# 14.2.1 稳定性

考虑系统

$$\dot {x} = f (t, x) + G (t, x) [ u + \delta (t, x, u) ] \tag {14.30}$$

其中， $x\in R^n$ 是状态， $u\in R^p$ 是控制输入， $f,G$ 和 $\delta$ 是 $(t,x,u)\in [0,\infty)\times D\times R^{p}$ 的函数，其中 $D\subset R^n$ 是包含原点的定义域。假设 $f,G$ 和 $\delta$ 对 $t$ 是分段连续的，对 $x$ 和 $u$ 是局部利普希茨的，函数 $f$ 和 $G$ 明确已知，而函数 $\delta$ 是包含各种不确定项的未知函数，这些不确定项是由于模型简化或参数不确定等因素造成的，不确定项 $\delta$ 满足匹配条件。系统的标称模型取为

$$\dot {x} = f (t, x) + G (t, x) u \tag {14.31}$$

基于上述标称模型,我们设计一个稳定的状态反馈控制器。假设已设计出反馈控制律 $u=\psi(t,x)$ ，使标称闭环系统

$$\dot {x} = f (t, x) + G (t, x) \psi (t, x) \tag {14.32}$$

的原点一致渐近稳定,进一步假设式(14.32)的李雅普诺夫函数已知,即有一个连续可微函数 $V(t,x)$ ,对于所有 $(t,x)\in[0,\infty)\times D$ ,满足不等式

$$\alpha_ {1} (\| x \|) \leqslant V (t, x) \leqslant \alpha_ {2} (\| x \|) \tag {14.33}\frac {\partial V}{\partial t} + \frac {\partial V}{\partial x} [ f (t, x) + G (t, x) \psi (t, x) ] \leqslant - \alpha_ {3} (\| x \|) \tag {14.34}$$

其中 $\alpha_{1},\alpha_{2}$ 和 $\alpha_{3}$ 是 $\mathcal{K}$ 类函数。假设当 $u = \psi (t,x) + v$ 时，不确定项 $\delta$ 满足不等式

$$\| \delta (t, x, \psi (t, x) + v) \| \leqslant \rho (t, x) + \kappa_ {0} \| v \|, \quad 0 \leqslant \kappa_ {0} < 1 \tag {14.35}$$

其中 $\rho: [0, \infty) \times D \to R$ 是非负的连续函数。关于不确定项 $\delta$ ，式(14.35)的估计是唯一已知的信息，函数 $\rho$ 是不确定项的大小，这里需要强调的是 $\rho$ 不必很小，只要已知即可。本节的目标是证明，在李雅普诺夫函数 $V$ 以及式(14.35)中的函数 $\rho$ 和常数 $\kappa_0$ 已知的情况下，可以设计一个附加反馈控制 $v$ ，使总的控制 $u = \psi(t, x) + v$ 能够在存在不确定项时，稳定实际系统(14.30)。 $v$ 的设计称为李雅普诺夫再设计。

在讨论李雅普诺夫再设计技术之前,先说明第13章的反馈线性化问题适合于当前问题的框架。

例 14.3 考虑反馈线性系统

$$\dot {x} = f (x) + G (x) u$$

其中 $f: D \to R^n$ 和 $G: D \to R^{n \times p}$ 是定义域 $D \subset R^n$ 上的光滑函数，并存在微分同胚的 $T: D \to R^n$ ，使 $D_z = T(D)$ 包含原点，且 $T(x)$ 满足偏微分方程

$$
\begin{array}{l} \frac {\partial T}{\partial x} f (x) = A T (x) - B \gamma (x) \alpha (x) \\ \frac {\partial T}{\partial x} G (x) = B \gamma (x) \\ \end{array}
$$

其中 $(A,B)$ 是可控的， $\gamma (x)$ 对于所有 $x\in D$ 是非奇异的。进行变量代换 $Z = T(x)$ ，将系统

变换为 $\dot{z} = Az + B\gamma (x)[u - \alpha (x)]$

同时考虑扰动系统 $\dot{x}=f(x)+\Delta_{f}(x)+[G(x)+\Delta_{G}(x)]u$ 为光滑扰动,且在 D 上满足条件 $^{①}$

$$\frac {\partial T}{\partial x} \Delta_ {f} (x) = B \gamma (x) \Delta_ {1} (x), \quad \Delta_ {G} (x) = G (x) \Delta_ {2} (x)$$

扰动系统可表示为方程(14.30)的形式,即

$$\dot {z} = A z - B \gamma (x) \alpha (x) + B \gamma (x) [ u + \delta (x, u) ]$$

其中， $\delta(x,u)=\Delta_{1}(x)+\Delta_{2}(x)u$ 。由于标称系统是可反馈线性化的，因此可把标称稳定反馈控制取为

$$\psi (x) = \alpha (x) - \gamma^ {- 1} (x) K z = \alpha (x) - \gamma^ {- 1} (x) K T (x)$$

K 的选择使矩阵 A-BK 为赫尔维茨矩阵。对于闭环系统
