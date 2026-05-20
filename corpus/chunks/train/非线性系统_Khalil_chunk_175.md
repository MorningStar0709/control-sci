$$\left\| e _ {1 \tau} \right\| _ {\mathcal {L}} \leqslant \frac {1}{1 - \gamma_ {1} \gamma_ {2}} \left(\left\| u _ {1 \tau} \right\| _ {\mathcal {L}} + \gamma_ {2} \left\| u _ {2 \tau} \right\| _ {\mathcal {L}} + \beta_ {2} + \gamma_ {2} \beta_ {1}\right) \tag {5.40}$$

同样,对于所有的 $\tau\in[0,\infty)$ 有

$$\left\| e _ {2 \tau} \right\| _ {\mathcal {L}} \leqslant \frac {1}{1 - \gamma_ {1} \gamma_ {2}} \left(\left\| u _ {2 \tau} \right\| _ {\mathcal {L}} + \gamma_ {1} \left\| u _ {1 \tau} \right\| _ {\mathcal {L}} + \beta_ {1} + \gamma_ {1} \beta_ {2}\right) \tag {5.41}$$

由三角不等式 $\| e\|_{\mathcal{L}}\leqslant \| e_1\|_{\mathcal{L}} + \| e_2\|_{\mathcal{L}}$ 即可完成证明。

图 5.1 所示的反馈连接为研究动力学系统的鲁棒性问题提供了便利的结构。通常, 模型不确定时的动力学系统可表示为 $H_{1}$ 和 $H_{2}$ 的反馈连接, 其中 $H_{1}$ 作为稳定的标称系统, $H_{2}$ 作为稳定的扰动系统。那么, 只要 $\gamma_{2}$ 足够小, 则 $\gamma_{1}\gamma_{2}<1$ 成立。因此, 对理解许多由研究动力学系统而产生的鲁棒性结果, 尤其是含反馈连接的动力学系统, 小增益定理提供了一个概念性的框架。许多可由李雅普诺夫稳定性推导的鲁棒性结果, 都可作为小增益定理的特例加以解释。

例 5.13 考虑图 5.1 所示的反馈连接。设 $H_{1}$ 为线性时不变系统，其赫尔维茨平方传递函数矩阵为 $G(s)=C(sI-A)^{-1}B$ ，又设 $H_{2}$ 为无记忆函数 $y_{2}=\psi(t,e_{2})$ ，满足

$$\| \psi (t, y) \| _ {2} \leqslant \gamma_ {2} \| y \| _ {2}, \forall t \geqslant 0, \forall y \in R ^ {m}$$

由定理5.4可知 $H_{1}$ 是有限增益 $\mathcal{L}_2$ 稳定的，其 $\mathcal{L}_2$ 增益为

$$\gamma_ {1} = \sup _ {w \in R} \| G (j \omega) \| _ {2}$$

从例 5.1 已得知 $H_{2}$ 为有限增益 $L_{2}$ 稳定的，且其 $L_{2}$ 增益小于或等于 $\gamma_{2}$ 。假设反馈连接是明确定义的，则由小增益定理可知，如果 $\gamma_{1}\gamma_{2}<1$ ，则系统是有限增益 $L_{2}$ 稳定的。

例5.14 考虑系统

$$\dot {x} = f (t, x, v + d _ {1} (t))\varepsilon \dot {z} = A z + B [ u + d _ {2} (t) ]v = C z$$

其中 $f$ 是其自变量的光滑函数， $A$ 为赫尔维茨矩阵，满足 $-CA^{-1}B = I, \varepsilon$ 是一个小的正参数，而 $d_{1}$ 和 $d_{2}$ 为扰动信号。这个模型的线性部分代表执行部件的动态特性，它明显比由非线性方程 $\dot{x} = f$ 表示的设备的动态特性快得多。扰动信号 $d_{1}$ 和 $d_{2}$ 分别在设备的输入端和执行部件的输入端进入系统。假设扰动信号 $d_{1}$ 和 $d_{2}$ 属于信号空间 $\mathcal{L}$ ，其中 $\mathcal{L}$ 为任意 $\mathcal{L}_{p}$ 空间，且控制目标是减小该扰动对状态 $x$ 的影响。如果可设计反馈控制使从 $(d_{1}, d_{2})$ 到 $x$ 的闭环输入-输出映射为有限增益 $\mathcal{L}$ 稳定的，且 $\mathcal{L}$ 增益小于某个给定容限 $\delta > 0$ ，就可以实现控制目标。为了简化设计，通常令 $\varepsilon = 0$ ，忽略执行部件的动态特性，并把 $v = -CA^{-1}B(u + d_{2}) = u + d_{2}$ 代入设备方程式，从而得到降阶模型

$$\dot {x} = f (t, x, u + d)$$

其中 $d = d_{1} + d_{2}$ 。假设状态变量可测得，我们用此模式设计一个状态反馈控制律 $u = \gamma (t,x)$ ，以满足设计目标。假设已有光滑状态反馈控制 $u = \gamma (t,x)$ ，对 $\gamma <  \delta$ 满足

$$\| x \| _ {\mathcal {L}} \leqslant \gamma \| d \| _ {\mathcal {L}} + \beta \tag {5.42}$$
